# The Daily Ledger — Template Notes

Internal notes documenting template features so every `run tdl` run applies
them consistently. Supersedes the original "Phases 2-4" draft of these notes
— several items below (especially the mode toggle) describe behavior that
changed after that draft was written.

## New files

- `editions.json` — single source of truth for edition metadata (date,
  headline, teaser, stats). **Always fetch this file directly at the start of
  a run** rather than relying on conversation memory — it has lagged the live
  site in past runs, and reconstructing from memory compounds the gap. Append
  a new entry every run, bump `latest_edition`.
- `feed.xml` — RSS feed generated from `editions.json`. Regenerate every run
  by prepending the new edition's `<item>` block (newest first) and updating
  `<lastBuildDate>`.

## Publishing flow

Files are **not** pushed to GitHub automatically — there is no working
write-capable GitHub connection available. Every run writes all 7 files to a
downloads folder and presents them to the user, who uploads them to
`unclejim7/The-Daily-Ledger` manually. Do not describe this flow as
"pushing to the repository" in user-facing copy; it's a manual step.

## Edition nav bar

Placed immediately after the `<body>` tag on every edition:

- `← [Previous date]` — live link to the prior dated HTML file
- `📁 Archive` — always links to `archive.html`
- `[Next date] →` — rendered as `<span class="nav-disabled">` until the next
  edition exists, then patched to a live `<a>` link on that next run. This
  patch is the *only* change made to a previously published edition.

## archive.html

Generated from `editions.json`, not hand-edited. Each run:

1. Add the new edition's entry at the top of the `editions` array in
   `editions.json` (already done as part of normal workflow).
1. Regenerate `archive.html`:
   - Same dark/light toggle as the newspaper itself
   - Top nav with a `← Today's Edition` link back to `index.html`
   - New entry at top with a `badge-latest` span reading "Latest"
   - Remove `badge-latest` from the previous top entry — exactly one
     `badge-latest` should exist in the file after regeneration
   - Each entry shows full date, day of week, headline, and a `Read →`
     button linking to the dated HTML file
   - Each entry includes `data-search="<lowercased date + headline + teaser>"`
     for the search/filter JS, plus a `.ae-teaser` paragraph
   - Group headers (`.archive-month`) by "Month YYYY," newest first
1. The search box and its JS are static — keep the `<script>` block intact
   when regenerating the page rather than rewriting it.

## On This Day card

Appears on `index.html` (today's edition) only, placed right after the lead
story, before the Markets & Finance section head.

- Default lookback: **7 editions ago** (one week), using `.otd-stamp` text
  "One Week Ago." If fewer than 8 editions exist, skip the card entirely.
- Compares whatever stats are present in both the target and current
  edition's `stats` object (commonly `btc`, `mortgage_30yr`, `sp500`). Show
  2 stats max.
- Once the archive passes ~30 editions, consider a monthly lookback option
  alongside the weekly one — not yet implemented.

## Sparklines

Two sparklines appear after the market table on `index.html`: Bitcoin (full
history) and S&P 500 (wherever `sp500` is present in stats — sparse series
are fine, the line just connects available points).

- Regenerate the SVG path data each run from the **full** `editions.json`
  series via script (don't hand-compute or estimate from memory) — the path
  scales to a 600×48 viewBox regardless of point count, with 4px padding.
- Validate that the array length used for coordinates matches the edition
  count before outputting the path.
- If a series exceeds ~60 points, consider switching from "all editions" to
  "last 30 editions" to keep the chart legible — not yet implemented.

## Weather banner

- Lives at/near the top of every edition, right after the masthead/ticker,
  before other sections, styled as a prominent `weather-banner-top` card
  with a `.wx-icon` SVG, headline, narrative, and a stats row.
- **Exception:** editions No. 1–17 intentionally retain a legacy weather
  placement from before this card existed. Do not retrofit old editions
  unless explicitly asked.
- `.wx-icon` SVG set: sunny (sun only), partly cloudy (sun + cloud), cloudy
  (cloud only, larger), rain (cloud + `.wx-rain` lines), storm (cloud +
  `.wx-bolt`), snow (cloud + `.wx-snow` dots). Choose based on conditions.

## Ticker

- Structure is `.ticker-wrap` containing `.ticker-track` directly — **no**
  `.ticker-label` element in the HTML and no corresponding CSS. Just the
  scrolling content on the orange bar.
- Animation is `animation: ticker-scroll 45s linear infinite`, keyframe name
  `ticker-scroll` only. Duration is 45s, not any other value.
- Content: BTC price, major index closes, mortgage rate, sports
  scores/schedules, a weather snippet, 1–2 Armstrong items, a health item,
  and a geopolitical headline. ALL CAPS. Duplicate every item exactly once
  for a seamless scroll loop.

## Light/dark mode toggle (current, canonical)

- `.mode-toggle` is a **round 30px icon button** — `border-radius: 50%`,
  `width: 30px`, `height: 30px`, `font-size: 1rem`, no letter-spacing, no
  uppercase, no text padding.
- **Emoji only, never text.** Starts as 🌙 (dark, the default). The inline
  `<script>` before `</body>` toggles `.light-mode` on `<body>` and swaps the
  button's content to ☀️ when light mode is active, back to 🌙 otherwise.
  Do **not** swap in the strings "Light Mode" / "Dark Mode" — that was an
  earlier iteration of this feature and is no longer correct.
- `.mode-toggle` lives in `.nav-right` alongside the Archive link and the
  forward-nav arrow/span.
- `.light-mode` token overrides live near `:root` at the top of `style.css`
  — that file is the canonical source for the mode-toggle CSS. After copying
  `style.css` each run, grep for `.mode-toggle {` and confirm
  `border-radius: 50%` and `width: 30px` are present and that "Light Mode" /
  "Dark Mode" text is absent, before shipping.
- Session-only — no localStorage/sessionStorage. These are real static HTML
  pages (not Claude artifacts), but staying dependency-free avoids a
  flash-of-wrong-theme and keeps the pages trivially portable.
- Prior editions (No. 1–19) were not retrofitted with the toggle and keep
  their original nav markup; this causes no broken styling since unused
  light-mode CSS simply goes unused on those pages.

## Corrections box

`.corrections-box` CSS exists in `style.css` but is unused by default. Only
add a `.corrections-box` block to an edition when there's an actual
correction to a prior day's reporting. Markup:

```html
<div class="corrections-box">
  <div class="cb-label">Correction</div>
  <p>In the June 14 edition, we reported X. The correct figure is Y.</p>
</div>
```

Place it near the top of `<div class="ledger-body">`, after the weather
banner / On This Day card, before the Markets section — corrections should
be prominent but not compete with the lead story.

## Print stylesheet

`@media print` block in `style.css` applies automatically, no per-run action
needed. Hides nav/ticker/toggle/search, flattens the dark theme to a white
background with dark text, removes decorative gradients and shadows.

## Verification suite (run before every delivery)

All of the following must pass before files are presented:

- Div open/close tag counts balance in every HTML file
- Zero inline `<style>` blocks in any HTML file
- `nav-disabled` count is exactly 1 in the new edition, exactly 0 in the
  patched prior edition
- Exactly one `badge-latest` span in `archive.html`
- `editions.json` parses as valid JSON and its entry count matches
  `latest_edition`
- RSS `<item>` count in `feed.xml` matches the total edition count
- `style.css` mode-toggle block contains `border-radius: 50%` and
  `width: 30px`, and does not contain the strings "Light Mode" / "Dark Mode"

## Vol. II rollover

No automatic trigger exists — this is a manual decision point.

**Trigger conditions to watch for:**

- Edition count reaches a round number (No. 100, or one full year ≈ No. 365)
- User explicitly requests a volume change (e.g., new year, redesign
  milestone)

**When rolling over to Vol. II:**

1. Edition numbering resets to No. 1 under the new volume (or continues
   continuously — user's call at the time).
1. Update `editions.json`: add a `"volume": "II"` field to each new edition's
   entry (or restructure to `{"volumes": {"I": [...], "II": [...]}}` if doing
   a clean split — decide based on how large Vol. I has grown).
1. `archive.html` groups would then need a Volume-level grouping above the
   Month-level grouping if both volumes are shown on one page, or Vol. I
   could be archived to a separate `archive-vol-1.html` with `archive.html`
   becoming Vol. II only plus a link back to the Vol. I archive.
1. Masthead `masthead-vol` text updates from "Vol. I" to "Vol. II" across
   the template for all new editions.

This is intentionally left as a documented decision point rather than
automated — a volume change is an editorial milestone, not a mechanical one.
