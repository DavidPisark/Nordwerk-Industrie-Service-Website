# TASK-002: Nordwerk Industrie-Service – Release Candidate Termin 4 (AC-01 bis AC-08)

- **Task-ID:** `TASK-002`
- **Projekt-ID:** `client-01`
- **Ziel-Repository (`target_dir`):** `client-01-website`
- **Zieldatei für den Agentenlauf:** `index.html` (Stylesheet `styles.css` bleibt eingebunden)
- **Produktprüfung:** `python test_website.py` (Prüffamilien F1–F4, Exit-Code 0 = bestanden)
- **Eingabestand:** RC1 aus Termin 3 (N-01, N-02, N-03, N-08, N-09 vorhanden)
- **Verantwortlich (Human Gate):** siehe `organization/roles.yaml` der Factory

## Ziel
Die bestehende Startseite wird zum vollständigen Release Candidate ausgebaut. **Alle bestehenden Inhalte, das Kontaktziel und die Navigation bleiben erhalten.** Es wird ausschließlich `index.html` geändert.

## Pflichtinhalte (exakter Wortlaut aus dem Kundenbriefing v1.0)

| Kennung | Inhalt | Platzierung |
|---|---|---|
| N-01 | `Nordwerk Industrie-Service` | Header-Marke und einzige `<h1>` |
| N-02 | `Praktische Unterstützung für Ihren technischen Betrieb.` | Hero unter der `<h1>` |
| N-03 | Titel `Wartungsplanung`, Text `Wir strukturieren Wartungsaufgaben und dokumentieren Zuständigkeiten für kleine technische Betriebe.` | Leistungskarte 1 |
| N-04 | Titel `Ersatzteilkoordination`, Text `Wir unterstützen bei der Abstimmung von Ersatzteilbedarfen und Lieferterminen.` | Leistungskarte 2 |
| N-05 | Titel `Betriebsdokumentation`, Text `Wir bringen technische Unterlagen in eine nachvollziehbare und nutzbare Struktur.` | Leistungskarte 3 |
| N-06 | `Kleine Produktionsbetriebe` und `Technische Serviceunternehmen` | Abschnitt „Zielgruppen“ als Liste |
| N-07 | `Ein fester Ansprechpartner, ein gemeinsam vereinbarter Leistungsumfang und nachvollziehbare Ergebnisse.` | Abschnitt „Arbeitsweise“ |
| N-08 | Linktext `Anfrage stellen`, Ziel `mailto:kontakt@nordwerk.example` | Hero und Kontaktabschnitt |
| N-09 | `Fiktives Unternehmen – Lehrprojekt der HAW Hamburg. Keine realen Angebote oder Kontaktaufnahme.` | Footer |

## Akzeptanzkriterien für diesen Task

1. **AC-01:** N-01 und N-02 in der Startansicht (Hero).
2. **AC-02:** Abschnitt `<section id="leistungen">` mit `<h2>Leistungen</h2>` und drei Karten `<article class="service-card">`, je mit `<h3>`-Titel und Absatz (N-03, N-04, N-05).
3. **AC-03:** `<section id="zielgruppen">` (`<h2>Zielgruppen</h2>`, `<ul>` mit beiden Zielgruppen) und `<section id="arbeitsweise">` (`<h2>Arbeitsweise</h2>`, N-07). **Keine** erfundenen Leistungsversprechen, Zahlen, Logos, Zertifikate, Referenzen oder Reaktionszeiten.
4. **AC-04:** Mindestens ein Link `<a href="mailto:kontakt@nordwerk.example">Anfrage stellen</a>`; keine andere `mailto:`-Adresse. N-09 sichtbar im `<footer>`.
5. **AC-05:** `<nav>` enthält Links auf `#leistungen`, `#zielgruppen`, `#arbeitsweise` und `#kontakt`; jedes `href="#…"` hat ein passendes `id`. Kontaktabschnitt `<section id="kontakt">`. Nur lokale Assets (`styles.css`), keine `http(s)://`-Verweise, keine CDNs, keine Skripte, kein PHP.
6. **AC-06:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">` bleibt erhalten; keine festen Breiten im Markup (kein Inline-`style` mit `width`).
7. **AC-07:** `<html lang="de">`, aussagekräftiger `<title>`, genau eine `<h1>`, Überschriften ohne übersprungene Ebene (h1 → h2 → h3); Bilder (falls vorhanden) mit passendem `alt`.
8. **AC-08:** Seite startet ohne Factory mit `python -m http.server 8000`; `python test_website.py` endet mit Exit-Code 0.

## Technische Vorgaben für den Agenten
- Vorhandene CSS-Klassen wiederverwenden: `header-container`, `brand`, `hero`, `hero-claim`, `cta-button`, `services`, `service-card`, `contact`. Neue Abschnitte dürfen die Klasse `services` mitbenutzen.
- Keine Inline-Styles, kein JavaScript, keine externen Ressourcen.
- Vollständigen Inhalt von `index.html` zurückgeben (kein Diff-Fragment).

## Explizite Annahmen
- **A-01:** Eine einzelne Seite mit Sprungmarken genügt (Kundenbriefing).
- **A-02:** Kontakt nur per `mailto:`; kein Formular, kein CMS, kein PHP (siehe Sicherheitsbewertung zu CVE-2026-109618 / CVE-2026-109619).
- **A-03:** Fehlende Gestaltung neuer Abschnitte in `styles.css` wird bei Bedarf manuell ergänzt und als menschliche Arbeit in `costs/usage.csv` erfasst.
