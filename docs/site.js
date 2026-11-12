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
