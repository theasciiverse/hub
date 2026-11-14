#!/usr/bin/env python3
"""Make the built website readable for search engines and link previews.

Runs in the site workflow after build_catalog.py, on the assembled public/
folder. The site's pages are drawn by site.js from catalog.json, so their
HTML alone holds no game text; this writes it in:

- one page per title at public/t/<id>/index.html, made from title.html, with
  the title's text (description, store page, history, credits, platforms) in
  the HTML itself, a proper <title>, meta description, canonical link, Open
  Graph and Twitter card tags, and JSON-LD; site.js then draws the live page
  over it as before (it removes the static text in header())
- the same kind of text, a list of every title with a link to its page, in
  the home page and the category pages, plus their meta and link-preview tags
- sitemap.xml and robots.txt

Link previews use public/t/<id>/poster.png when tools/posters.sh made one,
else img/og.png.

  python3 tools/build_pages.py public
"""
import html
import json
import re
import sys
from pathlib import Path

SITE = "https://asciiverse.sh"
KIND_PAGE = {"game": "games.html", "adventure": "adventures.html", "mud": "muds.html",
             "program": "programs.html", "art": "art.html", "movie": "movies.html"}
KIND_NAME = {"game": "a terminal game", "adventure": "a text adventure", "mud": "a MUD",
             "program": "a terminal program", "art": "terminal art", "movie": "an ASCII movie"}
PAGES = {  # page: (kinds listed, <h1>, meta description)
    "index.html": (list(KIND_PAGE), "Asciiverse: a home for terminal games",
                   "Asciiverse is a free home for games and programs that live in the terminal: roguelikes, "
                   "text adventures, MUDs, arcade games, puzzles and demos, old and new, each with a preview "
                   "and installed with one command."),
    "games.html": (["game"], "Games on Asciiverse",
                   "Terminal games on Asciiverse: roguelikes, arcade games, puzzles, card and board games, "
                   "strategy and more, from 1970s classics to new releases, each with a preview you can watch."),
    "adventures.html": (["adventure"], "Text adventures on Asciiverse",
                        "Text adventures on Asciiverse: Zork, Colossal Cave and new interactive fiction, "
                        "played in your terminal with the interpreter built in."),
    "muds.html": (["mud"], "MUDs on Asciiverse",
                  "MUDs on Asciiverse: the multi-user dungeons still running online, some for decades, "
                  "ready to play from your terminal."),
    "programs.html": (["program"], "Programs on Asciiverse", "Terminal programs and toys on Asciiverse."),
    "art.html": (["art"], "Art and demos on Asciiverse",
                 "Art and demos on Asciiverse: screensavers, effects and demoscene in the terminal."),
    "movies.html": (["movie"], "Movies on Asciiverse", "ASCII movies and animations on Asciiverse."),
}
OTHER_PAGES = {
    "get-av.html": "Get av, the Asciiverse launcher: browse, install, update and play terminal games with one command on Linux, macOS and Windows.",
    "history.html": "A history of games in the terminal, from Colossal Cave and Rogue to today, with every era playable on Asciiverse.",
    "submit.html": "Submit your terminal game or program to the Asciiverse catalog.",
    "support.html": "Support Asciiverse and the people who make its games.",
}

e = html.escape


def inline(s):
    s = e(s, quote=True)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', s)
    return s


def render_page(md):
    """site.js renderPage: ## and ### headings, paragraphs, lists, bold, italic, code, links."""
    out, para, lst = [], [], None

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def flush_list():
        nonlocal lst
        if lst:
            out.append(f"<{lst[0]}>" + "".join("<li>" + inline(i) + "</li>" for i in lst[1]) + f"</{lst[0]}>")
            lst = None

    for raw in md.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush_para(); flush_list(); continue
        m = re.match(r"^(###?) (.*)$", line)
        if m:
            flush_para(); flush_list()
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            continue
        m = re.match(r"^\s*([-*]|\d+\.) (.*)$", line)
        if m:
            flush_para()
            tag = "ol" if m.group(1)[0].isdigit() else "ul"
            if not lst or lst[0] != tag:
                flush_list(); lst = (tag, [])
            lst[1].append(m.group(2))
        elif lst and re.match(r"^\s+\S", raw):
            lst[1][-1] += " " + line.strip()
        else:
            flush_list(); para.append(line.strip())
    flush_para(); flush_list()
    return "\n".join(out)


def os_names(t):
    p = " ".join((t.get("platforms") or {}).keys())
    return [n for k, n in (("linux", "Linux"), ("apple", "macOS"), ("windows", "Windows")) if k in p]


def head_tags(title, desc, url, image, extra=""):
    return (f'<title>{e(title)}</title>\n'
            f'<meta name="description" content="{e(desc)}">\n'
            f'<link rel="canonical" href="{e(url)}">\n'
            f'<meta property="og:site_name" content="Asciiverse">\n'
            f'<meta property="og:type" content="website">\n'
            f'<meta property="og:title" content="{e(title)}">\n'
            f'<meta property="og:description" content="{e(desc)}">\n'
            f'<meta property="og:url" content="{e(url)}">\n'
            f'<meta property="og:image" content="{e(image)}">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:title" content="{e(title)}">\n'
            f'<meta name="twitter:description" content="{e(desc)}">\n'
            f'<meta name="twitter:image" content="{e(image)}">\n' + extra)


def set_head(doc, tags):
    doc = re.sub(r"<title>.*?</title>\n?", "", doc, count=1, flags=re.S)
    return doc.replace('<meta charset="utf-8">\n', '<meta charset="utf-8">\n' + tags, 1)


def set_app(doc, static):
    return doc.replace('<main id="app"></main>', f'<main id="app"><div class="static">{static}</div></main>', 1)


def title_list(titles):
    items = "".join(f'<li><a href="/t/{e(t["id"])}/">{e(t["title"])}</a>: {e(t.get("description", ""))}</li>'
                    for t in sorted(titles, key=lambda t: t["title"].lower()))
    return f"<ul>{items}</ul>"


def title_page(t, template, image, collections):
    tid = t["id"]
    url = f"{SITE}/t/{tid}/"
    kind = t.get("kind", "game")
    name = f'{t["title"]}, {KIND_NAME.get(kind, "a terminal game")} | Asciiverse'
    desc = t.get("description", "")
    dev = t.get("developer") or {}
    oses = os_names(t)
    ld = {
        "@context": "https://schema.org",
        "@type": "VideoGame" if kind in ("game", "adventure", "mud") else "SoftwareApplication",
        "name": t["title"], "description": desc, "url": url, "image": image,
        "applicationCategory": "Game" if kind in ("game", "adventure", "mud") else "MultimediaApplication",
        "operatingSystem": ", ".join(oses) or "Linux",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    }
    if dev.get("name"):
        ld["author"] = {"@type": "Person" if " " in dev["name"] and "team" not in dev["name"].lower() else "Organization",
                        "name": dev["name"], **({"url": dev["url"]} if dev.get("url") else {})}
    if t.get("genre"):
        ld["genre"] = t["genre"]
    if t.get("year"):
        ld["dateCreated"] = str(t["year"])
    if t.get("license"):
        ld["license"] = t["license"]
    if t.get("repo"):
        ld["codeRepository"] = f'https://github.com/{t["repo"]}'
    jsonld = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"
    doc = set_head(template, '<base href="/">\n' + head_tags(name, desc, url, image, jsonld))
    doc = doc.replace("<body>", f'<body data-id="{e(tid)}">', 1)

    page = KIND_PAGE.get(kind, "games.html")
    parts = [f'<p class="crumbs"><a href="/">Asciiverse</a> › <a href="/{page}">{e(kind)}s</a>'
             + (f' › {e(t["genre"])}' if t.get("genre") else "") + f' › {e(t["title"])}</p>',
             f'<h1>{e(t["title"])}</h1>', f'<p class="one">{e(desc)}</p>',
             f'<p>Install and play it with av: <code>av install {e(tid)}</code></p>']
    if t.get("page"):
        parts.append(f'<article class="page">{render_page(t["page"])}</article>')
    if t.get("provenance"):
        parts.append(f'<h2>Where it comes from</h2><p>{e(t["provenance"])}</p>')
    facts = []
    if dev.get("name"):
        facts.append(f'<li>Developer: {e(dev["name"])}</li>')
    up = t.get("upstream") or {}
    if up.get("name"):
        facts.append(f'<li>Original: {e(up["name"])}</li>')
    if t.get("year"):
        facts.append(f'<li>First released: {e(str(t["year"]))}</li>')
    if t.get("genre"):
        facts.append(f'<li>Genre: {e(t["genre"])}</li>')
    if oses:
        facts.append(f'<li>Runs on: {e(", ".join(oses))}</li>')
    if t.get("license"):
        facts.append(f'<li>License: {e(t["license"])}</li>')
    if t.get("repo"):
        facts.append(f'<li>Source: <a href="https://github.com/{e(t["repo"])}">github.com/{e(t["repo"])}</a></li>')
    parts.append("<ul>" + "".join(facts) + "</ul>")
    coll = t.get("collection")
    if coll and coll in collections:
        parts.append(f'<p>Part of {e(collections[coll].get("name", coll))}.</p>')
    static = '<div class="wrap">' + "\n".join(parts) + "</div>"
    return set_app(doc, static)


def main(public):
    public = Path(public)
    cat = json.loads((public / "data" / "catalog.json").read_text())
    titles = list(cat["titles"].values()) if isinstance(cat["titles"], dict) else cat["titles"]
    collections = cat.get("collections", {})
    template = (public / "title.html").read_text()
    default_image = f"{SITE}/img/og.png"
    urls = []

    for t in titles:
        d = public / "t" / t["id"]
        d.mkdir(parents=True, exist_ok=True)
        image = f'{SITE}/t/{t["id"]}/poster.png' if (d / "poster.png").exists() else default_image
        (d / "index.html").write_text(title_page(t, template, image, collections))
        urls.append((f'{SITE}/t/{t["id"]}/', (t.get("updated_at") or t.get("added") or "")[:10]))

    for name, (kinds, h1, desc) in PAGES.items():
        p = public / name
        if not p.exists():
            continue
        doc = p.read_text()
        listed = [t for t in titles if t.get("kind") in kinds]
        url = f"{SITE}/" if name == "index.html" else f"{SITE}/{name}"
        doc = set_head(doc, head_tags(h1, desc, url, default_image))
        if name == "index.html":
            groups = "".join(f'<h2><a href="/{KIND_PAGE[k]}">{e(KIND_PAGE[k][:-5].capitalize())}</a></h2>'
                             + title_list([t for t in titles if t.get("kind") == k])
                             for k in KIND_PAGE if any(t.get("kind") == k for t in titles))
            body = f'<h1>{e(h1)}</h1><p>{e(desc)}</p>{groups}'
        else:
            body = f'<h1>{e(h1)}</h1><p>{e(desc)}</p>{title_list(listed)}'
        doc = set_app(doc, f'<div class="wrap">{body}</div>')
        p.write_text(doc)
        newest = max((t.get("updated_at") or t.get("added") or "" for t in listed), default="")[:10]
        urls.append((url, newest))

    for name, desc in OTHER_PAGES.items():
        p = public / name
        if not p.exists():
            continue
        h1 = re.search(r"<title>(.*?)</title>", p.read_text(), re.S)
        title = h1.group(1) if h1 else "Asciiverse"
        p.write_text(set_head(p.read_text(), head_tags(html.unescape(title), desc, f"{SITE}/{name}", default_image)))
        urls.append((f"{SITE}/{name}", ""))

    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, mod in urls:
        sm.append(f"<url><loc>{e(loc)}</loc>" + (f"<lastmod>{mod}</lastmod>" if mod else "") + "</url>")
    sm.append("</urlset>")
    (public / "sitemap.xml").write_text("\n".join(sm) + "\n")
    (public / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(titles)} title pages, {len(urls)} sitemap entries")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
