/**
 * First Principles: 1-to-1 retake session requests.
 * Standalone Google Apps Script that writes to the Google Sheet below. Deploy as a web app:
 *   Execute as: Me   ·   Who has access: Anyone
 * GET  -> {"taken": [ISO slot, ...]}   (slots already requested or confirmed)
 * POST -> body is JSON text; saves the request in the sheet and emails OWNER.
 * To free a slot, set its Status to "Declined" or "Cancelled" in the sheet.
 */
const OWNER = 'gkinba@gmail.com';
const SHEET = 'Requests';
const BOOK_ID = '1rCl3bnapxf04526fLXhNB3rqiHZdEURpjUHWVMkBL1Y';  // "First Principles session requests" in Gowtham's Drive
const HEAD = ['Received', 'Slot (UTC)', 'Slot (Berlin)', 'Status', 'Name', 'Email', 'Level', 'Window sat', 'Result', 'Preparation', 'What they want', 'Time zone', 'Country'];
const FREE = ['Declined', 'Cancelled'];

function sheet_() {
  const ss = SpreadsheetApp.openById(BOOK_ID);
  let sh = ss.getSheetByName(SHEET);
  if (!sh) { sh = ss.insertSheet(SHEET); sh.appendRow(HEAD); sh.setFrozenRows(1); }
  return sh;
}
function taken_() {
  return sheet_().getDataRange().getValues().slice(1)
    .filter(function (r) { return FREE.indexOf(String(r[3])) < 0; })
    .map(function (r) { return String(r[1]); });
}
function out_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function clip_(s, n) { return String(s == null ? '' : s).replace(/^[=+\-@]/, "'$&").slice(0, n || 300); }
function esc_(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
function validSlot_(t) {
  const dow = Utilities.formatDate(t, 'Europe/Berlin', 'u'), hm = Utilities.formatDate(t, 'Europe/Berlin', 'HH:mm');
  return (dow === '6' && (hm === '10:00' || hm === '10:30')) || (dow === '7' && (hm === '15:00' || hm === '15:30'));
}

function doGet() { return out_({ taken: taken_() }); }

function doPost(e) {
  let d;
  try { d = JSON.parse(e.postData.contents); } catch (x) { return out_({ ok: false, error: 'format' }); }
  if (d.website) return out_({ ok: true });                       // spam trap
  const t = new Date(String(d.slot || '')), now = Date.now();
  if (isNaN(t) || t < now + 36 * 3600e3 || t > now + 190 * 86400e3 || !validSlot_(t)) return out_({ ok: false, error: 'slot' });
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email || '')) return out_({ ok: false, error: 'email' });
  if (['I', 'II'].indexOf(d.level) < 0) return out_({ ok: false, error: 'level' });
  if (!String(d.name || '').trim()) return out_({ ok: false, error: 'name' });
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const iso = t.toISOString();
    if (taken_().indexOf(iso) >= 0) return out_({ ok: false, error: 'taken' });
    const berlin = Utilities.formatDate(t, 'Europe/Berlin', 'EEE d MMM yyyy, HH:mm');
    const row = [new Date(), "'" + iso, berlin, 'Requested', clip_(d.name, 120), clip_(d.email, 200), 'Level ' + d.level,
      clip_(d.window, 120), clip_(d.result, 120), clip_(d.prep, 2000), clip_(d.goals, 2000), clip_(d.tz, 80), clip_(d.country, 80)];
    sheet_().appendRow(row);
    const rows = [['Slot', berlin + ' (Berlin) · ' + iso + ' UTC'], ['Candidate time', d.local || ''], ['Name', d.name], ['Email', d.email],
      ['Level', 'Level ' + d.level], ['Window sat', d.window], ['Result', d.result], ['Country', d.country], ['Time zone', d.tz],
      ['How they prepared', d.prep], ['What they want', d.goals]];
    const html = '<p>New 1-to-1 retake session request from firstprinciples.courses. Reply to this email to confirm and send the payment link.</p><table cellpadding="6" style="border-collapse:collapse">' +
      rows.map(function (r) { return '<tr><td style="border:1px solid #ddd;font-weight:bold;vertical-align:top">' + esc_(r[0]) + '</td><td style="border:1px solid #ddd;white-space:pre-wrap">' + esc_(r[1] || '') + '</td></tr>'; }).join('') +
      '</table><p>The slot is now blocked on the website. To free it, set Status to "Declined" or "Cancelled" in the Requests sheet: ' + SpreadsheetApp.openById(BOOK_ID).getUrl() + '</p>';
    MailApp.sendEmail({ to: OWNER, replyTo: String(d.email), name: 'First Principles bookings',
      subject: '1-to-1 request: Level ' + d.level + ', ' + berlin + ' (Berlin) - ' + String(d.name).slice(0, 60), htmlBody: html });
    return out_({ ok: true });
  } finally { lock.releaseLock(); }
}
