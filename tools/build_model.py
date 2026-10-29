#!/usr/bin/env python3
"""Build the turnable 3D model of the gripper (docs/assets/models/ssg48.glb) from the repository's URDF.

    python tools/build_model.py [--repo PATH] [--opening 0.5]

Reads SSG48_gripper_description/URDF/ssg48_gripper/urdf/par6_ssg48_urdf.urdf and its meshes from a clone of the
product repository (--repo, else $GRIPPER_REPO_DIR, else a sibling folder or ../../projects/<name>), places every
link's visual mesh with its joint and visual origins, opens the jaws to --opening of their travel (0 closed, 1 open),
colours the links as the URDF does but in the shop's grey and black, turns the model so the jaws point up (glTF is
Y-up), and writes a binary glTF that <model-viewer> shows on the landing page. Needs trimesh and numpy.
"""
from __future__ import annotations

import argparse
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
import trimesh
import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets" / "models" / "ssg48.glb"
URDF = Path("SSG48_gripper_description") / "URDF" / "ssg48_gripper" / "urdf" / "par6_ssg48_urdf.urdf"
MESHES = Path("SSG48_gripper_description") / "URDF" / "ssg48_gripper" / "meshes"
COLOURS = {"gripper": (0.82, 0.82, 0.80, 1.0), "jaw1": (0.10, 0.10, 0.10, 1.0), "jaw2": (0.10, 0.10, 0.10, 1.0)}


def find_repo(arg: str | None) -> Path:
    name = str(yaml.safe_load((ROOT / "versions.yml").read_text(encoding="utf-8"))["product"]["repository"]).rstrip("/").rsplit("/", 1)[-1]
    for c in (arg, os.environ.get("GRIPPER_REPO_DIR"), ROOT.parent / name, ROOT.parent.parent / "projects" / name):
        if c and (Path(c) / URDF).exists():
            return Path(c)
    sys.exit(f"build_model: no clone of {name} with {URDF} found; pass --repo PATH")


def origin_matrix(el) -> np.ndarray:
    """The 4x4 transform of a URDF <origin xyz rpy>."""
    if el is None:
        return np.eye(4)
    xyz = [float(v) for v in (el.get("xyz") or "0 0 0").split()]
    rpy = [float(v) for v in (el.get("rpy") or "0 0 0").split()]
    m = trimesh.transformations.euler_matrix(rpy[0], rpy[1], rpy[2], "sxyz")
    m[:3, 3] = xyz
    return m


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", help="the clone of the gripper repository")
    ap.add_argument("--opening", type=float, default=0.5, help="the jaws' opening, 0 closed to 1 open (default 0.5)")
    args = ap.parse_args(argv)
    repo = find_repo(args.repo)
    robot = ET.parse(repo / URDF).getroot()
    links = {l.get("name"): l for l in robot.findall("link")}
    joints = {j.find("child").get("link"): j for j in robot.findall("joint")}
    # the world transform of every link: the parent's, then the joint origin, then the joint motion
    world: dict[str, np.ndarray] = {}

    def transform(name: str) -> np.ndarray:
        if name in world:
            return world[name]
        j = joints.get(name)
        if j is None:
            world[name] = np.eye(4)
            return world[name]
        parent = transform(j.find("parent").get("link"))
        m = parent @ origin_matrix(j.find("origin"))
        if j.get("type") == "prismatic":
            axis = np.array([float(v) for v in (j.find("axis").get("xyz") if j.find("axis") is not None else "1 0 0").split()])
            lim = j.find("limit")
            lo, hi = float(lim.get("lower", 0)), float(lim.get("upper", 0))
            mimic = j.find("mimic")
            q = lo + (hi - lo) * args.opening
            if mimic is not None:   # the second jaw mirrors the first
                src = joints[[c for c, jj in joints.items() if jj.get("name") == mimic.get("joint")][0]]
                slo, shi = float(src.find("limit").get("lower", 0)), float(src.find("limit").get("upper", 0))
                q = (slo + (shi - slo) * args.opening) * float(mimic.get("multiplier", 1)) + float(mimic.get("offset", 0))
            slide = np.eye(4)
            slide[:3, 3] = axis * q
            m = m @ slide
        world[name] = m
        return m

    scene = trimesh.Scene()
    for name, link in links.items():
        visual = link.find("visual")
        if visual is None:
            continue
        mesh_el = visual.find("geometry/mesh")
        if mesh_el is None:          # a link without a mesh (a box, or an empty visual)
            continue
        mesh_file = repo / MESHES / Path(mesh_el.get("filename")).name
        mesh = trimesh.load(mesh_file, force="mesh")
        mesh.apply_transform(transform(name) @ origin_matrix(visual.find("origin")))
        rgba = COLOURS.get(name)
        if rgba is None:
            c = visual.find("material/color")
            rgba = tuple(float(v) for v in (c.get("rgba") if c is not None else "0.7 0.7 0.7 1").split())
        mesh.visual = trimesh.visual.TextureVisuals(material=trimesh.visual.material.PBRMaterial(
            baseColorFactor=[int(v * 255) for v in rgba], metallicFactor=0.0, roughnessFactor=0.65, doubleSided=True))
        scene.add_geometry(mesh, node_name=name, geom_name=name)
    # URDF Z-up with the jaws along -Z -> glTF Y-up with the jaws pointing up
    scene.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0]))
    scene.apply_translation(-scene.bounds.mean(axis=0))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    scene.export(OUT)
    ext = scene.extents * 1000
    print(f"wrote {OUT.relative_to(ROOT)}: {len(links)} links, {OUT.stat().st_size // 1024} KB, {ext[0]:.0f} x {ext[1]:.0f} x {ext[2]:.0f} mm")
    return 0


if __name__ == "__main__":
    sys.exit(main())
