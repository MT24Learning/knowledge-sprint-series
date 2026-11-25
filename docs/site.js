// Knowledge Sprint Series website. Static file: the page works without it.
(function () {
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealables = document.querySelectorAll(".reveal");
  var meters = document.querySelectorAll(".meter");

  if (reduce || !("IntersectionObserver" in window)) {
    revealables.forEach(function (el) { el.classList.add("on"); });
    meters.forEach(function (el) { el.classList.add("go"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add(entry.target.classList.contains("meter") ? "go" : "on");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    revealables.forEach(function (el) { io.observe(el); });
    meters.forEach(function (el) { io.observe(el); });
  }

  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", function () {
      var source = document.getElementById(button.getAttribute("data-copy"));
      if (!source) return;
      var text = source.textContent;
      var done = function () {
        var label = button.textContent;
        button.textContent = "Copied";
        setTimeout(function () { button.textContent = label; }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () {});
      } else {
        var range = document.createRange();
        range.selectNodeContents(source);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        try { document.execCommand("copy"); done(); } catch (err) { /* selection stays for manual copy */ }
      }
    });
  });
})();

// Header search: "/" focuses the field; on the search page the field shows the current query.
(function () {
  var field = document.getElementById("hq");
  if (!field) return;
  var q = new URLSearchParams(location.search).get("q");
  if (q && /\/search\/?$/.test(location.pathname)) field.value = q;
  document.addEventListener("keydown", function (ev) {
    if (ev.key !== "/" || ev.ctrlKey || ev.metaKey || ev.altKey) return;
    var t = ev.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    ev.preventDefault();
    field.focus();
    field.select();
  });
})();

// Back controls: go back in history when the visitor came from this site, else to the parent page.
(function () {
  var links = document.querySelectorAll("[data-back]");
  if (!links.length) return;
  var base = (document.querySelector('link[rel="canonical"]') || {}).href || "";
  var root = base ? new URL(".", new URL(base)).href.replace(/(sprints|phases|milestones|code|search)\/.*$/, "") : "";
  var fromSite = false;
  try {
    var ref = document.referrer ? new URL(document.referrer) : null;
    fromSite = !!ref && ref.origin === location.origin && ref.href !== location.href &&
      (!root || ref.pathname.indexOf(new URL(root).pathname) === 0);
  } catch (e) { fromSite = false; }
  links.forEach(function (a) {
    a.addEventListener("click", function (ev) {
      if (fromSite && window.history.length > 1) {
        ev.preventDefault();
        window.history.back();
      }
    });
  });
  var floating = document.querySelector(".back-float");
  if (!floating) return;
  var ticking = false;
  function update() {
    document.body.classList.toggle("scrolled", window.scrollY > 520);
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
  }, { passive: true });
  update();
})();

// Reading spotlight: on text pages the sticky image lights the part whose text is being read;
// clicking a part of the image scrolls to its text.
(function () {
  var box = document.querySelector(".spotlit");
  if (!box) return;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var spots = {};
  box.querySelectorAll(".spot").forEach(function (spot) {
    spots[spot.getAttribute("data-spot")] = spot;
    spot.addEventListener("click", function () {
      var target = document.querySelector('[data-spot="' + spot.getAttribute("data-spot") + '"]:not(.spot)');
      if (target) target.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    });
  });
  if (!("IntersectionObserver" in window)) return;
  var current = null;
  function light(key) {
    if (current) current.classList.remove("lit");
    current = spots[key] || null;
    if (current) current.classList.add("lit");
    box.classList.toggle("on", !!current);
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) light(entry.target.getAttribute("data-spot"));
    });
  }, { rootMargin: "-38% 0px -58% 0px" });
  document.querySelectorAll("[data-spot]:not(.spot)").forEach(function (el) { io.observe(el); });
})();
