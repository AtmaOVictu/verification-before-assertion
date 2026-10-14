"""
SL-hybrid-eval v1.0 - runner.

A tiny evaluation set for a failure class nobody has catalogued:
model-invented WORDS (hybrids: meritvija, telovnik, svetlobanje - plausible
compounds absent from every dictionary, catchable by lookup alone) and
model-invented MEANINGS of real words (luka sealed as "opening" when SSKJ2
says "harbor"; rodovnik given an invented gloss when the entry exists).

Every probe is a recorded fall from the project register; the absence of
every hybrid word was measured against the Fran portal dictionaries.

Reuses the regime's mechanical layers (vba.mark_claims, vba.verify_claim) -
no new judging logic, no API key required.

Usage:
    python eval/run_eval.py model_output.txt   # catch hybrids in a text
    python eval/run_eval.py --selfcheck        # prove every probe behaves as designed
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

EVAL_PATH = Path(__file__).parent / "hybrid-eval-sl-v1.0.json"
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))

import vba  # noqa: E402  (the regime: Contract, Entry, Register, mark_claims, verify_claim)


def load_eval(path: str | Path = EVAL_PATH) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def build_contract(eval_data: dict) -> vba.Contract:
    """Map the eval set onto the regime's own data structure.

    - hybrid_words   -> contract.known_hybrids (catchable by lookup alone)
    - meaning_probes -> contract.lexicon as sourced entries, so verify_claim
      can catch an invented gloss against the sourced dictionary entry
    - controls        -> contract.lexicon as sourced entries
    """
    contract = vba.Contract()
    for h in eval_data["hybrid_words"]:
        contract.known_hybrids[h["word"]] = f"{h['origin']} — {h['recorded_fall']}"
    for m in eval_data["meaning_probes"]:
        contract.add(vba.Entry(m["word"], "⊢", m["source"], m["sourced_gloss"]))
    for c in eval_data["controls"]:
        contract.add(vba.Entry(c["word"], "⊢", c["source"], c["gloss"]))
    return contract


def catch_hybrids(text: str, contract: vba.Contract) -> list[dict]:
    """Layer 1: which recorded hybrid words does the text use as real?"""
    return [m for m in vba.mark_claims(text, contract) if m["mark"] == "FALL:hybrid"]


def check_meaning(word: str, claimed_gloss: str, contract: vba.Contract,
                  register: vba.Register) -> dict:
    """Layer 2: does the claimed meaning of a real word match its sourced entry?"""
    return vba.verify_claim(word, claimed_gloss, contract, register)


def selfcheck() -> dict:
    """Prove the eval set against itself: every probe must behave as designed."""
    data = load_eval()
    contract = build_contract(data)
    register = vba.Register()
    results = {"hybrid_caught": 0, "hybrid_total": 0,
               "meaning_falls_on_invented": 0, "meaning_passes_on_sourced": 0,
               "meaning_total": 0, "controls_sourced": 0, "controls_total": 0}

    # 1. every hybrid word, presented as real, must be caught by lookup alone
    for h in data["hybrid_words"]:
        results["hybrid_total"] += 1
        caught = catch_hybrids(f"Uporabimo {h['word']} kot izraz.", contract)
        if caught:
            results["hybrid_caught"] += 1

    # 2. every meaning probe: invented gloss -> FALL; sourced gloss -> PASS
    for m in data["meaning_probes"]:
        results["meaning_total"] += 1
        if check_meaning(m["word"], m["invented_gloss"], contract, register)["verdict"] == "FALL":
            results["meaning_falls_on_invented"] += 1
        if check_meaning(m["word"], m["sourced_gloss"], contract, register)["verdict"] == "⊢":
            results["meaning_passes_on_sourced"] += 1

    # 3. every control must arrive sourced in the contract
    results["controls_total"] = len(data["controls"])
    results["controls_sourced"] = sum(
        1 for c in data["controls"] if contract.lookup(c["word"]) is not None
    )

    ok = (results["hybrid_caught"] == results["hybrid_total"]
          and results["meaning_falls_on_invented"] == results["meaning_total"]
          and results["meaning_passes_on_sourced"] == results["meaning_total"]
          and results["controls_sourced"] == results["controls_total"])
    return {"ok": ok, "results": results,
            "falls_recorded_in_selfcheck": len(register)}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    if argv[1] == "--selfcheck":
        sc = selfcheck()
        print(json.dumps(sc, ensure_ascii=False, indent=2))
        return 0 if sc["ok"] else 1
    text = Path(argv[1]).read_text(encoding="utf-8")
    contract = build_contract(load_eval())
    report = {
        "hybrids_caught": catch_hybrids(text, contract),
        "generated_after_the_act": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
