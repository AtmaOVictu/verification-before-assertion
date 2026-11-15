#!/usr/bin/env python3
"""LICENSE-MANIFEST — generator in sodba (VBL §0a: identifikacija; §12: TRANSPORT meri hash).

Zagon brez argumentov izpise svež manifest; --check sodi prijavljeni manifest proti telesom
in vrne 1 ob odmiku (rdeca prica v CI). Odvisnosti: nobene (hišni zakon).

Sanacija FAIL #2 (PAR.23 @licenca-vbl): različica se IZMERI iz telesa LICENSE.md (⟨NE-UGIBAJ⟩);
prej trdo zapisana 0.1210 × 10⁴ — brazgotina ostaja (KORENINA 0.2).

Kura T-23 (K-15, 15. 11. 2026): COVERED razširjen na telesi 0.1540 ⊙ ⟨MANIFEST-EN-DIH-PO-ROJSTVU⟩
(prelom pri rojstvih #48–#51: objava je tekla brez obnove manifesta; brazgotina ostaja).
"""

import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "LICENSE-MANIFEST.json")
LICENSE = os.path.join(ROOT, "LICENSE.md")
COVERED = ["LICENSE.md", "REGISTER-NEIMENOVANIH.jsonl", "REGISTER-PADCEV.jsonl",
          "VBL-0.1540-POPRAVLJALNI-STANDARD.md", "VBL-0.1540-REGISTER-KONTROL.json"]
SCAR = ("SANACIJA FAIL #2 (PAR.23 @licenca-vbl, 14. 11. 2026): version je prej bila trdo "
        "zapisana 0.1210 × 10⁴, dve rojstvi za telesi — sedaj izmerjena iz telesa "
        "LICENSE.md ⊙ ⟨NE-UGIBAJ⟩ (brazgotina ostaja ⊙ KORENINA 0.2)")


def license_version():
    """Izmeri različico iz glave telesa LICENSE.md — padec brez vrstice je sodba, ⟨ne⟩ ugibanje."""
    with open(LICENSE, encoding="utf-8") as f:
        head = f.read(4096)
    m = re.search(r"^Version (0\.\d{4}) × 10⁴", head, re.MULTILINE)
    if not m:
        print("LICENCA-NI-IZMERJENA: v glavi LICENSE.md ni vrstice »Version 0.NNNN × 10⁴« (⟨NE-UGIBAJ⟩)")
        sys.exit(1)
    return m.group(1) + " × 10⁴"


def entry(rel_path):
    with open(os.path.join(ROOT, rel_path), "rb") as f:
        data = f.read()
    return {"path": rel_path, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def generate():
    return {
        "license": "VBL — Verification Before Assertion License",
        "version": license_version(),
        "law": "identification by manifest: VBL §0a; transport measured by SHA-256: VBL §0.12",
        "scar": SCAR,
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
