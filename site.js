/* First Principles: diagrams draw themselves when seen; five small hands-on widgets. No libraries. */
(function () {
  document.documentElement.classList.add("js");
  var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

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
      var halo = document.createElementNS(NSV, "circle"); halo.setAttribute("r", 9); halo.setAttribute("fill", c); halo.setAttribute("fill-opacity", ".18");
      var dot = document.createElementNS(NSV, "circle"); dot.setAttribute("r", 3.6); dot.setAttribute("fill", "#fff");
      g.appendChild(halo); g.appendChild(dot); layer.appendChild(g);
      return { p: p, g: g, L: p.getTotalLength(), off: i * 0.37, sp: 5200 + i * 900 };
    });
    arrows.slice(0, 14).forEach(function (p, i) {
      var q = p.cloneNode(); q.setAttribute("class", "flow"); q.setAttribute("stroke", "#fff"); q.setAttribute("stroke-opacity", ".85");
      q.setAttribute("stroke-width", Math.max(2, +p.getAttribute("stroke-width") + 0.6)); q.style.animationDelay = (-i * 0.31) + "s"; layer.appendChild(q);
    });
    f._live = { tr: tr, t0: 0 }; return f._live;
  }
  var running = new Set(), raf = 0;
  function tick(now) {
    running.forEach(function (f) {
      var L = f._live; if (!L.t0) L.t0 = now;
      L.tr.forEach(function (t) {
        var u = ((now - L.t0) / t.sp + t.off) % 1, e = u < .5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
        var pt = t.p.getPointAtLength(e * t.L); t.g.setAttribute("transform", "translate(" + pt.x + "," + pt.y + ")");
        t.g.style.opacity = Math.min(1, Math.min(u, 1 - u) * 8);
      });
    });
    raf = running.size ? requestAnimationFrame(tick) : 0;
  }
  function goLive(f) { if (still) return; build(f); f.classList.add("live"); running.add(f); if (!raf) raf = requestAnimationFrame(tick); }
  function stopLive(f) { running.delete(f); f.classList.remove("live"); }
  function play(f) {
    clearTimeout(f._tm); f._done = false; stopLive(f); f.classList.remove("on"); void f.getBoundingClientRect(); f.classList.add("on");
    if (f._live) f._live.t0 = 0;
    f._tm = setTimeout(function () { f._done = true; if (f._vis !== false) goLive(f); }, (lastT(f) + 1.5) * 1000);
  }
  figs.forEach(function (f) {
    var host = f.closest("figure");
    if (host && !still) {
      var b = document.createElement("button"); b.type = "button"; b.className = "replay"; b.textContent = "Replay";
      b.setAttribute("aria-label", "Replay this diagram"); b.addEventListener("click", function () { play(f); }); var cap = host.querySelector("figcaption"); host.insertBefore(b, cap ? cap.nextSibling : null); host.classList.add("hasreplay");
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

  /* ---- intro reel: plays once, holds the wordmark; replay on request ---- */
  var reel = document.querySelector(".reel video");
  if (reel) {
    var btn = document.querySelector(".reel button");
    if (still) { reel.removeAttribute("autoplay"); reel.pause(); }
    if (btn) btn.addEventListener("click", function () { reel.currentTime = 0; reel.play(); });
  }

  /* ---- helpers for widgets ---- */
  var NS = "http://www.w3.org/2000/svg", C = { blue: "#58C4DD", teal: "#5CD0B3", yellow: "#FFFF00", ink: "#ECECEC", dim: "#8C8C8C", rule: "#3a3a3a", red: "#FC6255" };
  function el(n, a, txt) { var e = document.createElementNS(NS, n); for (var k in a) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; return e; }
  function svg(w, h) { return el("svg", { viewBox: "0 0 " + w + " " + h, class: "wsvg", role: "img" }); }
  function T(s, x, y, o) { o = o || {}; return el("text", { x: x, y: y, fill: o.fill || C.dim, "font-size": o.size || 13, "text-anchor": o.anchor || "start", "font-style": o.italic ? "italic" : "normal", "font-family": "CMU Serif, Georgia, serif" }, s); }
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
