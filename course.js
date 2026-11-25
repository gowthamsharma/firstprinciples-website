/* First Principles prerequisites course: lesson quizzes, progress, grading and the final test.
   Progress lives only in this browser (localStorage). */
(function () {
  "use strict";
  var KEY = "fp-course-v1";
  function load() {
    try { var d = JSON.parse(localStorage.getItem(KEY) || "{}"); d.lessons = d.lessons || {}; return d; }
    catch (e) { return { lessons: {} }; }
  }
  function save(d) { try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) { /* private mode: progress lasts for this page only */ } }
  var LETTERS = [[90, "A"], [80, "B"], [70, "C"], [60, "D"]];
  function letter(p) { for (var i = 0; i < LETTERS.length; i++) if (p >= LETTERS[i][0]) return LETTERS[i][1]; return "Not yet"; }
  // a lesson is complete at 60% or better (3 of 5; older 3-question records: 2 of 3)
  function passed(best, of) { return best / (of || 3) >= 0.6 - 1e-9; }
  function today() { return new Date().toISOString().slice(0, 10); }
  function fmtDate(iso) { try { return new Date(iso + "T12:00:00").toLocaleDateString(undefined, { day: "numeric", month: "long", year: "numeric" }); } catch (e) { return iso; } }

  /* ---------- lesson quiz ---------- */
  var lq = document.querySelector(".lq");
  if (lq) {
    var slug = lq.getAttribute("data-lesson"), items = lq.querySelectorAll("ol > li"), res = lq.querySelector(".lq-r");
    var d0 = load(); d0.last = slug; save(d0);
    var prev = d0.lessons[slug];
    function render() {
      var answered = 0, right = 0;
      items.forEach(function (li) { if (li.hasAttribute("data-a")) { answered++; if (li.getAttribute("data-a") === li.getAttribute("data-c")) right++; } });
      if (answered < items.length) {
        res.innerHTML = prev ? '<p class="lq-prev">Your best so far: <b>' + prev.best + " / " + items.length + "</b>" + (passed(prev.best, prev.of || items.length) ? " · lesson complete" : "") + "</p>" : "";
        return;
      }
      var d = load(), rec = d.lessons[slug] || { best: 0 };
      rec.best = Math.max(rec.best || 0, right); rec.last = right; rec.of = items.length; rec.at = today();
      d.lessons[slug] = rec; save(d); prev = rec;
      if (window.fpTrack) window.fpTrack(passed(right, items.length) ? "lesson_quiz_pass" : "lesson_quiz_fail", "last_lesson", slug);
      var done = Object.keys(d.lessons).filter(function (k) { return passed(d.lessons[k].best, d.lessons[k].of); }).length, total = +lq.getAttribute("data-total");
      var nextA = document.querySelector(".pager .next");
      res.innerHTML = '<div class="lq-score ' + (passed(right, items.length) ? "pass" : "fail") + '"><b>' + right + " / " + items.length + "</b><span>" +
        (right === items.length ? "Full marks. Lesson complete." : passed(right, items.length) ? "Lesson complete." : "Not yet: review the lesson and try again.") +
        "</span></div><p class=\"lq-meta\">Best score " + rec.best + " / " + items.length + " · " + done + " of " + total + " lessons complete</p>" +
        '<p class="lq-acts"><button type="button" class="btn line" data-retry>Try again</button>' +
        (nextA ? ' <a class="btn" href="' + nextA.getAttribute("href") + '">Next lesson</a>' : ' <a class="btn" href="course-test.html">Take the final test</a>') +
        ' <a class="lq-link" href="prerequisites.html">Course overview</a></p>';
    }
    lq.addEventListener("click", function (e) {
      var b = e.target.closest("button");
      if (!b) return;
      if (b.hasAttribute("data-retry")) {
        items.forEach(function (li) { li.removeAttribute("data-a"); li.className = ""; li.querySelectorAll(".lq-o button").forEach(function (x) { x.className = ""; x.disabled = false; }); li.querySelector(".lq-e").hidden = true; });
        render(); items[0].scrollIntoView({ behavior: "smooth", block: "center" }); return;
      }
      var li = b.closest("li");
      if (!li || li.hasAttribute("data-a")) return;
      var v = b.getAttribute("data-v"), c = li.getAttribute("data-c"), ok = v === c;
      li.setAttribute("data-a", v); li.className = ok ? "ok" : "no";
      li.querySelectorAll(".lq-o button").forEach(function (x) {
        x.disabled = true;
        if (x.getAttribute("data-v") === c) x.className = "right";
        else if (x === b) x.className = "wrong";
      });
      var ex = li.querySelector(".lq-e"); ex.hidden = false;
      ex.innerHTML = "<b>" + (ok ? "Correct." : "Not quite.") + "</b> " + li.getAttribute("data-x");
      render();
    });
    render();
  }

  /* ---------- course dashboard ---------- */
  var dash = document.querySelector(".cdash");
  function summary(d) {
    var rows = document.querySelectorAll(".cmod li[data-s]"), total = rows.length || 50, done = 0, sum = 0, n = 0;
    Object.keys(d.lessons).forEach(function (k) { var r = d.lessons[k]; sum += r.best / (r.of || 3); n++; if (passed(r.best, r.of)) done++; });
    var avg = n ? sum / n * 100 : 0;                // average over lessons taken
    var avgAll = sum / total * 100;                  // for the grade, lessons not taken count as zero
    var test = d.test ? d.test.best / d.test.of * 100 : null;
    var grade = n ? 0.7 * avgAll + 0.3 * (test || 0) : null;
    return { total: total, done: done, avg: avg, test: test, grade: grade, attempted: n };
  }
  if (dash) {
    var d = load(), S = summary(d), q = function (k) { return document.querySelector('[data-k="' + k + '"]'); };
    document.querySelectorAll(".cmod").forEach(function (mod) {
      var c = 0, lis = mod.querySelectorAll("li[data-s]");
      lis.forEach(function (li) {
        var r = d.lessons[li.getAttribute("data-s")], st = li.querySelector(".cs");
        if (!r) return;
        if (passed(r.best, r.of)) { c++; li.classList.add("done"); st.textContent = r.best + "/" + (r.of || 3); }
        else { li.classList.add("tried"); st.textContent = r.best + "/" + (r.of || 3) + " · retry"; }
      });
      var mp = mod.querySelector(".cmp"); mp.textContent = c + " / " + lis.length;
      if (c === lis.length) mp.classList.add("full");
    });
    q("done").textContent = S.done;
    q("bar").style.width = (S.done / S.total * 100).toFixed(1) + "%";
    q("avg").textContent = S.attempted ? Math.round(S.avg) + "%" : "–";
    q("test").textContent = S.test === null ? "–" : Math.round(S.test) + "%";
    q("grade").textContent = S.grade === null ? "–" : letter(S.grade);
    var order = Array.prototype.map.call(document.querySelectorAll(".cmod li[data-s]"), function (li) { return li; });
    var nextLi = order.filter(function (li) { var r = d.lessons[li.getAttribute("data-s")]; return !r || !passed(r.best, r.of); })[0];
    var cont = q("cont");
    if (nextLi) {
      var a = nextLi.querySelector("a");
      cont.href = a.getAttribute("href");
      cont.textContent = S.attempted ? "Continue: lesson " + +nextLi.querySelector(".cn").textContent : "Start lesson 1";
    } else { cont.href = "course-test.html"; cont.textContent = "All lessons complete"; }
    if (S.done === S.total && S.test !== null && S.test >= 70) {
      var rec = q("record"); rec.hidden = false;
      q("grade2").textContent = letter(S.grade) + " (" + Math.round(S.grade) + "%)";
      q("test2").textContent = Math.round(S.test) + "%";
      q("date").textContent = fmtDate(d.test.at || today());
      var nm = q("name"); nm.value = d.name || "";
      nm.addEventListener("input", function () { var x = load(); x.name = nm.value; save(x); });
      q("print").addEventListener("click", function () { window.print(); });
    }
    q("reset").addEventListener("click", function () {
      if (q("reset").getAttribute("data-armed")) { try { localStorage.removeItem(KEY); } catch (e) {} location.reload(); return; }
      q("reset").setAttribute("data-armed", "1"); q("reset").textContent = "Click again to erase all progress";
    });
  }

  /* ---------- final test ---------- */
  var box = document.querySelector('[data-k="test"]'), bankEl = document.getElementById("bank");
  if (box && bankEl) {
    var bank = JSON.parse(bankEl.textContent), N = 25, picked;
    function draw() {
      var idx = bank.map(function (_, i) { return i; });
      for (var i = idx.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = idx[i]; idx[i] = idx[j]; idx[j] = t; }
      picked = idx.slice(0, N).sort(function (a, b) { return a - b; }).map(function (i) { return bank[i]; });
      var h = '<p class="ct-top"><span data-k="count">0 of ' + N + ' answered</span><span class="ct-time" data-k="time">40:00</span></p><ol class="ct-q">';
      picked.forEach(function (q, i) {
        h += '<li data-i="' + i + '"><p class="ct-m">' + (q.p === 1 ? "Financial statements" : "Economics") + " · " + q.m + "</p><p>" + q.q + '</p><div class="lq-o">' +
          q.o.map(function (o, j) { return '<button type="button" data-v="' + j + '"><b>' + "ABCD"[j] + "</b>" + o + "</button>"; }).join("") + "</div></li>";
      });
      h += '</ol><p class="ct-sub"><button type="button" class="btn" data-k="submit" disabled>Submit the test</button> <span class="ct-hint">Answer every question to submit.</span></p><div class="ct-res" aria-live="polite"></div>';
      box.innerHTML = h;
      var t0 = Date.now(), tm = box.querySelector('[data-k="time"]'), timer = setInterval(function () {
        var left = Math.max(0, 2400 - Math.floor((Date.now() - t0) / 1000));
        tm.textContent = Math.floor(left / 60) + ":" + ("0" + left % 60).slice(-2);
        if (!left) { tm.classList.add("over"); tm.textContent = "Time is up (you can still finish)"; clearInterval(timer); }
      }, 1000);
      box.onclick = function (e) {
        var b = e.target.closest("button"); if (!b) return;
        if (b.getAttribute("data-k") === "submit") { clearInterval(timer); grade(); return; }
        if (b.getAttribute("data-k") === "again") { draw(); window.scrollTo({ top: box.offsetTop - 90, behavior: "smooth" }); return; }
        var li = b.closest("li[data-i]"); if (!li || box.classList.contains("graded")) return;
        li.querySelectorAll("button").forEach(function (x) { x.classList.toggle("sel", x === b); });
        li.setAttribute("data-a", b.getAttribute("data-v"));
        var n = box.querySelectorAll("li[data-a]").length;
        box.querySelector('[data-k="count"]').textContent = n + " of " + N + " answered";
        box.querySelector('[data-k="submit"]').disabled = n < N;
      };
      box.classList.remove("graded");
    }
    function grade() {
      box.classList.add("graded");
      var right = 0, parts = { 1: [0, 0], 2: [0, 0] }, miss = [];
      box.querySelectorAll("li[data-i]").forEach(function (li) {
        var q = picked[+li.getAttribute("data-i")], a = +li.getAttribute("data-a"), ok = a === q.c;
        parts[q.p][1]++; if (ok) { right++; parts[q.p][0]++; } else miss.push(q);
        li.className = ok ? "ok" : "no";
        li.querySelectorAll("button").forEach(function (x) { var v = +x.getAttribute("data-v"); x.disabled = true; if (v === q.c) x.classList.add("right"); else if (v === a) x.classList.add("wrong"); });
        var ex = document.createElement("p"); ex.className = "lq-e"; ex.innerHTML = "<b>" + (ok ? "Correct." : "Not quite.") + "</b> " + q.x + ' <a href="' + q.s + '.html">Lesson: ' + q.t + "</a>"; li.appendChild(ex);
      });
      var pct = right / N * 100, d = load(), best = d.test ? Math.max(d.test.best, right) : right;
      d.test = { best: best, of: N, last: right, at: today(), attempts: ((d.test && d.test.attempts) || 0) + 1 }; save(d);
      if (window.fpTrack) window.fpTrack("final_test_submitted", "final_test_score", Math.round(pct));
      var bar = function (lab, x) { var p = x[1] ? Math.round(x[0] / x[1] * 100) : 0; return '<div class="rd-bar"><span>' + lab + '</span><i><b style="width:' + Math.max(p, 3) + "%;background:" + (p >= 75 ? "#0FA968" : p >= 50 ? "#F2C200" : "#D64545") + '"></b></i><em>' + x[0] + "/" + x[1] + "</em></div>"; };
      var lessons = {}; miss.forEach(function (q) { lessons[q.s] = q.t; });
      box.querySelector(".ct-res").innerHTML = '<div class="ct-score ' + (pct >= 70 ? "pass" : "fail") + '"><b>' + right + " / " + N + "</b><span>" + Math.round(pct) + "% · " + (pct >= 70 ? "Pass" : "Below the 70% mark") + "</span></div>" +
        bar("Financial statements", parts[1]) + bar("Economics", parts[2]) +
        (miss.length ? "<p><b>Lessons to revisit:</b></p><ul>" + Object.keys(lessons).map(function (s) { return '<li><a href="' + s + '.html">' + lessons[s] + "</a></li>"; }).join("") + "</ul>" : "<p>Every answer correct.</p>") +
        '<p class="lq-acts"><button type="button" class="btn" data-k="again">New test</button> <a class="lq-link" href="prerequisites.html">Back to the course (best score ' + best + "/" + N + ")</a></p>";
      box.querySelector(".ct-sub").hidden = true;
      box.querySelector(".ct-res").scrollIntoView({ behavior: "smooth", block: "start" });
    }
    draw();
  }
})();
