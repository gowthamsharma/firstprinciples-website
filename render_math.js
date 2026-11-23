// Renders LaTeX to HTML for build_site.py. Input (stdin): JSON [[tex, displayMode], ...]. Output: JSON [html, ...].
const katex = require('katex');
let s = '';
process.stdin.on('data', d => s += d).on('end', () => {
  const items = JSON.parse(s);
  const out = items.map(([tex, display]) => {
    try { return katex.renderToString(tex, { displayMode: !!display, throwOnError: true, output: 'htmlAndMathml', strict: false }); }
    catch (e) { process.stderr.write('KaTeX error in: ' + tex + '\n  ' + e.message + '\n'); return katex.renderToString(tex, { displayMode: !!display, throwOnError: false, strict: false }); }
  });
  process.stdout.write(JSON.stringify(out));
});
