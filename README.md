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

- **Dark mode (default)** — near-black background (`#0f0e0c`), warm cream text (`#ede4ce`), orange-red accents (`#c8481a`), gold highlights (`#c9a227`)
- **Light mode toggle** — every edition and the archive include a Light/Dark mode switch in the top nav (session-only, no data stored)
- **Full broadsheet layout** — masthead, scrolling ticker, section headers, cards, market tables, weather banner with custom SVG icons, sports items, pull quotes, editor’s dispatch
- **“On This Day” callback** — each edition recalls the headline and key market stats from one week prior, with then-vs-now comparisons
- **Market sparklines** — inline SVG trend charts for Bitcoin and the S&P 500 across the full run of editions
- **Print-friendly** — a dedicated print stylesheet flattens the dark theme to a clean, readable layout for anyone who wants a hard copy
- **Mobile-friendly**, multi-file output (HTML + shared external CSS)
- **Typography:** Playfair Display, Libre Baskerville, Source Sans 3 (Google Fonts)
- All styling lives in `style.css` — no inline styles in any HTML file

-----

## File Structure

```
/
├── index.html              ← Today's edition (homepage)
├── archive.html            ← Searchable archive of all past editions
├── YYYY-MM-DD.html         ← Permanent dated copy of each edition
├── style.css               ← Shared stylesheet for all editions
├── editions.json           ← Structured metadata for every edition
├── feed.xml                ← RSS feed of all editions
├── TEMPLATE_NOTES.md        ← Internal notes on template features
└── README.md
```

Each edition includes a **navigation bar** linking to the previous edition, the archive, a light/dark mode toggle, and (once the next edition is generated) the following day’s edition — creating a fully browsable chain of issues.

-----

## Archive & Search

All past editions are permanently preserved as dated HTML files and indexed in [archive.html](https://unclejim7.github.io/The-Daily-Ledger/archive.html). The archive is generated from `editions.json` and includes:

- A **search box** that filters editions by date, headline, or topic in real time
- A one-line **teaser** for every edition
- Editions grouped by month and year, newest first, with the current issue marked **Latest**

-----

## RSS Feed

Subscribe to [feed.xml](https://unclejim7.github.io/The-Daily-Ledger/feed.xml) in any feed reader to get new editions as they’re published. The feed is generated from `editions.json` and includes a title, link, and teaser for every edition.

-----

## How It Works

Each `run tdl` run:

1. Confirms the current date
1. Runs all research searches in parallel across every coverage category (markets, Fed, crypto, geopolitics, mortgage rates, Armstrong Economics, weather, Cubs/Sox/Bulls/Hawks/Bears, health)
1. Fetches the Chicagoland forecast from the National Weather Service
1. Generates today’s edition — including the “On This Day” callback and updated sparkline charts — and writes the following files:

- `index.html` — today’s edition as the homepage
- `YYYY-MM-DD.html` — today’s permanent dated archive copy
- `editions.json` — today’s edition metadata appended, edition count incremented
- `archive.html` — regenerated from `editions.json` with today’s edition on top, marked **Latest**
- `feed.xml` — regenerated from `editions.json` with today’s edition added
- Previous day’s `YYYY-MM-DD.html` — patched so its forward-navigation arrow becomes a live link to today
- `style.css` — shared stylesheet (re-uploaded only when changed)

1. Files are pushed to this repository
1. GitHub Pages serves the updated site within ~30 seconds

-----

## Corrections

If a prior edition needs a factual correction, it’s noted in a small **Corrections** box near the top of the relevant day’s edition — used only when needed, so most editions won’t have one.

-----

## Tech Stack

- **AI engine:** [Claude](https://claude.ai) (Anthropic) — writer, editor, researcher, and publisher
- **Hosting:** GitHub Pages (free, static)
- **Languages:** HTML, CSS, vanilla JavaScript (search/filter, mode toggle — no frameworks, no build step)
- **Data sources:** Live web search, National Weather Service API, Armstrong Economics
- **Fonts:** Google Fonts

-----

*Curated daily for Nunya Biz · Est. May 2026 in GFY, USA*

*Published daily. No ads. No paywalls. No algorithms.*