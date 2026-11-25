"""Render the two language editions. Run with python3 site_source/build.py."""

from datetime import date
from html import escape
from pathlib import Path
import posixpath

from content import OPERATOR_ADDRESS, OPERATOR_EMAIL, OPERATOR_NAME, PAGES


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("en", "de")
ROUTES = {
    "home": "index.html",
    "about": "about.html",
    "events": "events.html",
    "resources": "resources.html",
    "get-involved": "get-involved.html",
    "imprint": "imprint.html",
    "privacy": "privacy.html",
}

UI = {
    "en": {
        "home": "Home", "about": "About us", "events": "Events", "resources": "Resources",
        "get-involved": "Get involved", "menu": "Menu", "skip": "Skip to content",
        "nav": "Main navigation", "language": "Language", "footer": "Footer navigation",
        "headline": ("Safer AI,", "on the Weser"),
        "intro": "We bring people in Bremen together to understand the risks of advanced AI and explore ways to make it safer.",
        "founding_update": "We started Safe AI Bremen in October 2026 and are planning our first event. Stay tuned!",
        "events_cta": "Explore events", "about_cta": "About the group",
        "alt": "Navy and amber illustration of Bremen’s old town and boats on the Weser beneath a low sun.",
        "start": "Find your starting point",
        "cards": [
            ("about", "people", "Our community", "Meet the ideas and questions that bring our local AI safety community together.", "About SAIBR"),
            ("events", "calendar", "Talks & meetups", "Find local announcements and online talks you can join from Bremen.", "Browse events"),
            ("resources", "book", "Learning resources", "Get to grips with AI safety through introductory readings, research and a map of the field.", "Explore resources"),
        ],
        "calendar": "On the calendar", "calendar_cta": "All events", "host": "Online talks hosted by Safe AI Germany.",
        "footer_line": "A local community exploring the safety of advanced AI.",
        "city": "Bremen, Germany", "imprint": "Imprint", "privacy": "Privacy", "national_events": "Full Safe AI Germany calendar",
        "network": "Safe AI Germany", "browse": "Explore", "deeper": "Further reading",
        "intro_link": "Why AI safety matters", "map_link": "AI safety concept map",
    },
    "de": {
        "home": "Startseite", "about": "Über uns", "events": "Veranstaltungen", "resources": "Materialien",
        "get-involved": "Mitmachen", "menu": "Menü", "skip": "Zum Inhalt",
        "nav": "Hauptnavigation", "language": "Sprache", "footer": "Navigation im Fußbereich",
        "headline": ("Sichere KI,", "an der Weser"),
        "intro": "Wir bringen Menschen in Bremen zusammen, die die Risiken fortgeschrittener KI verstehen und KI sicherer machen wollen.",
        "founding_update": "Wir haben Safe AI Bremen im Oktober 2026 gegründet und planen gerade unsere erste Veranstaltung. Bald gibt es mehr dazu!",
        "events_cta": "Zu den Veranstaltungen", "about_cta": "Über die Gruppe",
        "alt": "Die Bremer Altstadt und Boote auf der Weser unter einer tief stehenden Sonne, illustriert in Marineblau und Orange.",
        "start": "Finde deinen Einstieg",
        "cards": [
            ("about", "people", "Unsere Gruppe", "Entdecke die Ideen und Fragen, die uns in Bremen zum Thema KI-Sicherheit zusammenbringen.", "Über SAIBR"),
            ("events", "calendar", "Vorträge & Treffen", "Hier findest du lokale Ankündigungen und Online-Vorträge, an denen du aus Bremen teilnehmen kannst.", "Zu den Terminen"),
            ("resources", "book", "Lesen & lernen", "Verschaffe dir mit einführenden Texten, Forschungsberichten und einer Themenkarte einen Überblick.", "Materialien entdecken"),
        ],
        "calendar": "Im Kalender", "calendar_cta": "Alle Veranstaltungen", "host": "Online-Vorträge von Safe AI Germany.",
        "footer_line": "Eine Bremer Gruppe für alle, die sich mit KI-Sicherheit beschäftigen möchten.",
        "city": "Bremen, Deutschland", "imprint": "Impressum", "privacy": "Datenschutz", "national_events": "Alle Termine von Safe AI Germany",
        "network": "Safe AI Germany", "browse": "Entdecken", "deeper": "Zum Weiterlesen",
        "intro_link": "Warum KI-Sicherheit wichtig ist", "map_link": "Begriffe der KI-Sicherheit",
    },
}

# Line icons share a 24-unit grid and take their colour from the surrounding text.
ICONS = {
    "people": '<circle cx="9" cy="8" r="3"/><path d="M2.5 20v-2.4c0-3.3 2.8-5.1 6.5-5.1s6.5 1.8 6.5 5.1V20M16 5.1a3 3 0 0 1 0 5.8m2 2c2.2.7 3.5 2.3 3.5 4.7V20"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7.5 3v4.5M16.5 3v4.5M3 10h18m-13 4h2m4 0h2m-8 3.5h2"/>',
    "book": '<path d="M12 6.2C9.1 4.3 5.8 4 2.5 4.8v14.3c3.3-.8 6.6-.5 9.5 1.4 2.9-1.9 6.2-2.2 9.5-1.4V4.8C18.2 4 14.9 4.3 12 6.2zm0 0v14.3"/>',
    "pin": '<path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 1 1 14 0Z"/><circle cx="12" cy="10" r="2.4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "close": '<path d="m5 5 14 14M19 5 5 19"/>',
    "message": '<path d="M21 13.5a3 3 0 0 1-3 3h-8l-6 4v-4.5a3 3 0 0 1-1-2.2v-7a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3z"/><path d="M7 8.5h10m-10 4h6"/>',
}


def icon(name):
    return (f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


def filepath(lang, page):
    return ("de/" if lang == "de" else "") + ROUTES[page]


def href(lang, page, to_lang=None):
    if page not in ROUTES:
        return escape(page, quote=True)
    return posixpath.relpath(filepath(to_lang or lang, page), "de" if lang == "de" else ".")


def assets(lang):
    return ("../" if lang == "de" else "") + "assets/"


def nav_link(lang, current, page, classes=""):
    active = ' aria-current="page"' if page == current else ""
    return f'<a class="{classes}" href="{href(lang, page)}"{active}>{UI[lang][page]}</a>'


def header(lang, current):
    ui, base = UI[lang], assets(lang)
    nav = "".join(nav_link(lang, current, page) for page in ("about", "events", "resources"))
    join = nav_link(lang, current, "get-involved", "button button-navy header-cta")
    language_links = []
    for code in LANGUAGES:
        label = "English" if code == "en" else "Deutsch"
        active = ' aria-current="true"' if code == lang else ""
        language_links.append(f'<a href="{href(lang, current, code)}" lang="{code}" hreflang="{code}" '
                              f'aria-label="{label}"{active}>{code.upper()}</a>')
    return f"""
    <a class="skip" href="#main">{ui['skip']}</a>
    <header class="masthead" id="top"><div class="wrap header-row">
      <a class="brand" href="{href(lang, 'home')}" aria-label="Safe AI Bremen · {ui['home']}">
        <img src="{base}logo-header.svg" width="291" height="103" alt="Safe AI Bremen">
      </a>
      <nav class="main-nav" aria-label="{ui['nav']}">{nav}</nav>
      <div class="header-actions">
        <nav class="languages" aria-label="{ui['language']}">{icon('globe')}{'<span aria-hidden="true">/</span>'.join(language_links)}</nav>
        {join}
        <details class="mobile-menu">
          <summary aria-label="{ui['menu']}"><span class="open-icon">{icon('menu')}</span><span class="close-icon">{icon('close')}</span></summary>
          <nav aria-label="{ui['nav']}">{nav}{join}</nav>
        </details>
      </div>
    </div></header>"""


def footer(lang, current):
    ui = UI[lang]
    national = "https://safeaigermany.org/" + ("de/" if lang == "de" else "")
    links = "".join(nav_link(lang, current, key) for key in ("about", "events", "resources", "get-involved"))
    return f"""
    <footer class="footer"><div class="wrap">
      <div class="footer-main"><div class="footer-brand">
        <a href="{href(lang, 'home')}" aria-label="Safe AI Bremen · {ui['home']}"><img src="{assets(lang)}logo-footer.svg" alt="Safe AI Bremen" width="291" height="103"></a>
        <p>{ui['footer_line']}</p></div>
        <nav aria-label="{ui['footer']}"><h2>{ui['browse']}</h2>{links}</nav>
        <div class="footer-links"><h2>{ui['deeper']}</h2>
          <a href="{national}why-ai-safety/">{ui['intro_link']}</a>
          <a href="{national}concept-map/">{ui['map_link']}</a>
          <a href="{national}">{ui['network']}</a></div>
      </div>
      <div class="footer-base"><span>© Safe AI Bremen</span>
        <div class="footer-legal">{nav_link(lang, current, 'imprint')}{nav_link(lang, current, 'privacy')}</div>
        <span class="city">{icon('pin')} {ui['city']}</span></div>
    </div></footer>"""


def event_list(lang, items, compact=False):
    rows = []
    for event in items:
        start = date.fromisoformat(event["date"])
        months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        if lang == "de":
            months = ("Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez")
        details = "" if compact else f'<p>{escape(event["text"])}</p>'
        rows.append(f"""
          <li><article class="event-row">
            <time class="date-tile" datetime="{event['date']}"><span>{months[start.month-1]}</span><strong>{start.day}</strong></time>
            <div class="event-copy"><p class="meta">{escape(event['meta'])}</p>
              <h3><a href="{href(lang, event['href'])}">{escape(event['title'])}</a></h3>{details}</div>
          </article></li>""")
    return '<ul class="event-list">' + "".join(rows) + "</ul>"


def homepage(lang):
    ui, base = UI[lang], assets(lang)
    cards = []
    for page, symbol, title, text, link in ui["cards"]:
        cards.append(f"""
          <article class="feature-card"><div class="icon-tile">{icon(symbol)}</div>
            <h3>{escape(title)}</h3><p>{escape(text)}</p>
            <a class="text-link stretched" href="{href(lang, page)}">{escape(link)}</a>
          </article>""")
    events = PAGES[lang]["events"]["sections"][1]["items"]
    return f"""
    <main id="main">
      <section class="hero wrap" aria-labelledby="hero-title">
        <div class="hero-copy">
          <h1 id="hero-title">{ui['headline'][0]}<br>{ui['headline'][1]}<span class="amber-dot">.</span></h1>
          <p class="hero-intro">{ui['intro']}</p>
          <p class="hero-intro">{ui['founding_update']}</p>
          <div class="hero-actions">
            <a class="button button-amber" href="{href(lang, 'events')}">{icon('calendar')}{ui['events_cta']}</a>
            <a class="button button-outline" href="{href(lang, 'about')}">{ui['about_cta']}</a>
          </div>
        </div>
        <figure class="city-print">
          <img src="{base}bremen-weser.webp" srcset="{base}bremen-weser-small.webp 660w, {base}bremen-weser.webp 1200w"
               sizes="(max-width: 820px) 100vw, 48vw" alt="{ui['alt']}" width="1200" height="800" fetchpriority="high">
        </figure>
      </section>
      <section class="explore-section" aria-labelledby="explore-title"><div class="wrap">
        <h2 id="explore-title">{ui['start']}</h2>
        <div class="feature-grid">{''.join(cards)}</div>
      </div></section>
      <section class="calendar-section wrap" aria-labelledby="calendar-title">
        <div><h2 id="calendar-title">{ui['calendar']}</h2>
          <p>{ui['host']}</p>
          <a class="text-link" href="{href(lang, 'events')}">{ui['calendar_cta']}</a></div>
        {event_list(lang, events, compact=True)}
      </section>
    </main>"""


def article_items(lang, section):
    rows = []
    for item in section["items"]:
        meta = f'<p class="meta">{escape(item["meta"])}</p>' if "meta" in item else ""
        text = f'<p>{escape(item["text"])}</p>' if "text" in item else ""
        link = ""
        if "href" in item:
            link = f'<a class="text-link" href="{href(lang, item["href"])}">{escape(item["link"])}</a>'
        rows.append(f'<article class="article-item">{meta}<h3>{escape(item["title"])}</h3>'
                    f'{text}{link}</article>')
    return '<div class="article-items">' + "".join(rows) + "</div>"


def inside(lang, page):
    ui, data = UI[lang], PAGES[lang][page]
    sections = []
    for section in data["sections"]:
        paragraphs = [section["text"]] if "text" in section else section.get("paragraphs", [])
        body = "".join(f'<p class="section-prose">{escape(p)}</p>' for p in paragraphs)
        if section.get("operator_address"):
            street_address = "<br>".join(escape(line) for line in OPERATOR_ADDRESS)
            body += (f'<address class="operator-address"><strong>{escape(OPERATOR_NAME)}</strong><br>'
                     f'{street_address}<br><a href="mailto:{escape(OPERATOR_EMAIL)}">'
                     f'{escape(OPERATOR_EMAIL)}</a></address>')
        if "links" in section:
            links = [f'<li><a class="text-link" href="{href(lang, url)}">{escape(label)}</a></li>'
                     for label, url in section["links"]]
            body += '<ul class="source-links">' + "".join(links) + '</ul>'
        if "items" in section:
            if page == "events":
                body += event_list(lang, section["items"])
                national = "https://safeaigermany.org/" + ("de/" if lang == "de" else "") + "events/"
                body += f'<a class="text-link extra-link" href="{national}">{ui["national_events"]}</a>'
            else:
                body += article_items(lang, section)
        sections.append(f'<section class="editorial-row"><h2>{escape(section["title"])}</h2><div>{body}</div></section>')
    artwork = ""
    if page == "about":
        artwork = f'<div class="brand-plate"><img src="{assets(lang)}logo-primary.svg" alt="Safe AI Bremen" width="628" height="343"></div>'
    elif page in ("events", "resources", "get-involved"):
        symbol = {"events": "calendar", "resources": "book", "get-involved": "message"}[page]
        artwork = f'<div class="topic-plate" aria-hidden="true">{icon(symbol)}</div>'
    return f"""
    <main id="main" class="inner-page">
      <header class="inner-hero wrap"><div>
        <h1>{escape(data['title'])}<span class="amber-dot">.</span></h1>
        <p class="inner-intro">{escape(data['intro'])}</p></div>{artwork}</header>
      <div class="editorial wrap">{''.join(sections)}</div>
    </main>"""


def render(lang, page):
    ui, base = UI[lang], assets(lang)
    home = page == "home"
    title = "Safe AI Bremen | SAIBR" if home else f"{ui[page]} | Safe AI Bremen"
    description = ui["intro"] if home else PAGES[lang][page]["intro"]
    alternates = "\n".join(f'<link rel="alternate" hreflang="{code}" href="{href(lang, page, code)}">' for code in LANGUAGES)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#faf9f5">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  {alternates}
  <link rel="icon" href="{base}favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{base}site.css">
  <script src="{base}navigation.js" defer></script>
</head>
<body>{header(lang, page)}{homepage(lang) if home else inside(lang, page)}{footer(lang, page)}
</body>
</html>
"""


if __name__ == "__main__":
    for language in LANGUAGES:
        for name in ROUTES:
            destination = ROOT / filepath(language, name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(render(language, name), encoding="utf-8")
