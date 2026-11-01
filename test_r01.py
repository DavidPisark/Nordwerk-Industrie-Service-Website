"""
Automatisierte Prüfung für die isolierte Referenzaufgabe R-01 (Termin 4 Baseline / Termin 5 Vergleich).

Prüft:
  1. Alle regulären Prüffamilien F1–F4 aus test_website.py (keine Regressionen an N-01..N-09, Kontakt, Navigation, Assets, Bedienbarkeit).
  2. Zusätzlich die in R-01 geforderte Leistungskarte:
     - Titel: "Projektkoordination"
     - Text:  "Wir koordinieren klar abgegrenzte technische Vorhaben mit Ihrem Team."
"""

from __future__ import annotations

import sys
from pathlib import Path

from test_website import _load, _norm, verify_website

R01_TITLE = "Projektkoordination"
R01_TEXT = "Wir koordinieren klar abgegrenzte technische Vorhaben mit Ihrem Team."


def verify_r01(base_dir: Path | None = None) -> dict[str, list[str]]:
    root = (base_dir or Path(__file__).resolve().parent).resolve()
    results = verify_website(root)
    r01_errors: list[str] = []
    if not (root / "index.html").is_file():
        r01_errors.append("[R-01] index.html fehlt")
    else:
        _, page = _load(root)
        visible = page.visible_text
        if _norm(R01_TITLE) not in visible:
            r01_errors.append(f"[R-01] Leistungstitel fehlt: {R01_TITLE!r}")
        if _norm(R01_TEXT) not in visible:
            r01_errors.append(f"[R-01] Leistungstext fehlt: {R01_TEXT!r}")
    results["R-01 Zusatzleistung Projektkoordination"] = r01_errors
    return results


def test_r01_card_and_no_regressions():
    results = verify_r01()
    all_errors = [err for errs in results.values() for err in errs]
    assert not all_errors, "R-01 Prüfung fehlgeschlagen:\n- " + "\n- ".join(all_errors)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    res = verify_r01()
    failed = False
    for family, errs in res.items():
        status = "PASSED" if not errs else f"FAILED ({len(errs)})"
        print(f"{status:<12} {family}")
        for err in errs:
            print(f"             - {err}")
        failed = failed or bool(errs)
    print("ERGEBNIS R-01: " + ("FEHLGESCHLAGEN" if failed else "BESTANDEN (0 Regressionen)"))
    sys.exit(1 if failed else 0)
