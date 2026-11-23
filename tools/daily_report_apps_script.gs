/**
 * First Principles: daily visitor report (Microsoft Clarity Data Export API) emailed to OWNER.
 * Lives in the same Apps Script project as booking_apps_script.gs (uses OWNER, BOOK_ID, SHEET).
 * Setup once: Project Settings > Script properties > CLARITY_TOKEN = <token from Clarity > Settings > Data export>,
 * then run setupDailyReport() once (creates the 07:30 Europe/Berlin trigger).
 * Clarity allows 10 API calls a day; this uses 2.
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
  const want = name.toLowerCase().replace(/\s+/g, '');
  const m = (data || []).filter(function (x) { return String(x.metricName).toLowerCase().replace(/\s+/g, '') === want; })[0];
  return m ? m.information || [] : [];
}
function num_(v) { const n = Number(v); return isNaN(n) ? 0 : n; }
function path_(u) { return String(u || '').replace(/^https?:\/\/[^/]+/, '').replace(/[?#].*$/, '') || '/'; }
function esc2_(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
function dur_(sec) { sec = Math.round(num_(sec)); return sec >= 60 ? Math.floor(sec / 60) + ' min ' + (sec % 60) + ' s' : sec + ' s'; }
function table_(head, rows) {
  if (!rows.length) return '<p style="color:#667">No data.</p>';
  return '<table cellpadding="6" style="border-collapse:collapse;font:14px Arial,sans-serif">' +
    '<tr>' + head.map(function (h, i) { return '<th style="border-bottom:2px solid #145DA0;text-align:' + (i ? 'right' : 'left') + '">' + h + '</th>'; }).join('') + '</tr>' +
    rows.map(function (r) { return '<tr>' + r.map(function (c, i) { return '<td style="border-bottom:1px solid #e3e8ee;text-align:' + (i ? 'right' : 'left') + '">' + c + '</td>'; }).join('') + '</tr>'; }).join('') + '</table>';
}
function list_(data, name, n) {
  return metric_(data, name).map(function (x) { return [esc2_(x.name || 'Unknown'), num_(x.sessionsCount)]; })
    .sort(function (a, b) { return b[1] - a[1]; }).slice(0, n || 10);
}
function pageName_(k) { return k === '/' || k === '/index.html' ? 'Home' : k.replace(/^\//, '').replace(/\.html$/, ''); }

function dailyReport() {
  const errors = [];
  function safe(f) { try { return f(); } catch (e) { errors.push(String(e.message || e)); return []; } }
  const total = safe(function () { return clarity_(''); });
  const byUrl = safe(function () { return clarity_('URL'); });

  const tt = metric_(total, 'Traffic')[0] || {};
  const sessions = num_(tt.totalSessionCount) - num_(tt.totalBotSessionCount);
  const users = num_(tt.distinctUserCount || tt.distantUserCount);
  const pps = num_(tt.pagesPerSessionPercentage || tt.PagesPerSessionPercentage);
  const scroll = metric_(total, 'ScrollDepth')[0] || {}, eng = metric_(total, 'EngagementTime')[0] || {};
  const pct = function (m) { const x = metric_(total, m)[0]; return x ? Math.round(num_(x.sessionsWithMetricPercentage)) + '%' : '–'; };

  // most visited pages: Clarity's PopularPages, enriched with visitors per URL
  const P = {};
  metric_(total, 'PopularPages').forEach(function (x) { const k = path_(x.url || x.Url); P[k] = P[k] || {}; P[k].v = (P[k].v || 0) + num_(x.visitsCount); });
  metric_(byUrl, 'Traffic').forEach(function (x) { const k = path_(x.Url || x.URL || x.url); P[k] = P[k] || {}; P[k].s = (P[k].s || 0) + num_(x.totalSessionCount) - num_(x.totalBotSessionCount); P[k].u = (P[k].u || 0) + num_(x.distinctUserCount || x.distantUserCount); });
  metric_(byUrl, 'ScrollDepth').forEach(function (x) { const k = path_(x.Url || x.URL || x.url); if (P[k]) P[k].sd = num_(x.averageScrollDepth); });
  metric_(byUrl, 'EngagementTime').forEach(function (x) { const k = path_(x.Url || x.URL || x.url); if (P[k]) P[k].et = num_(x.activeTime); });
  const prow = Object.keys(P).map(function (k) { return [k, P[k]]; })
    .sort(function (a, b) { return ((b[1].v || 0) - (a[1].v || 0)) || ((b[1].s || 0) - (a[1].s || 0)); }).slice(0, 15)
    .map(function (e) {
      const k = e[0], v = e[1];
      return ['<a href="' + SITE + (k === '/' ? '/' : k) + '">' + esc2_(pageName_(k)) + '</a>', v.v || v.s || 0, v.s || '–', v.u || '–',
        v.sd != null ? Math.round(v.sd) + '%' : '–', v.et != null ? dur_(v.et) : '–'];
    });

  // 1-to-1 requests in the last 24 h
  let req = [];
  try {
    const since = Date.now() - 24 * 3600e3;
    req = SpreadsheetApp.openById(BOOK_ID).getSheetByName(SHEET).getDataRange().getValues().slice(1)
      .filter(function (r) { return r[0] instanceof Date && r[0].getTime() > since; })
      .map(function (r) {
        const slot = r[2] instanceof Date ? Utilities.formatDate(r[2], 'Europe/Berlin', 'EEE d MMM yyyy, HH:mm') : String(r[2]);
        return [esc2_(r[4]), esc2_(r[6]), slot, esc2_(r[3])];
      });
  } catch (e) { errors.push('Requests sheet: ' + e.message); }

  const day = Utilities.formatDate(new Date(Date.now() - 12 * 3600e3), 'Europe/Berlin', 'EEE d MMM yyyy');
  const h2 = function (t) { return '<h3 style="font:600 16px Arial,sans-serif;color:#0B1D33;margin:26px 0 8px">' + t + '</h3>'; };
  const kpi = function (v, l) { return '<td style="padding:10px 22px 10px 0;vertical-align:top"><div style="font:600 26px Arial,sans-serif;color:#145DA0">' + v + '</div><div style="font:12px Arial,sans-serif;color:#667">' + l + '</div></td>'; };
  const html = '<div style="max-width:760px;font:14px Arial,sans-serif;color:#22303f">' +
    '<h2 style="font:600 20px Arial,sans-serif;color:#0B1D33;margin:0 0 4px">firstprinciples.courses: the last 24 hours</h2>' +
    '<p style="color:#667;margin:0 0 12px">Report for ' + day + '. Only visitors who clicked Accept on the cookie banner are counted, so real traffic is higher.</p>' +
    '<table><tr>' + kpi(sessions, 'visits') + kpi(users, 'visitors') + kpi(pps ? pps.toFixed(1) : '–', 'pages per visit') +
    kpi(scroll.averageScrollDepth != null ? Math.round(num_(scroll.averageScrollDepth)) + '%' : '–', 'average scroll depth') +
    kpi(eng.activeTime != null ? dur_(eng.activeTime) : '–', 'active time per visit') + '</tr></table>' +
    h2('Most visited pages') + table_(['Page', 'Page views', 'Visits', 'Visitors', 'Scroll', 'Active time'], prow) +
    h2('Where visitors came from') + table_(['Referrer', 'Visits'], list_(total, 'ReferrerUrl', 10)) +
    h2('Countries') + table_(['Country', 'Visits'], list_(total, 'Country', 10)) +
    h2('Devices and browsers') + table_(['Device', 'Visits'], list_(total, 'Device', 5)) + '<div style="height:8px"></div>' + table_(['Browser', 'Visits'], list_(total, 'Browser', 5)) +
    h2('Signs of friction') + table_(['Signal', 'Visits with it'], [['Dead clicks (clicked something that does nothing)', pct('DeadClickCount')], ['Quick backs (left a page within seconds)', pct('QuickbackClick')], ['Rage clicks', pct('RageClickCount')], ['JavaScript errors', pct('ScriptErrorCount')]]) +
    h2('1-to-1 retake session requests') + (req.length ? table_(['Name', 'Level', 'Slot (Berlin)', 'Status'], req) : '<p style="color:#667">None in the last 24 hours.</p>') +
    (errors.length ? '<p style="color:#b23434">Problems: ' + esc2_(errors.join(' · ')) + '</p>' : '') +
    '<p style="color:#667;margin-top:24px">Recordings, heatmaps and longer date ranges: <a href="https://clarity.microsoft.com/projects/view/' + CLARITY_PROJECT + '/dashboard">Clarity dashboard</a> · Google search clicks: <a href="https://search.google.com/search-console/performance/search-analytics?resource_id=sc-domain%3Afirstprinciples.courses">Search Console</a></p></div>';
  MailApp.sendEmail({ to: OWNER, name: 'First Principles reports', subject: 'Website report ' + day + ': ' + sessions + ' visits, ' + users + ' visitors', htmlBody: html });
}
