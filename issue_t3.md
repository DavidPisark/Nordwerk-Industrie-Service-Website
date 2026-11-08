# TASK-001: Nordwerk Industrie-Service – Statische B2B-Website (Release-Kandidat 1)

- **Task-ID:** `TASK-001`
- **Projekt-ID:** `client-01`
- **Ziel-Repository (`target_dir`):** `client-01-website`
- **Zieldatei:** `index.html` (mit Stylesheet `styles.css`)
- **Zugewiesene Rollen:** `product_owner`, `project_manager`, `software_architect`, `backend_api_engineer`, `qa_test_engineer`, `ai_safety_security_engineer`, `integration_engineer`

## Scope für Termin 3 (Release-Kandidat 1)
Erstellung eines lauffähigen ersten Release-Kandidaten (RC1) der statischen Unternehmenswebsite für **Nordwerk Industrie-Service** in `index.html`:

1. **AC-01 (Start & Semantische Struktur):**
   - Lokal per `python -m http.server 8000` auslieferbar.
   - Semantisches HTML5 mit `<header>`, `<nav>`, `<main>`, `<h1>`, `<section>` und `<footer>`, `lang="de"`, `<meta charset="UTF-8">`, `<link rel="stylesheet" href="styles.css">`.
2. **AC-02 (Verbindliche Textbausteine im exakten Wortlaut für Termin 3):**
   - **`N-01` (Markenname):** `Nordwerk Industrie-Service`
   - **`N-02` (Hero-Claim):** `Praktische Unterstützung für Ihren technischen Betrieb.`
   - **`N-03` (Leistungsbereich 1):** `Wartungsplanung: Wir strukturieren Wartungsaufgaben und dokumentieren Zuständigkeiten für kleine technische Betriebe.`
3. **AC-03 (Kontakt für RC1):**
   - **`N-08` (Primärer Call-to-Action):** Link mit dem exakten Text `Anfrage stellen` und dem Linkziel `href="mailto:kontakt@nordwerk.example"`.
4. **AC-04 (Pflicht-Hinweis im Footer):**
   - **`N-09` (Rechtlicher & Projekt-Hinweis):** `Fiktives Unternehmen – Lehrprojekt der HAW Hamburg. Keine realen Angebote oder Kontaktaufnahme.`
5. **AC-05 (Keine erfundenen Inhalte / Keine externen Abhängigkeiten):**
   - Keine externen Links (`http://` oder `https://`), keine CDN-Skripte/Fonts, keine Tracker (`google-analytics`, `gtag(`), keine erfundenen Zertifikate (`ISO 9001`, `TÜV`) oder Versprechen (`24/7 Notdienst`).

## Explizite Annahmen (Clarifications)
- **A-01:** Für RC1 in Termin 3 wird der Call-to-Action über den im Briefing freigegebenen `mailto:kontakt@nordwerk.example`-Link abgebildet (kein Backend-Mailversand).
- **A-02:** Weitere Leistungsbereiche (`N-04`, `N-05`), der Arbeitsablauf (`N-06`) und die Zielgruppen (`N-07`) sind als Ausbaustufe für Termin 4 vorgesehen.
