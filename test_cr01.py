"""
Automatisierte Prüfung für CR-01: Englische Landing-Page + Zielgruppen-Erweiterung.

AC-01..08 Regressionsschutz (deutsche View): via test_website.py verify_website()
AC-09: Englische View (index_en.html):
  - EN-01: lang="en" gesetzt
  - EN-02: Titel "Nordwerk Industrie-Service" vorhanden
  - EN-03: Englischer Hero-Text vorhanden ("Practical support")
  - EN-04: "Project Coordination" Karte vorhanden (R-01 Erweiterung auf Englisch)
  - EN-05: "Technical procurement departments" als Zielgruppe vorhanden
  - EN-06: mailto:kontakt@nordwerk.example mit Label "Send request"
  - EN-07: Link zur deutschen Version (href="index.html") vorhanden
  - EN-08: Viewport-Meta vorhanden
  - EN-09: styles.css eingebunden
  - DE-10: "Technische Einkaufsabteilungen" in deutscher index.html vorhanden
  - DE-11: Link zur englischen Version (href="index_en.html") in deutscher Nav vorhanden
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from test_website import verify_website

ROOT = Path(__file__).resolve().parent


class _PageParser(HTMLParser):
    """Collect visible text, links, ids, headings, images and asset references."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text_parts: list[str] = []
        self.ids: set[str] = set()
        self.anchors: list[dict] = []  # {"href", "text", "in_nav"}
        self.assets: list[tuple[str, str]] = []  # (tag, url)
        self.headings: list[int] = []
        self.images_without_alt: list[str] = []
        self.title = ""
        self.html_lang = ""
        self.has_viewport = False
        self._in_title = False
        self._nav_depth = 0
        self._skip_depth = 0
        self._open_anchor: dict | None = None

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "html":
            self.html_lang = a.get("lang", "")
        elif tag == "title":
            self._in_title = True
        elif tag in ("script", "style"):
            self._skip_depth += 1
        elif tag == "nav":
            self._nav_depth += 1
        elif tag == "meta" and a.get("name", "").lower() == "viewport":
            self.has_viewport = True
        elif re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        elif tag == "img":
            if "alt" not in a:
                self.images_without_alt.append(a.get("src", "?"))
        if tag == "a" and "href" in a:
            self._open_anchor = {"href": a["href"].strip(), "text": "", "in_nav": self._nav_depth > 0}
            self.anchors.append(self._open_anchor)
        for attr in ("href", "src"):
            if attr in a and tag != "a":
                self.assets.append((tag, a[attr].strip()))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("script", "style") and self._skip_depth:
            self._skip_depth -= 1
        elif tag == "nav" and self._nav_depth:
            self._nav_depth -= 1
        elif tag == "a":
            self._open_anchor = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._skip_depth:
            return
        self.text_parts.append(data)
        if self._open_anchor is not None:
            self._open_anchor["text"] += data

    @property
    def visible_text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.text_parts)).strip()


def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _load_en() -> tuple[str, _PageParser]:
    html = (ROOT / "index_en.html").read_text(encoding="utf-8")
    parser = _PageParser()
    parser.feed(html)
    return html, parser


# ---------------------------------------------------------------- AC-01..08 Regression
def test_ac01_to_ac08_regression():
    """Regressionsschutz: deutsche View muss weiterhin alle Prüffamilien bestehen."""
    results = verify_website(ROOT)
    all_errors: list[str] = []
    for family, errors in results.items():
        all_errors.extend(errors)
    assert not all_errors, "Regression in test_website.py:\n- " + "\n- ".join(all_errors)


# ---------------------------------------------------------------- AC-09 Englische View
def test_en01_lang_attribute():
    """EN-01: lang="en" gesetzt."""
    _, page = _load_en()
    assert page.html_lang.lower() == "en", f'EN-01: html lang erwartet "en", gefunden: {page.html_lang!r}'


def test_en02_title():
    """EN-02: Titel "Nordwerk Industrie-Service" vorhanden."""
    _, page = _load_en()
    assert "Nordwerk Industrie-Service" in page.title, (
        f'EN-02: Titel fehlt "Nordwerk Industrie-Service" (gefunden: {page.title!r})'
    )


def test_en03_hero_text():
    """EN-03: Englischer Hero-Text vorhanden ("Practical support")."""
    _, page = _load_en()
    assert "Practical support" in page.visible_text, (
        'EN-03: Hero-Text "Practical support" nicht gefunden'
    )


def test_en04_project_coordination():
    """EN-04: "Project Coordination" Karte vorhanden (R-01 Erweiterung auf Englisch)."""
    _, page = _load_en()
    assert "Project Coordination" in page.visible_text, (
        'EN-04: Service-Karte "Project Coordination" nicht gefunden'
    )


def test_en05_technical_procurement():
    """EN-05: "Technical procurement departments" als Zielgruppe vorhanden."""
    _, page = _load_en()
    assert "Technical procurement departments" in page.visible_text, (
        'EN-05: Zielgruppe "Technical procurement departments" nicht gefunden'
    )


def test_en06_mailto_send_request():
    """EN-06: mailto:kontakt@nordwerk.example mit Label "Send request"."""
    _, page = _load_en()
    mailto = "mailto:kontakt@nordwerk.example"
    matching = [a for a in page.anchors if a["href"] == mailto and "Send request" in _norm(a["text"])]
    assert matching, (
        f'EN-06: Kein Link "Send request" mit Ziel {mailto} gefunden'
    )


def test_en07_link_to_german():
    """EN-07: Link zur deutschen Version (href="index.html") vorhanden."""
    _, page = _load_en()
    hrefs = [a["href"] for a in page.anchors]
    assert "index.html" in hrefs, 'EN-07: Link href="index.html" zur deutschen Version fehlt'


def test_en08_viewport_meta():
    """EN-08: Viewport-Meta vorhanden."""
    _, page = _load_en()
    assert page.has_viewport, 'EN-08: <meta name="viewport"> fehlt in index_en.html'


def test_en09_styles_css():
    """EN-09: styles.css eingebunden."""
    _, page = _load_en()
    css_links = [url for tag, url in page.assets if tag == "link" and "styles.css" in url]
    assert css_links, 'EN-09: styles.css nicht als Stylesheet eingebunden'


def test_de10_technische_einkaufsabteilungen():
    """DE-10: "Technische Einkaufsabteilungen" in deutscher index.html vorhanden."""
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = _PageParser()
    parser.feed(html)
    assert "Technische Einkaufsabteilungen" in parser.visible_text, (
        'DE-10: "Technische Einkaufsabteilungen" in index.html nicht gefunden'
    )


def test_de11_link_to_english():
    """DE-11: Link zur englischen Version (href="index_en.html") in deutscher Nav vorhanden."""
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = _PageParser()
    parser.feed(html)
    nav_hrefs = [a["href"] for a in parser.anchors if a["in_nav"]]
    assert "index_en.html" in nav_hrefs, (
        'DE-11: Link href="index_en.html" in <nav> der deutschen index.html fehlt'
    )


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    tests = [
        ("AC-01..08 Regression",               test_ac01_to_ac08_regression),
        ("EN-01 lang=en",                       test_en01_lang_attribute),
        ("EN-02 Title",                         test_en02_title),
        ("EN-03 Hero text",                     test_en03_hero_text),
        ("EN-04 Project Coordination",          test_en04_project_coordination),
        ("EN-05 Technical procurement dept.",   test_en05_technical_procurement),
        ("EN-06 mailto + Send request",         test_en06_mailto_send_request),
        ("EN-07 Link to German version",        test_en07_link_to_german),
        ("EN-08 Viewport meta",                 test_en08_viewport_meta),
        ("EN-09 styles.css linked",             test_en09_styles_css),
        ("DE-10 Technische Einkaufsabt.",       test_de10_technische_einkaufsabteilungen),
        ("DE-11 Link to English version",       test_de11_link_to_english),
    ]

    failed = False
    for label, fn in tests:
        try:
            fn()
            print(f"PASSED       {label}")
        except AssertionError as exc:
            print(f"FAILED       {label}")
            print(f"             {exc}")
            failed = True

    print("ERGEBNIS: " + ("FEHLGESCHLAGEN" if failed else "ALLE CR-01-PRÜFUNGEN BESTANDEN"))
    sys.exit(1 if failed else 0)
