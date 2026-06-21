#!/usr/bin/env python3
"""
patch_nav.py — The Daily Ledger nav structure fixer
Run this in your repo root after pulling the new style.css.

Fixes the nav in all editions that have the OLD structure:
  <nav class="edition-nav">
    <a href="prev">← June X</a>
    <span class="nav-right">
      <a href="archive.html" class="nav-archive">📁 Archive</a>
      <span class="nav-disabled">June Y →</span>  OR  <a href="...">June Y →</a>
      <button class="mode-toggle">Light Mode</button>
    </span>
  </nav>

Converts to the NEW structure:
  <nav class="edition-nav">
    <a href="prev">← June X</a>
    <a href="archive.html" class="nav-archive">📁 Archive</a>
    <span class="nav-right">
      <span class="nav-disabled">June Y →</span>  OR  <a href="...">June Y →</a>
      <button class="mode-toggle">Light Mode</button>
    </span>
  </nav>

Usage: python3 patch_nav.py
"""

import re
import glob
import os

def patch_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if this file has the OLD structure (archive inside nav-right)
    # Pattern: nav-right contains nav-archive
    old_pattern = re.compile(
        r'(<nav class="edition-nav">\s*)'           # nav open
        r'(<a [^>]*>.*?</a>)\s*'                    # prev link
        r'<span class="nav-right">\s*'              # nav-right open
        r'(<a [^>]*class="nav-archive"[^>]*>.*?</a>)\s*'  # archive link
        r'(.*?)'                                     # next link + button
        r'</span>\s*'                               # nav-right close
        r'(</nav>)',                                 # nav close
        re.DOTALL
    )

    m = old_pattern.search(content)
    if not m:
        return False, "no match (already new structure or different pattern)"

    nav_open   = m.group(1)
    prev_link  = m.group(2).strip()
    archive    = m.group(3).strip()
    rest       = m.group(4).strip()   # next-arrow + button
    nav_close  = m.group(5)

    new_nav = (
        f'{nav_open}'
        f'  {prev_link}\n'
        f'  {archive}\n'
        f'  <span class="nav-right">\n'
        f'    {rest}\n'
        f'  </span>\n'
        f'{nav_close}'
    )

    new_content = content[:m.start()] + new_nav + content[m.end():]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "patched"


def main():
    # Find all dated HTML editions (not index.html or archive.html)
    files = sorted(glob.glob('2026-*.html'))
    if not files:
        print("No 2026-*.html files found. Run this script from your repo root.")
        return

    patched = []
    skipped = []
    errors  = []

    for path in files:
        try:
            changed, reason = patch_file(path)
            if changed:
                patched.append(f"  ✓ {path}")
            else:
                skipped.append(f"  — {path}: {reason}")
        except Exception as e:
            errors.append(f"  ✗ {path}: {e}")

    print(f"\nThe Daily Ledger — Nav Patch Script")
    print(f"{'='*50}")
    print(f"\nPatched ({len(patched)}):")
    print('\n'.join(patched) if patched else "  (none)")
    print(f"\nSkipped ({len(skipped)}):")
    print('\n'.join(skipped) if skipped else "  (none)")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        print('\n'.join(errors))
    print(f"\nDone. Commit style.css + all patched files together.")


if __name__ == '__main__':
    main()
