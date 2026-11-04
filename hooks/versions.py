"""Write the version facts of versions.yml into the pages (the same hook as Source-Robotics/par6, for a product
that runs another product's firmware).

Six placeholders, each replaced when the site is built:

    <!-- doc-meta: KEY -->      a manual's version box, on its landing page: document number, the gripper release,
                                the driver firmware release (for a document that describes one), revision,
                                publication date, what it applies to
    <!-- documents-table -->    the list of every document, on the About page
    <!-- version: GROUP.KEY --> a component's version in running text, e.g. models.robot_descriptions: its tag
                                without the leading v (v2.18.1 is written 2.18.1)
    <!-- version-url: COMPONENT -->      the address of the component's files at its tag, {repository}/tree/{tag}, to
                                build a link to a folder: COMPONENT is firmware, software.KEY or models.KEY
    <!-- version-release: COMPONENT -->  the address of its release page, {repository}/releases/tag/{tag}
    <!-- version-link: COMPONENT -->     a link to the files at the tag with the version as its text, and the release
                                date when versions.yml has one

The facts live in versions.yml only. docs_version is the gripper release: the product repository's tag without
its V, and the name the site is published under. firmware.version is the driver firmware release the pages and
the generated reference describe; a new firmware release for the same gripper updates the site in place.
software and models are the other components the pages name with a version (the Python library, the robot
models). A malformed or missing fact, an unknown manual or an unknown component stops the build: a version on a
page is never guessed. The version placeholders are the same as PAROL-docs'. Registered in mkdocs.yml under
`hooks:`.
"""
from __future__ import annotations

import datetime
import re
from pathlib import Path

import yaml
from mkdocs.exceptions import PluginError

META_RE = re.compile(r"<!--\s*doc-meta:\s*([A-Za-z0-9_-]+)\s*-->")
TABLE_RE = re.compile(r"<!--\s*documents-table\s*-->")
VERSION_RE = re.compile(r"<!--\s*version:\s*([A-Za-z0-9_-]+)\.([A-Za-z0-9_-]+)\s*-->")
URL_RE = re.compile(r"<!--\s*version-(url|link|release):\s*([A-Za-z0-9_-]+)(?:\.([A-Za-z0-9_-]+))?\s*-->")
REQUIRED = ("number", "title", "revision", "status", "covers")

_facts: dict = {}


def load(path) -> dict:
    """versions.yml, checked. Raises PluginError naming what is wrong."""
    try:
        data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise PluginError(f"versions.yml: {exc}") from exc
    if not isinstance(data, dict):
        raise PluginError("versions.yml: not a mapping")
    docs_version = str(data.get("docs_version", ""))
    if not re.fullmatch(r"\d+(\.\d+)*", docs_version):
        raise PluginError(f"versions.yml: docs_version {docs_version!r} is not a gripper release, e.g. \"1.1\"")
    product = data.get("product")
    if not isinstance(product, dict) or not all(product.get(k) for k in ("name", "repository", "tag")):
        raise PluginError("versions.yml: product needs name, repository and tag")
    ptag = str(product["tag"])
    if not re.fullmatch(r"[Vv]\d+(\.\d+)*", ptag):
        raise PluginError(f"versions.yml: product.tag {ptag!r} is not a release tag like V1.1")
    if ptag[1:] != docs_version:
        raise PluginError(f"versions.yml: product.tag {ptag} does not belong to docs_version {docs_version}")
    fw = data.get("firmware")
    if not isinstance(fw, dict) or not all(fw.get(k) for k in ("name", "version", "repository", "tag")):
        raise PluginError("versions.yml: firmware needs name, version, repository and tag")
    fw_version = str(fw["version"])
    if not re.fullmatch(r"\d+", fw_version):
        raise PluginError(f"versions.yml: firmware.version {fw_version!r} is not a firmware release number, e.g. \"108\"")
    tag = str(fw["tag"])
    if not re.fullmatch(r"[Vv]\d+", tag):
        raise PluginError(f"versions.yml: firmware.tag {tag!r} is not a release tag like V108")
    if tag[1:] != fw_version:
        raise PluginError(f"versions.yml: firmware.tag {tag} does not belong to firmware.version {fw_version}")
    for group in ("software", "models"):
        comps = data.get(group) or {}
        if not isinstance(comps, dict):
            raise PluginError(f"versions.yml: {group} is not a mapping")
        for key, comp in comps.items():
            missing = [f for f in ("name", "repository", "tag") if not (comp or {}).get(f)]
            if missing:
                raise PluginError(f"versions.yml: {group} {key!r} lacks {', '.join(missing)}")
    manuals = data.get("manuals")
    if not isinstance(manuals, dict) or not manuals:
        raise PluginError("versions.yml: no manuals")
    for key, doc in manuals.items():
        missing = [f for f in REQUIRED if not (doc or {}).get(f)]
        if missing:
            raise PluginError(f"versions.yml: manual {key!r} lacks {', '.join(missing)}")
        if not re.fullmatch(r"\d{4}\.[A-Z]", str(doc["revision"])):
            raise PluginError(f"versions.yml: manual {key!r} revision {doc['revision']!r} is not YEAR.LETTER, e.g. 2026.A")
        if doc["status"] not in ("draft", "published"):
            raise PluginError(f"versions.yml: manual {key!r} status {doc['status']!r} is not draft or published")
        published = doc.get("published")
        if doc["status"] == "published" and not isinstance(published, datetime.date):
            raise PluginError(f"versions.yml: manual {key!r} is published but has no publication date (YYYY-MM-DD)")
    return data


def meta_block(key: str, data: dict) -> str:
    """The version box of manual `key`."""
    doc = data["manuals"].get(key)
    if doc is None:
        raise PluginError(f"doc-meta: no manual {key!r} in versions.yml")
    product, fw = data["product"], data["firmware"]
    draft = doc["status"] == "draft"
    lines = [f"**Document number:** {doc['number']}",
             f"**{product['name']} release:** {data['docs_version']}"]
    if doc.get("firmware"):
        lines.append(f"**Firmware:** {fw['name']} {fw['version']}")
    lines.append(f"**Revision:** {doc['revision']}" + (" (draft)" if draft else ""))
    published = doc.get("published")
    lines.append(f"**Published:** {published.isoformat() if isinstance(published, datetime.date) else '—'}")
    applies = f"{product['name']} release {data['docs_version']}"
    if doc.get("applies_to"):
        applies += f" {doc['applies_to']}"
    if doc.get("firmware"):
        applies += f", {fw['name']} firmware {fw['version']}"
    lines.append(f"**Applies to:** {applies}")
    lines.append("*Original instructions*")
    return '<div class="doc-meta" markdown>\n\n' + "\n\n".join(lines) + "\n\n</div>"


def documents_table(data: dict) -> str:
    """Every document, with its number and what it covers."""
    product, fw = data["product"], data["firmware"]
    rows = [f"| {d['title']} | {d['number']} | {d['covers']} |" for d in data["manuals"].values()]
    return ("| Document | Number | Covers |\n|---|---|---|\n" + "\n".join(rows) + "\n\n"
            f"A document marked with a firmware release describes {product['name']} release {data['docs_version']} "
            f"running {fw['name']} firmware {fw['version']}. The version selector in the header switches between "
            "gripper releases; a new firmware release for the same gripper updates the pages in place. The "
            "compatibility table says which firmware, Python library and hardware revisions work together.")


def version_text(group: str, key: str, data: dict) -> str:
    """<!-- version: group.key -->: the component's tag without a leading v. Unknown keys stop the build."""
    comp = (data.get(group) or {}).get(key) if group in ("software", "models") else None
    if not comp:
        raise PluginError(f"versions.yml: no {group}.{key} for <!-- version: {group}.{key} -->")
    tag = str(comp["tag"])
    return tag[1:] if re.fullmatch(r"v\d.*", tag) else tag


def component(group: str, key, data: dict) -> dict:
    """firmware, or software.KEY / models.KEY. Unknown names stop the build."""
    if group == "firmware" and key is None:
        comp = data.get("firmware")
    elif group in ("software", "models") and key:
        comp = (data.get(group) or {}).get(key)
    else:
        comp = None
    if not comp or not comp.get("repository") or not comp.get("tag"):
        name = group + (f".{key}" if key else "")
        raise PluginError(f"versions.yml: no {name} with a repository and a tag for <!-- version-url/link: {name} -->")
    return comp


def version_url(kind: str, group: str, key, data: dict) -> str:
    """<!-- version-url: ... -->, <!-- version-release: ... --> and <!-- version-link: ... -->."""
    comp = component(group, key, data)
    repo, tag = str(comp["repository"]).rstrip("/"), str(comp["tag"])
    if kind == "release":
        return f"{repo}/releases/tag/{tag}"
    url = f"{repo}/tree/{tag}"
    if kind == "url":
        return url
    text = str(comp["version"]) if group == "firmware" else (tag[1:] if re.fullmatch(r"v\d.*", tag) else tag)
    released = comp.get("released")
    date = f" ({released.isoformat()})" if isinstance(released, datetime.date) else ""
    return f"[{text}]({url}){date}"


def on_config(config):
    global _facts
    _facts = load(Path(config.config_file_path).parent / "versions.yml")
    config.extra["docs_version"] = _facts["docs_version"]
    config.extra["firmware_version"] = str(_facts["firmware"]["version"])
    return config


def on_page_markdown(markdown, page, config, files):
    markdown = META_RE.sub(lambda m: meta_block(m.group(1), _facts), markdown)
    markdown = VERSION_RE.sub(lambda m: version_text(m.group(1), m.group(2), _facts), markdown)
    markdown = URL_RE.sub(lambda m: version_url(m.group(1), m.group(2), m.group(3), _facts), markdown)
    return TABLE_RE.sub(lambda m: documents_table(_facts), markdown)
