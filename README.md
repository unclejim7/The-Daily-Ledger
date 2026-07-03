# 📰 The Daily Ledger

> *Truth, Clearly Delivered.*

**Live site:** [unclejim7.github.io/The-Daily-Ledger](https://unclejim7.github.io/The-Daily-Ledger)
**Repo:** [github.com/unclejim7/The-Daily-Ledger](https://github.com/unclejim7/The-Daily-Ledger)

-----

## What Is This?

The Daily Ledger is a fully custom, AI-generated HTML newspaper published daily via GitHub Pages. Each edition is a richly formatted dark-mode broadsheet covering markets, macroeconomics, the Federal Reserve, tax & accounting, Bitcoin & crypto, real estate, geopolitics, Armstrong Economics, Chicago sports, Chicagoland weather, and health, wellness & fitness — curated and written fresh every day.

Every edition is generated on demand using a single command typed into Claude:

```
run tdl
```

(Also recognized: "run the daily ledger," "new edition.")

Claude acts as writer and chief editor — running all research searches in parallel across every coverage category, pulling live Chicagoland weather, compiling the latest Armstrong Economics commentary, and assembling a complete multi-file HTML edition in dark-mode broadsheet style. The full build sequence, `editions.json` contract, and file-by-file mechanics are governed by Claude's internal `the-daily-ledger` skill.

-----

## Coverage Areas

|Section                    |Topics                                            |
|----------------------------|--------------------------------------------------|
|📈 Markets & Finance        |Equities, indices, commodities                    |
|📊 Macroeconomics           |Growth, inflation, labor data                     |
|🏦 Federal Reserve / FOMC   |Rate decisions, monetary policy                   |
|🧾 Tax & Accounting         |IRS news, filing deadlines, policy changes        |
|₿ Bitcoin & Crypto          |Price action, market sentiment                    |
|🏠 Real Estate              |Mortgage rates, housing market trends             |
|🌍 Geopolitics              |U.S. foreign policy and global developments       |
|📈 Armstrong Economics      |Latest Martin Armstrong / Market Talk commentary  |
|🌤️ Chicagoland Weather      |Local forecast for the Chicago metro area         |
|🏟️ Chicago Sports           |Cubs, White Sox, Bears, Bulls, Blackhawks         |
|💊 Health, Wellness & Fitness|Medical research, nutrition, fitness news        |
|🎲 Closing Triptych         |Random fact, word of the day, quote of the day    |

-----

## Design

- **Dark mode by default** — near-black background (`#0f0e0c`), warm cream text (`#ede4ce`), orange-red accents (`#c8481a`), gold highlights (`#c9a227`)
- **Light/dark toggle** — a single round icon button (🌙 in dark mode, ☀️ in light mode). Emoji only, no text label. Session-only — no data stored.
- **Full broadsheet layout** — masthead, scrolling ticker, section headers, cards, market tables, weather banner with custom SVG icons, sports items, health items, pull quotes, editor's dispatch
- **"On This Day" callback** — each edition recalls the headline and key market stats from one week prior, with then-vs-now comparisons
- **Market sparklines** — inline SVG trend charts for Bitcoin and the S&P 500 across the full run of editions
- **Print-friendly** — a dedicated print stylesheet flattens the dark theme to a clean, readable layout for anyone who wants a hard copy
- **Mobile-friendly**, multi-file output (HTML + shared external CSS)
- **Typography:** Playfair Display, Libre Baskerville, Source Sans 3 (Google Fonts)
- All styling lives in `style.css` — **no inline `<style>` blocks** in any HTML file; every HTML file links the stylesheet via `<link rel="stylesheet" href="style.css">`
- Dateline reads **Chicago, Illinois**

-----

## File Structure

```
/
├── index.html              ← Today's edition (homepage)
├── archive.html            ← Searchable archive of all past editions
├── YYYY-MM-DD.html         ← Permanent dated copy of each edition
├── style.css               ← Shared stylesheet for all editions
├── editions.json            ← Structured metadata for every edition
├── feed.xml                 ← RSS feed of all editions
├── TEMPLATE_NOTES.md        ← Internal notes on template features
└── README.md
```

Each edition includes a **navigation bar directly after `<body>`**: a live link back to the previous edition, a link to the archive, and a forward-navigation slot that stays disabled (`<span class="nav-disabled">`) until the next edition is published, at which point it's patched into a live link — creating a fully browsable chain of issues.

-----

## Archive & Search

All past editions are permanently preserved as dated HTML files and indexed in [archive.html](https://unclejim7.github.io/The-Daily-Ledger/archive.html), which is regenerated from `editions.json` on every run. It includes:

- The same dark/light toggle as the newspaper itself
- A top nav link back to today's edition (`index.html`)
- A **search box** that filters editions by date, headline, or topic in real time
- A one-line **teaser** for every edition
- Editions grouped by month and year, newest first, with the current issue marked **Latest**

-----

## RSS Feed

Subscribe to [feed.xml](https://unclejim7.github.io/The-Daily-Ledger/feed.xml) in any feed reader to get new editions as they're published. The feed is regenerated from `editions.json` on every run and includes a title, link, and teaser for every edition.

-----

## How It Works

Each `run tdl` run:

1. Confirms the current date and fetches `editions.json` as the authoritative record of prior editions
1. Runs all research searches in parallel across every coverage category (markets, macro, Fed, tax, crypto, real estate, geopolitics, Armstrong Economics, weather, Chicago sports, health)
1. Pulls the latest Chicagoland forecast
1. Generates today's edition — including the "On This Day" callback and updated sparkline charts

**Output — 7 files, downloaded for manual push:**

- `index.html` — today's edition as the homepage
- `YYYY-MM-DD.html` — today's permanent dated archive copy
- Previous day's `YYYY-MM-DD.html` — patched so its forward-navigation arrow becomes a live link to today
- `archive.html` — regenerated from `editions.json` with today's edition on top, marked **Latest**
- `editions.json` — today's edition metadata prepended, edition count incremented
- `feed.xml` — regenerated from `editions.json` with today's edition added
- `style.css` — shared stylesheet, included every run (re-upload only matters when it's actually changed)

**Important:** files are **not** pushed to GitHub automatically. There is no working write-capable GitHub connection in this environment, so every run stages all 7 files to a downloads folder and presents them for the user to manually upload to `unclejim7/The-Daily-Ledger`. Once uploaded, GitHub Pages serves the updated site within roughly 30 seconds.

-----

## Corrections

If a prior edition needs a factual correction, it's noted in a small **Corrections** box near the top of the relevant day's edition — used only when needed, so most editions won't have one.

-----

## Tech Stack

- **AI engine:** [Claude](https://claude.ai) (Anthropic) — writer, editor, researcher, and publisher
- **Hosting:** GitHub Pages (free, static)
- **Languages:** HTML, CSS, vanilla JavaScript (search/filter, mode toggle — no frameworks, no build step)
- **Data sources:** Live web search, Chicagoland weather data, Armstrong Economics
- **Fonts:** Google Fonts

-----

*Curated daily for Nunya Biz · Est. May 2026 in GFY, USA*

*Published daily. No ads. No paywalls. No algorithms.*
