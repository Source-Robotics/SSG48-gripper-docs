/* Loads Google's <model-viewer> library only on a page that shows a model: the library is a quarter of a megabyte
   compressed, and most pages have no model. The browser keeps it cached for the next page that has one. */
(function () {
  var SRC = "https://unpkg.com/@google/model-viewer@4.1.0/dist/model-viewer.min.js";
  function load() {
    if (!document.querySelector("model-viewer")) return;
    if (window.customElements && window.customElements.get("model-viewer")) return;
    if (document.getElementById("model-viewer-lib")) return;
    var s = document.createElement("script");
    s.type = "module";
    s.id = "model-viewer-lib";
    s.src = SRC;
    document.head.appendChild(s);
  }
  if (window.document$ && window.document$.subscribe) { window.document$.subscribe(load); }
  else if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", load); }
  else { load(); }
})();
