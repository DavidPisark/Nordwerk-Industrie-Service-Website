# Nordwerk Industrie-Service – Kundenwebsite (`client-01-website`)

Eigenständiges Kundenprodukt-Repository (`client-01-website`) für den fiktiven B2B-Kunden **Nordwerk Industrie-Service** (Hamburg) im Rahmen des Lehrprojekts der HAW Hamburg (Termine 3–5, aktuelles Release: **`CR-01-v1.0`** / **`v0.3.0`**).

## Gelieferte Artefakte in diesem Produkt-Repository (Termin 5)
- **[`index.html`](index.html):** Deutsche Hauptansicht (`N-01` bis `N-09`, erweitert in `CR-01` um die Zielgruppe *„Technische Einkaufsabteilungen“* und den Sprachwechsel-Link `English`).
- **[`index_en.html`](index_en.html):** Englische Einstiegsseite gemäß `CR-01` (*Nordwerk Industrie-Service*, *Practical support for your technical operations.*, *Maintenance planning*, *Spare parts coordination*, *Operational documentation*, *Technical purchasing departments*, *Request information* $\rightarrow$ `mailto:kontakt@nordwerk.example`, englischer Kurshinweis & Rücklink `Deutsch`).
- **[`styles.css`](styles.css):** Gemeinsames responsives Stylesheet für `375 px` und `1280 px` inkl. sichtbarem `:focus-visible`-Tastaturfokus (ohne externe Fonts/CDNs).
- **[`issue_cr01.md`](issue_cr01.md) & [`test_cr01.py`](test_cr01.py) (`test_cr01_en.py`):** Änderungs-Issue mit Auswirkungsanalyse sowie automatisiertes Prüfskript für `CR-01` + Regressionsprüfung `F1`–`F4`.
- **[`test_website.py`](test_website.py):** Deterministische Basis-Produktprüfung in vier Prüffamilien (`F1` Pflichtinhalt, `F2` Kontakt & Navigation, `F3` Lokale Verweise & PHP-Freiheit, `F4` Statische Bedienbarkeit).
- **[`SR-01-response.md`](SR-01-response.md):** Kundenantwort zur Sicherheitsanfrage `SR-01` (`CVE-2026-109618` / `CVE-2026-109619`, ENISA-Mitteilung vom `21.10.2026`) inkl. Komponentenübersicht (Altsystem `PHP 8.2`/CMS vs. statisches Produkt vs. Build/Test).
- **[`HANDOVER.md`](HANDOVER.md):** Release-, Abnahme- und Übergabeprotokoll (`AC-01` bis `AC-10`, Wartungshinweise, Trennung von technischer Freigabe und ausstehender Kundenabnahme).

---

## Eigenständiger Start ohne Factory (`AC-08` / `B6`)

Aus einem frischen Checkout dieses Produkt-Repositorys (ohne Factory, ohne LLM und ohne Datenbank):

```bash
python -m http.server 8000
```

Anschließend im Browser öffnen:
- **Deutsche Ansicht:** `http://localhost:8000/index.html`
- **Englische Ansicht (`CR-01`):** `http://localhost:8000/index_en.html`

## Automatisierte Produkt- und Regressionsprüfung ohne Factory ausführen (`AC-08` / `A3` / `B6`)

```bash
python test_website.py     # Prüffamilien F1–F4 (AC-01 bis AC-08)
python test_cr01.py        # F1–F4 Regression + CR-01 EN + CR-01 DE
python -m pytest -q test_website.py test_cr01.py
```

---

## AC-01 bis AC-10 Prüfliste & Abnahmestatus (Stand Termin 5: Release `CR-01-v1.0` / `v0.3.0`)

- **Technische Freigabe (Team 3):** ✅ **Technisch freigegeben** (`Mehrose Farooq`, `David Pisarkiewicz`, `Lars Boos`, `2026-11-09`)
- **Kundenabnahme (Dozent / Nordwerk):** ⬜ **Ausstehend** (Entscheidung im Termin 5; keine Selbstbehauptung *„vom Kunden akzeptiert“*)

| AC | Anforderung | Automatisierte Prüfung | Browser-Review (`375 px` & `1280 px`, Tastatur) | Technischer Status |
|---|---|---|---|---|
| **AC-01** | Firmenname (`N-01`) & Hauptaussage (`N-02`) auf Startansicht | `F1 Pflichtinhalt` (`PASSED`) | Hero-Sektion sichtbar | **Bestanden** |
| **AC-02** | Alle 3 Leistungen (`N-03` Wartungsplanung, `N-04` Ersatzteilkoordination, `N-05` Betriebsdokumentation) | `F1 Pflichtinhalt` (`PASSED`) | 3 Karten unter `#leistungen` geprüft | **Bestanden** |
| **AC-03** | Zielgruppen (`N-06`) & Arbeitsweise (`N-07`), keine erfundenen Versprechen | `F1 Pflichtinhalt` (`PASSED`) | `#zielgruppen` & `#arbeitsweise` geprüft | **Bestanden** |
| **AC-04** | Kontaktlink `mailto:kontakt@nordwerk.example` (`Anfrage stellen`, `N-08`) & Übungshinweis (`N-09`) | `F1` + `F2 Kontakt & Navigation` (`PASSED`) | Klicktest erfolgreich | **Bestanden** |
| **AC-05** | Navigation zu `#leistungen`, `#zielgruppen`, `#arbeitsweise`, `#kontakt`; lokale Assets (`styles.css`) | `F2` + `F3 Lokale Verweise & Assets` (`PASSED`) | Sprungmarken & `:target` getestet | **Bestanden** |
| **AC-06** | Kein horizontaler Überlauf bei `375 px` und `1280 px` Breite (`scrollWidth <= clientWidth`) in DE & EN | `F4` + `test_cr01.py` (Viewport-Meta) | Geprüft bei `375 px` & `1280 px` für `index.html` & `index_en.html` | **Bestanden** |
| **AC-07** | Dokumenttitel, `lang="de"` / `lang="en"`, Überschriften (`h1 -> h2 -> h3`), sichtbarer Tastaturfokus (`:focus-visible`) | `F4` + `test_cr01.py` (`PASSED`) | `Tab`-Navigation & Sprachwechsel per Tastatur in DE & EN geprüft | **Bestanden** |
| **AC-08** | Eigenständiger Start & separate Produkttests ohne Factory/LLM/DB | `test_website.py` & `test_cr01.py` (`Exit-Code 0`) | `python -m http.server 8000` aus frischem Checkout geprüft | **Bestanden** |
| **AC-09** | **`CR-01`:** Englische Ansicht (`index_en.html`) mit Pflichttexten + *„Technische Einkaufsabteilungen“* in DE + Sprachwechsel | `CR-01 EN` & `CR-01 DE` in `test_cr01.py` (`PASSED`) | Beide Sprachansichten & Links bei 375/1280 px geprüft | **Bestanden** |
| **AC-10** | **`SR-01` & Übergabe:** Sicherheitsantwort (`CVE-2026-109618`/`109619`), Komponentenübersicht & Wartungshinweis | `F3` (PHP-Freiheit) + [`SR-01-response.md`](SR-01-response.md) | Menschliche Faktenprüfung (David Pisarkiewicz & Lars Boos) | **Bestanden** |
