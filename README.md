# Grand Secretary — National Grand Lodge of Greece

The way in to the work of the Secretariat. This repository holds the menu;
each section keeps its own repository, its own history and its own site.

**https://dskiad.github.io/NGLG-GRAND-SECRETARY/**

> The link goes live once GitHub Pages is enabled for this repository:
> **Settings → Pages → Build and deployment → Source: _GitHub Actions_**.
> The workflow in `.github/workflows/pages.yml` publishes every push to `main`.

## The sections

| Section | Where it lives | Opens |
| --- | --- | --- |
| Registration forms | [`dskiad/nglg-registration-forms`](https://github.com/dskiad/nglg-registration-forms) | the register, with the live forms linked from it |
| Τεκτονικές Ομιλίες | [`dskiad/nglg-tektonikes-omilies`](https://github.com/dskiad/nglg-tektonikes-omilies) | [the library](https://dskiad.github.io/nglg-tektonikes-omilies/) |
| Bear Bell Ritual | [`dskiad/bear-bell-ritual`](https://github.com/dskiad/bear-bell-ritual) | the repository; the application itself is restricted |

## The three offices

This is one of three, each its own site, each carrying a switch to the other
two in its top bar:

| Office | Body | Repository |
| --- | --- | --- |
| Grand Chancellor | National Grand Lodge of Greece | [`Grand-Chancellor`](https://github.com/dskiad/Grand-Chancellor) |
| Grand Secretary | National Grand Lodge of Greece | this one |
| Grand Secretary | Masonic Order of Athelstan | [`ATHELSTAN-GRAND-SECRETARY`](https://github.com/dskiad/ATHELSTAN-GRAND-SECRETARY) |

Each keeps its own copy of `assets/portal.css`, so no site depends on another
being up.

## Adding a section

A section that lives elsewhere is a card in `index.html`:

```html
<a class="doc-card away" href="https://…">
  <span class="tag">Live</span>          <!-- or Registry, Restricted app, … -->
  <h3>Its name</h3>
  <p>One sentence on what it is.</p>
  <span class="where">owner / repo</span>
</a>
```

Point the card at the section's live site where it has one, and at its
repository where it does not. `away` marks a card that leaves this site; a
section still being built is a `<div class="doc-card soon">` with an
*In preparation* tag.

A section held **here** — a form of the Secretariat, filled in and downloaded
as a PDF — works the way the Chancellor's patents do: copy
`patents/past-grand-officer.html` and `assets/` from
[`dskiad/Grand-Chancellor`](https://github.com/dskiad/Grand-Chancellor), whose
README documents the engine.
