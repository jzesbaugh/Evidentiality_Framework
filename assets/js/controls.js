// Page controls: theme, copy as Markdown, copy an AI prompt, print. MIT licence.
(function () {
  var root = document.documentElement;
  root.classList.add('js');   // show the script-only buttons
  var order = ['auto', 'light', 'dark'];
  var label = { auto: 'Theme: auto', light: 'Theme: light', dark: 'Theme: dark' };
  function get() { try { return localStorage.getItem('theme') || 'auto'; } catch (e) { return 'auto'; } }
  function apply(t) {
    if (t === 'auto') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', t);
    document.querySelectorAll('iframe.visual').forEach(function (f) {
      try {
        var d = f.contentDocument && f.contentDocument.documentElement;
        if (!d) return;
        if (t === 'auto') d.removeAttribute('data-theme'); else d.setAttribute('data-theme', t);
      } catch (e) {}
    });
    var b = document.getElementById('t-theme'); if (b) b.textContent = label[t];
  }
  apply(get());
  document.addEventListener('DOMContentLoaded', function () {
    apply(get());
    function fit(f) {
      try { var d = f.contentDocument; if (d && d.body && d.body.childElementCount) { f.style.height = '60px'; f.style.height = (d.documentElement.scrollHeight + 8) + 'px'; } } catch (e) {}
    }
    document.querySelectorAll('iframe.visual').forEach(function (f) {
      f.addEventListener('load', function () { apply(get()); fit(f); });
      fit(f);
    });
    var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { document.querySelectorAll('iframe.visual').forEach(fit); }, 150); });
    var status = document.getElementById('t-status');
    function say(m) { if (status) { status.textContent = m; setTimeout(function () { status.textContent = ''; }, 2500); } }
    function copy(text, msg) {
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(function () { say(msg); }, function () { say('Copy failed'); });
      else say('Copy not supported here');
    }
    var th = document.getElementById('t-theme');
    if (th) th.addEventListener('click', function () {
      var t = order[(order.indexOf(get()) + 1) % order.length];
      try { localStorage.setItem('theme', t); } catch (e) {}
      apply(t);
    });
    var cm = document.getElementById('t-copy');
    if (cm) cm.addEventListener('click', function () {
      fetch(cm.dataset.md).then(function (r) { return r.text(); }).then(function (t) { copy(t, 'Markdown copied'); }, function () { say('Copy failed'); });
    });
    var ai = document.getElementById('t-ai');
    if (ai) ai.addEventListener('click', function () {
      copy('Please read this page and summarise it for me in plain language. Tell me what problem it describes, what it proposes, how strong the evidence is, and whether it fits my situation: ' + location.href.split('#')[0], 'Prompt copied: paste it into your AI assistant');
    });
    window.addEventListener('beforeprint', function () { document.querySelectorAll('details').forEach(function (d) { d.open = true; }); });
    var pr = document.getElementById('t-print');
    if (pr) pr.addEventListener('click', function () { window.print(); });
  });
})();
