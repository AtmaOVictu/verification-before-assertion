"""
Tests for the draft gate (preverba.py).
Each test names the fall class it guards — the same register entries
the gate was built from. No dependencies.

Run: python -m pytest test_preverba.py -v   (or: python test_preverba.py)
"""

import json

from preverba import findings_for, register_entry_count


def clean_fixture():
    """A synthetic clean draft, mirroring the sealed v1.9 structure."""
    draft = (
        "# Show HN — sealed draft v1.9\n"
        "\n"
        "> Sealed: 2026-10-14\n"
        "\n"
        "## Scars of v1.0–v1.8 (same day)\n"
        "\n"
        "The scar paragraphs count v1.0 through v1.8.\n"
        "Register: REGISTER-PADCEV.jsonl, entries 12 and 13.\n"
        "\n"
        "## Title (paste into \"title\")\n"
        "\n"
        "Show HN: A lexicon contract that makes an LLM mark its own inventions\n"
        "\n"
        "## Text (paste into \"text\")\n"
        "\n"
        "245 lines of dependency-free Python, 13 law-named unit tests "
        "plus a sealed-draft gate, CI.\n"
        "Four live runs on mistral-large-latest now.\n"
        "Register: REGISTER-PADCEV.jsonl, entry 24.\n"
        "\n"
        "⊢ sourced claims: 9→41, 9→36, 10→40, 9→43 (replicates) · "
        "⚠ open: 12→16, 13→15, 13→15, 12→15 (stays honest) · "
        "hybrids caught: 0→10, 0→1, 0→0, 0→0 (I publish the noise)\n"
    )
    vba_source = "x = 1\n" * 245
    law_test_source = "\n".join(f"def test_{i}(): pass" for i in range(13)) + "\n"
    register_text = "\n".join(
        json.dumps({"entry": i}) for i in range(1, 25)) + "\n"
    return draft, vba_source, law_test_source, register_text


def findings_for_fixture(fixture):
    draft, vba_source, law_test_source, register_text = fixture
    return findings_for(draft, vba_source, law_test_source, register_text)


# The clean draft: 0 findings (no present problem)

def test_clean_draft_passes_the_gate():
    assert findings_for_fixture(clean_fixture()) == []


# The fall of entry 14: a title sealed longer than the medium's limit

def test_title_over_80_is_caught():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    draft = draft.replace(
        "Show HN: A lexicon contract that makes an LLM mark its own inventions",
        "Show HN: " + "x" * 100)
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert any("title measures" in f for f in findings)


# The entry-18 class: a spoken count that the pairs contradict

def test_live_run_count_mismatch_is_caught():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    draft = draft.replace("0→10, 0→1, 0→0, 0→0", "0→10, 0→1, 0→0")
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert any("live runs" in f for f in findings)


# The fall of entry 13: a line count spoken without counting

def test_vba_line_count_stale_is_caught():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    vba_source = "x = 1\n" * 246
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert any("vba.py measures" in f for f in findings)


# The entry-24 class: a test count spoken without its scope

def test_law_test_count_stale_is_caught():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    law_test_source = "\n".join(
        f"def test_{i}(): pass" for i in range(12)) + "\n"
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert any("law-named" in f for f in findings)


# The heading falls of entries 19–22: a heading that undercounts its block

def test_scar_heading_undercount_is_caught():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    draft = draft.replace("## Scars of v1.0–v1.8", "## Scars of v1.0–v1.7")
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert any("scar heading stops" in f for f in findings)


# A citation that does not resolve against the register's body

def test_register_citation_stale_is_caught():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    register_text = "\n".join(
        json.dumps({"entry": i}) for i in range(1, 21)) + "\n"
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert any("register carries" in f for f in findings)


# The scar block quotes the falls' own words — history, not a claim
# (found on the gate itself at v1.9: the first cut flagged its own
# scar block's quoted history as a present claim)

def test_quoted_history_in_scars_is_not_a_present_claim():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    draft = draft.replace(
        "The scar paragraphs count v1.0 through v1.8.",
        'The v1.1 draft once spoke "~500 lines of dependency-free '
        'Python" and "three live runs" without counting — quoted '
        'history, not a present claim.')
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert findings == []


# A mask that cannot tell speech from claim must say so

def test_quote_imbalance_is_named_not_masked():
    draft, vba_source, law_test_source, register_text = clean_fixture()
    draft = draft.replace("Four live runs", 'Four "unclosed live runs')
    findings = findings_for(draft, vba_source, law_test_source, register_text)
    assert any("quote balance" in f for f in findings)


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
