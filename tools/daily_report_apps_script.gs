/**
 * First Principles: daily visitor report (Microsoft Clarity Data Export API) emailed to OWNER.
 * Lives in the same Apps Script project as booking_apps_script.gs (uses OWNER, BOOK_ID, SHEET).
 * Setup once: Project Settings > Script properties > CLARITY_TOKEN = <token from Clarity > Settings > Data export>,
 * then run setupDailyReport() once (creates the 07:30 Europe/Berlin trigger).
 * Clarity allows 10 API calls a day; this uses 5.
 */
const CLARITY_PROJECT = 'zf2slpx8uv';
const SITE = 'https://firstprinciples.courses';

function setupDailyReport() {
  ScriptApp.getProjectTriggers().filter(function (t) { return t.getHandlerFunction() === 'dailyReport'; })
    .forEach(function (t) { ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('dailyReport').timeBased().everyDays(1).atHour(7).nearMinute(30).inTimezone('Europe/Berlin').create();
}

function clarity_(dim) {
  const token = PropertiesService.getScriptProperties().getProperty('CLARITY_TOKEN');
  let url = 'https://www.clarity.ms/export-data/api/v1/project-live-insights?numOfDays=1';
  if (dim) url += '&dimension1=' + encodeURIComponent(dim);
  const r = UrlFetchApp.fetch(url, { headers: { Authorization: 'Bearer ' + token }, muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('Clarity ' + (dim || 'total') + ': HTTP ' + r.getResponseCode() + ' ' + r.getContentText().slice(0, 200));
  return JSON.parse(r.getContentText());
}
function metric_(data, name) {
  const m = data.filter(function (x) { return String(x.metricName).toLowerCase() === name.toLowerCase(); })[0];
  return m ? m.information || [] : [];
}
function num_(v) { const n = Number(v); return isNaN(n) ? 0 : n; }
function path_(u) { return String(u || '').replace(/^https?:\/\/[^/]+/, '').replace(/[?#].*$/, '') || '/'; }
function table_(head, rows) {
  if (!rows.length) return '<p style="color:#667">No data.</p>';
  return '<table cellpadding="6" style="border-collapse:collapse;font:14px Arial,sans-serif">' +
    '<tr>' + head.map(function (h, i) { return '<th style="border-bottom:2px solid #145DA0;text-align:' + (i ? 'right' : 'left') + '">' + h + '</th>'; }).join('') + '</tr>' +
    rows.map(function (r) { return '<tr>' + r.map(function (c, i) { return '<td style="border-bottom:1px solid #e3e8ee;text-align:' + (i ? 'right' : 'left') + '">' + c + '</td>'; }).join('') + '</tr>'; }).join('') + '</table>';
}
function byDim_(data, key) {
  const t = metric_(data, 'Traffic');
  return t.map(function (x) { return { k: x[key] || 'Unknown', s: num_(x.totalSessionCount) - num_(x.totalBotSessionCount), u: num_(x.distantUserCount), p: num_(x.PagesPerSessionPercentage) }; })
    .filter(function (x) { return x.s > 0; }).sort(function (a, b) { return b.s - a.s; });
}

function dailyReport() {
  const errors = [];
  function safe(f) { try { return f(); } catch (e) { errors.push(String(e.message || e)); return []; } }
  const total = safe(function () { return clarity_(''); });
  const pages = safe(function () { return clarity_('URL'); });
  const src = safe(function () { return clarity_('Source'); });
  const ctry = safe(function () { return clarity_('Country/Region'); });
  const dev = safe(function () { return clarity_('Device'); });

  const tt = metric_(total, 'Traffic')[0] || {};
  const sessions = num_(tt.totalSessionCount) - num_(tt.totalBotSessionCount), users = num_(tt.distantUserCount), pps = num_(tt.PagesPerSessionPercentage);
  const scroll = metric_(total, 'Scroll Depth')[0] || {}, eng = metric_(total, 'Engagement Time')[0] || {};

  // pages: merge traffic, scroll and engagement by URL
  const P = {};
  metric_(pages, 'Traffic').forEach(function (x) { const k = path_(x.Url || x.URL); P[k] = P[k] || { s: 0, u: 0 }; P[k].s += num_(x.totalSessionCount) - num_(x.totalBotSessionCount); P[k].u += num_(x.distantUserCount); });
  metric_(pages, 'Scroll Depth').forEach(function (x) { const k = path_(x.Url || x.URL); if (P[k]) P[k].sd = num_(x.averageScrollDepth); });
  metric_(pages, 'Engagement Time').forEach(function (x) { const k = path_(x.Url || x.URL); if (P[k]) P[k].et = num_(x.activeTime || x.totalTime); });
  metric_(pages, 'Popular Pages').forEach(function (x) { const k = path_(x.url || x.Url || x.URL); P[k] = P[k] || { s: 0, u: 0 }; P[k].v = num_(x.visitsCount || x.visits || x.count); });
  const prow = Object.keys(P).map(function (k) { return [k, P[k]]; })
    .sort(function (a, b) { return (b[1].v || b[1].s) - (a[1].v || a[1].s); }).slice(0, 15)
    .map(function (e) {
      const k = e[0], v = e[1];
      return ['<a href="' + SITE + (k === '/' ? '/' : k) + '">' + (k === '/' ? 'Home' : k.replace(/^\//, '').replace(/\.html$/, '')) + '</a>',
        v.v || v.s, v.u, v.sd != null ? Math.round(v.sd) + '%' : '–', v.et != null ? Math.round(v.et) + ' s' : '–'];
    });

  const simple = function (data, key, n) { return byDim_(data, key).slice(0, n || 10).map(function (x) { return [x.k, x.s, x.u]; }); };

  // 1-to-1 requests in the last 24 h
  let req = [];
  try {
    const since = Date.now() - 24 * 3600e3;
    req = SpreadsheetApp.openById(BOOK_ID).getSheetByName(SHEET).getDataRange().getValues().slice(1)
      .filter(function (r) { return r[0] instanceof Date && r[0].getTime() > since; })
      .map(function (r) { return [String(r[4]), String(r[6]), String(r[2]), String(r[3])]; });
  } catch (e) { errors.push('Requests sheet: ' + e.message); }

  const day = Utilities.formatDate(new Date(Date.now() - 12 * 3600e3), 'Europe/Berlin', 'EEE d MMM yyyy');
  const h2 = function (t) { return '<h3 style="font:600 16px Arial,sans-serif;color:#0B1D33;margin:26px 0 8px">' + t + '</h3>'; };
  const kpi = function (v, l) { return '<td style="padding:10px 18px 10px 0"><div style="font:600 26px Arial,sans-serif;color:#145DA0">' + v + '</div><div style="font:12px Arial,sans-serif;color:#667">' + l + '</div></td>'; };
  const html = '<div style="max-width:720px;font:14px Arial,sans-serif;color:#22303f">' +
    '<h2 style="font:600 20px Arial,sans-serif;color:#0B1D33;margin:0 0 4px">firstprinciples.courses: the last 24 hours</h2>' +
    '<p style="color:#667;margin:0 0 12px">Report for ' + day + '. Visitors who declined cookies are not counted (Clarity only loads after Accept).</p>' +
    '<table><tr>' + kpi(sessions, 'visits (sessions)') + kpi(users, 'visitors') + kpi(pps ? pps.toFixed(1) : '–', 'pages per visit') +
    kpi(scroll.averageScrollDepth != null ? Math.round(num_(scroll.averageScrollDepth)) + '%' : '–', 'average scroll') +
    kpi(eng.activeTime != null ? Math.round(num_(eng.activeTime)) + ' s' : '–', 'active time') + '</tr></table>' +
    h2('Most visited pages') + table_(['Page', 'Visits', 'Visitors', 'Scroll', 'Active time'], prow) +
    h2('Where visitors came from') + table_(['Source', 'Visits', 'Visitors'], simple(src, 'Source')) +
    h2('Countries') + table_(['Country', 'Visits', 'Visitors'], simple(ctry, 'Country/Region')) +
    h2('Devices') + table_(['Device', 'Visits', 'Visitors'], simple(dev, 'Device', 5)) +
    h2('1-to-1 retake session requests') + (req.length ? table_(['Name', 'Level', 'Slot (Berlin)', 'Status'], req) : '<p style="color:#667">None in the last 24 hours.</p>') +
    (errors.length ? '<p style="color:#b23434">Problems: ' + errors.join(' · ') + '</p>' : '') +
    '<p style="color:#667;margin-top:24px">Recordings, heatmaps and longer date ranges: <a href="https://clarity.microsoft.com/projects/view/' + CLARITY_PROJECT + '/dashboard">Clarity dashboard</a> · Google search clicks: <a href="https://search.google.com/search-console/performance/search-analytics?resource_id=sc-domain%3Afirstprinciples.courses">Search Console</a></p></div>';
  MailApp.sendEmail({ to: OWNER, name: 'First Principles reports', subject: 'Website report ' + day + ': ' + sessions + ' visits', htmlBody: html });
}
