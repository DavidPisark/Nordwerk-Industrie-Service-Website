"""
Teilprüfung CR-01 für den ersten Factory-Lauf (Zieldatei index_en.html):
Regression F1–F4 für index.html + englische Ansicht. Die deutschen Ergänzungen
prüft danach test_cr01.py (zweiter Lauf, Zieldatei index.html).
"""

from __future__ import annotations

import sys

from test_cr01 import verify_cr01


def test_cr01_en_only_and_no_regressions():
    results = verify_cr01(include_de=False)
    errors = [e for errs in results.values() for e in errs]
    assert not errors, "CR-01 EN fehlgeschlagen:\n- " + "\n- ".join(errors)


if __name__ == "__main__":
    sys.argv.append("--en")
    import runpy

    runpy.run_module("test_cr01", run_name="__main__")
