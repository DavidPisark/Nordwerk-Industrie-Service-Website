# Release-, Abnahme- & Übergabeprotokoll – Termin 5 (`CR-01-v1.0` / `v0.3.0`)

**Produkt:** Nordwerk Industrie-Service Website (`client-01-website`)  
**Kunde:** Nordwerk Industrie-Service (Hamburg)  
**Team:** PepeGroup (Team 3: David Pisarkiewicz, Maxim Bers, Lars Boos, Mehrose Farooq)  
**Datum:** 2026-11-09  
**Release-Tags im Produkt-Repository:** `CR-01-v1.0` & `v0.3.0` (Vorversionen: `v0.2.0-rc1` / `R-BASE` = `18d222b`, `v0.1.0-t3` = `3e6121b`)

---

## 1. Gelieferte Kundenänderung `CR-01` & Regressionsnachweis (`A1`–`A3`, `B1`–`B3`)

Ausgehend vom Termin-4-Stand (`7805e3b` / `v0.2.0-rc1`) wurde `CR-01` gemäß [`issue_cr01.md`](issue_cr01.md) in zwei echten Factory-Läufen umgesetzt:
- **Factory-Lauf A (`index_en.html`):** Commit `5227307` (Trace `52b69365-3d49-4bcd-9c4d-f51ab8c136e7.jsonl`, `43,53 s`, `8,6905` Credits, Freigabe: **Mehrose Farooq**).
- **Factory-Lauf B (`index.html`):** Commit `263d007` (Trace `c0ee2cc3-4031-4ce9-8188-d37da99a1583.jsonl`, `42,45 s`, `8,7329` Credits, Freigabe: **Mehrose Farooq**).
- **Review-Diff gegenüber T4-Release-Candidate (`18d222b`):**
  ```bash
  git diff 18d222b..HEAD -- index.html index_en.html
  ```
- **Automatisierte Regression & CR-01-Prüfung (`Exit-Code 0`):**
  ```bash
  python test_website.py   # F1, F2, F3, F4 -> ALLE PRUEFFAMILIEN BESTANDEN
  python test_cr01.py      # F1-F4 + CR-01 EN + CR-01 DE -> BESTANDEN (0 Regressionen)
  ```
- **Manuelles Browser- & Tastatur-Review (`375 px` / `1280 px` für `index.html` & `index_en.html`):**
  Durchgeführt und bestanden am `2026-11-09` durch **Lars Boos** und **David Pisarkiewicz** (kein horizontaler Überlauf bei `375 px` und `1280 px`, `:focus-visible`-Rahmen an allen Links, funktionierender Sprachwechsel `Deutsch` $\leftrightarrow$ `English` und `mailto:kontakt@nordwerk.example`).

---

## 2. Sicherheitsantwort `SR-01` & Komponentenübersicht (`B4`, `B5`, `D1`)

Die vollständige Kundenantwort zur Sicherheitsanfrage `SR-01` (`CVE-2026-109618` & `CVE-2026-109619`, ENISA-Mitteilung vom `21.10.2026`) inklusive Komponentenübersicht (Altsystem `PHP 8.2` + CMS vs. statische Lieferung vs. Build/Test) liegt direkt in diesem Repository unter:
- **[`SR-01-response.md`](SR-01-response.md)** *(geprüft und freigegeben durch David Pisarkiewicz & Lars Boos am `2026-11-09`)*.

---

## 3. Technische Freigabe vs. Kundenabnahme (`AC-01` bis `AC-10`, `B6`, `D1`)

- **Technische Freigabe (PepeGroup):** ✅ **Technisch freigegeben** (`2026-11-09`, 0 bekannte technische Restmängel).
- **Kundenabnahme (Dozent / Nordwerk):** ⬜ **Ausstehend (offene Kundenentscheidung im Termin 5)** – keine Selbstbehauptung *„vom Kunden akzeptiert“*.

| AC | Kriterium | Technischer Prüfstatus | Kundenabnahme |
| :--- | :--- | :--- | :--- |
| **AC-01..AC-04** | Pflichtinhalte `N-01`–`N-09`, Kontakt `mailto:kontakt@nordwerk.example`, Kurshinweis | ✅ `PASSED` (`F1`, `F2`) | ⬜ Ausstehend |
| **AC-05..AC-08** | Navigation, lokale Assets, PHP-Freiheit, 375/1280 px, Tastaturfokus, unabhängiger Start/Test | ✅ `PASSED` (`F2`–`F4` + Browser-Review) | ⬜ Ausstehend |
| **AC-09 (`CR-01`)** | Englische Ansicht (`index_en.html`), Zielgruppe *Technische Einkaufsabteilungen* in DE, Sprachwechsel | ✅ `PASSED` (`test_cr01.py` + Browser-Review) | ⬜ Ausstehend |
| **AC-10 (`SR-01`)** | Abgegrenzte Sicherheitsantwort, Komponentenübersicht, Start-/Test- & Wartungshinweis | ✅ `PASSED` ([`SR-01-response.md`](SR-01-response.md)) | ⬜ Ausstehend |

---

## 4. Eigenständige Start-, Test- und Wartungsanleitung (`B6`)

1. **Lokaler Start ohne Factory:**
   ```bash
   python -m http.server 8000
   # Deutsch:  http://localhost:8000/index.html
   # Englisch: http://localhost:8000/index_en.html
   ```
2. **Tests ausführen:**
   ```bash
   python test_website.py
   python test_cr01.py
   ```
3. **Wartungshinweis:**
   - Auslieferung erfordert nur einen statischen Webserver für `index.html`, `index_en.html` und `styles.css`.
   - Beim Hoster muss PHP im Auslieferungsverzeichnis deaktiviert und das Altsystem (CMS/Formular) abgeschaltet werden (siehe [`SR-01-response.md`](SR-01-response.md)).
   - Nach jeder künftigen Textänderung an `index.html` oder `index_en.html` sind vor Veröffentlichung `python test_website.py` und `python test_cr01.py` auszuführen.
