/* BA II Plus-style financial calculator: an original JavaScript replica of the key layout and behaviour
   (standard calculator in Chn or AOS, memories, TVM, amortisation, cash flows, bond, depreciation,
   statistics, percent change, interest conversion, date, profit margin, breakeven, formats, reset).
   First Principles, 2026. Written from scratch; no Texas Instruments code or firmware is used.
   BA II PLUS is a trademark of Texas Instruments. */
(function (root) {
  "use strict";

  /* ---------------------------------------------------------------- keys */
  // [id, primary label, second label, second id]
  var LAYOUT = [
    [["CPT", "CPT", "QUIT", "QUIT"], ["ENTER", "ENTER", "SET", "SET"], ["UP", "↑", "DEL", "DEL"], ["DOWN", "↓", "INS", "INS"], ["ONOFF", "ON|OFF", "", ""]],
    [["2ND", "2ND", "", ""], ["CF", "CF", "", ""], ["NPV", "NPV", "", ""], ["IRR", "IRR", "", ""], ["BS", "→", "", ""]],
    [["N", "N", "xP/Y", "XPY"], ["IY", "I/Y", "P/Y", "PY"], ["PV", "PV", "AMORT", "AMORT"], ["PMT", "PMT", "BGN", "BGN"], ["FV", "FV", "CLR TVM", "CLRTVM"]],
    [["PCT", "%", "K", "K"], ["SQRT", "√x", "RAND", "RAND"], ["SQ", "x²", "", ""], ["RECIP", "1/x", "", ""], ["DIV", "÷", "", ""]],
    [["INV", "INV", "HYP", "HYP"], ["LP", "(", "SIN", "SIN"], ["RP", ")", "COS", "COS"], ["POW", "yˣ", "TAN", "TAN"], ["MUL", "×", "x!", "FACT"]],
    [["LN", "LN", "eˣ", "EXP"], ["7", "7", "DATA", "DATA"], ["8", "8", "STAT", "STAT"], ["9", "9", "BOND", "BOND"], ["SUB", "−", "nPr", "NPR"]],
    [["STO", "STO", "ROUND", "ROUND"], ["4", "4", "DEPR", "DEPR"], ["5", "5", "Δ%", "DPCT"], ["6", "6", "BRKEVN", "BRKEVN"], ["ADD", "+", "nCr", "NCR"]],
    [["RCL", "RCL", "", ""], ["1", "1", "DATE", "DATE"], ["2", "2", "ICONV", "ICONV"], ["3", "3", "PROFIT", "PROFIT"], ["EQ", "=", "ANS", "ANS"]],
    [["CE", "CE|C", "CLR WORK", "CLRWORK"], ["0", "0", "MEM", "MEM"], ["DOT", ".", "FORMAT", "FORMAT"], ["NEG", "+|−", "RESET", "RESET"]]
  ];
  var KEY = {}, SECOND = {}, SECOND_OF = {};
  LAYOUT.forEach(function (row, r) {
    row.forEach(function (k, c) {
      KEY[k[0]] = { id: k[0], label: k[1], sec: k[2], secId: k[3], row: r, col: c };
      if (k[3]) { SECOND[k[0]] = k[3]; SECOND_OF[k[3]] = k[0]; }
    });
  });
  var BIN = { ADD: 1, SUB: 1, MUL: 2, DIV: 2, POW: 3, NPR: 3, NCR: 3 };
  var DAYS = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];

  /* ---------------------------------------------------------------- maths helpers */
  function r13(x) { // the calculator keeps 13 significant digits
    if (!isFinite(x) || x === 0) return x;
    return parseFloat(x.toPrecision(13));
  }
  function roundTo(x, d) { var f = Math.pow(10, d); return Math.round((x + (x >= 0 ? 1e-12 : -1e-12)) * f) / f; }
  function fact(n) { var r = 1; for (var i = 2; i <= n; i++) r *= i; return r; }

  function CalcError(n) { this.code = n; }
  function err(n) { throw new CalcError(n); }
  function chk(x) { if (!isFinite(x) || Math.abs(x) > 9.9999999999999e99) err(1); return r13(x); }

  /* dates are stored as day numbers (UTC days since 1970-01-01) */
  function dnum(y, m, d) { return Math.round(Date.UTC(y, m - 1, d) / 864e5); }
  function dparts(n) { var t = new Date(n * 864e5); return { y: t.getUTCFullYear(), m: t.getUTCMonth() + 1, d: t.getUTCDate(), w: t.getUTCDay() }; }
  function d360(a, b) {
    var p = dparts(a), q = dparts(b), d1 = p.d, d2 = q.d;
    if (d1 === 31) d1 = 30;
    if (d2 === 31 && d1 >= 30) d2 = 30;
    return (q.y - p.y) * 360 + (q.m - p.m) * 30 + (d2 - d1);
  }
  function addMonths(n, k, eom) {
    var p = dparts(n), m = p.m - 1 + k, y = p.y + Math.floor(m / 12); m = ((m % 12) + 12) % 12;
    var last = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    return dnum(y, m + 1, eom ? last : Math.min(p.d, last));
  }

  /* simple root finder: bracket by scanning, then bisect */
  function solve(f, lo, hi, steps) {
    var best = null, prevx = lo, prevf = f(lo);
    for (var k = 1; k <= steps; k++) {
      var x = lo + (hi - lo) * k / steps, fx = f(x);
      if (isFinite(prevf) && isFinite(fx) && (prevf === 0 || prevf * fx < 0)) {
        var a = prevx, b = x, fa = prevf;
        if (prevf === 0) { b = a; }
        for (var it = 0; it < 200 && b - a > 1e-15 * Math.max(1, Math.abs(a)); it++) {
          var m = (a + b) / 2, fm = f(m);
          if (fa * fm <= 0) b = m; else { a = m; fa = fm; }
        }
        var root = (a + b) / 2;
        if (best === null || Math.abs(root) < Math.abs(best)) best = root;
      }
      prevx = x; prevf = fx;
    }
    return best;
  }

  /* ---------------------------------------------------------------- the engine */
  function Engine() { this.factory(); }

  Engine.prototype.factory = function () {
    this.on = true;
    this.fmt = { dec: 2, rad: false, eurDate: false, eurSep: false, aos: false };
    this.mem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    this.tvm = { N: 0, IY: 0, PV: 0, PMT: 0, FV: 0, PY: 1, CY: 1, BGN: false };
    this.amort = { P1: 1, P2: 1 };
    this.cf = { CF0: 0, C: [], F: [], I: 0 };
    this.bond = { SDT: dnum(1990, 12, 31), CPN: 0, RDT: dnum(1990, 12, 31), RV: 100, ACT: true, two: true, YLD: 0, PRI: 0 };
    this.depr = { method: "SL", DB: 200, LIF: 1, M01: 1, CST: 0, SAL: 0, YR: 1 };
    this.stat = { X: [], Y: [], method: "LIN", XP: 0, YP: 0 };
    this.pct = { OLD: 0, NEW: 0, CH: 0, PD: 1 };
    this.iconv = { NOM: 0, EFF: 0, CY: 1 };
    this.date = { DT1: dnum(1990, 12, 31), DT2: dnum(1990, 12, 31), DBD: 0, ACT: true };
    this.profit = { CST: 0, SEL: 0, MAR: 0 };
    this.brk = { FC: 0, VC: 0, P: 0, PFT: 0, Q: 0 };
    this.seed = 1;
    this.lastAns = 0;
    this.clearStd();
    this.ws = null;
  };

  Engine.prototype.clearStd = function () {
    this.x = 0; this.entry = null; this.vals = []; this.ops = []; this.err = null;
    this.second = false; this.inv = false; this.hyp = false; this.pend = null; this.cpt = false;
    this.label = ""; this.eq = false; this.flag = ""; this.konst = null; this.lastKey = null; this.note = "";
    this.reset = false; this.dayName = "";
  };

  /* current number on screen */
  Engine.prototype.val = function () {
    if (this.entry !== null) {
      var s = this.entry.replace(/^-/, ""), v = parseFloat(s === "" || s === "." ? "0" : s);
      return this.entry.charAt(0) === "-" ? -v : v;
    }
    return this.x;
  };
  Engine.prototype.commit = function () { this.x = this.val(); this.entry = null; return this.x; };
  Engine.prototype.result = function (v) { this.x = chk(v); this.entry = null; };

  /* ---------------------------------------------------------------- expression handling */
  Engine.prototype.prec = function (op) { return this.fmt.aos ? BIN[op] : 1; };
  Engine.prototype.apply = function (a, op, b) {
    switch (op) {
      case "ADD": return chk(a + b);
      case "SUB": return chk(a - b);
      case "MUL": return chk(a * b);
      case "DIV": if (b === 0) err(1); return chk(a / b);
      case "POW":
        if (a < 0 && Math.round(b) !== b && Math.round(1 / b) % 2 !== 1) err(2);
        if (a < 0 && Math.round(b) !== b) return chk(-Math.pow(-a, b));
        return chk(Math.pow(a, b));
      case "NPR": case "NCR":
        if (a <= 0 || b <= 0 || a !== Math.round(a) || b !== Math.round(b) || b > a || a > 69) err(2);
        var p = fact(a) / fact(a - b); return chk(op === "NPR" ? p : p / fact(b));
    }
  };
  Engine.prototype.reduceWhile = function (minPrec) {
    while (this.ops.length && this.ops[this.ops.length - 1] !== "LP" && this.prec(this.ops[this.ops.length - 1]) >= minPrec) {
      var b = this.vals.pop(), a = this.vals.pop();
      this.vals.push(this.apply(a, this.ops.pop(), b));
    }
  };
  Engine.prototype.binary = function (op) {
    this.konst = null; this.kpend = null;
    var v = this.commit();
    if (this.lastKey && BIN[this.lastKey] && this.ops.length && this.ops[this.ops.length - 1] !== "LP") { this.ops[this.ops.length - 1] = op; return; }
    this.vals.push(v);
    this.reduceWhile(this.prec(op));
    if (this.ops.length >= 8) err(3);
    this.ops.push(op);
    this.x = this.vals[this.vals.length - 1];
  };
  Engine.prototype.equals = function () {
    var v = this.commit();
    if (this.kpend && this.vals.length) { this.konst = { op: this.kpend, c: v }; this.kpend = null; }
    if (!this.vals.length && this.konst && (this.lastKey === "num" || this.lastKey === "EQ")) {
      this.result(this.apply(v, this.konst.op, this.konst.c));
      this.lastAns = this.x; return;
    }
    this.vals.push(v);
    while (this.ops.length) {
      if (this.ops[this.ops.length - 1] === "LP") { this.ops.pop(); continue; }
      var b = this.vals.pop(), a = this.vals.pop();
      this.vals.push(this.apply(a, this.ops.pop(), b));
    }
    this.result(this.vals.pop()); this.vals = []; this.lastAns = this.x;
  };

  /* ---------------------------------------------------------------- TVM */
  Engine.prototype.rate = function (iy) {
    var t = this.tvm; if (t.PY <= 0 || t.CY <= 0) err(4);
    return Math.pow(1 + iy / (100 * t.CY), t.CY / t.PY) - 1;
  };
  Engine.prototype.tvmF = function (N, i, PV, PMT, FV) {
    var k = this.tvm.BGN ? 1 : 0;
    if (Math.abs(i) < 1e-14) return PV + PMT * N + FV;
    var v = Math.pow(1 + i, -N);
    return PV + PMT * (1 + i * k) * (1 - v) / i + FV * v;
  };
  Engine.prototype.tvmCompute = function (name) {
    var t = this.tvm, k = t.BGN ? 1 : 0, i = this.rate(t.IY), v, a, out;
    if (name === "IY") {
      var s = [t.PV, t.PMT, t.FV].filter(function (z) { return z !== 0; });
      if (s.every(function (z) { return z > 0; }) || s.every(function (z) { return z < 0; })) err(5);
      var self = this, f = function (r) { return self.tvmF(t.N, r, t.PV, t.PMT, t.FV); };
      var r = solve(f, -0.9999, 1, 4000);
      if (r === null) r = solve(f, 1, 50, 2000);
      if (r === null) err(7);
      out = 100 * t.CY * (Math.pow(1 + r, t.PY / t.CY) - 1);
    } else if (Math.abs(i) < 1e-14) {
      if (name === "N") { if (t.PMT === 0) err(5); out = -(t.PV + t.FV) / t.PMT; }
      if (name === "PV") out = -(t.PMT * t.N + t.FV);
      if (name === "PMT") { if (t.N === 0) err(5); out = -(t.PV + t.FV) / t.N; }
      if (name === "FV") out = -(t.PV + t.PMT * t.N);
    } else {
      v = Math.pow(1 + i, -t.N); a = (1 - v) / i;
      if (name === "PV") out = -(t.PMT * (1 + i * k) * a + t.FV * v);
      if (name === "FV") out = -(t.PV + t.PMT * (1 + i * k) * a) / v;
      if (name === "PMT") { if (t.N === 0) err(5); out = -(t.PV + t.FV * v) / ((1 + i * k) * a); }
      if (name === "N") {
        var G = t.PMT * (1 + i * k) / i, arg = (G - t.FV) / (t.PV + G);
        if (!(arg > 0)) err(5);
        out = Math.log(arg) / Math.log(1 + i);
      }
    }
    t[name] = chk(out);
    return t[name];
  };

  /* ---------------------------------------------------------------- amortisation */
  Engine.prototype.amortCalc = function () {
    var t = this.tvm, p1 = this.amort.P1, p2 = this.amort.P2;
    if (p2 < p1) err(2);
    var d = this.fmt.dec, i = this.rate(t.IY), pmt = roundTo(t.PMT, d), bal = t.PV, prn = 0, int = 0;
    for (var k = 1; k <= p2; k++) {
      var base = t.BGN ? bal + pmt : bal, ik = -roundTo(base * i, d);
      if (t.BGN && k === 1) ik = 0;
      var pk = pmt - ik;
      bal = roundTo(bal + pk, d);
      if (k >= p1) { prn += pk; int += ik; }
    }
    return { BAL: r13(bal), PRN: r13(prn), INT: r13(int) };
  };

  /* ---------------------------------------------------------------- cash flows */
  Engine.prototype.npv = function (r) {
    var c = this.cf, s = c.CF0, t = 0;
    for (var j = 0; j < c.C.length; j++) for (var f = 0; f < c.F[j]; f++) { t++; s += c.C[j] / Math.pow(1 + r, t); }
    return s;
  };
  Engine.prototype.irr = function () {
    var c = this.cf, all = [c.CF0].concat(c.C), pos = all.some(function (z) { return z > 0; }), neg = all.some(function (z) { return z < 0; });
    if (!pos || !neg) err(5);
    var self = this, r = solve(function (x) { return self.npv(x); }, -0.9999, 1, 4000);
    if (r === null) r = solve(function (x) { return self.npv(x); }, 1, 100, 4000);
    if (r === null) err(7);
    return chk(100 * r);
  };

  /* ---------------------------------------------------------------- bond (standard securities methods) */
  Engine.prototype.bondSetup = function () {
    var b = this.bond, M = b.two ? 2 : 1, step = 12 / M;
    if (b.RDT <= b.SDT) err(6);
    if (b.RV <= 0 || b.CPN < 0) err(4);
    var eom = dparts(b.RDT).d === new Date(Date.UTC(dparts(b.RDT).y, dparts(b.RDT).m, 0)).getUTCDate();
    var next = b.RDT, n = 0, prev;
    while (true) { prev = addMonths(b.RDT, -step * (n + 1), eom); if (prev <= b.SDT) break; next = prev; n++; }
    var N = n + 1, E, A, DSC, DSR;
    if (b.ACT) { E = next - prev; A = b.SDT - prev; DSC = next - b.SDT; DSR = b.RDT - b.SDT; }
    else { E = 360 / M; A = d360(prev, b.SDT); DSC = E - A; DSR = d360(b.SDT, b.RDT); }
    return { M: M, N: N, E: E, A: A, DSC: DSC, DSR: DSR, C: b.CPN / M };
  };
  Engine.prototype.bondPrice = function (Y) {
    var b = this.bond, s = this.bondSetup(), y = Y / 100 / s.M;
    if (s.N === 1) return (b.RV + s.C) / (1 + (s.DSR / s.E) * y) - (s.A / s.E) * s.C;
    var p = b.RV / Math.pow(1 + y, s.N - 1 + s.DSC / s.E);
    for (var K = 1; K <= s.N; K++) p += s.C / Math.pow(1 + y, K - 1 + s.DSC / s.E);
    return p - (s.A / s.E) * s.C;
  };
  Engine.prototype.bondAI = function () { var s = this.bondSetup(); return s.C * s.A / s.E; };

  /* ---------------------------------------------------------------- depreciation */
  Engine.prototype.deprCalc = function () {
    var p = this.depr, d = this.fmt.dec, L = p.LIF, cst = p.CST, sal = p.SAL, f1 = (13 - p.M01) / 12;
    if (sal > cst) err(2);
    if (L <= 0 || p.YR <= 0 || p.M01 < 1 || p.M01 >= 13) err(4);
    var rbv = cst, dep = 0, syd = L * (L + 1) / 2;
    var Dk = function (k) { return (k >= 1 && k <= L) ? (cst - sal) * (L - k + 1) / syd : 0; };
    for (var y = 1; y <= p.YR; y++) {
      var rdv = rbv - sal, frac = (y === 1) ? f1 : 1;
      if (p.method === "SL") dep = (cst - sal) / L * frac;
      else if (p.method === "SYD") dep = y === 1 ? f1 * Dk(1) : f1 * Dk(y) + (1 - f1) * Dk(y - 1);
      else {
        var rate = p.DB / (100 * L);
        dep = rbv * rate * frac;
        if (p.method === "DBX") {
          var left = L - (y === 1 ? 0 : f1 + (y - 2));
          var sl = left > 0 ? (rbv - sal) / left * frac : rdv;
          if (sl > dep) dep = sl;
        }
      }
      dep = roundTo(Math.min(Math.max(dep, 0), rdv), d);
      var lastYear = Math.ceil(L + (f1 < 1 ? 1 : 0) - 1e-9);
      if (y >= lastYear) dep = roundTo(rdv, d);
      if (y > lastYear) dep = 0;
      rbv = roundTo(rbv - dep, d);
    }
    return { DEP: dep, RBV: rbv, RDV: roundTo(rbv - sal, d) };
  };

  /* ---------------------------------------------------------------- statistics */
  Engine.prototype.statCalc = function () {
    var s = this.stat, one = s.method === "1-V", n = 0, sx = 0, sxx = 0, sy = 0, syy = 0, sxy = 0, tx = 0, ty = 0, txx = 0, tyy = 0, txy = 0;
    for (var k = 0; k < s.X.length; k++) {
      var x = s.X[k], y = s.Y[k];
      if (one) { n += y; sx += y * x; sxx += y * x * x; continue; }
      n++; sx += x; sxx += x * x; sy += y; syy += y * y; sxy += x * y;
      var X = (s.method === "Ln" || s.method === "PWR") ? Math.log(x) : x, Y = (s.method === "EXP" || s.method === "PWR") ? Math.log(y) : y;
      tx += X; ty += Y; txx += X * X; tyy += Y * Y; txy += X * Y;
    }
    var o = { n: n, SX: sx, SXX: sxx, SY: sy, SYY: syy, SXY: sxy };
    if (n === 0) return o;
    o.xbar = sx / n; o.Sx = n > 1 ? Math.sqrt(Math.max(0, (sxx - n * o.xbar * o.xbar) / (n - 1))) : 0; o.sx = Math.sqrt(Math.max(0, sxx / n - o.xbar * o.xbar));
    if (!one) {
      o.ybar = sy / n; o.Sy = n > 1 ? Math.sqrt(Math.max(0, (syy - n * o.ybar * o.ybar) / (n - 1))) : 0; o.sy = Math.sqrt(Math.max(0, syy / n - o.ybar * o.ybar));
      var den = n * txx - tx * tx;
      if (den !== 0) {
        o.b = (n * txy - tx * ty) / den; var a0 = (ty - o.b * tx) / n;
        o.a = (s.method === "EXP" || s.method === "PWR") ? Math.exp(a0) : a0;
        var dr = Math.sqrt(den * (n * tyy - ty * ty)); o.r = dr ? (n * txy - tx * ty) / dr : 0;
      }
    }
    return o;
  };
  Engine.prototype.predict = function (x, inverse) {
    var o = this.statCalc(), m = this.stat.method, a = o.a, b = o.b;
    if (a === undefined) err(1);
    if (!inverse) {
      if (m === "LIN") return a + b * x; if (m === "Ln") return a + b * Math.log(x);
      if (m === "EXP") return a * Math.exp(b * x); return a * Math.pow(x, b);
    }
    var y = x;
    if (m === "LIN") return (y - a) / b; if (m === "Ln") return Math.exp((y - a) / b);
    if (m === "EXP") return Math.log(y / a) / b; return Math.pow(y / a, 1 / b);
  };

  /* ---------------------------------------------------------------- dates */
  Engine.prototype.parseDate = function (v) {
    var s = Math.abs(v).toFixed(4), ip = parseInt(s, 10), fr = s.split(".")[1];
    var a = ip, b = parseInt(fr.slice(0, 2), 10), yy = parseInt(fr.slice(2, 4), 10);
    var m = this.fmt.eurDate ? b : a, d = this.fmt.eurDate ? a : b, y = yy < 80 ? 2000 + yy : 1900 + yy;
    var t = dparts(dnum(y, m, d));
    if (m < 1 || m > 12 || t.m !== m || t.d !== d) err(6);
    return dnum(y, m, d);
  };
  Engine.prototype.showDate = function (n) {
    var p = dparts(n), dd = (p.d < 10 ? "0" : "") + p.d;
    return this.fmt.eurDate ? (p.d + "-" + (p.m < 10 ? "0" : "") + p.m + "-" + p.y) : (p.m + "-" + dd + "-" + p.y);
  };

  /* ---------------------------------------------------------------- worksheets */
  function V(label, type, get, set, extra) { var o = { label: label, type: type, get: get, set: set }; for (var k in extra || {}) o[k] = extra[k]; return o; }

  Engine.prototype.sheet = function (name) {
    var e = this, t = this.tvm;
    switch (name) {
      case "PY": return [V("P/Y", "enter", function () { return t.PY; }, function (v) { if (v <= 0) err(4); t.PY = v; t.CY = v; }),
                         V("C/Y", "enter", function () { return t.CY; }, function (v) { if (v <= 0) err(4); t.CY = v; })];
      case "BGN": return [V(function () { return t.BGN ? "BGN" : "END"; }, "setting", null, null, { toggle: function () { t.BGN = !t.BGN; } })];
      case "AMORT": return [
        V("P1", "enter", function () { return e.amort.P1; }, function (v) { if (v < 1 || v > 9999 || v !== Math.round(v)) err(4); e.amort.P1 = v; }, { cpt: function () { var w = e.amort.P2 - e.amort.P1 + 1; e.amort.P1 += w; e.amort.P2 += w; return e.amort.P1; } }),
        V("P2", "enter", function () { return e.amort.P2; }, function (v) { if (v < 1 || v > 9999 || v !== Math.round(v)) err(4); e.amort.P2 = v; }, { cpt: function () { var w = e.amort.P2 - e.amort.P1 + 1; e.amort.P1 += w; e.amort.P2 += w; return e.amort.P2; } }),
        V("BAL", "auto", function () { return e.amortCalc().BAL; }), V("PRN", "auto", function () { return e.amortCalc().PRN; }), V("INT", "auto", function () { return e.amortCalc().INT; })];
      case "CF": {
        var c = this.cf, list = [V("CFo", "enter", function () { return c.CF0; }, function (v) { c.CF0 = v; })];
        var addPair = function (j) {
          var nn = (j + 1 < 10 ? "0" : "") + (j + 1);
          list.push(V("C" + nn, "enter", function () { return c.C[j] || 0; }, function (v) { if (j >= c.C.length) { if (j >= 24) err(4); c.C.push(v); c.F.push(1); } else c.C[j] = v; }, { cfIndex: j }));
          if (j < c.C.length) list.push(V("F" + nn, "enter", function () { return c.F[j]; }, function (v) { if (v < 0.5 || v > 9999) err(4); c.F[j] = v; }, { cfIndex: j }));
        };
        for (var j = 0; j < c.C.length; j++) addPair(j);
        if (c.C.length < 24) addPair(c.C.length);
        return list;
      }
      case "NPV": return [V("I", "enter", function () { return e.cf.I; }, function (v) { e.cf.I = v; }),
                          V("NPV", "compute", function () { return e.cfNPV || 0; }, null, { cpt: function () { return (e.cfNPV = chk(e.npv(e.cf.I / 100))); } })];
      case "IRR": return [V("IRR", "compute", function () { return e.cfIRR || 0; }, null, { cpt: function () { return (e.cfIRR = e.irr()); } })];
      case "BOND": {
        var b = this.bond;
        return [V("SDT", "date", function () { return b.SDT; }, function (v) { b.SDT = e.parseDate(v); }),
                V("CPN", "enter", function () { return b.CPN; }, function (v) { if (v < 0) err(4); b.CPN = v; }),
                V("RDT", "date", function () { return b.RDT; }, function (v) { b.RDT = e.parseDate(v); }),
                V("RV", "enter", function () { return b.RV; }, function (v) { if (v <= 0) err(4); b.RV = v; }),
                V(function () { return b.ACT ? "ACT" : "360"; }, "setting", null, null, { toggle: function () { b.ACT = !b.ACT; } }),
                V(function () { return b.two ? "2/Y" : "1/Y"; }, "setting", null, null, { toggle: function () { b.two = !b.two; } }),
                V("YLD", "ec", function () { return b.YLD; }, function (v) { b.YLD = v; }, { cpt: function () {
                  if (b.PRI <= 0) err(4);
                  var r = solve(function (y) { return e.bondPrice(y) - b.PRI; }, -99, 300, 8000); if (r === null) err(7); return (b.YLD = chk(r)); } }),
                V("PRI", "ec", function () { return b.PRI; }, function (v) { if (v <= 0) err(4); b.PRI = v; }, { cpt: function () { return (b.PRI = chk(e.bondPrice(b.YLD))); } }),
                V("AI", "auto", function () { return e.bondAI(); })];
      }
      case "DEPR": {
        var p = this.depr, M = ["SL", "SYD", "DB", "DBX"];
        return [V(function () { return p.method; }, function () { return (p.method === "DB" || p.method === "DBX") ? "settingenter" : "setting"; },
                  function () { return p.DB; }, function (v) { if (v <= 0) err(4); p.DB = v; }, { toggle: function () { p.method = M[(M.indexOf(p.method) + 1) % M.length]; } }),
                V("LIF", "enter", function () { return p.LIF; }, function (v) { if (v <= 0) err(4); p.LIF = v; }),
                V("M01", "enter", function () { return p.M01; }, function (v) { if (v < 1 || v >= 13) err(4); p.M01 = v; }),
                V("CST", "enter", function () { return p.CST; }, function (v) { if (v < 0) err(4); p.CST = v; }),
                V("SAL", "enter", function () { return p.SAL; }, function (v) { if (v < 0) err(4); p.SAL = v; }),
                V("YR", "enter", function () { return p.YR; }, function (v) { if (v <= 0 || v !== Math.round(v)) err(4); p.YR = v; }, { cpt: function () { return ++p.YR; } }),
                V("DEP", "auto", function () { return e.deprCalc().DEP; }), V("RBV", "auto", function () { return e.deprCalc().RBV; }), V("RDV", "auto", function () { return e.deprCalc().RDV; })];
      }
      case "DATA": {
        var s = this.stat, l = [];
        var add = function (j) {
          var nn = (j + 1 < 10 ? "0" : "") + (j + 1);
          l.push(V("X" + nn, "enter", function () { return s.X[j] || 0; }, function (v) { if (j >= s.X.length) { if (j >= 50) err(4); s.X.push(v); s.Y.push(1); } else s.X[j] = v; }, { dataIndex: j }));
          l.push(V("Y" + nn, "enter", function () { return j < s.Y.length ? s.Y[j] : 1; }, function (v) { if (j >= s.X.length) { s.X.push(0); s.Y.push(v); } else s.Y[j] = v; }, { dataIndex: j }));
        };
        for (var q = 0; q < s.X.length; q++) add(q);
        if (s.X.length < 50) add(s.X.length);
        return l;
      }
      case "STAT": {
        var st = this.stat, one = st.method === "1-V", O = function (k) { return function () { var o = e.statCalc(); if (o.n === 0 && k !== "n") err(1); return o[k] === undefined ? err(1) : o[k]; }; };
        var MS = ["LIN", "Ln", "EXP", "PWR", "1-V"];
        var l2 = [V(function () { return st.method; }, "setting", null, null, { toggle: function () { st.method = MS[(MS.indexOf(st.method) + 1) % MS.length]; } }),
                  V("n", "auto", O("n")), V("x̄", "auto", O("xbar")), V("Sx", "auto", O("Sx")), V("σx", "auto", O("sx"))];
        if (!one) l2 = l2.concat([V("ȳ", "auto", O("ybar")), V("Sy", "auto", O("Sy")), V("σy", "auto", O("sy")), V("a", "auto", O("a")), V("b", "auto", O("b")), V("r", "auto", O("r")),
                  V("X'", "ec", function () { return st.XP; }, function (v) { st.XP = v; }, { cpt: function () { return (st.XP = chk(e.predict(st.YP, true))); } }),
                  V("Y'", "ec", function () { return st.YP; }, function (v) { st.YP = v; }, { cpt: function () { return (st.YP = chk(e.predict(st.XP, false))); } })]);
        l2 = l2.concat([V("Σx", "auto", O("SX")), V("Σx²", "auto", O("SXX"))]);
        if (!one) l2 = l2.concat([V("Σy", "auto", O("SY")), V("Σy²", "auto", O("SYY")), V("Σxy", "auto", O("SXY"))]);
        return l2;
      }
      case "DPCT": {
        var c2 = this.pct, g = function () { return c2; };
        return [V("OLD", "ec", function () { return c2.OLD; }, function (v) { c2.OLD = v; }, { cpt: function () { return (c2.OLD = chk(c2.NEW / Math.pow(1 + c2.CH / 100, c2.PD))); } }),
                V("NEW", "ec", function () { return c2.NEW; }, function (v) { c2.NEW = v; }, { cpt: function () { return (c2.NEW = chk(c2.OLD * Math.pow(1 + c2.CH / 100, c2.PD))); } }),
                V("%CH", "ec", function () { return c2.CH; }, function (v) { c2.CH = v; }, { cpt: function () { if (c2.OLD === 0) err(1); return (c2.CH = chk(100 * (Math.pow(c2.NEW / c2.OLD, 1 / c2.PD) - 1))); } }),
                V("#PD", "ec", function () { return c2.PD; }, function (v) { c2.PD = v; }, { cpt: function () { var q = c2.NEW / c2.OLD; if (!(q > 0)) err(5); return (c2.PD = chk(Math.log(q) / Math.log(1 + c2.CH / 100))); } })];
      }
      case "ICONV": {
        var ic = this.iconv;
        return [V("NOM", "ec", function () { return ic.NOM; }, function (v) { ic.NOM = v; }, { cpt: function () { return (ic.NOM = chk(100 * ic.CY * (Math.pow(1 + ic.EFF / 100, 1 / ic.CY) - 1))); } }),
                V("EFF", "ec", function () { return ic.EFF; }, function (v) { ic.EFF = v; }, { cpt: function () { return (ic.EFF = chk(100 * (Math.pow(1 + ic.NOM / (100 * ic.CY), ic.CY) - 1))); } }),
                V("C/Y", "enter", function () { return ic.CY; }, function (v) { if (v <= 0) err(4); ic.CY = v; })];
      }
      case "DATE": {
        var dt = this.date, diff = function () { return dt.ACT ? dt.DT2 - dt.DT1 : d360(dt.DT1, dt.DT2); };
        var rng = function (n) { if (n < dnum(1980, 1, 1) || n > dnum(2079, 12, 31)) err(4); return n; };
        return [V("DT1", "date", function () { return dt.DT1; }, function (v) { dt.DT1 = e.parseDate(v); }, { cpt: function () { if (!dt.ACT) err(5); return (dt.DT1 = rng(dt.DT2 - dt.DBD)); } }),
                V("DT2", "date", function () { return dt.DT2; }, function (v) { dt.DT2 = e.parseDate(v); }, { cpt: function () { if (!dt.ACT) err(5); return (dt.DT2 = rng(dt.DT1 + dt.DBD)); } }),
                V("DBD", "ec", function () { return dt.DBD; }, function (v) { dt.DBD = v; }, { cpt: function () { return (dt.DBD = diff()); } }),
                V(function () { return dt.ACT ? "ACT" : "360"; }, "setting", null, null, { toggle: function () { dt.ACT = !dt.ACT; } })];
      }
      case "PROFIT": {
        var pr = this.profit;
        return [V("CST", "ec", function () { return pr.CST; }, function (v) { pr.CST = v; }, { cpt: function () { return (pr.CST = chk(pr.SEL * (1 - pr.MAR / 100))); } }),
                V("SEL", "ec", function () { return pr.SEL; }, function (v) { pr.SEL = v; }, { cpt: function () { if (pr.MAR === 100) err(1); return (pr.SEL = chk(pr.CST / (1 - pr.MAR / 100))); } }),
                V("MAR", "ec", function () { return pr.MAR; }, function (v) { pr.MAR = v; }, { cpt: function () { if (pr.SEL === 0) err(1); return (pr.MAR = chk(100 * (pr.SEL - pr.CST) / pr.SEL)); } })];
      }
      case "BRKEVN": {
        var k = this.brk;
        return [V("FC", "ec", function () { return k.FC; }, function (v) { k.FC = v; }, { cpt: function () { return (k.FC = chk(k.P * k.Q - k.VC * k.Q - k.PFT)); } }),
                V("VC", "ec", function () { return k.VC; }, function (v) { k.VC = v; }, { cpt: function () { if (k.Q === 0) err(1); return (k.VC = chk((k.P * k.Q - k.FC - k.PFT) / k.Q)); } }),
                V("P", "ec", function () { return k.P; }, function (v) { k.P = v; }, { cpt: function () { if (k.Q === 0) err(1); return (k.P = chk((k.FC + k.PFT) / k.Q + k.VC)); } }),
                V("PFT", "ec", function () { return k.PFT; }, function (v) { k.PFT = v; }, { cpt: function () { return (k.PFT = chk(k.P * k.Q - k.FC - k.VC * k.Q)); } }),
                V("Q", "ec", function () { return k.Q; }, function (v) { k.Q = v; }, { cpt: function () { if (k.P === k.VC) err(1); return (k.Q = chk((k.FC + k.PFT) / (k.P - k.VC))); } })];
      }
      case "MEM": {
        var mm = this.mem, l3 = [];
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(function (d) { l3.push(V("M" + d, "enter", function () { return mm[d]; }, function (v) { mm[d] = v; })); });
        return l3;
      }
      case "FORMAT": {
        var f = this.fmt;
        return [V("DEC", "enter", function () { return f.dec; }, function (v) { if (v < 0 || v > 9 || v !== Math.round(v)) err(4); f.dec = v; }),
                V(function () { return f.rad ? "RAD" : "DEG"; }, "setting", null, null, { toggle: function () { f.rad = !f.rad; } }),
                V(function () { return f.eurDate ? "Eur" : "US"; }, "setting", null, null, { toggle: function () { f.eurDate = !f.eurDate; }, hint: "date" }),
                V(function () { return f.eurSep ? "Eur" : "US"; }, "setting", null, null, { toggle: function () { f.eurSep = !f.eurSep; }, hint: "separator" }),
                V(function () { return f.aos ? "AOS" : "Chn"; }, "setting", null, null, { toggle: function () { f.aos = !f.aos; } })];
      }
    }
    return [];
  };

  Engine.prototype.clearSheet = function (name) {
    var e = this;
    switch (name) {
      case "PY": e.tvm.PY = 1; e.tvm.CY = 1; break;
      case "BGN": e.tvm.BGN = false; break;
      case "AMORT": e.amort = { P1: 1, P2: 1 }; break;
      case "CF": e.cf.CF0 = 0; e.cf.C = []; e.cf.F = []; break;
      case "NPV": e.cf.I = 0; e.cfNPV = 0; break;
      case "IRR": e.cfIRR = 0; break;
      case "BOND": e.bond = { SDT: dnum(1990, 12, 31), CPN: 0, RDT: dnum(1990, 12, 31), RV: 100, ACT: true, two: true, YLD: 0, PRI: 0 }; break;
      case "DEPR": e.depr.LIF = 1; e.depr.YR = 1; e.depr.CST = 0; e.depr.SAL = 0; e.depr.M01 = 1; break;
      case "DATA": e.stat.X = []; e.stat.Y = []; break;
      case "STAT": e.stat.method = "LIN"; e.stat.XP = 0; e.stat.YP = 0; break;
      case "DPCT": e.pct = { OLD: 0, NEW: 0, CH: 0, PD: 1 }; break;
      case "ICONV": e.iconv.NOM = 0; e.iconv.EFF = 0; break;
      case "DATE": e.date.DT1 = dnum(1990, 12, 31); e.date.DT2 = dnum(1990, 12, 31); e.date.DBD = 0; break;
      case "PROFIT": e.profit = { CST: 0, SEL: 0, MAR: 0 }; break;
      case "BRKEVN": e.brk = { FC: 0, VC: 0, P: 0, PFT: 0, Q: 0 }; break;
      case "MEM": e.mem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; break;
      case "FORMAT": e.fmt = { dec: 2, rad: false, eurDate: false, eurSep: false, aos: false }; break;
    }
  };

  Engine.prototype.openSheet = function (name, index) {
    this.entry = null; this.vals = []; this.ops = []; this.cpt = false; this.konst = null;
    this.ws = { name: name, i: index || 0, flag: "" };
    this.syncSheet(true);
  };
  Engine.prototype.cur = function () { var l = this.sheet(this.ws.name); if (this.ws.i >= l.length) this.ws.i = l.length - 1; return l[this.ws.i]; };
  Engine.prototype.syncSheet = function (fresh) {
    var v = this.cur(), typ = typeof v.type === "function" ? v.type() : v.type;
    this.entry = null; this.dayName = "";
    if (fresh) this.ws.flag = "";
    if (typ === "auto") { this.x = chk(v.get()); this.ws.flag = "*"; }
    else if (typ === "setting") this.x = null;
    else this.x = v.get();
    if (typ === "date" && this.ws.flag === "*") this.dayName = DAYS[dparts(this.x).w];
  };
  Engine.prototype.move = function (dir) {
    var l = this.sheet(this.ws.name), n = l.length;
    this.ws.i = (this.ws.i + dir + n) % n;
    this.ws.flag = ""; this.syncSheet(false);
  };

  /* ---------------------------------------------------------------- key dispatch */
  Engine.prototype.press = function (id) {
    try { this.dispatch(id); }
    catch (ex) {
      if (ex instanceof CalcError) { this.err = ex.code; this.entry = null; this.vals = []; this.ops = []; this.second = false; this.cpt = false; this.pend = null; }
      else throw ex;
    }
    return this;
  };

  Engine.prototype.dispatch = function (id) {
    if (id === "ONOFF") { var was = this.on; this.clearStd(); this.ws = null; this.on = !was; return; }
    if (!this.on) return;
    if (this.err) { if (id === "CE") { this.err = null; this.x = 0; this.entry = null; } else if (id === "2ND") { this.second = !this.second; } else if (this.second && id === "CPT") { this.err = null; this.second = false; this.quit(); } return; }

    if (id === "2ND") { this.second = !this.second; return; }
    if (this.second) { this.second = false; id = SECOND[id] || id; }

    if (this.reset) { this.reset = false; if (id === "ENTER") { this.factory(); this.note = "RST"; } else this.quit(); return; }

    // pending STO / RCL
    if (this.pend) {
      var pd = this.pend;
      if (/^[0-9]$/.test(id)) {
        var d = +id;
        if (pd.k === "STO") {
          var v = this.commit();
          if (pd.op) this.mem[d] = this.apply(this.mem[d], pd.op, v); else this.mem[d] = v;
        } else { this.result(this.mem[d]); }
        this.pend = null; this.lastKey = "mem"; return;
      }
      if (pd.k === "STO" && BIN[id] && !pd.op) { pd.op = id; return; }
      if (pd.k === "STO" && id === "RAND") { this.seed = Math.abs(Math.round(this.commit())) || 1; this.pend = null; return; }
      if (pd.k === "RCL" && /^(N|IY|PV|PMT|FV)$/.test(id)) {
        this.result(this.tvm[id]); this.pend = null;
        if (!this.ws) { this.label = KEY[id].label; this.eq = true; this.flag = ""; }
        return;
      }
      this.pend = null;
    }

    if (/^[0-9]$/.test(id) || id === "DOT") { this.digit(id === "DOT" ? "." : id); this.lastKey = "num"; return; }

    switch (id) {
      case "BS":
        if (this.entry !== null) { this.entry = this.entry.slice(0, -1); if (this.entry === "" || this.entry === "-") this.entry = null, this.x = 0; }
        else if (this.ws) { /* nothing */ }
        return;
      case "CE":
        if (this.entry !== null) { this.entry = null; this.x = 0; if (this.ws) this.syncSheet(false); return; }
        if (this.ws) { this.syncSheet(false); return; }
        this.vals = []; this.ops = []; this.x = 0; this.cpt = false; this.konst = null; this.label = ""; this.eq = false; this.flag = ""; return;
      case "QUIT": this.quit(); return;
      case "NEG":
        if (this.entry !== null) this.entry = this.entry.charAt(0) === "-" ? this.entry.slice(1) : "-" + this.entry;
        else if (this.x !== null) { this.entry = null; this.x = -this.x; this.negLoose = true; if (this.ws) this.ws.flag = ""; }
        return;
      case "RESET": this.ws = null; this.clearStd(); this.reset = true; return;
      case "CLRTVM": var keep = { PY: this.tvm.PY, CY: this.tvm.CY, BGN: this.tvm.BGN }; this.tvm = { N: 0, IY: 0, PV: 0, PMT: 0, FV: 0, PY: keep.PY, CY: keep.CY, BGN: keep.BGN }; this.x = 0; this.entry = null; this.label = ""; this.eq = false; this.flag = ""; return;
      case "STO": this.pend = { k: "STO" }; return;
      case "RCL": this.pend = { k: "RCL" }; return;
      case "ANS": this.result(this.lastAns); this.lastKey = "ans"; return;
      case "INV": this.inv = !this.inv; return;
      case "HYP": this.hyp = !this.hyp; return;
      case "CPT":
        if (this.ws) { this.wsCompute(); return; }
        this.cpt = true; return;
    }

    // worksheet openers
    var openers = { PY: "PY", BGN: "BGN", AMORT: "AMORT", CF: "CF", NPV: "NPV", IRR: "IRR", BOND: "BOND", DEPR: "DEPR", DATA: "DATA", STAT: "STAT", DPCT: "DPCT", ICONV: "ICONV", DATE: "DATE", PROFIT: "PROFIT", BRKEVN: "BRKEVN", MEM: "MEM", FORMAT: "FORMAT" };
    if (openers[id]) { this.label = ""; this.openSheet(openers[id]); return; }

    // TVM keys
    if (/^(N|IY|PV|PMT|FV)$/.test(id)) {
      if (this.cpt && !this.ws) { this.cpt = false; var out = this.tvmCompute(id); this.result(out); this.label = KEY[id].label; this.eq = true; this.flag = "*"; this.lastAns = out; return; }
      var v2 = this.commit(); this.tvm[id] = v2; this.lastAns = v2;
      if (!this.ws) { this.label = KEY[id].label; this.eq = true; this.flag = "◁"; }
      this.lastKey = "tvm"; return;
    }
    if (id === "XPY") { this.result(this.commit() * this.tvm.PY); this.lastKey = "fn"; return; }

    if (this.ws) {
      if (id === "UP") { this.move(-1); return; }
      if (id === "DOWN") { this.move(1); return; }
      if (id === "ENTER") { this.wsEnter(); return; }
      if (id === "SET") { this.wsSet(); return; }
      if (id === "CLRWORK") { this.clearSheet(this.ws.name); if (this.ws.name === "DATA" || this.ws.name === "CF") this.ws.i = 0; this.syncSheet(true); return; }
      if (id === "DEL" || id === "INS") { this.wsDelIns(id); return; }
    } else if (id === "UP" || id === "DOWN" || id === "ENTER" || id === "SET" || id === "DEL" || id === "INS") { return; }
    if (id === "CLRWORK") { return; }

    this.label = ""; this.eq = false; this.flag = "";
    if (BIN[id]) { if (this.ws) this.ws.flag = ""; this.binary(id); this.lastKey = id; return; }
    if (id === "EQ") { this.equals(); this.lastKey = "EQ"; return; }
    if (id === "LP") { if (this.ops.filter(function (o) { return o === "LP"; }).length >= 15) err(3); this.ops.push("LP"); this.entry = null; this.lastKey = "LP"; return; }
    if (id === "RP") {
      if (this.ops.indexOf("LP") < 0) return;
      this.vals.push(this.commit()); this.reduceWhile(-1);
      if (this.ops[this.ops.length - 1] === "LP") this.ops.pop();
      this.x = this.vals.pop(); this.lastKey = "RP"; return;
    }
    if (id === "K") {
      var top = this.ops[this.ops.length - 1];
      if (!top || top === "LP") return;
      if (this.entry === null && BIN[this.lastKey]) { this.kpend = top; return; }  // n op K c =
      var c = this.commit(); this.konst = { op: top, c: c }; this.x = c;              // n op c K =
      return;
    }
    if (id === "PCT") {
      var v3 = this.commit(), t2 = this.ops[this.ops.length - 1];
      if ((t2 === "ADD" || t2 === "SUB") && this.vals.length) this.result(this.vals[this.vals.length - 1] * v3 / 100);
      else this.result(v3 / 100);
      return;
    }
    this.unary(id);
  };

  Engine.prototype.digit = function (ch) {
    if (this.ws) { var v = this.cur(), typ = typeof v.type === "function" ? v.type() : v.type; if (typ === "setting" || typ === "auto" || (typ === "compute")) return; this.ws.flag = ""; }
    if (!this.ws) { this.label = ""; this.eq = false; this.flag = ""; }
    if (this.entry === null) this.entry = "";
    var neg = this.entry.charAt(0) === "-", body = neg ? this.entry.slice(1) : this.entry;
    if (ch === "." && body.indexOf(".") >= 0) return;
    if (body.replace(/[^0-9]/g, "").length >= 10 && ch !== ".") return;
    if (body === "0" && ch !== ".") body = "";
    if (body === "" && ch === ".") body = "0";
    this.entry = (neg ? "-" : "") + body + ch;
  };

  Engine.prototype.unary = function (id) {
    var x = this.commit(), f = this.fmt, ang = function (a) { return f.rad ? a : a * Math.PI / 180; }, unang = function (a) { return f.rad ? a : a * 180 / Math.PI; };
    var inv = this.inv, hyp = this.hyp; this.inv = false; this.hyp = false;
    var out;
    switch (id) {
      case "SQRT": if (x < 0) err(2); out = Math.sqrt(x); break;
      case "SQ": out = x * x; break;
      case "RECIP": if (x === 0) err(1); out = 1 / x; break;
      case "LN": if (inv) { out = Math.exp(x); break; } if (x <= 0) err(2); out = Math.log(x); break;
      case "EXP": out = Math.exp(x); break;
      case "FACT": if (x < 0 || x > 69 || x !== Math.round(x)) err(2); out = fact(x); break;
      case "ROUND": out = roundTo(x, f.dec === 9 ? 9 : f.dec); break;
      case "RAND": this.seed = (this.seed * 16807) % 2147483647; out = this.seed / 2147483647; break;
      case "SIN": case "COS": case "TAN":
        if (hyp) {
          var H = { SIN: [Math.sinh, Math.asinh], COS: [Math.cosh, Math.acosh], TAN: [Math.tanh, Math.atanh] }[id];
          out = inv ? H[1](x) : H[0](x); if (!isFinite(out)) err(2); break;
        }
        if (inv) { var I = { SIN: Math.asin, COS: Math.acos, TAN: Math.atan }[id]; out = unang(I(x)); if (isNaN(out)) err(2); break; }
        out = { SIN: Math.sin, COS: Math.cos, TAN: Math.tan }[id](ang(x)); if (Math.abs(out) < 1e-13) out = 0; break;
      default: return;
    }
    this.result(out); this.lastKey = "fn";
  };

  Engine.prototype.quit = function () {
    this.ws = null; this.entry = null; this.x = 0; this.vals = []; this.ops = []; this.cpt = false; this.label = ""; this.eq = false; this.flag = ""; this.konst = null; this.dayName = "";
  };

  Engine.prototype.wsEnter = function () {
    var v = this.cur(), typ = typeof v.type === "function" ? v.type() : v.type;
    if (typ === "auto" || typ === "compute" || typ === "setting") return;
    var val = this.val(); this.entry = null;
    if (typ === "date" && this.lastKey !== "num") { this.syncSheet(false); return; }
    v.set(val); this.lastAns = val;
    this.syncSheet(false); this.ws.flag = "◁";
  };
  Engine.prototype.wsSet = function () { var v = this.cur(); if (v.toggle) { v.toggle(); this.syncSheet(false); } };
  Engine.prototype.wsCompute = function () {
    var v = this.cur();
    if (!v.cpt) return;
    var out = v.cpt(); this.entry = null; this.syncSheet(false); this.ws.flag = "*"; this.lastAns = typeof out === "number" ? out : this.lastAns;
    var typ = typeof v.type === "function" ? v.type() : v.type;
    if (typ === "date") this.dayName = DAYS[dparts(this.x).w];
    if (this.ws.name === "AMORT" || (this.ws.name === "DEPR" && v.label === "YR")) this.ws.flag = "◁";
  };
  Engine.prototype.wsDelIns = function (id) {
    var v = this.cur(), w = this.ws.name;
    if (w === "CF" && v.cfIndex !== undefined && v.cfIndex < this.cf.C.length) {
      var j = v.cfIndex;
      if (id === "DEL") { this.cf.C.splice(j, 1); this.cf.F.splice(j, 1); this.ws.i = 1 + 2 * j; }
      else { if (this.cf.C.length >= 24) err(4); this.cf.C.splice(j, 0, 0); this.cf.F.splice(j, 0, 1); this.ws.i = 1 + 2 * j; }
      this.syncSheet(true);
    }
    if (w === "DATA" && v.dataIndex !== undefined && v.dataIndex < this.stat.X.length) {
      var q = v.dataIndex;
      if (id === "DEL") { this.stat.X.splice(q, 1); this.stat.Y.splice(q, 1); }
      else { this.stat.X.splice(q, 0, 0); this.stat.Y.splice(q, 0, 1); }
      this.ws.i = 2 * q; this.syncSheet(true);
    }
  };

  /* ---------------------------------------------------------------- display model */
  Engine.prototype.formatNumber = function (v) {
    var dec = this.fmt.dec, sepT = this.fmt.eurSep ? "." : ",", sepD = this.fmt.eurSep ? "," : ".";
    if (v === null || v === undefined) return "";
    if (!isFinite(v)) return "Error";
    var neg = v < 0, a = Math.abs(v), s;
    var sci = function () {
      var e = Math.floor(Math.log10(a)), m = a / Math.pow(10, e);
      if (+m.toFixed(7) >= 10) { m /= 10; e++; }
      var ms = dec === 9 ? (+m.toPrecision(8)).toString() : m.toFixed(Math.min(dec, 7));
      return { m: ms.replace(".", sepD), e: (e < 0 ? "-" : "") + (Math.abs(e) < 10 ? "0" : "") + Math.abs(e) };
    };
    if (a !== 0 && (a >= 1e10 || (dec === 9 && a < 1e-9))) { var z = sci(); return { neg: neg, text: z.m, exp: z.e }; }
    if (dec === 9) {
      var ip = Math.floor(a).toString().length; s = a.toFixed(Math.max(0, 10 - ip));
      if (s.indexOf(".") >= 0) s = s.replace(/0+$/, "").replace(/\.$/, ".");
      if (s.indexOf(".") < 0) s += ".";
    } else s = a.toFixed(dec);
    var parts = s.split("."), int = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, sepT);
    var out = int + (s.indexOf(".") >= 0 ? sepD + parts[1] : "");
    if (Math.abs(v) > 0 && +s === 0) neg = neg && false;
    return { neg: neg, text: out };
  };
  Engine.prototype.formatEntry = function () {
    var e = this.entry, neg = e.charAt(0) === "-", b = neg ? e.slice(1) : e, sepT = this.fmt.eurSep ? "." : ",", sepD = this.fmt.eurSep ? "," : ".";
    var p = b.split("."), int = (p[0] || "0").replace(/\B(?=(\d{3})+(?!\d))/g, sepT);
    return { neg: neg, text: int + (b.indexOf(".") >= 0 ? sepD + p[1] : "") };
  };

  Engine.prototype.display = function () {
    var a = { "2nd": this.second, INV: this.inv, HYP: this.hyp, COMPUTE: false, ENTER: false, SET: false, UPDN: false, DEL: false, INS: false, BGN: this.tvm.BGN, RAD: this.fmt.rad };
    var out = { on: this.on, label: "", eq: false, text: "", neg: false, exp: "", flag: "", ann: a, err: null, extra: "" };
    if (!this.on) return out;
    if (this.err) { out.err = "Error " + this.err; return out; }
    if (this.reset) { out.label = "RST ?"; a.ENTER = true; return out; }
    if (this.cpt && !this.ws) a.COMPUTE = true;
    if (this.ws) {
      var v = this.cur(), typ = typeof v.type === "function" ? v.type() : v.type, lab = typeof v.label === "function" ? v.label() : v.label;
      a.UPDN = this.sheet(this.ws.name).length > 1;
      if (typ === "enter" || typ === "date" || typ === "settingenter") a.ENTER = true;
      if (typ === "compute" || typ === "ec" || v.cpt) a.COMPUTE = typ !== "enter" || !!v.cpt;
      if (typ === "ec" ) a.ENTER = true;
      if (typ === "setting" || typ === "settingenter") a.SET = true;
      if ((this.ws.name === "CF" && v.cfIndex !== undefined) || (this.ws.name === "DATA")) { a.DEL = true; a.INS = true; }
      if (typ === "setting") { out.label = lab; if (v.hint) out.extra = v.hint; return out; }
      if (typ === "settingenter") { out.label = lab; }
      else out.label = lab;
      if (this.entry !== null) { var f = this.formatEntry(); out.text = f.text; out.neg = f.neg; return out; }
      out.eq = typ !== "settingenter";
      out.flag = this.ws.flag;
      if (typ === "date") { out.text = this.showDate(this.x); out.extra = this.dayName; return out; }
      var n = this.formatNumber(this.x); out.text = n.text; out.neg = n.neg; out.exp = n.exp || "";
      return out;
    }
    if (this.pend) { out.label = this.pend.k; }
    if (this.entry !== null) { var g = this.formatEntry(); out.text = g.text; out.neg = g.neg; return out; }
    var m = this.formatNumber(this.x); out.text = m.text; out.neg = m.neg; out.exp = m.exp || "";
    if (this.label) { out.label = this.label; out.eq = this.eq; out.flag = this.flag; }
    if (this.note === "RST") { out.label = "RST"; this.note = ""; }
    return out;
  };

  /* ---------------------------------------------------------------- recipes: friendly tokens -> key ids */
  var NAMES = { "CPT": "CPT", "ENTER": "ENTER", "UP": "UP", "DOWN": "DOWN", "↑": "UP", "↓": "DOWN", "ON/OFF": "ONOFF", "2ND": "2ND", "CF": "CF", "NPV": "NPV", "IRR": "IRR",
    "→": "BS", "BS": "BS", "N": "N", "I/Y": "IY", "PV": "PV", "PMT": "PMT", "FV": "FV", "%": "PCT", "SQRT": "SQRT", "X2": "SQ", "1/X": "RECIP", "/": "DIV", "÷": "DIV",
    "INV": "INV", "(": "LP", ")": "RP", "Y^X": "POW", "*": "MUL", "×": "MUL", "LN": "LN", "-": "SUB", "−": "SUB", "+": "ADD", "STO": "STO", "RCL": "RCL", "=": "EQ",
    "CE/C": "CE", ".": "DOT", "+/-": "NEG" };
  var SECNAMES = { "QUIT": "QUIT", "SET": "SET", "DEL": "DEL", "INS": "INS", "XP/Y": "XPY", "P/Y": "PY", "AMORT": "AMORT", "BGN": "BGN", "CLR_TVM": "CLRTVM", "K": "K", "RAND": "RAND",
    "HYP": "HYP", "SIN": "SIN", "COS": "COS", "TAN": "TAN", "X!": "FACT", "E^X": "EXP", "DATA": "DATA", "STAT": "STAT", "BOND": "BOND", "NPR": "NPR", "ROUND": "ROUND", "DEPR": "DEPR",
    "Δ%": "DPCT", "DELTA%": "DPCT", "BRKEVN": "BRKEVN", "NCR": "NCR", "DATE": "DATE", "ICONV": "ICONV", "PROFIT": "PROFIT", "ANS": "ANS", "CLR_WORK": "CLRWORK", "MEM": "MEM", "FORMAT": "FORMAT", "RESET": "RESET" };
  // returns [{keys:[ids], chip:{sec:bool,label}}]
  function parse(str) {
    var out = [];
    str.trim().split(/\s+/).forEach(function (tok) {
      if (!tok) return;
      if (tok.charAt(0) === "@") { out.push({ cmd: tok.slice(1) }); return; }
      var up = tok.toUpperCase();
      if (/^-?\d*\.?\d+$/.test(tok)) {
        var ks = []; tok.replace("-", "").split("").forEach(function (ch) { ks.push(ch === "." ? "DOT" : ch); });
        if (tok.charAt(0) === "-") ks.push("NEG");
        out.push({ keys: ks, chip: { label: tok.replace("-", "") + (tok.charAt(0) === "-" ? " +|−" : ""), num: true } }); return;
      }
      if (SECNAMES[up] && !(up in NAMES)) { var id = SECNAMES[up]; out.push({ keys: ["2ND", SECOND_OF[id]], chip: { sec: true, label: KEY[SECOND_OF[id]].sec } }); return; }
      if (NAMES[up]) { var k = NAMES[up]; out.push({ keys: [k], chip: { label: KEY[k].label } }); return; }
      if (SECNAMES[up]) { var id2 = SECNAMES[up]; out.push({ keys: ["2ND", SECOND_OF[id2]], chip: { sec: true, label: KEY[SECOND_OF[id2]].sec } }); return; }
    });
    return out;
  }

  var api = { Engine: Engine, LAYOUT: LAYOUT, KEY: KEY, SECOND: SECOND, parse: parse, dnum: dnum };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.BA2 = api;
})(typeof window !== "undefined" ? window : globalThis);

/* ======================================================================= user interface */
(function () {
  "use strict";
  if (typeof document === "undefined") return;
  var B = window.BA2;

  /* seven-segment digits */
  var SEG = { "0": "abcdef", "1": "bc", "2": "abdeg", "3": "abcdg", "4": "bcfg", "5": "acdfg", "6": "acdefg", "7": "abc", "8": "abcdefg", "9": "abcdfg", "-": "g", " ": "", "E": "adefg", "r": "eg", "o": "cdeg" };
  var POLY = {
    a: "2,1 12,1 10.5,3 3.5,3", b: "12.6,1.6 12.6,11 11,10 11,3.2", c: "12.6,13 12.6,22.4 11,20.8 11,14", d: "2,23 12,23 10.5,21 3.5,21",
    e: "1.4,13 3,14 3,20.8 1.4,22.4", f: "1.4,1.6 3,3.2 3,10 1.4,11", g: "2,12 3.5,11 10.5,11 12,12 10.5,13 3.5,13"
  };
  function segChar(ch, dp, comma) {
    var on = SEG[ch] || "", s = '<svg class="sg" viewBox="0 0 17 24" aria-hidden="true">';
    for (var k in POLY) s += '<polygon points="' + POLY[k] + '" class="' + (on.indexOf(k) >= 0 ? "on" : "off") + '"/>';
    if (dp || comma) s += '<rect x="13.6" y="20.6" width="2.4" height="2.4" class="on"/>';
    if (comma) s += '<path d="M15.6,23 L14.2,25.6" class="cm"/>';
    return s + "</svg>";
  }
  function segText(text, cells) {
    // text like "-1,234.56": separators attach to previous digit
    var out = [], i;
    for (i = 0; i < text.length; i++) {
      var ch = text.charAt(i);
      if ((ch === "." || ch === ",") && out.length) { out[out.length - 1][ch === "." ? 1 : 2] = true; continue; }
      if (ch === "." || ch === ",") { out.push(["0", ch === ".", ch === ","]); continue; }
      out.push([ch, false, false]);
    }
    while (out.length < cells) out.unshift([" ", false, false]);
    return out.map(function (c) { return segChar(c[0], c[1], c[2]); }).join("");
  }

  var CATS = {
    tvm: ["N", "IY", "PV", "PMT", "FV", "CPT"], cf: ["CF", "NPV", "IRR"], nav: ["ENTER", "UP", "DOWN", "2ND", "BS", "CE", "ONOFF"],
    ws: ["7", "8", "9", "4", "5", "6", "1", "2", "3", "DOT", "NEG"], mem: ["STO", "RCL", "0"]
  };
  var CATNAME = { tvm: "Time value of money", cf: "Cash flows (NPV, IRR)", nav: "Move, enter, clear", ws: "Worksheets (2ND + number key)", mem: "Memory", math: "Arithmetic and functions" };
  function catOf(id) { for (var c in CATS) if (CATS[c].indexOf(id) >= 0) return c; return "math"; }

  function mount(host) {
    var e = new B.Engine();
    var el = document.createElement("div");
    el.className = "ba2-calc"; el.tabIndex = 0; el.setAttribute("role", "application");
    el.setAttribute("aria-label", "Interactive financial calculator with the BA II Plus key layout. Click the keys or type on your keyboard.");
    var keysHtml = "";
    B.LAYOUT.forEach(function (row, r) {
      row.forEach(function (k, c) {
        var span = (k[0] === "EQ") ? ' style="grid-row:' + (r + 1) + ' / span 2;grid-column:' + (c + 1) + '"' : ' style="grid-row:' + (r + 1) + ';grid-column:' + (c + 1) + '"';
        var cls = "k k-" + k[0].toLowerCase() + " cat-" + catOf(k[0]) + (/^[0-9]$|^DOT$|^NEG$/.test(k[0]) ? " num" : "") + (k[0] === "2ND" ? " second" : "") + (k[0] === "ONOFF" ? " power" : "");
        keysHtml += '<div class="cell"' + span + '><span class="sec">' + (k[2] || "&nbsp;") + '</span><button type="button" class="' + cls + '" data-k="' + k[0] + '" aria-label="' + k[1] + (k[2] ? " (second: " + k[2] + ")" : "") + '">' + k[1] + "</button></div>";
      });
    });
    el.innerHTML =
      '<div class="ba2-top"><span class="ba2-brand">Financial calculator</span><span class="ba2-model">BA II PLUS layout</span></div>' +
      '<div class="ba2-lcd" aria-live="polite"><div class="ann"></div><div class="row"><div class="lab"></div><div class="num"></div></div></div>' +
      '<div class="ba2-keys">' + keysHtml + "</div>" +
      '<div class="ba2-caption" aria-hidden="true"></div>';
    host.appendChild(el);
    var tools = document.createElement("div");
    tools.className = "ba2-tools";
    tools.innerHTML = '<button type="button" data-act="exam">Exam settings</button><button type="button" data-act="reset">Reset</button><button type="button" data-act="map" aria-pressed="false">Key map</button><button type="button" data-act="speed" class="spd">Speed: slow</button>';
    var after = host.classList.contains("ba2-host") ? host.parentNode : host;
    if (after === host) host.appendChild(tools); else after.insertBefore(tools, host.nextSibling);
    var legend = document.createElement("div");
    legend.className = "ba2-legend"; legend.hidden = true;
    legend.innerHTML = Object.keys(CATNAME).map(function (c) { return '<span class="lg cat-' + c + '"><i></i>' + CATNAME[c] + "</span>"; }).join("");
    if (after === host) host.appendChild(legend); else after.insertBefore(legend, tools.nextSibling);

    var lcd = el.querySelector(".ba2-lcd"), ann = lcd.querySelector(".ann"), lab = lcd.querySelector(".lab"), num = lcd.querySelector(".num"), cap = el.querySelector(".ba2-caption");
    var ANN = ["2nd", "INV", "HYP", "COMPUTE", "ENTER", "SET", "UPDN", "DEL", "INS", "BGN", "RAD"];

    function render() {
      var d = e.display();
      el.classList.toggle("off", !d.on);
      ann.innerHTML = ANN.map(function (a) { return '<span class="' + (d.ann[a] ? "lit" : "") + '">' + (a === "UPDN" ? "↑↓" : a) + "</span>"; }).join("");
      if (!d.on) { lab.textContent = ""; num.innerHTML = ""; return; }
      if (d.err) { lab.innerHTML = '<span class="txt">' + d.err + "</span>"; num.innerHTML = ""; return; }
      lab.innerHTML = (d.label ? '<span class="txt">' + d.label + "</span>" : "") + (d.eq ? '<span class="eq">=</span>' : "");
      var flag = d.flag === "*" ? '<span class="fl">*</span>' : "", ent = d.flag === "◁" ? '<span class="fl en">◁</span>' : "";
      var extra = d.extra ? '<span class="xt">' + d.extra + "</span>" : "";
      if (!d.text && !d.exp) { num.innerHTML = extra; return; }
      num.innerHTML = flag + (d.neg ? segChar("-") : "") + segText(d.text, d.neg ? 0 : 0) + (d.exp ? '<span class="ex">' + segText(d.exp.replace("-", "-"), 0) + "</span>" : "") + ent + extra;
    }

    function flash(id) {
      var b = el.querySelector('[data-k="' + id + '"]');
      if (!b) return;
      el.querySelectorAll(".k.cur").forEach(function (x) { x.classList.remove("cur"); });
      b.classList.remove("hit"); void b.offsetWidth; b.classList.add("hit", "cur");
      clearTimeout(b._ht); b._ht = setTimeout(function () { b.classList.remove("hit"); }, 900);
      clearTimeout(el._ct); el._ct = setTimeout(function () { b.classList.remove("cur"); }, playing ? 2600 : 700);
    }
    var _tracked = false;
    function press(id, quiet) { e.press(id); render(); if (!quiet) flash(id); if (!_tracked && !quiet && window.fpTrack) { _tracked = true; window.fpTrack("calculator_used"); } }

    el.querySelector(".ba2-keys").addEventListener("click", function (ev) {
      var b = ev.target.closest("button[data-k]"); if (!b) return;
      stop(); press(b.getAttribute("data-k")); el.focus({ preventScroll: true });
    });
    var KB = { "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", ".": "DOT", ",": "DOT", "+": "ADD", "-": "SUB", "*": "MUL", "x": "MUL", "/": "DIV",
      "=": "EQ", "Enter": "EQ", "Backspace": "BS", "Escape": "CE", "Delete": "CE", "(": "LP", ")": "RP", "^": "POW", "%": "PCT", "ArrowUp": "UP", "ArrowDown": "DOWN" };
    el.addEventListener("keydown", function (ev) {
      if (ev.ctrlKey || ev.metaKey || ev.altKey) return;
      var id = KB[ev.key]; if (!id) return;
      ev.preventDefault(); stop(); press(id);
    });
    tools.addEventListener("click", function (ev) {
      var b = ev.target.closest("button[data-act]"); if (!b) return;
      var a = b.getAttribute("data-act");
      stop();
      if (a === "reset") { e.factory(); render(); say("Reset to factory settings: 2 decimals, chain maths, P/Y = 1."); }
      if (a === "exam") { examSettings(); render(); say("Exam settings: 9 decimals (floating), AOS maths, P/Y = C/Y = 1, END mode."); }
      if (a === "speed") { spIdx = (spIdx + 1) % SPEEDS.length; try { localStorage.setItem("fp-ba2-speed", spIdx); } catch (x) {} b.textContent = "Speed: " + SPEEDS[spIdx][0]; return; }
      if (a === "map") { var on = !el.classList.contains("map"); el.classList.toggle("map", on); legend.hidden = !on; b.setAttribute("aria-pressed", on ? "true" : "false"); }
    });
    function examSettings() { e.factory(); e.fmt.dec = 9; e.fmt.aos = true; }

    var SPEEDS = [["slow", 1150], ["normal", 750], ["fast", 420]], spIdx = 0;
    try { var sv = parseInt(localStorage.getItem("fp-ba2-speed"), 10); if (sv >= 0 && sv < 3) spIdx = sv; } catch (x) {}
    tools.querySelector(".spd").textContent = "Speed: " + SPEEDS[spIdx][0];
    var capTimer;
    function say(t) { cap.textContent = t; cap.classList.add("show"); clearTimeout(capTimer); capTimer = setTimeout(function () { cap.classList.remove("show"); }, 3200); }

    /* ---------------- player */
    var playing = null;
    function stop() { if (playing) { playing.cancel = true; playing = null; } document.querySelectorAll(".try.playing").forEach(function (t) { t.classList.remove("playing"); }); }
    function play(steps, chips, done, speed) {
      stop();
      var job = { cancel: false }; playing = job;
      var queue = [], si, ci = 0;
      for (si = 0; si < steps.length; si++) {
        var st = steps[si];
        if (st.cmd) { queue.push({ cmd: st.cmd }); continue; }
        for (var k = 0; k < st.keys.length; k++) queue.push({ key: st.keys[k], chip: ci, last: k === st.keys.length - 1, step: st });
        ci++;
      }
      var q = 0, dt = speed || SPEEDS[spIdx][1];
      function tick() {
        if (job.cancel) return;
        if (q >= queue.length) { chips.forEach(function (c) { c.classList.remove("now"); }); playing = null; if (done) done(); return; }
        var it = queue[q++];
        if (it.cmd) {
          if (it.cmd === "exam") { examSettings(); render(); say("Starting from exam settings"); }
          if (it.cmd === "fresh") { e.factory(); render(); say("Starting from a reset calculator"); }
          setTimeout(tick, 250); return;
        }
        chips.forEach(function (c, i) { c.classList.toggle("now", i === it.chip); c.classList.toggle("done", i < it.chip); });
        press(it.key);
        if (it.last) say(it.step.chip.sec ? "2ND, then " + it.step.chip.label : it.step.chip.label);
        // digits inside one number go quicker; a pause after each finished entry lets you read the screen
        setTimeout(tick, it.step.chip.num && !it.last ? dt * 0.4 : (it.key === "2ND" ? dt * 0.6 : dt));
      }
      tick();
      return job;
    }

    render();
    return { el: el, engine: e, render: render, press: press, play: play, stop: stop, say: say, exam: function () { examSettings(); render(); } };
  }

  /* ---------------- page wiring */
  function chipHtml(step) {
    if (step.cmd) return "";
    var c = step.chip;
    if (c.num) return '<span class="chip-k num">' + c.label + "</span>";
    if (c.sec) return '<span class="chip-k sec"><small>2ND</small>' + c.label + "</span>";
    return '<span class="chip-k">' + c.label + "</span>";
  }

  function init() {
    var dockHost = document.getElementById("ba2dock"), dock = null;
    if (dockHost) dock = mount(dockHost.querySelector(".ba2-host"));
    document.querySelectorAll("[data-ba2]").forEach(function (h) { if (!h.closest("#ba2dock")) mount(h); });
    if (!dock) return;
    dock.exam(); document.body.classList.add("has-dock");
    var sheet = dockHost, toggle = dockHost.querySelector(".dock-toggle");
    function openSheet(open) { sheet.classList.toggle("open", open); if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false"); fit(); }
    if (toggle) toggle.addEventListener("click", function () { openSheet(!sheet.classList.contains("open")); });
    function fit() {
      var host = dockHost.querySelector(".ba2-host"), mobile = window.matchMedia("(max-width: 1023px)").matches;
      var calc = host.querySelector(".ba2-calc"), w = 330, h = calc.offsetHeight || 640;
      host.style.setProperty("--h", h + "px");
      var s = mobile ? Math.min(1, (window.innerWidth - 24) / w, (window.innerHeight * 0.56) / h) : Math.max(0.72, Math.min(1, (window.innerHeight - 200) / h));
      host.style.setProperty("--s", s.toFixed(3));
    }
    window.addEventListener("resize", fit); fit();

    document.querySelectorAll(".try").forEach(function (box) {
      var steps = B.parse(box.getAttribute("data-keys") || "");
      var row = box.querySelector(".chips");
      row.innerHTML = steps.map(chipHtml).join("");
      var chips = Array.prototype.slice.call(row.querySelectorAll(".chip-k"));
      var real = steps.filter(function (s) { return !s.cmd; });
      var sim = new B.Engine();
      steps.forEach(function (st) {
        if (st.cmd === "exam") { sim.factory(); sim.fmt.dec = 9; sim.fmt.aos = true; }
        else if (st.cmd === "fresh") sim.factory();
        else if (st.keys) st.keys.forEach(function (k) { sim.press(k); });
      });
      var d = sim.display(), shown = d.err ? d.err : ((d.label ? d.label + (d.eq ? " = " : " ") : "") + (d.neg ? "\u2212" : "") + (d.text || "") + (d.exp ? " \u00D710^" + d.exp : "") + (d.extra ? " " + d.extra : "") + (d.flag === "*" ? "  (computed)" : ""));
      var see = document.createElement("p"); see.className = "try-out see"; see.innerHTML = "Screen at the end: <b>" + shown.trim() + "</b>";
      row.parentNode.insertBefore(see, row.nextSibling);
      var btn = box.querySelector(".try-play");
      btn.addEventListener("click", function () {
        if (box.classList.contains("playing")) { dock.stop(); box.classList.remove("playing"); btn.textContent = "Play on the calculator"; return; }
        if (window.matchMedia("(max-width: 1023px)").matches) openSheet(true);
        document.querySelectorAll(".try.playing").forEach(function (t) { t.classList.remove("playing"); t.querySelector(".try-play").textContent = "Play on the calculator"; });
        box.classList.add("playing"); btn.textContent = "Stop";
        var cmds = steps.filter(function (s) { return s.cmd; });
        dock.play(cmds.concat(real), chips, function () {
          box.classList.remove("playing"); btn.textContent = "Play again";
          chips.forEach(function (c) { c.classList.add("done"); c.classList.remove("now"); });
        });
      });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
