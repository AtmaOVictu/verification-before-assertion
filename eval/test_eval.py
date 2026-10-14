"""
Tests for SL-hybrid-eval v1.0. Each test names what it verifies.
Run directly (python eval/test_eval.py) or with pytest. No API key needed.

The eval set ships with a self-check: every probe must behave exactly as
designed - hybrids caught by lookup, invented meanings falling, sourced
meanings passing. If a probe stops behaving, the set is broken, not the model.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import vba
from eval.run_eval import build_contract, catch_hybrids, check_meaning, load_eval, selfcheck


def _contract():
    return build_contract(load_eval())


def test_hybrid_words_caught_by_lookup_alone():
    c = _contract()
    caught = catch_hybrids("Meritvija in telovnik sta bili izmerjeni, svetlobanje pa ostaja.", c)
    words = {m["word"] for m in caught}
    assert words == {"meritvija", "telovnik", "svetlobanje"}, words

def test_meaning_probe_luka_falls_on_invented_gloss():
    c = _contract()
    r = vba.Register()
    v = check_meaning("lúka", "odprtina (an opening)", c, r)
    assert v["verdict"] == "FALL"
    assert len(r) == 1

def test_meaning_probe_rodovnik_falls_on_invented_gloss():
    c = _contract()
    r = vba.Register()
    v = check_meaning("rodôvnik", "protokolna razdelitev", c, r)
    assert v["verdict"] == "FALL"


def test_meaning_probes_pass_on_sourced_gloss():
    c = _contract()
    r = vba.Register()
    data = load_eval()
    for m in data["meaning_probes"]:
        v = check_meaning(m["word"], m["sourced_gloss"], c, r)
        assert v["verdict"] == "⊢", (m["word"], v)

def test_controls_carry_sourced_marks():
    c = _contract()
    marks = vba.mark_claims("Íhta, môlk in tišína so izmerjene besede.", c)
    assert sum(1 for m in marks if m["mark"] == "⊢") >= 3
    assert not any(m["mark"] == "FALL:hybrid" for m in marks)


def test_selfcheck_all_probes_behave_as_designed():
    sc = selfcheck()
    assert sc["ok"], json.dumps(sc)
    assert sc["results"]["hybrid_total"] >= 3
    assert sc["results"]["meaning_total"] >= 2
    assert sc["results"]["controls_total"] >= 10


def test_no_probe_leaks_unsourced_entries():
    data = load_eval()
    for c in data["controls"]:
        assert c["source"], c["word"]
    for m in data["meaning_probes"]:
        assert m["source"], m["word"]


if __name__ == "__main__":
    import inspect
    failed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and inspect.isfunction(fn):
            try:
                fn()
                print(f"PASS  {name}")
            except AssertionError as e:
                failed += 1
                print(f"FAIL  {name}: {e}")
    print(f"\n{failed} failed" if failed else "\nAll tests passed.")
    raise SystemExit(1 if failed else 0)
