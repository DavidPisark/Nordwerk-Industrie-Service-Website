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


---

## AC-01 bis AC-08 Prüfliste & Browser-Review (Stand Termin 4: `v0.2.0-rc1` / `R-BASE`, Commit `18d222b`)

| AC | Anforderung | Automatisierte Prüffamilie (`test_website.py`) | Browser-Review (`http://localhost:8000`) | Status |
|---|---|---|---|---|
| **AC-01** | Firmenname (`N-01`) & Hauptaussage (`N-02`) auf Startansicht | `F1 Pflichtinhalt` (`PASSED`) | Hero-Sektion sichtbar | **Bestanden** |
| **AC-02** | Alle 3 Leistungen (`N-03` Wartungsplanung, `N-04` Ersatzteilkoordination, `N-05` Betriebsdokumentation) | `F1 Pflichtinhalt` (`PASSED`) | 3 Karten unter `#leistungen` geprüft | **Bestanden** |
| **AC-03** | Zielgruppen (`N-06`) & Arbeitsweise (`N-07`), keine erfundenen Versprechen | `F1 Pflichtinhalt` (`PASSED`) | `#zielgruppen` & `#arbeitsweise` geprüft | **Bestanden** |
| **AC-04** | Kontaktlink `mailto:kontakt@nordwerk.example` (`Anfrage stellen`, `N-08`) & Übungshinweis (`N-09`) | `F1` + `F2 Kontakt & Navigation` (`PASSED`) | Klicktest erfolgreich | **Bestanden** |
| **AC-05** | Navigation zu `#leistungen`, `#zielgruppen`, `#arbeitsweise`, `#kontakt`; lokale Assets (`styles.css`) | `F2` + `F3 Lokale Verweise & Assets` (`PASSED`) | Sprungmarken & `:target` getestet | **Bestanden** |
| **AC-06** | Kein horizontaler Überlauf bei `375 px` und `1280 px` Breite (`scrollWidth <= clientWidth`) | `F4 Bedienbarkeit statisch` (Viewport-Meta) | Geprüft bei `375 px` & `1280 px` (Prüfer: David Pisarkiewicz, Lars Boos) | **Bestanden** |
| **AC-07** | Dokumenttitel, `lang="de"`, Überschriften (`h1 -> h2 -> h3`), sichtbarer Tastaturfokus (`:focus-visible`) | `F4 Bedienbarkeit statisch` (`PASSED`) | `Tab`-Navigation durch alle Links geprüft (Prüfer: Lars Boos) | **Bestanden** |
| **AC-08** | Eigenständiger Start & separate Produkttests ohne Factory/LLM/DB | `python test_website.py` (`Exit-Code 0`) | `python -m http.server 8000` aus frischem Checkout geprüft | **Bestanden** |
