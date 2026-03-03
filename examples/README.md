# Examples

This folder contains minimal examples other teams can copy into their service repositories.

## Django

- `examples/django/templatetags/vite.py` — a small template tag that demonstrates reading Vite's `manifest.json` and rendering correct asset paths via Django `static()`.

## Build and deploy notes

- Build output: run `npm run build` (or `yarn build`) in CI or locally. The build produces a `dist/` directory containing fingerprinted assets and a Vite `manifest.json` that maps source entry names to hashed filenames.
- Deploy static files: copy or expose the contents of `dist/` into your Django staticfiles directory so Django can serve them (or let your webserver serve `dist/` directly).
- Use the Vite manifest in templates: read `dist/manifest.json` at deploy-time to look up the correct hashed filenames for the CSS and JS produced by the build and render `<link>`/`<script>` tags server-side. This guarantees the CSS is present even when JS is disabled.

## Example minimal Django template helper

The file `examples/django/templatetags/vite.py` is a tiny, copyable example. In short, copy the file into your service under `myproject/templatetags/vite.py`, adapt the `MANIFEST_PATH` to point at your built `dist/manifest.json` location and load the tag in your templates with `{% load vite %}`.

Usage in a Django template (example):

```django
{% load vite %}
<link rel="manifest" href="{% static 'assets/manifest.json' %}">
<link rel="stylesheet" href="{% vite_asset 'src/javascripts/application.js' 'css' %}">
<script type="module" src="{% vite_asset 'src/javascripts/application.js' %}"></script>
```

## Notes

- Keep helper logic in your service repo — this example demonstrates the pattern but does not couple the starter to Django.
- You may cache the parsed `manifest.json` in memory or reload it when the file changes.
- Alternatively, expose `dist/manifest.json` as an artifact from CI and have your deploy pipeline inject correct asset paths into settings or templates.
