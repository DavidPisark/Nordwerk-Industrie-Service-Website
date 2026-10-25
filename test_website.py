"""
Automated Product Verification for Nordwerk Industrie-Service (Release Candidate 1 / Session 3).
Checks exact customer briefing text blocks (N-01, N-02, N-03, N-08, N-09), semantic HTML5 structure,
accessibility attributes, and strict absence of external trackers or invented claims.
"""

from pathlib import Path
import sys


REQUIRED_SNIPPETS = {
    "N-01 (Brand Name)": "Nordwerk Industrie-Service",
    "N-02 (Hero Claim)": "Praktische Unterstützung für Ihren technischen Betrieb.",
    "N-03 (Service 1 Text)": (
        "Wartungsplanung: Wir strukturieren Wartungsaufgaben und dokumentieren "
        "Zuständigkeiten für kleine technische Betriebe."
    ),
    "N-08 (CTA Label)": "Anfrage stellen",
    "N-08 (Mailto Link)": "mailto:kontakt@nordwerk.example",
    "N-09 (Course Notice)": (
        "Fiktives Unternehmen – Lehrprojekt der HAW Hamburg. "
        "Keine realen Angebote oder Kontaktaufnahme."
    ),
}

FORBIDDEN_PATTERNS = [
    "https://",
    "http://",
    "google-analytics",
    "gtag(",
    "ISO 9001",
    "TÜV",
    "24/7 Notdienst",
]


def verify_website(base_dir: Path | None = None) -> list[str]:
    root = base_dir or Path(__file__).resolve().parent
    errors: list[str] = []

    index_path = root / "index.html"
    css_path = root / "styles.css"

    if not index_path.is_file():
        return ["index.html is missing"]
    if not css_path.is_file():
        errors.append("styles.css is missing")

    html = index_path.read_text(encoding="utf-8")

    if 'lang="de"' not in html and "lang='de'" not in html:
        errors.append("Missing lang='de' attribute on <html>")

    for tag in ("<header", "<main", "<footer", "<h1", "<nav"):
        if tag not in html:
            errors.append(f"Missing semantic HTML element: {tag}")

    for key, text in REQUIRED_SNIPPETS.items():
        if text not in html:
            errors.append(f"Missing required customer content {key}: {text!r}")

    for forbidden in FORBIDDEN_PATTERNS:
        if forbidden.lower() in html.lower():
            errors.append(f"Forbidden external dependency or unverified claim found: {forbidden!r}")

    if css_path.is_file():
        css = css_path.read_text(encoding="utf-8")
        if ":focus-visible" not in css:
            errors.append("Missing keyboard focus styling (:focus-visible) in styles.css")

    return errors


def test_nordwerk_rc1_website():
    errors = verify_website()
    assert not errors, "Website validation failed:\n- " + "\n- ".join(errors)


if __name__ == "__main__":
    found_errors = verify_website()
    if found_errors:
        print("FAILED Nordwerk RC1 verification:", file=sys.stderr)
        for err in found_errors:
            print(f" - {err}", file=sys.stderr)
        sys.exit(1)
    print("PASSED: All Nordwerk RC1 checks (N-01, N-02, N-03, N-08, N-09, HTML5, CSS focus, zero external dependencies).")
    sys.exit(0)
