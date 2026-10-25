# Nordwerk Industrie-Service – Kundenwebsite (Release-Kandidat 1)

Eigenständiges Kundenprodukt-Repository (`client-01-website`) für den fiktiven B2B-Kunden **Nordwerk Industrie-Service** im Rahmen des Lehrprojekts der HAW Hamburg (Termin 3).

## Produkt-Stack & Begründung
- **Technischer Stack:** Statisches, semantisches HTML5 (`index.html`) und modernes, responsives CSS3 (`styles.css`) ohne externe Frameworks, CDNs oder Tracker.
- **Lokale Qualitätsprüfung:** `test_website.py` prüft deterministisch alle Pflichtbausteine aus dem Kundenbriefing (`N-01`, `N-02`, `N-03`, `N-08`, `N-09`), semantische Tags, Tastaturfokus (`:focus-visible`) und die Abwesenheit erfundener Aussagen oder externer Abhängigkeiten.

## Lokal starten (statischer Webserver)

```bash
python -m http.server 8000
```

Anschließend im Browser öffnen: `http://localhost:8000`

## Automatisierte Produktprüfung ausführen

```bash
python test_website.py
```

Oder via `pytest`:

```bash
pytest -q test_website.py
```
