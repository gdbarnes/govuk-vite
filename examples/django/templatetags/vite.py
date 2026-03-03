"""
Minimal Django template tag example for reading Vite's `manifest.json`.

Copy this file to `yourproject/templatetags/vite.py` and load it in templates with `{% load vite %}`.
This example is intentionally tiny and non-opinionated — adapt it for caching, settings integration,
or to read the manifest from a configured path.
"""
import json
from pathlib import Path
from django import template
from django.templatetags.static import static

register = template.Library()

# Adjust this path to where your build writes the Vite manifest in your deploy pipeline
MANIFEST_PATH = Path(__file__).resolve().parents[3] / 'dist' / 'manifest.json'

try:
    with open(MANIFEST_PATH, 'r') as f:
        MANIFEST = json.load(f)
except Exception:
    MANIFEST = {}

@register.simple_tag
def vite_asset(entry_name, asset_type='js'):
    """Return a static path for a built Vite asset.

    entry_name should match the key in Vite's manifest.json, e.g. "src/javascripts/application.js".
    asset_type: 'js' or 'css'. For CSS, the helper will return the first CSS file listed for the entry.
    """
    entry = MANIFEST.get(entry_name)
    if not entry:
        return ''
    if asset_type == 'css':
        css_list = entry.get('css') or []
        if not css_list:
            return ''
        return static(css_list[0])
    # default: return the JS file
    return static(entry['file'])
