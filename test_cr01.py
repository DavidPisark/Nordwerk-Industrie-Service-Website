"""
Automatisierte Prüfung für die Kundenänderung CR-01 (Termin 5).

Prüft:
  1. Regression: alle Prüffamilien F1–F4 aus test_website.py für index.html (AC-01..AC-08).
  2. CR-01 EN: englische Ansicht index_en.html mit den verbindlichen Inhalten aus dem
     Aufgabenblatt Termin 5 (Titel, Hauptaussage, drei Leistungen, Zielgruppe, Kontakt, Hinweis),
     Sprachkennzeichnung lang="en", Dokumenttitel, Viewport, Sprachwechsel und lokale Verweise.
  3. CR-01 DE: deutsche Ansicht index.html mit zusätzlicher Zielgruppe
     „Technische Einkaufsabteilungen“ und Sprachwechsel zur englischen Ansicht.

Aufruf:  python test_cr01.py          (alle Familien)
         python test_cr01.py --en     (nur Regression + EN, für den ersten Teillauf)
"""

from __future__ import annotations

import sys
from pathlib import Path

from test_website import _PageParser, _is_external, _load, _norm, verify_website

EN_FILE = "index_en.html"
EN_TITLE = "Nordwerk Industrie-Service"
EN_REQUIRED_TEXT = [
    "Nordwerk Industrie-Service",
    "Practical support for your technical operations.",
    "Maintenance planning",
    "Spare parts coordination",
    "Operational documentation",
    "Technical purchasing departments",
    "Request information",
    "Fictional company – HAW Hamburg course project. No real offers or contact.",
]
CONTACT_HREF = "mailto:kontakt@nordwerk.example"
DE_AUDIENCE = "Technische Einkaufsabteilungen"


def _load_en(root: Path) -> _PageParser | None:
    path = root / EN_FILE
    if not path.is_file():
        return None
    parser = _PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def check_en(root: Path) -> list[str]:
    errors: list[str] = []
    page = _load_en(root)
    if page is None:
        return [f"[CR-01 EN] {EN_FILE} fehlt"]
    visible = page.visible_text
    for text in EN_REQUIRED_TEXT:
        if _norm(text) not in visible:
            errors.append(f"[CR-01 EN] Pflichttext fehlt: {text!r}")
    if _norm(page.title) != EN_TITLE:
        errors.append(f"[CR-01 EN] <title> ist {page.title!r}, erwartet {EN_TITLE!r}")
    if not page.html_lang.lower().startswith("en"):
        errors.append(f"[CR-01 EN] <html lang> ist {page.html_lang!r}, erwartet 'en'")
    if not page.has_viewport:
        errors.append("[CR-01 EN] Viewport-Meta fehlt")
    contact = [a for a in page.anchors if a["href"] == CONTACT_HREF]
    if not contact:
        errors.append(f"[CR-01 EN] Kontaktlink {CONTACT_HREF} fehlt")
    elif not any("Request information" in _norm(a["text"]) for a in contact):
        errors.append("[CR-01 EN] Kontaktlink trägt nicht den Text 'Request information'")
    if not any(a["href"] in ("index.html", "./index.html") for a in page.anchors):
        errors.append("[CR-01 EN] Sprachwechsel-Link zur deutschen Ansicht (index.html) fehlt")
    for a in page.anchors:
        href = a["href"]
        if href == "#" or (href.startswith("#") and href[1:] not in page.ids):
            errors.append(f"[CR-01 EN] Interner Link {href!r} hat kein Ziel (id fehlt)")
        if _is_external(href):
            errors.append(f"[CR-01 EN] Externe Abhängigkeit nicht erlaubt: {href!r}")
    for tag, url in page.assets:
        if not url or _is_external(url) or url.startswith(("#", "data:")):
            continue
        if not (root / url.split("#")[0].split("?")[0]).exists():
            errors.append(f"[CR-01 EN] lokaler Verweis zeigt ins Leere: <{tag}> {url}")
    return errors


def check_de(root: Path) -> list[str]:
    errors: list[str] = []
    if not (root / "index.html").is_file():
        return ["[CR-01 DE] index.html fehlt"]
    _, page = _load(root)
    if _norm(DE_AUDIENCE) not in page.visible_text:
        errors.append(f"[CR-01 DE] Zielgruppe fehlt: {DE_AUDIENCE!r}")
    if not any(a["href"] in (EN_FILE, "./" + EN_FILE) for a in page.anchors):
        errors.append(f"[CR-01 DE] Sprachwechsel-Link zur englischen Ansicht ({EN_FILE}) fehlt")
    return errors


def verify_cr01(base_dir: Path | None = None, include_de: bool = True) -> dict[str, list[str]]:
    root = (base_dir or Path(__file__).resolve().parent).resolve()
    results = verify_website(root)
    results["CR-01 EN Englische Ansicht"] = check_en(root)
    if include_de:
        results["CR-01 DE Zielgruppe & Sprachwechsel"] = check_de(root)
    return results


def test_cr01_en_and_no_regressions():
    results = verify_cr01(include_de=False)
    errors = [e for errs in results.values() for e in errs]
    assert not errors, "CR-01 EN fehlgeschlagen:\n- " + "\n- ".join(errors)


def test_cr01_de():
    errors = check_de(Path(__file__).resolve().parent)
    assert not errors, "CR-01 DE fehlgeschlagen:\n- " + "\n- ".join(errors)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    res = verify_cr01(include_de="--en" not in sys.argv)
    failed = False
    for family, errs in res.items():
        status = "PASSED" if not errs else f"FAILED ({len(errs)})"
        print(f"{status:<12} {family}")
        for err in errs:
            print(f"             - {err}")
        failed = failed or bool(errs)
    print("ERGEBNIS CR-01: " + ("FEHLGESCHLAGEN" if failed else "BESTANDEN (0 Regressionen)"))
    sys.exit(1 if failed else 0)
