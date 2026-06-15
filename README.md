# 📰 The Daily Ledger

> *Truth, Clearly Delivered.*

**Live site:** [unclejim7.github.io/The-Daily-Ledger](https://unclejim7.github.io/The-Daily-Ledger)

-----

## What Is This?

The Daily Ledger is a fully custom, AI-generated HTML newspaper published daily via GitHub Pages. Each edition is a richly formatted dark-mode broadsheet covering markets, the Federal Reserve, Bitcoin & crypto, geopolitics, real estate, Armstrong Economics, Chicagoland weather, Chicago sports, and health & wellness — curated and written fresh every day.

Every edition is generated on demand using a single command typed into Claude:

```
run tdl
```

Claude acts as writer and chief editor — running all research searches in parallel across every coverage category, pulling live Chicagoland weather from the National Weather Service, compiling the latest Armstrong Economics commentary, and assembling a complete multi-file HTML edition in dark-mode broadsheet style.

-----

## Coverage Areas

|Section                 |Topics                                          |
|------------------------|------------------------------------------------|
|📈 Markets & Finance     |Equities, indices, commodities                  |
|🏦 Federal Reserve / FOMC|Rate decisions, monetary policy                 |
|₿ Bitcoin & Crypto      |Price action, market sentiment                  |
|🌍 Geopolitics           |U.S.–Iran conflict and other global developments|
|🏠 Real Estate           |Mortgage rates, housing market trends           |
|📊 Armstrong Economics   |Latest Martin Armstrong / Market Talk commentary|
|🌤️ Chicagoland Weather   |NWS forecast for the Chicago metro area         |
|🏟️ Chicago Sports        |Cubs, White Sox, Bulls, Blackhawks, Bears       |
|💊 Health & Wellness     |Medical research, nutrition, fitness news       |
|🎲 Closing Triptych      |Random fact, word of the day, quote of the day  |

-----

## Design

- **Dark mode** — near-black background (`#0f0e0c`), warm cream text (`#ede4ce`), orange-red accents (`#c8481a`), gold highlights (`#c9a227`)
- **Full broadsheet layout** — masthead, scrolling ticker, section headers, cards, market tables, weather banner, sports items, pull quotes, editor’s dispatch
- **Mobile-friendly**, multi-file output (HTML + shared external CSS)
- **Typography:** Playfair Display, Source Sans 3 (Google Fonts)
- All styling lives in `style.css` — no inline styles in any HTML file

-----

## File Structure

```
/
├── index.html              ← Today's edition (homepage)
├── archive.html            ← Full archive of all past editions
├── YYYY-MM-DD.html         ← Permanent dated copy of each edition
├── style.css               ← Shared stylesheet for all editions
└── README.md
```

Each edition includes a **navigation bar** linking to the previous edition, the archive, and (once the next edition is generated) the following day’s edition — creating a fully browsable chain of issues.

-----

## How It Works

Each `run tdl` run:

1. Confirms the current date
1. Runs all research searches in parallel across every coverage category (markets, Fed, crypto, geopolitics, mortgage rates, Armstrong Economics, weather, Cubs/Sox/Bulls/Hawks/Bears, health)
1. Fetches the Chicagoland forecast from the National Weather Service
1. Generates today’s edition and writes 5 files:
- `index.html` — today’s edition as the homepage
- `YYYY-MM-DD.html` — today’s permanent dated archive copy
- `archive.html` — updated archive index with today’s edition on top, marked **Latest**
- Previous day’s `YYYY-MM-DD.html` — patched so its forward-navigation arrow becomes a live link to today
- `style.css` — shared stylesheet (re-uploaded only when changed)
1. Files are pushed to this repository
1. GitHub Pages serves the updated site within ~30 seconds

-----

## Archive

All past editions are permanently preserved as dated HTML files and linked from [archive.html](https://unclejim7.github.io/The-Daily-Ledger/archive.html). Editions are grouped by month and year, with the newest issue always shown at the top with a **Latest** badge.

-----

## Tech Stack

- **AI engine:** [Claude](https://claude.ai) (Anthropic) — writer, editor, researcher, and publisher
- **Hosting:** GitHub Pages (free, static)
- **Languages:** HTML, CSS
- **Data sources:** Live web search, National Weather Service API, Armstrong Economics
- **Fonts:** Google Fonts

-----

*Curated daily for Nunya Biz · Est. May 2026 in GFY, USA*

*Published daily. No ads. No paywalls. No algorithms.*