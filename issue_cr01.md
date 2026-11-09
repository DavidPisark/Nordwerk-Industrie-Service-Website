# CR-01: Englische Einstiegsseite und zusätzliche Zielgruppe (Termin 5)

- **Task-ID:** `CR-01`
- **Projekt-ID:** `client-01`
- **Ziel-Repository (`target_dir`):** Produkt-Checkout auf Branch `cr-01-factory`, Basis `7805e3b` (= Release Candidate `v0.2.0-rc1` / `18d222b` + README-Doku)
- **Zieldateien:** `index_en.html` (Lauf 1, neue englische Ansicht), `index.html` (Lauf 2, deutsche Ergänzungen)
- **Prüfskripte:** `test_cr01_en.py` (Lauf 1), `test_cr01.py` (Lauf 2 und Endabnahme), `test_website.py` (Regression AC-01..AC-08)

## Kundenwunsch (Aufgabenblatt Termin 5, Abschnitt 1)
> Wir möchten internationale Anfragen ermöglichen und künftig auch technische Einkaufsabteilungen ansprechen. Bitte ergänzen Sie eine kurze englische Einstiegsseite bzw. klar bezeichnete englische Ansicht. Die bisherige deutsche Website soll erhalten bleiben.

## Auswirkungsanalyse
- **Neu:** `index_en.html` als eigene englische Ansicht. Sie nutzt dieselbe `styles.css` und dieselbe Seitenstruktur wie `index.html` (Header mit Navigation, Hero, Leistungen, Zielgruppen, Kontakt, Footer).
- **Geändert:** `index.html` bekommt eine dritte Zielgruppe und einen Sprachwechsel-Link. Sonst bleibt alles unverändert.
- **Unverändert:** `styles.css` und alle Bilder/Assets. Kein JavaScript, kein PHP, kein Formular, keine externen Dienste.
- **Risiko:** Eine Regression in der deutschen Ansicht. `test_website.py` (F1–F4) läuft deshalb in beiden Läufen mit.

## Verbindliche Inhalte der englischen Ansicht `index_en.html` (wörtlich übernehmen)
| Element | Inhalt |
|---|---|
| Dokumenttitel `<title>` und Hauptüberschrift `<h1>` | **Nordwerk Industrie-Service** |
| Hauptaussage | **Practical support for your technical operations.** |
| Leistungen (drei Karten, je `<h3>`) | **Maintenance planning**, **Spare parts coordination**, **Operational documentation** |
| Zusätzliche Zielgruppe | **Technical purchasing departments** |
| Kontakt | Link mit Text **Request information** auf `mailto:kontakt@nordwerk.example` |
| Hinweis (sichtbar, z. B. im Footer) | **Fictional company – HAW Hamburg course project. No real offers or contact.** |

Weitere Anforderungen:
- `<html lang="en">`, `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">`, `<link rel="stylesheet" href="styles.css">`.
- Sprachwechsel: In der Navigation ein Link `<a href="index.html" hreflang="de" lang="de">Deutsch</a>`.
- Ein kurzer englischer Einstieg reicht, keine vollständige Übersetzung. **Keine** Zahlen, Preise, Fristen oder Leistungsversprechen ergänzen.
- Überschriften-Hierarchie ohne Sprünge (h1 → h2 → h3). Alle Links per Tastatur erreichbar.

## Verbindliche Ergänzungen der deutschen Ansicht `index.html`
- In der bestehenden Zielgruppen-Liste einen weiteren Eintrag **Technische Einkaufsabteilungen** ergänzen.
- In der Navigation einen Sprachwechsel-Link `<a href="index_en.html" hreflang="en" lang="en">English</a>` ergänzen.
- Alles andere bleibt Zeichen für Zeichen erhalten (AC-01..AC-08, N-01..N-09, Kontakt `Anfrage stellen`, alle Navigationsziele).

## Akzeptanzkriterien
1. `python test_cr01_en.py` endet nach Lauf 1 mit Exit-Code 0.
2. `python test_cr01.py` und `python test_website.py` enden nach Lauf 2 mit Exit-Code 0 (0 Regressionen).
3. Browser-Review bei 375 px und 1280 px sowie per Tastatur (Tab-Reihenfolge, sichtbarer Fokus) für beide Ansichten durch einen Menschen. Das ist nicht automatisiert.
