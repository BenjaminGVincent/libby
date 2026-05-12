"""MkDocs build hook: append `?v=<hash>` cache-busters to extra_css / extra_javascript links.

Each entry in `mkdocs.yml::extra_css` and `extra_javascript` gets a content-hash
query string appended at build time, so a stylesheet edit ships with a fresh
URL and the browser is forced to re-fetch instead of serving the old version
from disk cache. Mirrors the cache-bust pattern already used on case-page
download links (`?v=<hash>` on each PDF / HTML artifact).

Wired into mkdocs.yml via `hooks: [scripts/mkdocs_hooks.py]`.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

_HASHES: dict[str, str] = {}


def _content_hash(path: Path, length: int = 8) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:length]


def on_pre_build(config):
    """Compute hashes for every extra_css / extra_javascript file once per build."""
    docs_dir = Path(config["docs_dir"])
    _HASHES.clear()
    for asset_rel in (config.get("extra_css") or []) + (config.get("extra_javascript") or []):
        # `extra_css` / `extra_javascript` entries can be plain strings or
        # dict-like ExtraScriptValue objects (mkdocs >= 1.5). Normalize.
        asset_str = str(asset_rel)
        asset_path = docs_dir / asset_str
        if asset_path.exists():
            _HASHES[Path(asset_str).name] = _content_hash(asset_path)


def on_post_page(output: str, page, config) -> str:
    """Rewrite <link href="...filename"> and <script src="...filename"> with `?v=<hash>`.

    Matches the final filename across mkdocs's relative-path rewriting (e.g.
    `../stylesheets/trial-table.css` on a nested page).
    """
    if not _HASHES:
        return output
    for filename, h in _HASHES.items():
        # Stylesheet links — match href ending in the filename, append ?v=hash
        # (skip if a query string is already present).
        css_pattern = re.compile(
            r'(<link\b[^>]*?\bhref=")([^"?]*?/)?(' + re.escape(filename) + r')(")',
            flags=re.IGNORECASE,
        )
        output = css_pattern.sub(
            lambda m, h=h: f'{m.group(1)}{m.group(2) or ""}{m.group(3)}?v={h}{m.group(4)}',
            output,
        )
        # Script tags — same shape for extra_javascript.
        js_pattern = re.compile(
            r'(<script\b[^>]*?\bsrc=")([^"?]*?/)?(' + re.escape(filename) + r')(")',
            flags=re.IGNORECASE,
        )
        output = js_pattern.sub(
            lambda m, h=h: f'{m.group(1)}{m.group(2) or ""}{m.group(3)}?v={h}{m.group(4)}',
            output,
        )
    return output
