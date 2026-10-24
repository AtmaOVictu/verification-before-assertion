#!/usr/bin/env python3
"""LICENSE-MANIFEST — generator in sodba (VBL §0a: identifikacija; §12: TRANSPORT meri hash).

Zagon brez argumentov izpise svež manifest; --check sodi prijavljeni manifest proti telesom
in vrne 1 ob odmiku (rdeca prica v CI). Odvisnosti: nobene (hišni zakon)."""

import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "LICENSE-MANIFEST.json")
COVERED = ["LICENSE.md", "REGISTER-NEIMENOVANIH.jsonl", "REGISTER-PADCEV.jsonl"]


def entry(rel_path):
    with open(os.path.join(ROOT, rel_path), "rb") as f:
        data = f.read()
    return {"path": rel_path, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def generate():
    return {
        "license": "VBL — Verification Before Assertion License",
        "version": "10.0.0",
        "law": "identification by manifest: VBL §0a; transport measured by SHA-256: VBL §12",
        "items": [entry(p) for p in COVERED if os.path.exists(os.path.join(ROOT, p))],
    }


def check():
    if not os.path.exists(MANIFEST):
        print("MANIFEST-ODMIK: LICENSE-MANIFEST.json manjka (VBL §0a — identifikacija brez prijave)")
        return 1
    with open(MANIFEST, encoding="utf-8") as f:
        current = json.load(f)
    fresh = generate()
    if current.get("items") != fresh["items"]:
        print("MANIFEST-ODMIK: telesi se ne ujemata s prijavljenim manifestom (VBL §0a/§12)")
        for a in current.get("items", []):
            for b in fresh["items"]:
                if a.get("path") == b.get("path") and a != b:
                    print("  ", a.get("path"),
                          "manifest:", str(a.get("sha256"))[:12],
                          "telesi:", str(b.get("sha256"))[:12])
        return 1
    print("MANIFEST-DRZI (VBL §0a):", ", ".join(i["path"] for i in fresh["items"]))
    return 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    print(json.dumps(generate(), ensure_ascii=False, indent=2))
