# Issue CR-01: Englische Landing-Page + Zielgruppen-Erweiterung

**Task-ID:** CR-01  
**Status:** Implemented  
**Datum:** 2026-11-08  
**Bearbeitet in:** `client-01-website/`

---

## Beschreibung

CR-01 erweitert das Nordwerk-Projekt um zwei Änderungen:

1. **Englische Landing-Page** (`index_en.html`): Eine vollständige englische Übersetzung der deutschen `index.html`, inklusive einer neuen Service-Karte „Project Coordination" und der neuen Zielgruppe „Technical procurement departments".
2. **Zielgruppen-Erweiterung in der deutschen View** (`index.html`): Hinzufügen von „Technische Einkaufsabteilungen" als dritte Zielgruppe sowie eines Sprachschalter-Links zur englischen Version in der Navigation.

---

## Impact-Analyse

### Geänderte Dateien

| Datei | Art der Änderung | Details |
|---|---|---|
| `index.html` | Modifiziert | +1 Zielgruppe (`Technische Einkaufsabteilungen`), +1 Nav-Link (`index_en.html`) |
| `index_en.html` | **Neu** | Vollständige englische Version der Landing-Page |
| `test_cr01.py` | **Neu** | Pytest-Testdatei für CR-01-Akzeptanzkriterien (EN-01..EN-09, DE-10, DE-11) |
| `issue_cr01.md` | **Neu** | Diese Dokumentationsdatei |

### Nicht geänderte Dateien

| Datei | Status |
|---|---|
| `styles.css` | Unverändert – von `index_en.html` mitgenutzt |
| `test_website.py` | Unverändert – Regressionstests bleiben bestehen |

---

## Akzeptanzkriterien

### AC-09 – Englische View (`index_en.html`)

| ID | Kriterium | Prüfung |
|---|---|---|
| EN-01 | `<html lang="en">` gesetzt | `html_lang == "en"` |
| EN-02 | Titel „Nordwerk Industrie-Service" vorhanden | `<title>` enthält den Firmennamen |
| EN-03 | Englischer Hero-Text vorhanden | Sichtbarer Text enthält „Practical support" |
| EN-04 | Service-Karte „Project Coordination" vorhanden | Sichtbarer Text enthält „Project Coordination" |
| EN-05 | Zielgruppe „Technical procurement departments" vorhanden | Sichtbarer Text enthält den Eintrag |
| EN-06 | `mailto:kontakt@nordwerk.example` mit Label „Send request" | Anchor mit href + Linktext |
| EN-07 | Link zur deutschen Version (`href="index.html"`) in Navigation | Anchor-Liste enthält `index.html` |
| EN-08 | `<meta name="viewport">` vorhanden | Parser erkennt Viewport-Meta |
| EN-09 | `styles.css` als Stylesheet eingebunden | `<link rel="stylesheet" href="styles.css">` |

### Deutsche View (`index.html`)

| ID | Kriterium | Prüfung |
|---|---|---|
| DE-10 | „Technische Einkaufsabteilungen" in `index.html` vorhanden | Sichtbarer Text enthält den Eintrag |
| DE-11 | Link zur englischen Version (`href="index_en.html"`) in `<nav>` | Nav-Anchor-Liste enthält `index_en.html` |

---

## Regressions-Hinweis

> [!IMPORTANT]
> `test_website.py` muss nach dieser Änderung **vollständig bestehen** (Exit-Code 0).  
> Die Prüffamilien F1–F4 (AC-01..AC-08) werden in `test_cr01.py` als `test_ac01_to_ac08_regression()` via `verify_website()` automatisch mitgeprüft.

Folgende Eigenschaften der deutschen View bleiben unverändert und werden durch den Regressionstest gesichert:

- Alle Pflichtinhalte N-01 bis N-09
- Kontakt-Link `mailto:kontakt@nordwerk.example` mit Label „Anfrage stellen"
- Navigation zu `#leistungen` und `#kontakt`
- Alle lokalen Verweise existieren (kein externer CDN, kein PHP)
- `lang="de"`, genau eine `<h1>`, Viewport-Meta, Fokus-CSS

---

## Testausführung

```bash
cd client-01-website

# Regressionstests (deutsch)
python test_website.py

# CR-01-spezifische Tests
python test_cr01.py

# Oder via pytest
python -m pytest -q test_website.py test_cr01.py
```
