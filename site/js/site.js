// Asciiverse website, design mockup. Reads data/catalog.json, shaped like
// hub's generated catalog (hub/catalog/SCHEMA.md), and renders the pages.

const LOGO =
  "▄▀█ █▀ █▀▀ █ █ █ █ █▀▀ █▀█ █▀ █▀▀\n" +
  "█▀█ ▄█ █▄▄ █ █ ▀▄▀ ██▄ █▀▄ ▄█ ██▄";

const PLAYER_OPTS = { theme: "asciiverse", fit: "width", controls: false, idleTimeLimit: 2,
  terminalFontFamily: '"Iosevka Term AV", "Cascadia Code", monospace', terminalLineHeight: 1.2 };

function el(html) {
  const t = document.createElement("template");
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
}

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

async function loadCatalog() {
  if (location.protocol === "file:") {
    document.body.innerHTML = `<p style="font:15px/1.6 monospace;color:#d5dbe1;padding:40px">
      This page loads catalog.json and the casts with fetch(), which browsers block on file:// pages.<br>
      Serve the folder instead: <code style="color:#7fdc5e">python3 -m http.server 8765 --bind 127.0.0.1</code>
      and open <a style="color:#ffb000" href="http://127.0.0.1:8765/">http://127.0.0.1:8765/</a></p>`;
    throw new Error("opened from file://");
  }
  // players measure the font when created, so it must be loaded first
  await document.fonts.load('16px "Iosevka Term AV"').catch(() => {});
  const r = await fetch("data/catalog.json");
  const cat = await r.json();
  if (cat.schema_version !== 1) throw new Error("unknown catalog schema_version " + cat.schema_version);
  // upstream projects holding several games, each game its own title (SCHEMA.md, "Collections")
  window.COLLECTIONS = cat.collections || {};
  return Object.values(cat.titles);
}

function platformsLabel(t) {
  const p = Object.keys(t.platforms || {});
  const out = [];
  if (p.some(x => x.includes("linux"))) out.push("LNX");
  if (p.some(x => x.includes("apple"))) out.push("MAC");
  if (p.some(x => x.includes("windows"))) out.push("WIN");
  return out.join(" ");
}

// The page Markdown subset from SCHEMA.md: ## and ### headings, paragraphs,
// lists (one nesting level), bold, italic, inline code, http(s) links.
function renderPage(md) {
  const inline = s => esc(s)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>")
    .replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" rel="noopener">$1</a>');
  const out = [];
  let para = [], list = null;
  const flushPara = () => { if (para.length) { out.push("<p>" + inline(para.join(" ")) + "</p>"); para = []; } };
  const flushList = () => { if (list) { out.push(`<${list.tag}>` + list.items.map(i => "<li>" + inline(i) + "</li>").join("") + `</${list.tag}>`); list = null; } };
  for (const raw of md.split("\n")) {
    const line = raw.trimEnd();
    let m;
    if (!line.trim()) { flushPara(); flushList(); continue; }
    if ((m = line.match(/^(###?) (.*)$/))) {
      flushPara(); flushList();
      out.push(`<h${m[1].length}>${inline(m[2])}</h${m[1].length}>`);
    } else if ((m = line.match(/^\s*([-*]|\d+\.) (.*)$/))) {
      flushPara();
      const tag = /\d/.test(m[1]) ? "ol" : "ul";
      if (!list || list.tag !== tag) { flushList(); list = { tag, items: [] }; }
      list.items.push(m[2]);
    } else if (list && /^\s+\S/.test(raw)) {
      list.items[list.items.length - 1] += " " + line.trim();
    } else {
      flushList();
      para.push(line.trim());
    }
  }
  flushPara(); flushList();
  return out.join("\n");
}

// Players size themselves from their container, so they are only created
// once attached and visible; that also means off-screen casts never load.
const lazy = new IntersectionObserver(entries => {
  for (const e of entries) if (e.isIntersecting) { lazy.unobserve(e.target); e.target.mount(); }
}, { rootMargin: "300px" });

function mountPlayer(box, url, opts) {
  box.mount = () => { box.player = AsciinemaPlayer.create(url, box, opts); };
  lazy.observe(box);
  return box;
}

// A terminal tile showing the cast's still frame; plays while hovered.
// FRESH!: new to Asciiverse, whatever the game's age (David, 2026-11-13). Shown for
// 30 days from the day the title arrived (catalog.json's `added`), counted here so
// it drops off without a rebuild; titles from the launch day itself never count.
const LAUNCH_DAY = "2026-11-03", FRESH_DAYS = 30;
function isFresh(t) {
  if (!t.added || t.added <= LAUNCH_DAY) return false;
  const age = (Date.now() - Date.parse(t.added + "T00:00:00Z")) / 864e5;
  return age < FRESH_DAYS;
}
// The diagonal corner banners on a still or player: OLD! top left, NEW! top right,
// FRESH! in whichever top corner is free (OLD! and NEW! never come together).
function corners(box, t, big = false) {
  const b = big ? " big" : "";
  if (t.old) box.append(el(`<div class="old${b}">OLD!</div>`));
  if (t.new) box.append(el(`<div class="new${b}">NEW!</div>`));
  if (isFresh(t)) box.append(el(`<div class="fresh${t.new ? " left" : ""}${b}">FRESH!</div>`));
  return box;
}
// The same as pills beside a title, and as small marks in the library lists.
function pills(t) {
  return (t.old ? ` <span class="old-pill">OLD!</span>` : "") + (t.new ? ` <span class="new-pill">NEW!</span>` : "")
    + (isFresh(t) ? ` <span class="fresh-pill">FRESH!</span>` : "");
}
function marks(t) {
  return (t.old ? `<span class="m old-m">OLD!</span>` : t.new ? `<span class="m new-m">NEW!</span>` : "")
    + (isFresh(t) ? `<span class="m fresh-m">FRESH!</span>` : "");
}
// The newest arrivals first, for the Fresh shelves.
function freshest(list) {
  return list.filter(isFresh).sort((a, b) => b.added.localeCompare(a.added) || a.title.localeCompare(b.title));
}

function tile(t, { hover = true, at } = {}) {
  const box = el(`<div class="term fixed"></div>`);
  const still = at ?? t.thumbnail_at ?? 5;
  mountPlayer(box, t.cast_url, { ...PLAYER_OPTS, fit: "both", poster: "npt:" + still, loop: true });
  if (hover) {
    let started = false;
    box.addEventListener("pointerenter", () => {
      const p = box.player; if (!p) return;
      box.classList.add("live");
      if (!started) { p.seek(still).then(() => p.play()); started = true; } else p.play();
    });
    box.addEventListener("pointerleave", () => { box.classList.remove("live"); box.player?.pause(); });
  }
  return box;
}

// where donations to Asciiverse go: the header's Support menu, the footer
// and support.html read this list
const SUPPORT = [
  ["GitHub Sponsors", "https://github.com/sponsors/theasciiverse", "monthly or one-time"],
  ["Patreon", "https://www.patreon.com/asciiverse", "monthly membership"],
];
const supportLinks = () => SUPPORT.map(([n, u, d]) =>
  `<a href="${u}" target="_blank" rel="noopener"><b>${n}</b><span>${d}</span></a>`).join("")
  + `<a href="support.html"><b>More ways to help</b><span>and the makers' own pages</span></a>`;

function header(active, sub = "home") {
  const nav = [["index.html", "Catalog"], ["get-av.html", "Get av"], ["history.html", "History"], ["submit.html", "Submit a title"]];
  const head = el(`
  <div class="site-head">
    <header class="top"><div class="wrap">
      <a class="logo" href="index.html" aria-label="Asciiverse">${LOGO}<small>WHERE TEXT COMES ALIVE</small></a>
      <nav class="mainnav">${nav.map(([h, n]) => `<a href="${h}" class="${n === active ? "on" : ""}">${n}</a>`).join("")}</nav>
      <div class="right"><details class="support"><summary class="btn-av">♥ Support</summary><div class="support-menu">${supportLinks()}</div></details></div>
    </div></header>
    <div class="subnav"><div class="wrap">
      ${[["index.html", "Home", "home"], ["games.html", "Games", "games"], ["adventures.html", "Text adventures", "adventures"], ["muds.html", "MUDs", "muds"], ["programs.html", "Programs", "programs"], ["art.html", "Art & Demos", "art"], ["movies.html", "Movies", "movies"]]
        .map(([h, n, k]) => `<a href="${h}" class="${sub === k ? "on" : ""}">${n}</a>`).join("")}
      <label class="search"><span>/</span><input placeholder="search titles, tags, developers"></label>
    </div></div>
  </div>`);
  headerSearch(head.querySelector(".search"));
  // the Support menu closes on a click anywhere else
  const sup = head.querySelector(".support");
  document.addEventListener("click", e => { if (!sup.contains(e.target)) sup.open = false; });
  // the header stays at the top; pages that pin things under it read its height
  requestAnimationFrame(() => {
    const set = () => document.documentElement.style.setProperty("--head-h", head.offsetHeight + "px");
    set(); window.addEventListener("resize", set);
  });
  return head;
}

// The header's search: every title in the catalog, matched on its title,
// tags, genre and developer; a click (or Enter on the first) opens it on its
// kind's page. "/" anywhere on the page puts the cursor in the box.
const KIND_PAGE = { game: "games.html", adventure: "adventures.html", program: "programs.html",
  art: "art.html", mud: "muds.html", movie: "movies.html" };
function headerSearch(box) {
  const input = box.querySelector("input");
  const menu = el(`<div class="search-menu" hidden></div>`);
  box.append(menu);
  let all = null;
  const load = () => all ??= loadCatalog().then(ts => ts.filter(t => KIND_PAGE[t.kind])).catch(() => []);
  const score = (t, q) => {
    const title = t.title.toLowerCase();
    if (title.startsWith(q)) return 0;
    if (title.includes(q) || t.id.includes(q)) return 1;
    const rest = [...(t.topics || []), t.genre, t.theme, t.developer?.name, t.upstream?.name]
      .filter(Boolean).join(" ").toLowerCase();
    return rest.includes(q) ? 2 : -1;
  };
  const href = t => `${KIND_PAGE[t.kind]}#${t.id}`;
  async function show() {
    const q = input.value.trim().toLowerCase();
    if (!q) { menu.hidden = true; return; }
    const hits = (await load()).map(t => [score(t, q), t]).filter(([s]) => s >= 0)
      .sort((a, b) => a[0] - b[0] || a[1].title.localeCompare(b[1].title)).map(([, t]) => t);
    if (q !== input.value.trim().toLowerCase()) return;     // typed on meanwhile
    menu.innerHTML = hits.length
      ? hits.slice(0, 8).map(t => `<a href="${href(t)}"><b>${esc(t.title)}${isFresh(t) ? ` <i class="fresh-m">FRESH!</i>` : ""}</b><span>${esc(t.kind === "mud" ? "MUD" : t.kind)}${t.genre ? " · " + esc(t.genre) : ""}${t.developer?.name ? " · " + esc(t.developer.name) : ""}</span></a>`).join("")
        + (hits.length > 8 ? `<p>${hits.length - 8} more: type a little more</p>` : "")
      : `<p>Nothing matches "${esc(input.value.trim())}"</p>`;
    menu.hidden = false;
  }
  input.addEventListener("focus", load);
  input.addEventListener("input", show);
  input.addEventListener("keydown", e => {
    if (e.key === "Escape") { input.value = ""; menu.hidden = true; input.blur(); }
    if (e.key === "Enter") { const a = menu.querySelector("a"); if (a) { location.href = a.href; menu.hidden = true; input.blur(); } }
  });
  menu.addEventListener("click", e => { if (e.target.closest("a")) menu.hidden = true; });
  document.addEventListener("click", e => { if (!box.contains(e.target)) menu.hidden = true; });
  document.addEventListener("keydown", e => {
    if (e.key === "/" && !/^(INPUT|TEXTAREA)$/.test(document.activeElement?.tagName)) { e.preventDefault(); input.focus(); }
  });
}

function footer() {
  return el(`
  <footer class="foot"><div class="wrap">
    <div class="ascii">${LOGO}</div>
    <div>A home for terminal games and programs.<br>Funded by donations, built in the open.</div>
    <div><a href="get-av.html">Get av</a><br><a href="submit.html">Submit your game</a><br><a href="https://github.com/theasciiverse/hub/blob/master/RECORDING.md">Recording guide</a><br><a href="https://github.com/theasciiverse/hub/blob/master/catalog/SCHEMA.md">Catalog format</a></div>
    <div><a href="https://github.com/theasciiverse/av">av on GitHub</a><br><a href="https://github.com/theasciiverse/hub">hub on GitHub</a><br><a href="support.html">Support</a>: ${SUPPORT.map(([n, u]) => `<a href="${u}" target="_blank" rel="noopener">${n}</a>`).join(" · ")}</div>
  </div></footer>`);
}

// Copies text to the clipboard: the Clipboard API where the browser allows
// it, else the older execCommand route through a hidden text area. Resolves
// to whether it worked, so a button only says "copied" when it did.
async function copyText(text) {
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return true;
    }
  } catch (e) { /* refused: try the older way */ }
  const ta = document.createElement("textarea");
  ta.value = text;
  ta.setAttribute("readonly", "");
  ta.style.cssText = "position:fixed;top:0;left:0;opacity:0;pointer-events:none";
  document.body.append(ta);
  ta.select();
  let ok = false;
  try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
  ta.remove();
  return ok;
}
// What a copy button does: copy, say so, and when nothing could copy,
// select the command on the page so Ctrl+C (Cmd+C) takes it.
async function copyFeedback(btn, text, codeEl) {
  const label = btn.dataset.label || (btn.dataset.label = btn.textContent);
  if (await copyText(text)) {
    btn.textContent = "copied";
  } else {
    if (codeEl) {
      const r = document.createRange(); r.selectNodeContents(codeEl);
      const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
    }
    btn.textContent = /Mac/.test(navigator.platform) ? "press ⌘C" : "press Ctrl+C";
  }
  setTimeout(() => (btn.textContent = label), 1600);
}
function copyButton(btn, text) {
  btn.addEventListener("click", () => copyFeedback(btn, text, btn.parentElement?.querySelector("code")));
}

function installLine(t) {
  const n = el(`<div class="install"><code>av install ${esc(t.id)}</code><button>copy</button></div>`);
  copyButton(n.querySelector("button"), "av install " + t.id);
  return n;
}

// The one-line installers for av itself (install.sh and install.ps1 at the site root).
const AV_INSTALL = [
  ["curl", "curl -fsSL https://asciiverse.sh/install.sh | sh"],
  ["wget", "wget -qO- https://asciiverse.sh/install.sh | sh"],
  ["PowerShell", "irm https://asciiverse.sh/install.ps1 | iex"],
  [".deb", "curl -fsSLO https://asciiverse.sh/releases/av/latest/av_amd64.deb && sudo apt install ./av_amd64.deb",
    "Debian and Ubuntu: Asciiverse in your applications menu, and tab completion. On ARM, <code>av_arm64.deb</code>."],
];

// The tab that works out of the box: Ubuntu's desktop ships wget but not
// curl (its 24.04 and 26.04 image manifests), macOS ships curl.
function avInstaller() {
  const ua = navigator.userAgent;
  const first = /Windows/.test(ua) ? 2 : /Linux/.test(ua) && !/Android/.test(ua) ? 1 : 0;
  return tabbedInstall(AV_INSTALL, first);
}

// Tabs over one install line: [[tab name, command, optional note], ...]
function tabbedInstall(options, first = 0) {
  const n = el(`<div class="av-get"><div class="av-tabs" role="tablist"></div><div class="install"><code></code><button>copy</button></div><p class="tab-note"></p></div>`);
  const tabs = n.querySelector(".av-tabs"), code = n.querySelector("code"), note = n.querySelector(".tab-note");
  let cmd = "";
  function pick(i) {
    cmd = options[i][1]; code.textContent = cmd;
    note.innerHTML = options[i][2] || ""; note.hidden = !options[i][2];
    tabs.querySelectorAll("button").forEach((b, j) => b.setAttribute("aria-selected", i === j));
  }
  options.forEach(([name], i) => {
    const b = el(`<button role="tab">${name}</button>`); b.onclick = () => pick(i); tabs.append(b);
  });
  const btn = n.querySelector(".install button");
  // A line that downloads and runs a script (curl ... | sh, irm ... | iex)
  // is never put on the clipboard by the page: content blockers such as
  // uBlock Origin stop that (their ClickFix guard) and warn the reader. The
  // button selects it instead, and the reader's own Ctrl+C copies it.
  const fetchAndRun = c => /\|\s*(sudo\s+)?(sh|bash|zsh|iex)\b/.test(c) || /\b(irm|iwr|Invoke-(RestMethod|WebRequest))\b/i.test(c);
  btn.addEventListener("click", () => {
    if (!fetchAndRun(cmd)) return copyFeedback(btn, cmd, code);
    const r = document.createRange(); r.selectNodeContents(code);
    const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
    btn.textContent = /Mac/.test(navigator.platform) ? "now \u2318C" : "now Ctrl+C";
    setTimeout(() => (btn.textContent = "copy"), 2500);
  });
  pick(first);
  return n;
}

// A capsule card: front picture (the cast's still frame), title, one-liner, genre, platforms.
function capsule(t) {
  const c = el(`<a class="cap" href="title.html?id=${t.id}"></a>`);
  const tl = tile(t);
  tl.append(el(`<span class="playing">▶ preview</span>`));
  corners(tl, t);
  c.append(tl);
  c.append(el(`<div class="cap-body"><h4>${esc(t.title)}</h4><p>${esc(t.description)}</p>
    <div class="cap-foot"><span class="genre">${esc(t.genre || t.kind)}</span><span>${esc(t.developer?.name)}</span><span class="plat">${platformsLabel(t)}</span></div></div>`));
  return c;
}

// Steam's scrolling shelf: one row of capsules, a page at a time, arrows either side, page marks below.
// after the developer: the original a port or package came from; for a story
// (its author is the developer) only the year it first came out
function byline(t) {
  if (!t.upstream) return "";
  if (t.kind === "adventure") { const y = /(\d{4})$/.exec(t.upstream.name || ""); return y ? `, ${y[1]}` : ""; }
  // nothing to add when the developer is the original's author
  if (t.upstream.name === t.developer?.name) return "";
  return `, after ${esc(t.upstream.name)}`;
}

// Where a title comes from: who made it, what Asciiverse changed, and links to the
// original project, our source and the list of changes. Store page and library pane.
function provenance(t, cls = "box prov") {
  if (!t.provenance && !t.upstream) return null;
  const host = u => { try { return new URL(u).host.replace(/^www\./, ""); } catch { return ""; } };
  const gh = t.repo ? `https://github.com/${t.repo}` : "";
  const links = [];
  if (t.upstream?.url) links.push(`<a href="${esc(t.upstream.url)}"><b>Original</b> ${esc(t.upstream.name)} <span class="host">${esc(host(t.upstream.url))}</span></a>`);
  if (gh) links.push(`<a href="${gh}"><b>Our source</b> ${esc(t.repo)} <span class="host">github.com</span></a>`);
  if (gh && t.changes) links.push(`<a href="${gh}/blob/HEAD/${esc(t.changes)}"><b>${/PATCHES/.test(t.changes) ? "Our changes" : "Provenance"}</b> ${esc(t.changes)}</a>`);
  return el(`<div class="${cls}"><h3>Where it comes from</h3>${t.provenance ? `<p>${esc(t.provenance)}</p>` : ""}<div class="prov-links">${links.join("")}</div></div>`);
}

function shelf(title, sub, list, more, card = capsule) {
  const s = el(`<section class="sect shelf"><div class="sect-head"><h2>${title}</h2><span class="sub">${sub}</span>${more ? `<a class="more" href="${more}">see all</a>` : ""}</div>
    <div class="shelf-body"><button class="shelf-arrow prev" aria-label="scroll back">‹</button>
    <div class="shelf-track"></div>
    <button class="shelf-arrow next" aria-label="scroll on">›</button></div><div class="dots shelf-dots"></div></section>`);
  const track = s.querySelector(".shelf-track"), dots = s.querySelector(".shelf-dots");
  list.forEach(t => track.append(card(t)));
  const page = () => track.clientWidth + 12;
  s.querySelector(".prev").onclick = () => track.scrollBy({ left: -page(), behavior: "smooth" });
  s.querySelector(".next").onclick = () => track.scrollBy({ left: page(), behavior: "smooth" });
  function update() {
    const pages = Math.max(1, Math.ceil((track.scrollWidth - 4) / page()));
    const at = Math.round(track.scrollLeft / page());
    if (dots.children.length !== pages) {
      dots.replaceChildren(...Array.from({ length: pages }, (_, i) => {
        const b = el(`<button aria-label="page ${i + 1}"></button>`);
        b.onclick = () => track.scrollTo({ left: i * page(), behavior: "smooth" });
        return b;
      }));
    }
    [...dots.children].forEach((b, i) => b.classList.toggle("on", i === at));
    s.classList.toggle("fits", pages === 1);
    s.querySelector(".prev").disabled = track.scrollLeft < 4;
    s.querySelector(".next").disabled = track.scrollLeft + track.clientWidth > track.scrollWidth - 4;
  }
  track.addEventListener("scroll", () => requestAnimationFrame(update), { passive: true });
  new ResizeObserver(update).observe(track);
  return s;
}

// Steam's library: a sidebar listing every title of one kind, and a main pane
// that shows the shelves ("Home") or the selected title. The selection lives
// in location.hash, so a title can be linked to and Back works.
function library({ label, items, groups, home, detail, badge, mark = () => "", empty = "Nothing here right now." }) {
  const root = el(`<div class="lib">
    <aside class="lib-side">
      <button class="lib-home">Home</button>
      <div class="lib-kind">${label}<span>${items.filter(t => t.kind !== "client").length}</span></div>
      <label class="lib-filter"><span>/</span><input placeholder="filter ${label.toLowerCase()}"></label>
      <nav class="lib-list"></nav>
    </aside>
    <div class="lib-main"></div></div>`);
  const list = root.querySelector(".lib-list"), main = root.querySelector(".lib-main");
  document.body.classList.add("lib-page");
  const byTitle = (a, b) => a.title.localeCompare(b.title, "en", { sensitivity: "base" });
  if (!items.length) list.append(el(`<p class="lib-none">${empty}</p>`));
  for (const g of groups || [{ items }]) {
    if (g.label) list.append(el(`<div class="lib-group">${g.label}</div>`));
    if (!g.items.length && g.empty) list.append(el(`<p class="lib-none">${g.empty}</p>`));
    for (const t of g.keepOrder ? g.items : [...g.items].sort(byTitle)) {
      list.append(el(`<a href="#${t.id}" data-id="${t.id}"><span class="badge" style="background:${badgeColor(t.genre || t.theme || t.kind)}">${esc(badge(t))}</span><span class="name">${esc(t.title)}</span>${mark(t)}</a>`));
    }
  }
  root.querySelector(".lib-filter input").addEventListener("input", e => {
    const q = e.target.value.trim().toLowerCase();
    list.querySelectorAll("a").forEach(a => (a.hidden = q && !a.textContent.toLowerCase().includes(q)));
  });
  root.querySelector(".lib-home").onclick = () => { history.pushState(null, "", location.pathname); route(); };
  function route() {
    main.querySelectorAll(".term").forEach(b => b.player?.dispose?.());
    const t = items.find(x => "#" + x.id === location.hash);
    list.querySelectorAll("a").forEach(a => a.classList.toggle("on", !!t && a.dataset.id === t.id));
    root.querySelector(".lib-home").classList.toggle("on", !t);
    main.replaceChildren();
    if (t) main.append(detail(t)); else home(main);
    // a home with nothing on its shelves still says something
    if (!t && !main.children.length) main.append(el(`<section class="sect"><p class="lib-none">${empty}</p></section>`));
    main.append(footer());               // the footer scrolls with the pane
    main.scrollTop = 0; window.scrollTo({ top: 0 });
  }
  window.addEventListener("hashchange", route);
  route();

  return root;
}

// colour of a sidebar badge, from the title's genre or theme, so neighbours differ at a glance
function badgeColor(key) {
  let h = 0; for (const c of key || "") h = (h * 31 + c.charCodeAt(0)) % 360;
  return `hsl(${h} 45% 42%)`;
}

// The selected game in the library pane: recording, facts, install line.
function gameDetail(t) {
  const d = el(`<section class="lib-detail">
    <div class="lib-hero"><div class="term live"></div></div>
    <div class="lib-bar">
      <div class="install"><code>av install ${esc(t.id)}</code><button>copy</button></div>
      <dl><dt>Genre</dt><dd>${esc(t.genre || t.kind)}</dd><dt>Runs on</dt><dd>${platformsLabel(t) || "LNX"}</dd>
        <dt>Version</dt><dd>${esc(t.version || "")}</dd></dl>
      <a class="store" href="title.html?id=${t.id}">Store page ›</a>
    </div>
    <h1>${esc(t.title)}${pills(t)}</h1>
    <p class="one">${esc(t.description)}</p>
    <div class="tags">${(t.topics || []).map(x => `<span class="tag">${esc(x)}</span>`).join("")}</div>
    <p class="by">by ${esc(t.developer?.name || "")}${byline(t)}</p>
  </section>`);
  const pv = provenance(t, "prov lib-prov");
  if (pv) d.append(pv);
  const box = d.querySelector(".term");
  mountPlayer(box, t.cast_url, { ...PLAYER_OPTS, autoPlay: true, loop: true, startAt: Math.max(0, (t.thumbnail_at || 5) - 2) });
  copyButton(d.querySelector(".install button"), "av install " + t.id);
  return d;
}

// A MUD has no recording: its card and its library page are text, the world's age and address.
function mudCard(m) {
  const c = el(`<a class="cap mud-cap" href="#${m.id}">
    ${m.cast_url ? "" : `<div class="mud-face"><span class="yr">${m.since || "?"}</span><span class="th">${esc(m.theme || "")}</span><span class="nm">${esc(m.title)}</span></div>`}
    <div class="cap-body"><h4>${esc(m.title)}</h4><p>${esc(m.description)}</p>
      <div class="cap-foot"><span class="genre">${esc(m.theme || "mud")}</span><span class="plat">${m.since || ""}</span></div></div></a>`);
  // the front picture is the world's own greeting screen, as it stands once it has finished drawing
  if (m.cast_url) {
    const tl = tile(m, { at: m.thumbnail_at ?? 60 });
    tl.append(el(`<span class="since-badge">${m.since || ""}</span>`));
    c.prepend(tl);
  }
  return c;
}

function mudDetail(m) {
  const addr = `${m.connect.host} ${m.connect.port}`;
  const d = el(`<section class="lib-detail">
    ${m.cast_url ? `<div class="lib-hero"><div class="term live"></div></div>` : `<div class="mud-hero"><span class="yr">online since ${m.since || "?"}</span><span class="nm">${esc(m.title)}</span><span class="th">${esc(m.theme || "")}</span></div>`}
    <div class="lib-bar">
      <div class="slot"></div>
      <dl><dt>Since</dt><dd>${m.since || "?"}</dd><dt>Theme</dt><dd>${esc(m.theme || "")}</dd>${m.language ? `<dt>Language</dt><dd>${esc(m.language)}</dd>` : ""}</dl>
      ${m.website ? `<a class="store" href="${esc(m.website)}">Website ›</a>` : ""}
    </div>
    <h1>${esc(m.title)}</h1>
    <p class="one">${esc(m.description)}</p>
    <div class="tags">${(m.topics || []).map(x => `<span class="tag">${esc(x)}</span>`).join("")}</div>
  </section>`);
  // the greeting draws once and stays, like connecting for real; no replay loop
  if (m.cast_url) mountPlayer(d.querySelector(".lib-hero .term"), m.cast_url, { ...PLAYER_OPTS, autoPlay: true, loop: false });
  const tls = m.connect.tls_port;
  const opts = [];
  if (tls) opts.push(["openssl", `openssl s_client -quiet -connect ${m.connect.host}:${tls}`, "Connects without a MUD client."]);
  opts.push(["telnet", `telnet ${addr}`, "Works for every MUD. On Windows, turn on the Telnet Client in Windows Features first."]);
  d.querySelector(".slot").replaceWith(tabbedInstall(opts));
  return d;
}

// Terminal MUD clients, from each project's own README (checked 2026-10-12).
// Platform values: "yes", or a short note for how it runs there today; null means not yet.
const MUD_CLIENTS = [
  { id: "lera", kind: "client", title: "Lera", theme: "client", lang: "Rust", license: "MIT", ours: true,
    version: "0.1.0", released: "November 2026", website: "https://github.com/theasciiverse/lera",
    description: "The Asciiverse MUD client: pick a world from the list and you are in, with scrollback that keeps the live text in view and your health and mana in the status line",
    platforms: { Linux: "yes (x86-64, ARM64)", macOS: "yes (Intel, Apple silicon)", Windows: "yes (x86-64, ARM64)" },
    tls: "yes: whenever the world offers it, or <code>lera host port --tls</code>; certificates checked against the Mozilla root set built in",
    packaged: "programs.html#lera",
    install: [["av", "av install lera", "Linux, macOS and Windows, x86-64 and ARM64. av's Connect on any MUD in the catalog opens it in Lera."],
              ["download", "https://github.com/theasciiverse/lera/releases/latest", "The release archives for every system, from the project's GitHub."]] },
  { id: "blightmud", kind: "client", title: "Blightmud", theme: "client", lang: "Rust", license: "GPL-3.0",
    version: "5.7.1", released: "May 2026", website: "https://github.com/Blightmud/Blightmud",
    description: "Terminal MUD client in Rust with Lua scripting and screen-reader support",
    platforms: { Linux: "yes (x86-64, ARM64)", macOS: "yes (Intel, Apple silicon)", Windows: null }, windowsNote: "runs under WSL",
    tls: "yes: <code>--connect host:port --tls</code>, certificate checked",
    packaged: "programs.html#blightmud",
    install: [["av", "av install blightmud", "The Asciiverse build: Linux x86-64 and ARM64, Intel and Apple silicon Macs."],
              [".deb", "https://github.com/theasciiverse/blightmud/releases/download/v5.7.1-av.1/blightmud-asciiverse_5.7.1-1_amd64.deb", "Debian 12, Ubuntu 22.04 and newer, from the Asciiverse release (arm64 too). No menu entry."],
              [".rpm", "https://github.com/theasciiverse/blightmud/releases/download/v5.7.1-av.1/blightmud-asciiverse-5.7.1-1.x86_64.rpm", "Fedora and openSUSE, from the Asciiverse release (aarch64 too)."],
              ["cargo", "cargo install --git https://github.com/blightmud/blightmud blightmud", "Needs Rust, and openssl and alsa development files to build."],
              ["Homebrew", "brew tap Blightmud/blightmud", "Apple silicon. Then install blightmud from the tap."],
              ["Debian/Ubuntu", "https://github.com/Blightmud/Blightmud/releases", "A .deb package on the releases page."]] },
  { id: "tintin", kind: "client", title: "TinTin++", theme: "client", lang: "C", license: "GPL-3.0-or-later",
    version: "2.02.61", released: "January 2026", website: "https://tintin.mudhalla.net",
    description: "Veteran console MUD client with its own scripting language, PCRE triggers and a mapper",
    platforms: { Linux: "yes (x86-64, ARM64)", macOS: "yes (Apple silicon; Intel not yet)", Windows: "yes (upstream's WinTin++ installer)" },
    tls: "yes: <code>#ssl &lt;name&gt; &lt;host&gt; &lt;port&gt;</code>, through GnuTLS. It pins certificates the way SSH does: the first connection saves the server's certificate, later ones warn if it changes or expires",
    packaged: "programs.html#tintin",
    install: [["av", "av install tintin", "The Asciiverse build, fully static: Linux x86-64 and ARM64, and Apple silicon Macs."],
              [".deb", "https://github.com/theasciiverse/tintin/releases/download/v2.02.61-av.1/tintin-asciiverse_2.02.61-1_amd64.deb", "Debian and Ubuntu, from the Asciiverse release (arm64 too). Installs tt++; no menu entry."],
              [".rpm", "https://github.com/theasciiverse/tintin/releases/download/v2.02.61-av.1/tintin-asciiverse-2.02.61-1.x86_64.rpm", "Fedora and openSUSE, from the Asciiverse release (aarch64 too)."],
              ["Debian/Ubuntu", "sudo apt install tintin++", "The distribution's own package, often an older version."],
              ["Windows", "https://tintin.mudhalla.net/download.php", "WinTin++ installer, bundles the Mintty terminal."],
              ["source", "https://tintin.mudhalla.net/download.php", "Source tarball for every other system."]] },
  { id: "durthang", kind: "client", title: "Durthang", theme: "client", lang: "Rust", license: "GPL-3.0",
    version: "0.2.0", released: "July 2026", website: "https://github.com/Pommersche92/durthang",
    description: "Young terminal MUD client in Rust and Ratatui, with passwords kept in the system keyring",
    platforms: { Linux: "yes (x86-64, ARM64)", macOS: "yes (Intel, Apple silicon)", Windows: "yes (x86-64, ARM64)" },
    tls: "yes: plain TCP or TLS with the system's root certificates",
    packaged: "programs.html#durthang",
    install: [["av", "av install durthang", "The Asciiverse build: Linux, macOS and Windows, x86-64 and ARM64, with saved passwords working on macOS and Windows too."],
              [".deb", "https://github.com/theasciiverse/durthang/releases/download/v0.2.0-av.1/durthang_0.2.0-1_amd64.deb", "Debian and Ubuntu, from the Asciiverse release (arm64 too). No menu entry: start it from a terminal or from av."],
              [".rpm", "https://github.com/theasciiverse/durthang/releases/download/v0.2.0-av.1/durthang-0.2.0-1.x86_64.rpm", "Fedora and openSUSE, from the Asciiverse release (aarch64 too)."],
              ["cargo", "cargo install durthang", "Upstream's own release, any system with Rust 1.85 or newer."]] },
  { id: "tinyfugue", kind: "client", title: "TinyFugue", theme: "client", lang: "C", license: "GPL-2.0-or-later",
    version: "5.0 beta 8", released: "a classic", website: "https://tinyfugue.sourceforge.net/",
    description: "The classic Unix MUD client, still packaged by Linux distributions as tf5",
    platforms: { Linux: "yes (x86-64, ARM64)", macOS: "yes (Apple silicon)", Windows: null }, windowsNote: "Unix only",
    tls: "not checked",
    packaged: "programs.html#tinyfugue",
    install: [["av", "av install tinyfugue", "The Asciiverse build with Debian's patches, fully static: Linux x86-64 and ARM64, and Apple silicon Macs."],
              [".deb", "https://github.com/theasciiverse/tinyfugue/releases/download/v5.0b8-av.1/tinyfugue-asciiverse_5.0b8-1_amd64.deb", "Debian and Ubuntu, from the Asciiverse release (arm64 too). Installs tf; no menu entry."],
              [".rpm", "https://github.com/theasciiverse/tinyfugue/releases/download/v5.0b8-av.1/tinyfugue-asciiverse-5.0b8-1.x86_64.rpm", "Fedora and openSUSE, from the Asciiverse release (aarch64 too)."],
              ["Debian/Ubuntu", "sudo apt install tf5", "Debian's own tf5 package."]] },
];

function clientDetail(c) {
  const plat = Object.entries(c.platforms).map(([os, v]) =>
    `<div class="plat-cell ${v ? "ok" : "no"}"><b>${os}</b><span>${v ? esc(v) : "not yet" + (c.windowsNote && os === "Windows" ? `, ${esc(c.windowsNote)}` : "")}</span></div>`).join("");
  const d = el(`<section class="lib-detail">
    <div class="client-hero"><span class="nm">${esc(c.title)}</span><span class="th">${esc(c.role || "MUD client")} · ${esc(c.lang)} · ${esc(c.license)}</span>
      <p>${esc(c.description)}</p></div>
    <div class="plat-row">${plat}</div>
    <div class="lib-bar"><div class="slot"></div>
      <dl>${c.version ? `<dt>Version</dt><dd>${esc(c.version)}</dd>` : ""}<dt>Released</dt><dd>${esc(c.released)}</dd></dl>
      <a class="store" href="${esc(c.website)}">Project ›</a></div>
    <h1>${esc(c.title)}</h1>
    ${c.packaged ? `<p class="one"><b>In the Asciiverse catalog:</b> ${c.ours ? "made" : "built and packaged"} by Asciiverse, installable with av. <a href="${c.packaged}">Its catalog page ›</a></p>` : ""}
    <p class="by">${c.ours ? "Made by Asciiverse, for every world on this page; av will launch the others too." : c.packaged ? "Not made by Asciiverse. Listed so you can pick the one you like; av will launch any of them." : "Not made by Asciiverse, and not in the Asciiverse catalog yet: install it as shown above."}</p>
  </section>`);
  d.querySelector(".slot").replaceWith(tabbedInstall(c.install));
  return d;
}

function clientCard(c) {
  const p = Object.entries(c.platforms).map(([os, v]) => `<span class="${v ? "" : "off"}">${{ Linux: "LNX", macOS: "MAC", Windows: "WIN" }[os]}</span>`).join(" ");
  return el(`<a class="cap mud-cap" href="#${c.id}">
    <div class="mud-face"><span class="th">${esc(c.lang)} · ${esc(c.license)}</span><span class="nm" style="font-size:22px">${esc(c.title)}</span><span class="th">${esc(c.version)}</span></div>
    <div class="cap-body"><h4>${esc(c.title)}</h4><p>${esc(c.description)}</p>
      <div class="cap-foot"><span class="genre">${esc(c.lang)}</span><span class="plat client-plat">${p}</span></div></div></a>`);
}

// Interpreters for text adventures: one program plays many story files.
// Facts from Debian 13 (packages, versions, copyright files) and each
// project's own pages, checked 2026-10-12. Only checked platforms are listed.
const IF_INTERPRETERS = [
  { id: "frotz", kind: "client", role: "Interpreter", title: "Frotz", old: true, theme: "client", lang: "C", license: "GPL-2.0-or-later",
    version: "2.55", released: "February 2025", website: "https://davidgriffith.gitlab.io/frotz/",
    description: "The standard player for Z-machine stories: Infocom's games, Zork among them, and most classic interactive fiction",
    platforms: { Linux: "yes (x86-64, ARM64)", macOS: "yes (Intel, Apple silicon)", Windows: null }, windowsNote: "curses is for Unix terminals",
    packaged: "programs.html#frotz",
    install: [["av", "av install frotz", "The Asciiverse build: static on Linux, system libraries only on macOS. Stories such as Zork already include it."],
              ["Debian/Ubuntu", "sudo apt install frotz", "Then: frotz <story file>"],
              ["source", "https://gitlab.com/DavidGriffith/frotz", "Source and other builds on the project's GitLab."]] },
  { id: "glulxe", kind: "client", role: "Interpreter", title: "Glulxe", theme: "client", lang: "C", license: "MIT",
    version: "0.6.1", released: "in Debian 13", website: "https://github.com/erkyrath/glulxe",
    description: "Andrew Plotkin's player for Glulx, the format most modern Inform 7 games use",
    platforms: { Linux: "yes (x86-64; ARM64 with the first release)", macOS: "with the first release (Intel, Apple silicon)", Windows: null }, windowsNote: "GlkTerm is a curses library for Unix terminals",
    packaged: "programs.html#glulxe",
    install: [["av", "av install glulxe", "The Asciiverse build with GlkTerm, for the terminal: static on Linux, system libraries only on macOS. Stories such as Counterfeit Monkey already include it."],
              ["Debian/Ubuntu", "sudo apt install glulxe", "Then: glulxe <story file>"],
              ["source", "https://github.com/erkyrath/glulxe", "Source on the project's GitHub."]] },
  { id: "frobtads", kind: "client", role: "Interpreter", title: "FrobTADS", theme: "client", lang: "C++", license: "TADS Freeware License",
    version: "2.0", released: "May 2021", website: "https://github.com/realnc/frobtads",
    description: "The terminal player for TADS 2 and TADS 3 games, with the TADS development tools",
    platforms: { Linux: "yes (x86-64; ARM64 with the first release)", macOS: "with the first release (Intel, Apple silicon)", Windows: null }, windowsNote: "its curses interface is for Unix terminals",
    packaged: "programs.html#frobtads",
    install: [["av", "av install frobtads", "The Asciiverse build of the player, frob: static on Linux, system libraries only on macOS. Stories such as I Am Prey already include it."],
              ["source", "https://github.com/realnc/frobtads", "Not in Debian 13; source on the project's GitHub."]] },
  { id: "scottfree", kind: "client", role: "Interpreter", title: "ScottFree", theme: "client", lang: "C", license: "GPL-2.0-or-later",
    version: "", released: "in Debian 13", website: "https://packages.debian.org/scottfree",
    description: "Plays Scott Adams' adventures from the late 1970s, Pirate Adventure among them",
    platforms: { Linux: "yes (Debian package scottfree)" },
    install: [["Debian/Ubuntu", "sudo apt install scottfree", "Then: scottfree <game file>"]] },
];

