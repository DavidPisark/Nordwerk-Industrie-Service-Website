# R-01: Isolierte Referenzaufgabe (Termin 4 Baseline / Termin 5 Vergleich)

- **Task-ID:** `R-01`
- **Projekt-ID:** `client-01`
- **Ziel-Repository (`target_dir`):** `client-01-website` (auf eigenem Branch `experiment/r-01-baseline` ab Basis-Commit `R-BASE`)
- **Zieldatei:** `index.html`
- **Prüfskript:** `test_r01.py`

## Verbindliche Aufgabenstellung (Aufgabenblatt Termin 4, Abschnitt 4)
> Ergänze unter den Leistungen die Karte **„Projektkoordination“** mit dem Text **„Wir koordinieren klar abgegrenzte technische Vorhaben mit Ihrem Team.“** Alle bisherigen Inhalte, Kontaktziele und Navigation müssen erhalten bleiben.

## Akzeptanzkriterien für R-01
1. **Neue Leistungskarte vorhanden:**
   - Innerhalb von `<section class="services" id="leistungen">` wird eine weitere Karte (`<article class="service-card">`) mit Überschrift `<h3>Projektkoordination</h3>` und Text `<p>Wir koordinieren klar abgegrenzte technische Vorhaben mit Ihrem Team.</p>` ergänzt.
2. **Keine Regressionen (AC-01 bis AC-08 bleiben vollständig erhalten):**
   - Alle bisherigen Pflichtbausteine (`N-01` bis `N-09`), alle drei bisherigen Leistungen (`Wartungsplanung`, `Ersatzteilkoordination`, `Betriebsdokumentation`), beide Zielgruppen (`N-06`), die Arbeitsweise (`N-07`), das Kontaktziel `mailto:kontakt@nordwerk.example` (`Anfrage stellen`) sowie alle Navigationslinks (`#leistungen`, `#zielgruppen`, `#arbeitsweise`, `#kontakt`) bleiben unverändert erhalten.
   - `python test_r01.py` (und `python test_website.py`) enden mit Exit-Code `0`.
