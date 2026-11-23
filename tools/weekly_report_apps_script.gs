/**
 * First Principles: weekly visitor report (Microsoft Clarity Data Export API) emailed to OWNER.
 * Lives in the same Apps Script project as booking_apps_script.gs (uses OWNER, BOOK_ID, SHEET).
 * Clarity's API only returns the last 1-3 days, so collectDaily() saves each day's numbers to the
 * "Stats" tab every morning (2 of Clarity's 10 daily API calls), and weeklyReport() adds up the last
 * 7 days every Monday morning and emails them.
 * Setup once: Script property CLARITY_TOKEN, then run setupWeeklyReport().
 */
const CLARITY_PROJECT = 'zf2slpx8uv';
const SITE = 'https://firstprinciples.courses';
const STATS = 'Stats';

function setupWeeklyReport() {
  ScriptApp.getProjectTriggers().filter(function (t) { return ['dailyReport', 'collectDaily', 'weeklyReport'].indexOf(t.getHandlerFunction()) >= 0; })
    .forEach(function (t) { ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('collectDaily').timeBased().everyDays(1).atHour(7).nearMinute(15).inTimezone('Europe/Berlin').create();
  ScriptApp.newTrigger('weeklyReport').timeBased().onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(8).nearMinute(0).inTimezone('Europe/Berlin').create();
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
function statsSheet_() {
  const ss = SpreadsheetApp.openById(BOOK_ID);
  let sh = ss.getSheetByName(STATS);
  if (!sh) { sh = ss.insertSheet(STATS); sh.appendRow(['Collected', 'Visits', 'Visitors', 'Pages per visit', 'Scroll %', 'Active s', 'Detail (JSON)']); sh.setFrozenRows(1); }
  return sh;
}

/** Runs every morning: saves the last 24 hours to the Stats tab. */
function collectDaily() {
  const total = clarity_(''), byUrl = clarity_('URL');
  const tt = metric_(total, 'Traffic')[0] || {};
  const visits = num_(tt.totalSessionCount) - num_(tt.totalBotSessionCount);
  const users = num_(tt.distinctUserCount || tt.distantUserCount);
  const pps = num_(tt.pagesPerSessionPercentage);
  const scroll = num_((metric_(total, 'ScrollDepth')[0] || {}).averageScrollDepth);
  const active = num_((metric_(total, 'EngagementTime')[0] || {}).activeTime);
  const pages = {};
  metric_(total, 'PopularPages').forEach(function (x) { const k = path_(x.url); pages[k] = pages[k] || {}; pages[k].v = (pages[k].v || 0) + num_(x.visitsCount); });
  metric_(byUrl, 'Traffic').forEach(function (x) { const k = path_(x.Url || x.URL || x.url); pages[k] = pages[k] || {}; pages[k].s = (pages[k].s || 0) + num_(x.totalSessionCount) - num_(x.totalBotSessionCount); });
  metric_(byUrl, 'ScrollDepth').forEach(function (x) { const k = path_(x.Url || x.URL || x.url); if (pages[k]) pages[k].sd = num_(x.averageScrollDepth); });
  metric_(byUrl, 'EngagementTime').forEach(function (x) { const k = path_(x.Url || x.URL || x.url); if (pages[k]) pages[k].et = num_(x.activeTime); });
  const lists = {};
  ['ReferrerUrl', 'Country', 'Device', 'Browser'].forEach(function (m) {
    lists[m] = {}; metric_(total, m).forEach(function (x) { lists[m][x.name || 'Unknown'] = (lists[m][x.name || 'Unknown'] || 0) + num_(x.sessionsCount); });
  });
  const friction = {};
  ['DeadClickCount', 'QuickbackClick', 'RageClickCount', 'ScriptErrorCount'].forEach(function (m) { const x = metric_(total, m)[0]; if (x) friction[m] = num_(x.sessionsWithMetricPercentage); });
  statsSheet_().appendRow([new Date(), visits, users, pps, scroll, active, JSON.stringify({ pages: pages, lists: lists, friction: friction })]);
}

function table_(head, rows) {
  if (!rows.length) return '<p style="color:#667">No data.</p>';
  return '<table cellpadding="6" style="border-collapse:collapse;font:14px Arial,sans-serif">' +
    '<tr>' + head.map(function (h, i) { return '<th style="border-bottom:2px solid #145DA0;text-align:' + (i ? 'right' : 'left') + '">' + h + '</th>'; }).join('') + '</tr>' +
    rows.map(function (r) { return '<tr>' + r.map(function (c, i) { return '<td style="border-bottom:1px solid #e3e8ee;text-align:' + (i ? 'right' : 'left') + '">' + c + '</td>'; }).join('') + '</tr>'; }).join('') + '</table>';
}
function pageName_(k) { return k === '/' || k === '/index.html' ? 'Home' : k.replace(/^\//, '').replace(/\.html$/, ''); }
function change_(now, before) {
  if (!before) return '';
  const d = Math.round(100 * (now - before) / before);
  return ' <span style="font:12px Arial,sans-serif;color:' + (d >= 0 ? '#0a7d4d' : '#b23434') + '">' + (d >= 0 ? '+' : '') + d + '% vs last week</span>';
}

/** Runs every Monday: adds up the last 7 days and emails the report. */
function weeklyReport() {
  const now = Date.now(), DAY = 864e5;
  const rows = statsSheet_().getDataRange().getValues().slice(1).filter(function (r) { return r[0] instanceof Date; });
  const thisWeek = rows.filter(function (r) { return r[0].getTime() > now - 7 * DAY + 3600e3; });
  const lastWeek = rows.filter(function (r) { const t = r[0].getTime(); return t <= now - 7 * DAY + 3600e3 && t > now - 14 * DAY + 3600e3; });
  const sum = function (rs, i) { return rs.reduce(function (a, r) { return a + num_(r[i]); }, 0); };
  const wavg = function (rs, i) { const w = sum(rs, 1); return w ? rs.reduce(function (a, r) { return a + num_(r[i]) * num_(r[1]); }, 0) / w : 0; };
  const visits = sum(thisWeek, 1), visitors = sum(thisWeek, 2), prevVisits = sum(lastWeek, 1), prevVisitors = sum(lastWeek, 2);

  const P = {}, L = { ReferrerUrl: {}, Country: {}, Device: {}, Browser: {} }, F = {}, FW = {};
  thisWeek.forEach(function (r) {
    let d; try { d = JSON.parse(r[6]); } catch (e) { return; }
    const w = num_(r[1]);
    Object.keys(d.pages || {}).forEach(function (k) {
      const p = d.pages[k], q = P[k] = P[k] || { v: 0, s: 0, sdw: 0, etw: 0, w: 0 };
      q.v += num_(p.v); q.s += num_(p.s);
      if (p.sd != null) { q.sdw += num_(p.sd) * num_(p.s || 1); q.etw += num_(p.et) * num_(p.s || 1); q.w += num_(p.s || 1); }
    });
    Object.keys(L).forEach(function (m) { const src = (d.lists || {})[m] || {}; Object.keys(src).forEach(function (n) { L[m][n] = (L[m][n] || 0) + num_(src[n]); }); });
    Object.keys(d.friction || {}).forEach(function (m) { F[m] = (F[m] || 0) + num_(d.friction[m]) * w; FW[m] = (FW[m] || 0) + w; });
  });
  const prow = Object.keys(P).map(function (k) { return [k, P[k]]; })
    .sort(function (a, b) { return (b[1].v - a[1].v) || (b[1].s - a[1].s); }).slice(0, 20)
    .map(function (e) {
      const k = e[0], v = e[1];
      return ['<a href="' + SITE + (k === '/' ? '/' : k) + '">' + esc2_(pageName_(k)) + '</a>', v.v || v.s, v.s || '–',
        v.w ? Math.round(v.sdw / v.w) + '%' : '–', v.w ? dur_(v.etw / v.w) : '–'];
    });
  const top = function (m, n) { return Object.keys(L[m]).map(function (k) { return [esc2_(k), L[m][k]]; }).sort(function (a, b) { return b[1] - a[1]; }).slice(0, n); };
  const fr = function (m) { return FW[m] ? Math.round(F[m] / FW[m]) + '%' : '–'; };

  // days of the week
  const daily = thisWeek.map(function (r) { return [Utilities.formatDate(new Date(r[0].getTime() - DAY), 'Europe/Berlin', 'EEE d MMM'), num_(r[1]), num_(r[2])]; });

  // 1-to-1 requests in the last 7 days
  let req = [];
  try {
    req = SpreadsheetApp.openById(BOOK_ID).getSheetByName(SHEET).getDataRange().getValues().slice(1)
      .filter(function (r) { return r[0] instanceof Date && r[0].getTime() > now - 7 * DAY; })
      .map(function (r) {
        const slot = r[2] instanceof Date ? Utilities.formatDate(r[2], 'Europe/Berlin', 'EEE d MMM yyyy, HH:mm') : String(r[2]);
        return [esc2_(r[4]), esc2_(r[6]), slot, esc2_(r[3])];
      });
  } catch (e) { }

  const from = Utilities.formatDate(new Date(now - 7 * DAY), 'Europe/Berlin', 'd MMM'), to = Utilities.formatDate(new Date(now - DAY), 'Europe/Berlin', 'd MMM yyyy');
  const h2 = function (t) { return '<h3 style="font:600 16px Arial,sans-serif;color:#0B1D33;margin:26px 0 8px">' + t + '</h3>'; };
  const kpi = function (v, l) { return '<td style="padding:10px 22px 10px 0;vertical-align:top"><div style="font:600 26px Arial,sans-serif;color:#145DA0">' + v + '</div><div style="font:12px Arial,sans-serif;color:#667">' + l + '</div></td>'; };
  const html = '<div style="max-width:760px;font:14px Arial,sans-serif;color:#22303f">' +
    '<h2 style="font:600 20px Arial,sans-serif;color:#0B1D33;margin:0 0 4px">firstprinciples.courses: week of ' + from + ' to ' + to + '</h2>' +
    '<p style="color:#667;margin:0 0 12px">' + thisWeek.length + ' of 7 days collected. Only visitors who clicked Accept on the cookie banner are counted, so real traffic is higher. Visitors are counted per day, so someone who came back on three days counts three times.</p>' +
    '<table><tr>' + kpi(visits + change_(visits, prevVisits), 'visits') + kpi(visitors + change_(visitors, prevVisitors), 'daily visitors (summed)') +
    kpi(wavg(thisWeek, 3) ? wavg(thisWeek, 3).toFixed(1) : '–', 'pages per visit') + kpi(Math.round(wavg(thisWeek, 4)) + '%', 'average scroll depth') +
    kpi(dur_(wavg(thisWeek, 5)), 'active time per visit') + '</tr></table>' +
    h2('Day by day') + table_(['Day', 'Visits', 'Visitors'], daily) +
    h2('Most visited pages this week') + table_(['Page', 'Page views', 'Visits', 'Scroll', 'Active time'], prow) +
    h2('Where visitors came from') + table_(['Referrer', 'Visits'], top('ReferrerUrl', 10)) +
    h2('Countries') + table_(['Country', 'Visits'], top('Country', 12)) +
    h2('Devices and browsers') + table_(['Device', 'Visits'], top('Device', 5)) + '<div style="height:8px"></div>' + table_(['Browser', 'Visits'], top('Browser', 5)) +
    h2('Signs of friction') + table_(['Signal', 'Visits with it'], [['Dead clicks (clicked something that does nothing)', fr('DeadClickCount')], ['Quick backs (left a page within seconds)', fr('QuickbackClick')], ['Rage clicks', fr('RageClickCount')], ['JavaScript errors', fr('ScriptErrorCount')]]) +
    h2('1-to-1 retake session requests this week') + (req.length ? table_(['Name', 'Level', 'Slot (Berlin)', 'Status'], req) : '<p style="color:#667">None this week.</p>') +
    '<p style="color:#667;margin-top:24px">Recordings, heatmaps and longer date ranges: <a href="https://clarity.microsoft.com/projects/view/' + CLARITY_PROJECT + '/dashboard">Clarity dashboard</a> · Google search clicks: <a href="https://search.google.com/search-console/performance/search-analytics?resource_id=sc-domain%3Afirstprinciples.courses">Search Console</a> · Daily numbers: Stats tab in <a href="' + SpreadsheetApp.openById(BOOK_ID).getUrl() + '">First Principles session requests</a></p></div>';
  MailApp.sendEmail({ to: OWNER, name: 'First Principles reports', subject: 'Weekly website report ' + from + '–' + to + ': ' + visits + ' visits', htmlBody: html });
}
