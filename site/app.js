/* AI Benchmarks Explained — plain, dependency-free site behavior.
 * Everything is local; no network calls, no tracking. */

(function () {
  "use strict";

  /* ---- Glossary: live filter on glossary.html ---- */
  var search = document.getElementById("glossary-search");
  var list = document.getElementById("glossary-list");
  var emptyNote = document.getElementById("no-results");

  if (search && list && emptyNote) {
    var entries = Array.prototype.slice.call(list.children);
    search.addEventListener("input", function () {
      var q = search.value.trim().toLowerCase();
      var visible = 0;
      entries.forEach(function (entry) {
        var text = entry.textContent.toLowerCase();
        var show = q === "" || text.indexOf(q) !== -1;
        entry.classList.toggle("hidden", !show);
        if (show) visible += 1;
      });
      emptyNote.classList.toggle("hidden", visible > 0);
    });
  }

  /* ---- Worked example: show the hidden leaderboard slices ---- */
  var slicesBtn = document.getElementById("show-slices");
  var slicesTable = document.getElementById("lb-slices");
  if (slicesBtn && slicesTable) {
    slicesBtn.addEventListener("click", function () {
      var nowHidden = slicesTable.classList.toggle("hidden");
      slicesBtn.setAttribute("aria-expanded", String(!nowHidden));
      slicesBtn.textContent = nowHidden
        ? "Show the hidden slices"
        : "Hide the hidden slices";
    });
  }

  /* ---- Sanity-test scorecard: add 0/1/2 seven times, out of 14 ---- */
  var form = document.getElementById("score-form");
  var totalEl = document.getElementById("score-total");
  var verdictEl = document.getElementById("score-verdict");
  if (form && totalEl && verdictEl) {
    var MAX = 14;
    var update = function () {
      var total = 0;
      for (var i = 1; i <= 7; i += 1) {
        var el = document.getElementById("s" + i);
        if (el) total += parseInt(el.value, 10) || 0;
      }
      totalEl.textContent = "Total: " + total + " / " + MAX;
      var verdict;
      if (total >= 11) {
        verdict = "11 or more: worth a bigger trial — ideally with a clean " +
          "constraint exercise. If tied with another model, favor the one " +
          "that passed the honesty probes.";
      } else if (total >= 7) {
        verdict = "7 to 10: usable with supervision. Watch exactly which " +
          "exercises lost points — those are your model's homework.";
      } else {
        verdict = "Under 7: probably exhausting, whatever its leaderboard " +
          "says. See chapter 02 for why the banner number disagrees.";
      }
      verdictEl.textContent = verdict;
    };
    form.addEventListener("change", update);
    update();
  }
})();
