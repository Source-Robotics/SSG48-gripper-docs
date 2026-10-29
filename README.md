# SSG-48 gripper documentation

The documentation of the SSG-48 adaptive electric gripper by [Source Robotics](https://source-robotics.com): the
manual (safety, technical data, installation, setup, operation, firmware), the gripper's CAN and UART reference,
and guides.

**Read it at [docs.source-robotics.com/SSG48-gripper-docs](https://docs.source-robotics.com/SSG48-gripper-docs/).**

The hardware files are in
[Source-Robotics/SSG-48-adaptive-electric-gripper](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper);
the gripper runs the firmware of the Spectral Micro driver,
[Source-Robotics/Spectral-Micro-BLDC-controller](https://github.com/Source-Robotics/Spectral-Micro-BLDC-controller).

## What is in this repository

| | |
|---|---|
| `docs/` | the pages: the manual chapters at the top level, `build/`, `reference/`, `guides/`, `support/`, `appendix/` |
| `docs/build/bill-of-materials.md`, `docs/assets/bom/` | written by `tools/sync_bom.py` from the gripper repository's BOM and its reference images. Never edit |
| `docs/includes/` | text shared by pages (glossary, symbols, abbreviations) and the data the reference pages are built from |
| `docs/includes/can_commands.yml`, `uart_commands.yml` | the hand-written descriptions of the CAN messages and UART commands a gripper needs (`partial: true`: the rest of the driver's commands are on the Spectral Micro site) |
| `docs/includes/generated/` | written by `tools/sync_firmware.py` from the firmware's release tag: `firmware_facts.json`, `firmware_release_notes.md`. Never edit |
| `versions.yml` | every version fact: the gripper release the site is versioned by, the firmware release it describes, the manual's number and revision |
| `compatibility.yml` | which firmware release works with which bootloader, gripper hardware, Python library and ROS 2 driver |
| `hooks/` | `versions.py` writes the version facts into the pages; `firmware_pages.py` builds the reference pages; `llms.py` writes the Markdown twin of every page, `llms.txt` and `llms-full.txt` |
| `docs/assets/models/ssg48/` | the 3D model of the configurator on the landing page, written by `tools/build_model.py` from the repository's URDF. Never edit |
| `tools/` | `sync_firmware.py`, `sync_bom.py`, `build_model.py`, `test_tools.py`, `root_404.html` |
| `overrides/` | the theme changes: the older-version banner, the edit/report line, the header's repository card |

The site is built with [MkDocs](https://www.mkdocs.org/) and the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, in the same form as the
[Spectral Micro](https://github.com/Source-Robotics/Spectral Micro-docs) and [PAR6](https://github.com/Source-Robotics/par6)
documentation; the hooks and tools are the same files.

## Preview it locally

You need Python 3.11 or newer.

```bash
git clone https://github.com/Source-Robotics/SSG48-gripper-docs.git
cd SSG48-gripper-docs
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt      # Linux and macOS: .venv/bin/pip
mkdocs serve
```

Open `http://127.0.0.1:8000/SSG48-gripper-docs/`. The page reloads by itself when you save a file.

Every push and pull request runs `python tools/test_tools.py` and `mkdocs build --strict`, which fails on a broken
link or a missing page. Run both before you open a pull request.

## The reference is generated from the firmware

The command IDs, the frame lengths the firmware accepts, the responses it sends, the list of UART commands with
their kind, argument type and what they print are read from the Spectral firmware's source **at its release tag**
by `tools/sync_firmware.py`. The descriptions, units and byte layouts are written by hand in
`docs/includes/can_commands.yml` and `uart_commands.yml`, for the commands a gripper needs. The build fails when
the two disagree: a command the descriptions name and the firmware does not have, or a byte layout that does not
fit the frame.

```bash
python tools/sync_firmware.py            # write docs/includes/generated/ from firmware.tag in versions.yml
python tools/sync_firmware.py --check    # exit 1 if they are out of date
```

The tool needs a clone of the Spectral firmware repository with its tags, next to this repository or named by
`--firmware PATH` / `FIRMWARE_DIR`, and the network for the release notes (`--no-network` keeps the file that is
there). The CI build does not run it; the generated files are committed.

## The bill of materials is copied from the gripper repository

`docs/build/bill-of-materials.md` is the gripper repository's BOM, as it is, with its reference images shown
inline: `tools/sync_bom.py` reads a clone of the repository named in `versions.yml` (`--repo PATH`,
`$GRIPPER_REPO_DIR`, a sibling folder or `../../projects/<name>`), converts the note blocks, copies and scales the
images into `docs/assets/bom/`, and writes a header naming the commit it copied. A wrong part or a broken link is
fixed in the repository's file, then:

```bash
python tools/sync_bom.py            # rewrite the page and the images from the clone
python tools/sync_bom.py --check    # exit 1 if the page is out of date
```

## The 3D model, the Markdown twins and the feedback widget

`tools/build_model.py` builds `docs/assets/models/ssg48/` from the gripper repository's URDF (the same `--repo`
as the BOM tool; needs `trimesh`): the body, one file per finger option, and `viewer.json`. The landing and
dimensions pages show them in the configurator `docs/javascripts/gripper-viewer.js` (three.js from a CDN, through
the import map in `overrides/main.html`, loaded only on those pages): turn and zoom, open the jaws, choose the
fingers and the colours. Run the tool again when the meshes change.

`hooks/llms.py` writes, at every build, a Markdown twin of every page next to its HTML (`…/index.md`), `llms.txt`
(an index of the twins by tab) and `llms-full.txt` (every page in one file), with the links absolute to the
published version (`extra.llms_base`). The "Copy this page as Markdown" button in the page header reads the twin.

The "Was this page helpful?" widget at the end of every page is configured under `extra.analytics.feedback`;
`overrides/partials/integrations/analytics/custom.html` handles the vote (remembered in the browser, sent to
`extra.feedback_endpoint` when one is set) and loads Plausible page analytics when `extra.analytics.property` is
the site's domain.

Two more site features live here as a pilot: the "Last update" date under every page comes from the
`git-revision-date-localized` plugin (the page's last commit; the CI checks out the whole history for it), and
comments through Giscus are wired in `overrides/partials/comments.html` and configured under `extra.comments`
in `mkdocs.yml`, which also says how to obtain the IDs that turn them on. The calculator on the Force and speed
page is `docs/javascripts/gripper-calculator.js`, driven by the data attributes of its block.

## Versions and releases

The site is versioned by **gripper release**: the version the product repository tags (`V1.1`, ...), published
under that name (`1.1`, ...). The version selector in the site's header switches between releases, and a page of
an older release says so in a bar at the top. The versions are built with [mike](https://github.com/jimporter/mike)
and kept in the `gh-pages` branch; `latest` points at the newest.

The gripper runs the Spectral driver's firmware, and the pages describe one firmware release (the version box
on the landing page names it). A new firmware release for the same gripper does not make a new version of the
site: the pages are updated in place, with a new revision letter.

**All version facts live in `versions.yml`, never in a page**: `docs_version` (the gripper release, which is also
the name the version is published under) with `product.tag` (`V` + `docs_version`), `firmware.version` with
`firmware.tag` (`V` + `firmware.version`), and the manual's number, title, revision, status and publication date.
`hooks/versions.py` writes them into the version box on the landing page and into the list of documents on the
About page; a malformed or missing fact stops the build.

### When the firmware releases a new version

1. Set `firmware.version` and `firmware.tag` in `versions.yml`; add a row to `compatibility.yml`, with the docs
   cell naming this site's version.
2. Run `python tools/sync_firmware.py`. If the firmware changed a gripper command, the build now fails until
   `can_commands.yml` / `uart_commands.yml` describe it: write the description.
3. Update the pages for what changed, using the release notes; give the manual a new revision letter in
   `versions.yml` and a line in its *Document history* on `docs/about.md`.
4. Commit and push to `main`. The site republishes the current version with the new firmware.

### When the gripper releases a new version

1. Set `docs_version`, `product.tag` and `product.released` in `versions.yml`, and the manual's `applies_to` if
   the hardware the manual applies to changed.
2. Update the pages for what changed in the hardware; a new revision letter and a *Document history* line.
3. Commit and push to `main`. The site publishes the new version, `latest` moves to it, and the previous
   gripper release's pages stay as they were.

### Publishing

`.github/workflows/publish.yml` publishes on every push to `main`: the tests, a strict build, then `mike deploy`
for `docs_version` with the alias `latest`. In the repository's Settings, under Pages, the source must be "Deploy
from a branch", branch `gh-pages`, folder `/ (root)`. Never run `mkdocs gh-deploy` on this repository: it would
overwrite every version mike keeps there.

The root of `gh-pages` also carries `404.html` (source: `tools/root_404.html`). It forwards addresses from before
the versioning, such as `/SSG48-gripper-docs/page3_control/`, to the same page under `latest/`, where the `redirects`
plugin in `mkdocs.yml` maps the old page names to the new pages. To preview the published versions locally, with
the version selector, run `mike serve`.

## The site's address

The site is served at `https://docs.source-robotics.com/SSG48-gripper-docs/`: the organisation's docs domain plus this
repository's name. Never rename this repository (its address would change and GitHub does not forward the old one),
and never add a `CNAME` file or a custom domain to it (that would take it out of the shared domain).

## License

- **Text and images:** [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/),
  see [LICENSE](LICENSE). You may copy, adapt and share them, also commercially, if you credit Source Robotics and
  share your changes under the same license.
- **Code:** the [MIT license](LICENSE-CODE). This covers the code examples in the pages and the site's own code
  (hooks, tools, overrides, scripts), so you can use an example in your own program without other conditions.
- **Names and logos:** the Source Robotics name, the product names and the logos are not covered by either license.
  The gripper's hardware design is licensed separately, in the product repository.

By contributing you agree that your contribution is published under these licenses.

## Contributing

A small fix can be made from the browser: every page ends with a link to edit it on GitHub. For anything larger,
open an issue first, then a pull request. The *Contributing* page on the site has the house rules. Questions about
the gripper itself go to the product repository's issue tracker.
