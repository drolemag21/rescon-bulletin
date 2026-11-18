// RESCON Bulletin: progressive enhancement only. The site is fully readable without JS.
(function () {
  "use strict";

  // 1. Show times in the viewer's local timezone.
  var full = new Intl.DateTimeFormat(undefined, {
    year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit", timeZoneName: "short"
  });
  var dateOnly = new Intl.DateTimeFormat(undefined, { weekday: "short", year: "numeric", month: "short", day: "numeric" });
  document.querySelectorAll("time[datetime]").forEach(function (el) {
    var iso = el.getAttribute("datetime");
    if (el.hasAttribute("data-date-only")) {
      var p = iso.split("-").map(Number); // calendar date, no timezone shift
      if (p.length === 3) el.textContent = dateOnly.format(new Date(p[0], p[1] - 1, p[2]));
      return;
    }
    var d = new Date(iso);
    if (!isNaN(d)) { el.title = d.toISOString(); el.textContent = full.format(d); }
  });

  // 2. Stale notice: the site is built at update time, so say so when the last update is old.
  var stale = document.querySelector(".stale-notice[data-last-update]");
  if (stale) {
    var last = new Date(stale.getAttribute("data-last-update"));
    var hours = (Date.now() - last.getTime()) / 36e5;
    if (hours > 24) {
      var days = Math.floor(hours / 24);
      var badge = document.querySelector(".rescon-num");
      var name = document.querySelector(".rescon-name");
      stale.textContent = "No update in " + days + (days === 1 ? " day" : " days") +
        (badge ? " · RESCON " + badge.textContent.trim() + (name ? " " + name.textContent.trim() : "") : "") +
        ". The Daily and Weekly sections below reflect the last update, not today.";
      stale.hidden = false;
    }
  }

  // 3. Archive filters.
  var form = document.querySelector("form.filters");
  if (form) {
    var selects = form.querySelectorAll("select[data-filter]");
    var entries = document.querySelectorAll("article.entry");
    var groups = document.querySelectorAll(".day-group");
    var out = form.querySelector(".filter-count");
    var apply = function () {
      var shown = 0;
      entries.forEach(function (e) {
        var ok = true;
        selects.forEach(function (s) {
          if (!s.value) return;
          var vals = (e.getAttribute("data-" + s.getAttribute("data-filter")) || "").split(" ");
          if (vals.indexOf(s.value) === -1) ok = false;
        });
        e.hidden = !ok;
        if (ok) shown++;
      });
      groups.forEach(function (g) { g.hidden = !g.querySelector("article.entry:not([hidden])"); });
      out.textContent = shown + " of " + entries.length + " entries";
    };
    selects.forEach(function (s) { s.addEventListener("change", apply); });
    form.hidden = false;
    apply();
  }
})();
