/* First Principles: diagrams draw themselves when seen; five small hands-on widgets. No libraries. */
(function () {
  document.documentElement.classList.add("js");
  var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- header shadow once the page scrolls ---- */
  var top = document.querySelector(".top");
  if (top) { var onScroll = function () { top.classList.toggle("scrolled", window.scrollY > 8); }; window.addEventListener("scroll", onScroll, { passive: true }); onScroll(); }

  /* ---- hero video: loops quietly; still for reduced motion ---- */
  var hv = document.querySelector(".hero video");
  if (hv) {
    if (still) { hv.removeAttribute("autoplay"); hv.pause(); }
  }

  /* ---- featured tabs ---- */
  var tabs = document.querySelectorAll('.feature [role="tab"]');
  tabs.forEach(function (t, i) {
    t.addEventListener("click", function () {
      tabs.forEach(function (u, j) { var on = u === t; u.setAttribute("aria-selected", on); var pn = document.getElementById(u.getAttribute("aria-controls")); pn.hidden = !on; pn.classList.toggle("in", on); });
    });
    t.addEventListener("keydown", function (e) { var k = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0; if (k) { var n = tabs[(i + k + tabs.length) % tabs.length]; n.focus(); n.click(); } });
  });

  /* ---- diagrams: draw when seen, then stay alive (tracers, flowing arrows, pulsing dots); replay on request ---- */
  var NSV = "http://www.w3.org/2000/svg";
  var figs = document.querySelectorAll(".fx");
  function lastT(f) { var m = 0; f.querySelectorAll("[style*='--t']").forEach(function (e) { var v = parseFloat(e.style.getPropertyValue("--t")) || 0; if (v > m) m = v; }); return m; }
  function npts(p) { return ((p.getAttribute("d") || "").match(/L/g) || []).length; }
  function build(f) {
    if (f._live) return f._live;
    var layer = document.createElementNS(NSV, "g"); layer.setAttribute("class", "live"); f.appendChild(layer);
    var curves = [], arrows = [];
    f.querySelectorAll("path.d").forEach(function (p) { if (p.closest(".live")) return; var n = npts(p); if (n >= 25) curves.push(p); else if (n >= 1 && n <= 4 && !p.getAttribute("stroke-dasharray")) arrows.push(p); });
    curves.sort(function (a, b) { return b.getTotalLength() - a.getTotalLength(); });
    var tr = curves.slice(0, 3).map(function (p, i) {
      var g = document.createElementNS(NSV, "g"), c = p.getAttribute("stroke");
      var halo = document.createElementNS(NSV, "circle"); halo.setAttribute("r", 9); halo.setAttribute("fill", c); halo.setAttribute("fill-opacity", ".2");
      var dot = document.createElementNS(NSV, "circle"); dot.setAttribute("r", 3.6); dot.setAttribute("fill", "#fff");
      g.appendChild(halo); g.appendChild(dot); layer.appendChild(g);
      /* sample the path once, so each frame is a cheap interpolation */
      var L = p.getTotalLength(), N = Math.max(60, Math.min(400, Math.round(L / 3))), xs = new Float32Array(N + 1), ys = new Float32Array(N + 1);
      for (var k = 0; k <= N; k++) { var q = p.getPointAtLength(L * k / N); xs[k] = q.x; ys[k] = q.y; }
      return { g: g, xs: xs, ys: ys, N: N, off: i * 0.37, sp: (6500 + i * 1100) * Math.max(0.8, Math.min(1.6, L / 600)), shown: false };
    });
    arrows.slice(0, 14).forEach(function (p, i) {
      var q = p.cloneNode(); q.setAttribute("class", "flow"); q.setAttribute("stroke", "#fff"); q.setAttribute("stroke-opacity", ".85");
      q.setAttribute("stroke-width", Math.max(2, +p.getAttribute("stroke-width") + 0.6)); q.style.animationDelay = (-i * 0.37) + "s"; layer.appendChild(q);
    });
    f._live = { tr: tr, t0: 0 }; return f._live;
  }
  function ease(u) { return u < .5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; }
  var running = new Set(), raf = 0;
  function tick(now) {
    running.forEach(function (f) {
      var L = f._live; if (!L.t0) L.t0 = now;
      L.tr.forEach(function (t) {
        var u = ((now - L.t0) / t.sp + t.off) % 1, x = ease(u) * t.N, k = Math.floor(x), r = x - k, k2 = Math.min(k + 1, t.N);
        t.g.setAttribute("transform", "translate(" + (t.xs[k] + (t.xs[k2] - t.xs[k]) * r).toFixed(2) + "," + (t.ys[k] + (t.ys[k2] - t.ys[k]) * r).toFixed(2) + ")");
        var vis = u > 0.04 && u < 0.96; if (vis !== t.shown) { t.g.classList.toggle("vis", vis); t.shown = vis; }
      });
    });
    raf = running.size && !document.hidden ? requestAnimationFrame(tick) : 0;
  }
  function kick() { if (!raf && running.size && !document.hidden) raf = requestAnimationFrame(tick); }
  document.addEventListener("visibilitychange", kick);
  function goLive(f) { if (still) return; build(f); f.classList.add("live"); running.add(f); kick(); }
  function stopLive(f) { running.delete(f); f.classList.remove("live"); }
  function play(f) {
    clearTimeout(f._tm); f._done = false; stopLive(f); f.classList.remove("on"); void f.getBoundingClientRect();
    requestAnimationFrame(function () { f.classList.add("on"); });
    if (f._live) f._live.t0 = 0;
    f._tm = setTimeout(function () { f._done = true; if (f._vis !== false) goLive(f); }, (lastT(f) + 1.7) * 1000);
  }
  figs.forEach(function (f) {
    var host = f.closest("figure");
    if (host && !still) {
      var b = document.createElement("button"); b.type = "button"; b.className = "replay"; b.textContent = "Replay";
      b.setAttribute("aria-label", "Replay this diagram"); b.addEventListener("click", function () { play(f); });
      var cap = host.querySelector("figcaption"); host.insertBefore(b, cap ? cap.nextSibling : null);
    }
  });
  if (!("IntersectionObserver" in window) || still) { figs.forEach(function (f) { f.classList.add("on"); }); }
  else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var f = e.target; f._vis = e.isIntersecting;
        if (e.isIntersecting) { if (!f.classList.contains("on")) play(f); else if (f._done) goLive(f); }
        else stopLive(f);
      });
    }, { threshold: 0.3 });
    figs.forEach(function (f) { io.observe(f); });
  }

  /* ---- helpers for widgets ---- */
  var NS = "http://www.w3.org/2000/svg", C = { blue: "#58C4DD", teal: "#5CD0B3", yellow: "#FFFF00", ink: "#ECECEC", dim: "#8C8C8C", rule: "#3a3a3a", red: "#FC6255" };
  function el(n, a, txt) { var e = document.createElementNS(NS, n); for (var k in a) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; return e; }
  function svg(w, h) { return el("svg", { viewBox: "0 0 " + w + " " + h, class: "wsvg", role: "img" }); }
  function T(s, x, y, o) { o = o || {}; return el("text", { x: x, y: y, fill: o.fill || C.dim, "font-size": o.size || 13, "text-anchor": o.anchor || "start", "font-style": o.italic ? "italic" : "normal", "font-family": "Figtree, Segoe UI, Arial, sans-serif" }, s); }
  function axes(g, x0, y0, x1, y1, xl, yl) {
    g.appendChild(el("path", { d: "M" + x0 + "," + y1 + " L" + x0 + "," + y0 + " L" + x1 + "," + y0, fill: "none", stroke: C.rule }));
    if (xl) g.appendChild(T(xl, x1, y0 + 22, { anchor: "end", italic: true }));
    if (yl) g.appendChild(T(yl, x0 + 6, y1 - 6, { italic: true }));
  }
  function fmt(v, d) { return v.toLocaleString("en-US", { minimumFractionDigits: d || 0, maximumFractionDigits: d || 0 }); }
  function seg(box, names, onpick) {
    var s = document.createElement("div"); s.className = "seg"; s.setAttribute("role", "group");
    names.forEach(function (n, i) {
      var b = document.createElement("button"); b.type = "button"; b.textContent = n; b.setAttribute("aria-pressed", i === 0 ? "true" : "false");
      b.addEventListener("click", function () { s.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", "false"); }); b.setAttribute("aria-pressed", "true"); onpick(i); });
      s.appendChild(b);
    });
    box.appendChild(s); return s;
  }
  function slider(box, label, min, max, step, val, oninput) {
    var l = document.createElement("label"); l.textContent = label;
    var r = document.createElement("input"); r.type = "range"; r.min = min; r.max = max; r.step = step; r.value = val;
    r.addEventListener("input", function () { oninput(+r.value); }); l.appendChild(r); box.appendChild(l); return r;
  }
  function frame(w) { var c = document.createElement("div"); c.className = "controls"; var out = document.createElement("p"); out.className = "out"; out.setAttribute("aria-live", "polite"); w.appendChild(c); return { c: c, out: out }; }

  var W = {
    /* price elasticity along a straight demand line Q = 100 - P */
    elasticity: function (w) {
      var f = frame(w), s = svg(640, 300); w.appendChild(s); w.appendChild(f.out);
      var x0 = 50, y0 = 270, x1 = 620, y1 = 20, X = function (q) { return x0 + q / 100 * (x1 - x0); }, Y = function (p) { return y0 - p / 100 * (y0 - y1); };
      function draw(P) {
        s.innerHTML = ""; var g = el("g", {}); s.appendChild(g); axes(g, x0, y0, x1, y1, "quantity", "price");
        var Q = 100 - P, E = P / Q;
        g.appendChild(el("rect", { x: x0, y: Y(P), width: X(Q) - x0, height: y0 - Y(P), fill: C.teal, "fill-opacity": 0.28 }));
        g.appendChild(el("line", { x1: X(0), y1: Y(100), x2: X(100), y2: Y(0), stroke: C.blue, "stroke-width": 2.4 }));
        g.appendChild(el("circle", { cx: X(50), cy: Y(50), r: 3, fill: C.dim }));
        g.appendChild(T("unit elastic", X(50) + 8, Y(50) - 6, { italic: true }));
        g.appendChild(el("circle", { cx: X(Q), cy: Y(P), r: 6, fill: C.yellow }));
        g.appendChild(T("revenue = " + fmt(P * Q), x0 + 10, y0 - 10, { fill: C.ink }));
        g.appendChild(T("elastic", X(12), Y(80), { italic: true })); g.appendChild(T("inelastic", X(80), Y(14), { italic: true }));
        var verdict = E > 1.02 ? "elastic, so a small price cut would raise revenue" : E < 0.98 ? "inelastic, so a small price rise would raise revenue" : "unit elastic, so revenue is at its maximum";
        f.out.innerHTML = "Price " + P + ", quantity " + Q + ": elasticity |E| = P/Q = <b>" + fmt(E, 2) + "</b>, " + verdict + ".";
      }
      slider(f.c, "Price", 5, 95, 1, 70, draw); draw(70);
    },
    /* three depreciation methods for the same asset */
    depreciation: function (w) {
      var f = frame(w), s = svg(640, 300); w.appendChild(s); w.appendChild(f.out);
      var cost = 10000, salv = 1000, n = 5, units = [3000, 2500, 2000, 1500, 1000];
      function sched(m) {
        var e = [], bv = cost;
        for (var t = 0; t < n; t++) {
          var d = m === 0 ? (cost - salv) / n : m === 1 ? Math.min(bv * 2 / n, bv - salv) : (cost - salv) * units[t] / 10000;
          if (m === 1 && t === n - 1) d = bv - salv;
          e.push(d); bv -= d;
        }
        return e;
      }
      function draw(m) {
        s.innerHTML = ""; var g = el("g", {}); s.appendChild(g);
        var x0 = 50, y0 = 260, x1 = 620, y1 = 20; axes(g, x0, y0, x1, y1, "year", "amount");
        var e = sched(m), bv = cost, step = (x1 - x0) / n, Y = function (v) { return y0 - v / cost * (y0 - y1); }, pts = [[x0, Y(cost)]];
        e.forEach(function (d, t) {
          var x = x0 + (t + 0.5) * step;
          g.appendChild(el("rect", { x: x - step * 0.22, y: Y(d), width: step * 0.44, height: y0 - Y(d), fill: C.blue, "fill-opacity": 0.75 }));
          g.appendChild(T(fmt(d), x, Y(d) - 6, { anchor: "middle", fill: C.ink, size: 12 }));
          g.appendChild(T(String(t + 1), x, y0 + 18, { anchor: "middle" }));
          bv -= d; pts.push([x0 + (t + 1) * step, Y(bv)]);
        });
        g.appendChild(el("polyline", { points: pts.map(function (p) { return p.join(","); }).join(" "), fill: "none", stroke: C.yellow, "stroke-width": 2 }));
        g.appendChild(T("book value", pts[1][0] + 6, pts[1][1] - 8, { fill: C.yellow, italic: true }));
        g.appendChild(el("line", { x1: x0, x2: x1, y1: Y(salv), y2: Y(salv), stroke: C.dim, "stroke-dasharray": "4 4" }));
        g.appendChild(T("salvage 1,000", x1, Y(salv) - 6, { anchor: "end", italic: true }));
        var names = ["Straight-line spreads the cost evenly", "Double-declining charges 40% of the remaining book value, so early years carry more", "Units-of-production follows how hard the machine is used"];
        f.out.innerHTML = names[m] + ". Year-1 expense: <b>" + fmt(e[0]) + "</b>. Total over five years is always 9,000: only the timing changes.";
      }
      seg(f.c, ["Straight-line", "Double-declining", "Units of production"], draw); draw(0);
    },
    /* FIFO, LIFO, weighted average with rising purchase prices */
    inventory: function (w) {
      var f = frame(w), s = svg(640, 200); w.appendChild(s); w.appendChild(f.out);
      var lots = [[100, 10], [100, 12], [100, 14]], sold = 200, rev = 200 * 20;
      function calc(m) {
        if (m === 2) { var avg = 12; return { cogs: sold * avg, ei: 100 * avg, used: null }; }
        var order = m === 0 ? [0, 1, 2] : [2, 1, 0], left = sold, cogs = 0, used = [0, 0, 0];
        order.forEach(function (i) { var u = Math.min(left, lots[i][0]); used[i] = u; cogs += u * lots[i][1]; left -= u; });
        return { cogs: cogs, ei: 3600 - cogs, used: used };
      }
      function draw(m) {
        s.innerHTML = ""; var g = el("g", {}); s.appendChild(g);
        var r = calc(m);
        lots.forEach(function (l, i) {
          var x = 40 + i * 120, sold = r.used ? r.used[i] === 100 : null;
          g.appendChild(el("rect", { x: x, y: 40, width: 100, height: 120, fill: m === 2 ? C.blue : (sold ? C.blue : C.teal), "fill-opacity": m === 2 ? 0.45 : 0.75 }));
          g.appendChild(T("100 units", x + 50, 95, { anchor: "middle", fill: "#000", size: 14 }));
          g.appendChild(T("at " + l[1], x + 50, 115, { anchor: "middle", fill: "#000", size: 14 }));
          g.appendChild(T(["bought first", "bought second", "bought last"][i], x + 50, 180, { anchor: "middle", italic: true }));
        });
        g.appendChild(T("Blue = sold (cost of sales)", 40, 26, { fill: C.blue })); g.appendChild(T("Teal = still on the shelf", 230, 26, { fill: C.teal }));
        var bx = 440, sc = 120 / 3600;
        [["Cost of sales", r.cogs, C.blue], ["Ending inventory", r.ei, C.teal], ["Gross profit", rev - r.cogs, C.yellow]].forEach(function (b, i) {
          var y = 60 + i * 60;
          g.appendChild(T(b[0], bx, y - 8, { fill: C.ink, size: 13 }));
          g.appendChild(el("rect", { x: bx, y: y, width: b[1] * sc * 1.2, height: 18, fill: b[2], "fill-opacity": 0.8 }));
          g.appendChild(T(fmt(b[1]), bx + b[1] * sc * 1.2 + 8, y + 14, { fill: C.ink }));
        });
        var msg = ["FIFO sends the oldest, cheapest units to cost of sales: lower expense, higher profit, and an inventory figure close to today's prices",
                   "LIFO sends the newest, dearest units to cost of sales: higher expense, lower profit and tax, and stale old costs left on the balance sheet (US GAAP only, not allowed under IFRS)",
                   "Weighted average uses one blended cost of 12 for every unit, so it sits between the two"];
        f.out.innerHTML = msg[m] + ". Revenue is 4,000 in every case.";
      }
      seg(f.c, ["FIFO", "LIFO", "Weighted average"], draw); draw(0);
    },
    /* effective-interest amortisation of a bond issued at a discount or premium */
    bond: function (w) {
      var f = frame(w), s = svg(640, 300); w.appendChild(s); w.appendChild(f.out);
      var face = 1000, c = 50, n = 5;
      function draw(r) {
        r = r / 100; s.innerHTML = ""; var g = el("g", {}); s.appendChild(g);
        var price = 0; for (var t = 1; t <= n; t++) price += c / Math.pow(1 + r, t); price += face / Math.pow(1 + r, n);
        var x0 = 50, y0 = 260, x1 = 620, y1 = 30, lo = 850, hi = 1100, X = function (t) { return x0 + t / n * (x1 - x0); }, Y = function (v) { return y0 - (v - lo) / (hi - lo) * (y0 - y1); };
        axes(g, x0, y0, x1, y1, "year", "carrying amount");
        g.appendChild(el("line", { x1: x0, x2: x1, y1: Y(face), y2: Y(face), stroke: C.dim, "stroke-dasharray": "4 4" }));
        g.appendChild(T("face value 1,000", x1, Y(face) - 6, { anchor: "end", italic: true }));
        var cv = price, pts = [[X(0), Y(cv)]], ie1 = cv * r;
        for (t = 1; t <= n; t++) { cv = cv + cv * r - c; pts.push([X(t), Y(cv)]); }
        g.appendChild(el("polyline", { points: pts.map(function (p) { return p.join(","); }).join(" "), fill: "none", stroke: C.blue, "stroke-width": 2.6 }));
        pts.forEach(function (p, i) { g.appendChild(el("circle", { cx: p[0], cy: p[1], r: i === 0 ? 6 : 3.5, fill: i === 0 ? C.yellow : C.blue })); g.appendChild(T(String(i), p[0], y0 + 18, { anchor: "middle" })); });
        var kind = Math.abs(price - face) < 0.5 ? "at par" : price < face ? "at a discount" : "at a premium";
        f.out.innerHTML = "Market rate " + fmt(r * 100, 1) + "% vs 5% coupon: issued " + kind + " for <b>" + fmt(price, 1) + "</b>. Year-1 interest expense = " + fmt(r * 100, 1) + "% × " + fmt(price, 1) + " = " + fmt(ie1, 1) + ", cash coupon 50, so the carrying amount moves by " + fmt(ie1 - c, 1) + " towards 1,000.";
      }
      slider(f.c, "Market rate at issue", 2, 9, 0.5, 7, draw); draw(7);
    },
    /* the money multiplier as rounds of re-lending */
    multiplier: function (w) {
      var f = frame(w), s = svg(640, 260); w.appendChild(s); w.appendChild(f.out);
      function draw(rr) {
        rr = rr / 100; s.innerHTML = ""; var g = el("g", {}); s.appendChild(g);
        var x0 = 40, y0 = 230, x1 = 620, y1 = 20, rounds = 15, step = (x1 - x0) / rounds; axes(g, x0, y0, x1, y1, "round of lending", "new deposits");
        var d = 1000, tot = 0;
        for (var i = 0; i < rounds; i++) { var h = d / 1000 * (y0 - y1); g.appendChild(el("rect", { x: x0 + i * step + step * 0.15, y: y0 - h, width: step * 0.7, height: h, fill: i === 0 ? C.yellow : C.blue, "fill-opacity": 0.8 })); tot += d; d *= (1 - rr); }
        f.out.innerHTML = "Reserve requirement " + fmt(rr * 100) + "%: each bank keeps " + fmt(rr * 100) + "% and lends the rest, which is deposited again. Money multiplier 1/" + fmt(rr, 2) + " = <b>" + fmt(1 / rr, 1) + "</b>, so 1,000 of new reserves can support up to " + fmt(1000 / rr) + " of deposits.";
      }
      slider(f.c, "Reserve requirement (%)", 5, 50, 1, 10, draw); draw(10);
    }
  };
  document.querySelectorAll("[data-widget]").forEach(function (w) { var k = w.getAttribute("data-widget"); if (W[k]) W[k](w); });
})();

/* ---- header menu: burger on small screens, tap-to-open sections, Escape closes ---- */
(function () {
  var burger = document.querySelector(".burger"), nav = document.getElementById("mainnav");
  if (!burger || !nav) return;
  burger.addEventListener("click", function () { var open = !nav.classList.contains("open"); nav.classList.toggle("open", open); burger.setAttribute("aria-expanded", open ? "true" : "false"); });
  nav.querySelectorAll(".mx").forEach(function (b) {
    b.addEventListener("click", function () {
      var m = b.parentNode.querySelector(".mega"), open = !m.classList.contains("open");
      m.classList.toggle("open", open); b.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (document.activeElement && nav.contains(document.activeElement)) document.activeElement.blur();
    nav.classList.remove("open"); burger.setAttribute("aria-expanded", "false");
  });
})();

/* ---- "Are you ready for Level I?" self-check ---- */
(function () {
  var box = document.querySelector('[data-widget="readiness"]');
  if (!box) return;
  var C = { b: "#1565C0", s: "#3DBEF0", y: "#F2C200", g: "#0FA968", r: "#D64545", t: "#5B6B7A", l: "#DCE3EA" };
  function svg(w, h, body) { return '<svg viewBox="0 0 ' + w + " " + h + '" class="rd-vis" aria-hidden="true">' + body + "</svg>"; }
  var V = {
    normal: (function () {
      var p = "", sh = "";
      for (var i = 0; i <= 100; i++) { var x = -3 + i * 0.06, y = Math.exp(-x * x / 2); p += (i ? "L" : "M") + (10 + i * 2.2).toFixed(1) + "," + (100 - y * 80).toFixed(1); }
      for (var j = 33; j <= 67; j++) { var xx = -3 + j * 0.06, yy = Math.exp(-xx * xx / 2); sh += (j === 33 ? "M" + (10 + j * 2.2) + ",100 L" : "L") + (10 + j * 2.2).toFixed(1) + "," + (100 - yy * 80).toFixed(1); }
      sh += " L" + (10 + 67 * 2.2) + ",100 Z";
      return svg(240, 120, '<path d="' + sh + '" fill="' + C.s + '" opacity=".35"/><path d="' + p + '" fill="none" stroke="' + C.b + '" stroke-width="2.5"/><line x1="10" x2="230" y1="100" y2="100" stroke="' + C.t + '"/>' +
        '<text x="82" y="114" font-size="10" fill="' + C.t + '">−1σ</text><text x="116" y="114" font-size="10" fill="' + C.t + '">μ</text><text x="150" y="114" font-size="10" fill="' + C.t + '">+1σ</text><text x="120" y="70" font-size="13" text-anchor="middle" fill="' + C.b + '" font-weight="700">?</text>');
    })(),
    grow: svg(240, 120, [0, 1, 2, 3, 4, 5].map(function (k) { var h = 50 * Math.pow(1.05, k) * 1.25; return '<rect x="' + (20 + k * 36) + '" y="' + (106 - h) + '" width="24" height="' + h + '" fill="' + (k === 5 ? C.y : C.s) + '"/><text x="' + (32 + k * 36) + '" y="118" font-size="10" text-anchor="middle" fill="' + C.t + '">' + k + "</text>"; }).join("")),
    pv: svg(240, 120, '<line x1="30" x2="210" y1="70" y2="70" stroke="' + C.t + '" stroke-width="2"/><circle cx="30" cy="70" r="5" fill="' + C.b + '"/><circle cx="210" cy="70" r="5" fill="' + C.y + '"/><text x="30" y="98" text-anchor="middle" font-size="11" fill="' + C.t + '">today</text><text x="210" y="98" text-anchor="middle" font-size="11" fill="' + C.t + '">1 year</text><text x="210" y="56" text-anchor="middle" font-size="13" fill="#102742" font-weight="700">1,100</text><text x="30" y="56" text-anchor="middle" font-size="13" fill="' + C.b + '" font-weight="700">?</text><path d="M195,40 Q120,10 45,40" fill="none" stroke="' + C.b + '" stroke-width="1.5" marker-end="url(#ah)"/><defs><marker id="ah" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="' + C.b + '"/></marker></defs><text x="120" y="22" text-anchor="middle" font-size="10" fill="' + C.t + '">discount at 10%</text>'),
    spread: svg(240, 120, (function () {
      var a = [112, 116, 120, 121, 124, 128, 118], b = [60, 85, 102, 130, 150, 172, 190], o = '<text x="8" y="40" font-size="12" fill="#102742" font-weight="700">A</text><text x="8" y="90" font-size="12" fill="#102742" font-weight="700">B</text><line x1="24" x2="232" y1="36" y2="36" stroke="' + C.l + '"/><line x1="24" x2="232" y1="86" y2="86" stroke="' + C.l + '"/>';
      a.forEach(function (x) { o += '<circle cx="' + x + '" cy="36" r="5" fill="' + C.s + '"/>'; }); b.forEach(function (x) { o += '<circle cx="' + x + '" cy="86" r="5" fill="' + C.b + '"/>'; }); return o; })()),
    bs: svg(240, 120, '<rect x="30" y="20" width="80" height="80" fill="' + C.s + '" opacity=".4"/><text x="70" y="64" text-anchor="middle" font-size="12" fill="#102742">Assets</text><rect x="130" y="20" width="80" height="44" fill="' + C.y + '" opacity=".5"/><text x="170" y="46" text-anchor="middle" font-size="12" fill="#102742">Liabilities</text><rect x="130" y="64" width="80" height="36" fill="' + C.g + '" opacity=".35"/><text x="170" y="86" text-anchor="middle" font-size="12" fill="#102742">Equity</text><text x="120" y="114" text-anchor="middle" font-size="11" fill="' + C.t + '">always equal</text>'),
    credit: svg(240, 120, '<rect x="20" y="40" width="60" height="40" rx="4" fill="none" stroke="' + C.b + '" stroke-width="2"/><text x="50" y="65" text-anchor="middle" font-size="11" fill="#102742">goods</text><line x1="84" x2="150" y1="60" y2="60" stroke="' + C.t + '" stroke-width="2" marker-end="url(#ah2)"/><defs><marker id="ah2" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="' + C.t + '"/></marker></defs><text x="117" y="50" text-anchor="middle" font-size="10" fill="' + C.t + '">sold for 100</text><text x="195" y="56" text-anchor="middle" font-size="11" fill="#102742">customer</text><text x="195" y="72" text-anchor="middle" font-size="10" fill="' + C.t + '">pays in 60 days</text>'),
    sd: svg(240, 120, '<line x1="30" x2="30" y1="10" y2="104" stroke="' + C.t + '"/><line x1="30" x2="225" y1="104" y2="104" stroke="' + C.t + '"/><path d="M40,20 L200,96" stroke="' + C.b + '" stroke-width="2.5"/><path d="M40,96 L200,20" stroke="' + C.y + '" stroke-width="2.5"/><path d="M80,20 L225,88" stroke="' + C.b + '" stroke-width="2.5" stroke-dasharray="5 4"/><text x="206" y="22" font-size="11" fill="#8a6d00">S</text><text x="190" y="110" font-size="11" fill="' + C.b + '">D</text><text x="226" y="84" font-size="11" fill="' + C.b + '">D′</text><text x="18" y="16" font-size="10" fill="' + C.t + '">P</text><text x="218" y="118" font-size="10" fill="' + C.t + '">Q</text>'),
    infl: svg(240, 120, '<rect x="50" y="34" width="50" height="70" fill="' + C.b + '"/><text x="75" y="28" text-anchor="middle" font-size="12" fill="#102742" font-weight="700">6%</text><text x="75" y="118" text-anchor="middle" font-size="10" fill="' + C.t + '">interest</text><rect x="140" y="57" width="50" height="47" fill="' + C.r + '" opacity=".75"/><text x="165" y="51" text-anchor="middle" font-size="12" fill="#102742" font-weight="700">4%</text><text x="165" y="118" text-anchor="middle" font-size="10" fill="' + C.t + '">inflation</text>'),
    bond: svg(240, 120, '<line x1="40" x2="200" y1="62" y2="42" stroke="#102742" stroke-width="4"/><path d="M110,104 L120,56 L130,104 Z" fill="' + C.t + '"/><text x="44" y="52" font-size="12" fill="' + C.b + '" font-weight="700">price ?</text><text x="160" y="30" font-size="12" fill="' + C.r + '" font-weight="700">rates ↑</text>'),
    divers: svg(240, 120, (function () {
      var a = "", b = "", c = "";
      for (var i = 0; i <= 40; i++) { var x = 14 + i * 5.4, u = Math.sin(i * 0.7) * 26, v = Math.sin(i * 0.7 + 2.4) * 26; a += (i ? "L" : "M") + x + "," + (60 + u); b += (i ? "L" : "M") + x + "," + (60 + v); c += (i ? "L" : "M") + x + "," + (60 + (u + v) / 2); }
      return '<path d="' + a + '" fill="none" stroke="' + C.s + '" stroke-width="1.6" opacity=".8"/><path d="' + b + '" fill="none" stroke="' + C.y + '" stroke-width="1.6" opacity=".9"/><path d="' + c + '" fill="none" stroke="#102742" stroke-width="2.6"/><text x="226" y="114" text-anchor="end" font-size="10" fill="' + C.t + '">dark line = 50/50 mix</text>'; })())
  };
  var S1 = [
    ["time", "How many hours a week can you study, every week, for five to six months?", ["Under 6", "6 to 11", "12 or more"]],
    ["time", "How settled are the next six months (exams, a move, a new job, a newborn)?", ["Very busy", "Some disruption", "Fairly stable"]],
    ["eng", "How comfortable are you reading dense English under time pressure?", ["It's a struggle", "OK", "Comfortable"]],
    ["why", "Do you know which job you want the CFA to help you get?", ["Not really", "A rough idea", "Yes, clearly"]],
    ["admin", "Do you meet the entry rule (final year of a degree, a degree, or 4,000 hours of work and/or study) and have a valid passport?", ["No / not sure", "Will soon", "Yes"]]
  ];
  var K = [
    ["quant", "normal", "In a normal distribution, roughly what share of outcomes lies within one standard deviation of the mean?", ["50%", "68%", "95%", "99.7%"], 1, "About 68% lies within ±1σ, 95% within ±2σ and 99.7% within ±3σ. You will use these numbers for confidence intervals and risk at every level."],
    ["quant", "grow", "You invest 1,000 at 5% a year, compounded annually. About how much do you have after 5 years?", ["1,250", "1,276", "1,300", "1,050"], 1, "1,000 × 1.05⁵ = 1,276. Simple interest would give 1,250; compounding earns interest on interest."],
    ["quant", "pv", "What is 1,100 received in one year worth today, if the interest rate is 10%?", ["990", "1,000", "1,010", "1,100"], 1, "Present value = 1,100 ÷ 1.10 = 1,000. Discounting is compounding run backwards, and it underlies every valuation in the CFA Program."],
    ["quant", "spread", "Both sets of points have the same average. Which has the higher standard deviation?", ["A", "B", "They are equal", "You cannot tell"], 1, "Standard deviation measures how far points typically sit from their mean. B's points are far more spread out, so its standard deviation is higher."],
    ["acct", "bs", "A company borrows 500 in cash from a bank. What happens on its balance sheet?", ["Assets +500, equity +500", "Assets +500, liabilities +500", "Only cash changes", "Profit rises by 500"], 1, "Cash (an asset) rises by 500 and so does the loan (a liability). Borrowing is not income, and assets = liabilities + equity still holds."],
    ["acct", "credit", "A firm sells goods for 100 on 60-day credit this month. This month, what happens to revenue and cash?", ["Revenue 100, cash 100", "Revenue 0, cash 0", "Revenue 100, cash 0", "Revenue 0, cash 100"], 2, "Under accrual accounting revenue is recorded when the goods are delivered, not when cash arrives. That is why profit and cash flow differ."],
    ["econ", "sd", "Demand for a product rises (the demand curve shifts right) while supply is unchanged. What happens to price?", ["It rises", "It falls", "It stays the same", "Supply falls"], 0, "At the old price buyers now want more than sellers offer, so the price is bid up until the market clears at a higher price and quantity."],
    ["econ", "infl", "A deposit pays 6% a year and inflation is 4%. Roughly what is your real return?", ["10%", "6%", "4%", "2%"], 3, "Real return ≈ nominal return − inflation = 6% − 4% = 2% (more precisely 1.06 ÷ 1.04 − 1 = 1.9%)."],
    ["markets", "bond", "Market interest rates rise. What happens to the price of a bond you already own that pays a fixed coupon?", ["It rises", "It falls", "It does not change", "It depends on the issuer only"], 1, "New bonds now pay more, so yours is worth less: its fixed payments are discounted at a higher rate. Price and yield move in opposite directions."],
    ["markets", "divers", "Two assets each have 20% volatility and do not move perfectly together. A 50/50 portfolio of them has volatility of:", ["More than 20%", "Exactly 20%", "Less than 20%", "40%"], 2, "Unless the correlation is exactly +1, some ups offset some downs, so the mix is less volatile than either asset. That is diversification."]
  ];
  var AREA = { quant: "Quantitative methods", acct: "Financial statements", econ: "Economics", markets: "Markets and investing" };
  var FIX = {
    quant: 'Revisit compounding, discounting and basic statistics; our <a href="blog-ba-ii-plus-calculator-guide.html">BA II Plus guide</a> walks through the time-value maths, and the <a href="blog-cfa-level-1-formula-sheet.html">formula sheet</a> lists what to know.',
    acct: 'Take the financial statements part of the <a href="prerequisites.html">prerequisites course</a>, starting with <a href="prereq-three-statements.html">the three statements</a> and <a href="prereq-accrual-accounting.html">accrual accounting</a>.',
    econ: 'Take the economics part of the <a href="prerequisites.html">prerequisites course</a>, starting with <a href="prereq-inflation-price-indexes.html">inflation</a> and <a href="prereq-market-structures.html">market structures</a>.',
    markets: 'Read <a href="blog-first-principles-method.html">the first-principles method</a>: bond pricing and diversification both follow from discounting and from how returns combine.'
  };
  var ADV = {
    time: 'Time is the biggest risk. Most people who pass report <b>300+ hours</b>; at under 6 hours a week that takes about a year. Book a later window or free up hours first.',
    eng: 'The exam is in English only. Practise timed reading with question banks early, not just at the end.',
    why: 'Be clear why you are doing it: the motivation has to last 300 hours. See <a href="blog-cfa-jobs-salaries.html">CFA jobs and salaries</a>.',
    admin: 'Check eligibility before anything else: see <a href="blog-cfa-requirements.html">CFA requirements</a>.'
  };
  var h = '<div class="rd"><p class="rd-intro">Part 1 is about your situation; part 2 is a quick knowledge check with answers explained as you go. Nothing is sent anywhere.</p>';
  h += '<h3 class="rd-h">Part 1 · Your situation</h3><ol class="rd-s">';
  S1.forEach(function (q, i) {
    h += '<li><p>' + q[1] + '</p><div class="rd-opts" role="radiogroup">' + q[2].map(function (o, j) {
      return '<label><input type="radio" name="rs' + i + '" value="' + j + '"><span>' + o + "</span></label>"; }).join("") + "</div></li>";
  });
  h += '</ol><h3 class="rd-h">Part 2 · Do you know the basics?</h3><ol class="rd-k">';
  K.forEach(function (q, i) {
    h += '<li class="rd-q" data-i="' + i + '"><div class="rd-pic">' + V[q[1]] + '<span class="rd-tag">' + AREA[q[0]] + '</span></div><div><p>' + q[2] + '</p><div class="rd-opts four" role="radiogroup">' +
      q[3].map(function (o, j) { return '<label><input type="radio" name="rk' + i + '" value="' + j + '"><span>' + o + "</span></label>"; }).join("") +
      '</div><p class="rd-exp" hidden></p></div></li>';
  });
  h += '</ol><div class="rd-out" aria-live="polite"><p>Answer all fifteen questions to see your result.</p></div></div>';
  box.innerHTML = h;
  var out = box.querySelector(".rd-out");
  box.addEventListener("change", function (e) {
    var t = e.target;
    if (t.name && t.name.indexOf("rk") === 0) {
      var i = +t.name.slice(2), q = K[i], li = box.querySelector('.rd-q[data-i="' + i + '"]'), ok = +t.value === q[4];
      li.classList.remove("ok", "no"); li.classList.add(ok ? "ok" : "no");
      li.querySelectorAll("label").forEach(function (l, j) { l.classList.toggle("right", j === q[4]); });
      var ex = li.querySelector(".rd-exp"); ex.hidden = false; ex.innerHTML = "<b>" + (ok ? "Correct." : "Not quite.") + "</b> " + q[5];
    }
    var sc = {}, n = 0, tot = 0, kc = 0, kn = 0, area = {};
    S1.forEach(function (q, i) { var c = box.querySelector('input[name="rs' + i + '"]:checked'); if (!c) return; n++; tot += +c.value; sc[q[0]] = Math.min(sc[q[0]] === undefined ? 2 : sc[q[0]], +c.value); });
    K.forEach(function (q, i) { var c = box.querySelector('input[name="rk' + i + '"]:checked'); var a = area[q[0]] = area[q[0]] || [0, 0]; a[1]++; if (!c) return; kn++; if (+c.value === q[4]) { kc++; a[0]++; } });
    var left = S1.length + K.length - n - kn;
    if (left) { out.innerHTML = "<p>" + left + " question" + (left > 1 ? "s" : "") + " to go.</p>"; return; }
    var sit = Math.round(tot / (2 * S1.length) * 100), kno = Math.round(kc / K.length * 100), verdict;
    if (sc.admin === 0) verdict = "First check that you can register: the entry rules come before everything else.";
    else if (sit >= 70 && kno >= 80) verdict = "You look ready. Pick a window five to six months away, register early and start this week.";
    else if (sit >= 50 && kno >= 50) verdict = "Nearly ready. Close the gaps below in the first month of your plan, then follow a normal five-to-six-month schedule.";
    else verdict = "Not yet. Spend one or two months on the foundations below, then start the full plan; you will save time overall.";
    var bars = Object.keys(AREA).map(function (k) { var a = area[k], p = Math.round(a[0] / a[1] * 100);
      return '<div class="rd-bar"><span>' + AREA[k] + '</span><i><b style="width:' + Math.max(p, 3) + '%;background:' + (p >= 75 ? C.g : p >= 50 ? C.y : C.r) + '"></b></i><em>' + a[0] + "/" + a[1] + "</em></div>"; }).join("");
    var tips = Object.keys(FIX).filter(function (k) { return area[k][0] < area[k][1]; }).map(function (k) { return "<li>" + FIX[k] + "</li>"; })
      .concat(Object.keys(ADV).filter(function (k) { return sc[k] !== undefined && sc[k] < 2; }).map(function (k) { return "<li>" + ADV[k] + "</li>"; })).join("");
    out.innerHTML = '<div class="rd-scores"><p><b>' + sit + '%</b><span>situation</span></p><p><b>' + kc + "/" + K.length + '</b><span>knowledge</span></p></div>' + bars +
      "<p class=\"rd-verdict\">" + verdict + "</p>" + (tips ? "<ul>" + tips + "</ul>" : "") + '<p><a class="btn" href="prerequisites.html">Start the prerequisites course</a></p>';
  });
})();
