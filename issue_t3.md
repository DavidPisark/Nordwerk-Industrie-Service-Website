# TASK-001: Nordwerk Industrie-Service – Statische B2B-Website (Release-Kandidat 1)

- **Task-ID:** `TASK-001`
- **Projekt-ID:** `client-01`
- **Ziel-Repository (`target_dir`):** `client-01-website`
- **Zugewiesene Rollen:** `product_owner`, `project_manager`, `software_architect`, `backend_api_engineer`, `qa_test_engineer`, `ai_safety_security_engineer`, `integration_engineer`

## Scope für Termin 3 (Release-Kandidat 1)
Erstellung eines lauffähigen ersten Release-Kandidaten (RC1) der statischen Unternehmenswebsite für **Nordwerk Industrie-Service**:
1. **AC-01 (Start & Struktur):** Lokal per `python -m http.server 8000` auslieferbar, semantisches HTML5 (`header`, `nav`, `main`, `section`, `footer`), Deutsch (`lang="de"`), UTF-8, responsives Layout (375 px bis 1280 px) und sichtbare `:focus-visible`-Markierung.
2. **AC-02 (Teilmenge Termin 3):** Exakte Einbindung von `N-01` (`Nordwerk Industrie-Service`), `N-02` (`Praktische Unterstützung für Ihren technischen Betrieb.`) sowie mindestens eines Leistungsbereichs (`N-03` Wartungsplanung). Weitere Leistungsbereiche (`N-04`, `N-05`, `N-06`, `N-07`) folgen in Termin 4/5.
3. **AC-03 (Kontakt für RC1):** Primärer Call-to-Action `N-08` (`Anfrage stellen`) als `mailto:kontakt@nordwerk.example`.
4. **AC-04 (Pflicht-Hinweis):** Sichtbarer Hinweis `N-09` (`Fiktives Unternehmen – Lehrprojekt der HAW Hamburg. Keine realen Angebote oder Kontaktaufnahme.`).
5. **AC-05 (Keine erfundenen Inhalte):** Verzicht auf unbestätigte Zertifikate, Kennzahlen, Kundenlogos oder externe Tracker/CDNs.

## Explizite Annahmen (Clarifications)
- **A-01:** Für RC1 in Termin 3 wird der Call-to-Action über den im Briefing freigegebenen `mailto:kontakt@nordwerk.example`-Link abgebildet (kein Backend-Mailversand).
- **A-02:** Leistungsbereiche `N-04` (Technische Dokumentation) und `N-05` (Ersatzteil- & Arbeitsvorbereitung) sowie der Arbeitsablauf (`N-06`) sind als Ausbaustufe für Termin 4 vorgesehen.
