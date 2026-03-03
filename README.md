# GOV.UK Vite starter

[![version](https://img.shields.io/badge/version-1.0.0-blue)](package.json) [![govuk-frontend](https://img.shields.io/badge/govuk--frontend-%5E6.0.0-orange)](https://www.npmjs.com/package/govuk-frontend) [![vite](https://img.shields.io/badge/vite-%5E7.3.1-lightgrey)](https://vitejs.dev/) [![node](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org/) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

A minimal Vite-based starter for compiling GOV.UK Frontend assets and styles. This project is aimed at engineers working on GOV.UK services who want a small, modern build setup for assets (JS/CSS) while using the official `govuk-frontend` package. It is a lightweight alternative to Webpack-based asset pipelines and can be used as a simpler starting point for service teams.

**Status:** Lightweight starter — intended as a reference and starting point for service teams.

**Goals:**

- Provide a simple Vite workflow for local development and production builds.
- Ship GOV.UK Frontend assets and Sass-based styles.
- Keep configuration minimal so teams can adapt it to their deployment flows.

**Prerequisites**

- Node.js (LTS recommended)
- npm (or Yarn / pnpm)

**Quick start**

Install dependencies:

```bash
# npm
npm install

# or using Yarn
yarn
```

Start the dev server (live reload):

```bash
# npm
npm run dev

# or using Yarn
yarn dev
```

Build for production:

```bash
# npm
npm run build

# or using Yarn
yarn build
```

Preview a production build locally:

```bash
# npm
npm run preview

# or using Yarn
yarn preview
```

**What’s included**

- `index.html` — example entry that includes compiled assets.
- `src/javascripts/application.js` — JS entrypoint where you can import GOV.UK components.
- `src/stylesheets/application.scss` — Sass entry importing `govuk-frontend` styles and custom overrides.
- `vite.config.js` — minimal Vite config, including static copy plugin if needed.

**Using GOV.UK Frontend**

This starter uses the `govuk-frontend` npm package. Import components or styles from it in your JS/Sass. For example, in `src/stylesheets/application.scss` you might have:

```scss
@import 'govuk-frontend/govuk/all';
// your overrides here
```

And in `src/javascripts/application.js`:

```js
import 'govuk-frontend/govuk/all';
import '../stylesheets/application.scss';

// Initialise any GOV.UK JS modules as required by your service
```

**Project structure**

- Root files for quick review: `package.json`, `vite.config.js`, `index.html`.
- Source: `src/` — place your JS, Sass, and assets here.
- Output: `dist/` — created after `npm run build` (ready to deploy).

**Customisation & deployment notes**

- This repo is intentionally minimal; adapt `vite.config.js` to integrate with your CI/CD or asset pipeline.
- Ensure your deployment serves the `dist/` directory and sets appropriate caching headers for assets.

**Django integration**

If you use Django, we keep a small, copyable example in `examples/` that demonstrates the recommended pattern for production use. See [examples/README.md](examples/README.md#django) for details.

**Troubleshooting**

- If Sass compilation fails, ensure you have a compatible `sass` version in `devDependencies` and a supported Node.js version.
- If GOV.UK styles/components behave unexpectedly, check you are importing `govuk-frontend` correctly and using the expected HTML markup.

**Contributing**

- This repo is a starter template. If you improve the setup, please open a PR with a clear rationale and minimal, focused changes.

**License**

- See the repository `LICENSE` file.
