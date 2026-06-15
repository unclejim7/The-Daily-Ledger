# The Daily Ledger — Template Notes (Phases 2-4 additions)

These notes document new template features added in this build (June 15, 2026,
alongside edition No. 20) so future `run tdl` runs apply them consistently.

## New files

- `editions.json` — single source of truth for edition metadata (date, headline,
  teaser, stats). Append a new entry every run, bump `latest_edition`.
- `feed.xml` — RSS feed generated from `editions.json`. Regenerate every run by
  prepending the new edition’s `<item>` block (newest first) and updating
  `<lastBuildDate>`.

## archive.html (Phase 2)

Now generated from `editions.json`, not hand-edited. Each run:

1. Add the new edition’s entry at the top of the `editions` array in
   `editions.json` (already done as part of normal workflow).
1. Regenerate `archive.html`:
- New entry at top with `badge-latest` span
- Remove `badge-latest` from the previous “Latest” entry
- Each entry includes `data-search="<lowercased date + headline + teaser>"`
  for the search/filter JS, and a `.ae-teaser` paragraph
- Group headers (`.archive-month`) by “Month YYYY”
1. The search box and its JS are static — don’t need regenerating, just keep
   the `<script>` block intact when regenerating the page.

## On This Day card (Phase 3)

Appears on `index.html` only (today’s edition), placed right after the lead
story, before the Markets & Finance section head.

- Default lookback: **7 editions ago** (one week), using `.otd-stamp` text
  “One Week Ago”. If fewer than 8 editions exist, skip the card entirely.
- Compares whatever stats are present in both the target and current edition’s
  `stats` object (commonly `btc`, `mortgage_30yr`, `sp500`). Show 2 stats max.
- Once the archive passes ~30 editions (~1 month), consider switching lookback
  to “30 days ago” / “one month ago” for a more meaningful comparison, and
  eventually support both weekly and monthly callbacks side by side.

## Sparklines (Phase 3)

Two sparklines appear after the market table on `index.html`: Bitcoin (full
history) and S&P 500 (wherever `sp500` is present in stats — sparse weeks are
fine, the line just connects available points).

- Regenerate the SVG path data each run from the full `editions.json` series
  — the path scales to a 600x48 viewBox regardless of point count.
- If a series exceeds ~60 points (roughly 2 months of daily editions),
  consider switching from “all editions” to “last 30 editions” to keep the
  chart legible.

## Weather icons (Phase 3)

`.wx-icon` SVG set replaces the weather banner emoji. Current icon: partly
cloudy (sun + cloud). Build out the rest of the set as conditions warrant:
sunny (sun only), cloudy (cloud only, larger), rain (cloud + wx-rain lines),
storm (cloud + wx-bolt), snow (cloud + wx-snow dots). Reuse `.wx-outline`,
`.wx-sun`, `.wx-cloud`, `.wx-rain`, `.wx-bolt`, `.wx-snow` classes already
defined in `style.css` — just compose new `<svg class="wx-icon">` markup
per condition.

## Light/dark mode toggle (Phase 4)

- `.mode-toggle` button lives in `.nav-right` alongside the Archive link and
  forward-nav arrow.
- JS is a small inline `<script>` before `</body>`: toggles `.light-mode` on
  `<body>`, swaps button label. Session-only — no localStorage (per artifact
  storage restrictions; this is a real HTML page, not a Claude artifact, but
  keeping it dependency-free is simpler and avoids a flash-of-wrong-theme).
- `.light-mode` token overrides live at the top of `style.css` near `:root`.
- New editions: copy the nav structure (`.nav-right` wrapper) and the toggle
  script verbatim. Prior editions (No. 1-19) were NOT retrofitted — they keep
  their original nav markup and simply won’t have a toggle (no broken styling
  results from this, light-mode CSS just goes unused on those pages).

## Corrections box (Phase 4)

`.corrections-box` CSS exists in `style.css` but is unused by default. Only
add a `.corrections-box` block to an edition when there’s an actual correction
to a prior day’s reporting. Markup:

```html
<div class="corrections-box">
  <div class="cb-label">Correction</div>
  <p>In the June 14 edition, we reported X. The correct figure is Y.</p>
</div>
```

Place it near the top of `<div class="ledger-body">`, after the weather
banner / On This Day card, before the Markets section — corrections should be
prominent but not compete with the lead story.

## Print stylesheet (Phase 4)

`@media print` block added to `style.css`. No action needed per-run — it
applies automatically. Hides nav/ticker/toggle/search, flattens dark theme to
white background with dark text, removes decorative gradients and shadows.

## Vol. II rollover (Phase 4)

No automatic trigger exists yet — this is a manual decision point.

**Trigger conditions to watch for:**

- Edition count reaches a round number (No. 100, or one full year ≈ No. 365)
- J explicitly requests a volume change (e.g., new year, redesign milestone)

**When rolling over to Vol. II:**

1. Edition numbering resets to No. 1 under the new volume (or continues
   continuously — J’s call at the time).
1. Update `editions.json`: add a `"volume": "II"` field to each new edition’s
   entry (or restructure to `{"volumes": {"I": [...], "II": [...]}}` if doing
   a clean split — decide based on how large Vol. I has grown).
1. `archive.html` groups would then need a Volume-level grouping above the
   Month-level grouping if both volumes are shown on one page, or Vol. I
   could be archived to a separate `archive-vol-1.html` with `archive.html`
   becoming Vol. II only plus a link back to the Vol. I archive.
1. Masthead `masthead-vol` text updates from “Vol. I” to “Vol. II” across
   the template for all new editions.

This is intentionally left as a documented decision point rather than
automated — a volume change is an editorial milestone, not a mechanical one.