// Handles the Tableau loading state, a fallback message, and the mobile menu.
(function () {
  "use strict";

  var LOAD_TIMEOUT_MS = 25000; // Show the fallback if the dashboard takes too long.

  var viz = document.getElementById("tableauViz");
  var loading = document.getElementById("vizLoading");
  var error = document.getElementById("vizError");
  var settled = false;

  function showLoaded() {
    if (settled) return;
    settled = true;
    if (loading) loading.hidden = true;
  }

  function showError() {
    if (settled) return;
    settled = true;
    if (loading) loading.hidden = true;
    if (error) error.hidden = false;
    if (viz) viz.hidden = true;
  }

  if (viz) {
    // Fired by the Tableau Embedding API once the dashboard is ready to use.
    viz.addEventListener("firstinteractive", showLoaded);
    // Some versions also report load failures with this event.
    viz.addEventListener("vizloaderror", showError);
    // Safety net: nothing happened in time (blocked script, offline, wrong URL).
    window.setTimeout(showError, LOAD_TIMEOUT_MS);
  }

  // If the Tableau script failed to define <tableau-viz> shortly after load, fail early.
  window.addEventListener("load", function () {
    window.setTimeout(function () {
      if (!window.customElements || !customElements.get("tableau-viz")) showError();
    }, 8000);
  });

  // Mobile menu toggle.
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    menu.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }
})();