# Nordwerk Industrie-Service – Kundenwebsite (`client-01-website`)

Eigenständiges Kundenprodukt-Repository (`client-01-website`) für den fiktiven B2B-Kunden **Nordwerk Industrie-Service** (Hamburg) im Rahmen des Lehrprojekts der HAW Hamburg (Termine 3–5).

## Produkt-Stack & Architektur
- **Technischer Stack:** Statisches, semantisches HTML5 (`index.html`) und modernes, responsives CSS3 (`styles.css`) ohne externe Frameworks, CDNs, Tracker oder serverseitige Skripte (kein PHP – schließt `CVE-2026-109618` & `CVE-2026-109619` architektonisch aus).
- **Automatisierte Produktprüfung (`test_website.py`):** Prüft deterministisch in vier Prüffamilien (`F1`–`F4`):
  - **F1 Pflichtinhalt (`AC-01`–`AC-04`):** Alle Pflichtbausteine `N-01` bis `N-09` aus dem Kundenbriefing v1.0 vorhanden; keine erfundenen Leistungsversprechen, Zertifikate oder Tracker.
  - **F2 Kontakt & Navigation (`AC-04`, `AC-05`):** Kontaktlink `mailto:kontakt@nordwerk.example` mit Beschriftung `Anfrage stellen`, Navigation (`<nav>`) zu `#leistungen` und `#kontakt`, alle internen `#`-Sprungziele existieren im DOM.
  - **F3 Lokale Verweise & Assets / PHP-Freiheit (`AC-05`, `AC-08`):** Alle lokalen Assets (`styles.css`) existieren im Checkout, keine externen `http(s)://`-Abhängigkeiten, keine `.php`-Dateien oder Server-Tags.
  - **F4 Bedienbarkeit statisch (`AC-06`, `AC-07`):** `<title>`, `<html lang="de">`, `<meta name="viewport">`, genau eine `<h1>`, keine übersprungenen Überschriftenebenen (`h1 -> h2 -> h3`), `alt`-Attribute bei Bildern, sichtbarer Tastaturfokus (`:focus-visible`).

## Eigenständiger Start ohne Factory (`AC-08`)

Aus einem frischen Checkout dieses Produkt-Repositorys (ohne laufende Factory, ohne LLM und ohne Datenbank):

```bash
python -m http.server 8000
```

Anschließend im Browser öffnen: `http://localhost:8000`

## Automatisierte Produktprüfung ohne Factory ausführen (`AC-08` / `B6`)

```bash
python test_website.py
```

Oder via `pytest`:

```bash
python -m pytest -q test_website.py
```

## Isolierte Referenzaufgabe `R-01` prüfen (Termin 4 Baseline / Termin 5 Vergleich)

Auf dem separaten Experiment-Branch (`experiment/r-01-baseline` ab Tag `R-BASE`):

```bash
python test_r01.py
```
