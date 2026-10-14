"""
preverba.py — the draft gate: the register's promises as code.

The sealed outreach draft is a body of claims. Until this gate existed,
every one of those claims was checked by hand — and the register
carries the falls that walked through (entries 13, 14, 18, 19–22, 24,
25): numbers spoken without counting, a title sealed longer than the
medium's own limit, a heading that undercounted its own block. This
file turns those promises into code: it verifies the sealed draft
against the medium it is sealed for and against the repository's own
measured bodies.

Two layers learned on the gate itself:

One — quoted speech is history, a report of a claim (L4), and history
is verified against the archive that carries it, not against present
bodies. The gate scans unquoted speech for present claims; and the
exemption is itself verified: every number-bearing quote must live in
a paragraph that names its register witness (the citation resolves
separately), and no number-bearing quote may stand in the paste body —
history does not belong in what you post. An unbalanced quote is
named, not masked, because a mask that cannot tell speech from claim
must say so.

The gate verifies claims, not bytes; the hand still verifies meaning
(L2). Counting is lookup, not judgment.

Run: python preverba.py   (exit 1 if the sealed draft is stale)
No dependencies.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

RUN_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
}

# a number inside a quoted span: a digit, or a small counting word —
# the marks of a fall's own words quoted as history
QUOTE_NUMBER_RE = re.compile(
    r"\d+|\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven"
    r"|twelve|thirteen|fourteen|fifteen|twenty|hundred|thousand|million"
    r")\b", re.IGNORECASE)


def register_entry_count(register_text: str) -> int:
    """Entries = the register's non-empty lines (append-only body)."""
    return len([line for line in register_text.splitlines() if line.strip()])


def mask_quoted(text: str) -> str:
    """Mask characters inside double-quoted spans (newlines kept).

    Quoted speech is history — a report of a claim (L4), verified
    against the register, not against present bodies. Everything
    unquoted is what the draft speaks as present truth. The exemption
    itself is verified: see checks (g) and (h).
    """
    chars: list[str] = []
    inside = False
    for ch in text:
        if ch == '"':
            inside = not inside
            chars.append('"')
        elif inside and ch != "\n":
            chars.append(" ")
        else:
            chars.append(ch)
    return "".join(chars)


def findings_for(draft: str, vba_source: str, law_test_source: str,
                 register_text: str) -> list[str]:
    """Check the sealed draft against the medium and the measured bodies.

    Returns a list of findings; an empty list means the draft is
    consistent with everything the repository can measure.
    """
    findings: list[str] = []

    # A mask that cannot tell speech from claim must say so — an
    # unbalanced quote is named, never silently masked.
    if draft.count('"') % 2 != 0:
        findings.append("quote balance: the draft carries an odd number "
                        "of double quotes — the gate cannot tell "
                        "quoted history from present claim")

    claims = mask_quoted(draft)

    # (a) the medium's hard limit — the HN title field truncates at 80
    # (the fall of entry 14, measured before the seal since v1.3)
    # Scanned on the raw draft: the heading itself carries quotes.
    m = re.search(r'## Title \(paste into "title"\)\n\n(.+)', draft)
    if m is None:
        findings.append('title measures: no "## Title" block found '
                         "in the draft")
    else:
        title = m.group(1).split("\n")[0]
        if len(title) > 80:
            findings.append(f"title measures: {len(title)} characters — "
                            "the medium truncates at 80")

    # (b) the spoken live-run count vs the pairs carried per metric
    # (the entry-18 class: a countable falsehood)
    m = re.search(r"\b([Oo]ne|[Tt]wo|[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix"
                  r"|[Ss]even|[Ee]ight|[Nn]ine|[Tt]en) live runs\b", claims)
    if m:
        claimed_runs = RUN_WORDS[m.group(1).lower()]
        results_line = None
        for line in claims.splitlines():
            if line.startswith("⊢ sourced claims:"):
                results_line = line
                break
        if results_line is None:
            findings.append("live runs: the draft speaks live runs but "
                            "carries no '⊢ sourced claims:' line")
        else:
            for group in results_line.split("·"):
                pairs = group.count("→")
                if pairs and pairs != claimed_runs:
                    metric = group.split(":")[0].strip()
                    findings.append(f"live runs: the draft speaks "
                                    f"{claimed_runs} live runs but the "
                                    f"'{metric}' metric carries {pairs} "
                                    "pairs")

    # (c) the spoken vba.py line count vs the file's own body
    # (the fall of entry 13: a number spoken without counting)
    m = re.search(r"(\d+) lines of dependency-free Python", claims)
    if m:
        counted = len(vba_source.splitlines())
        if int(m.group(1)) != counted:
            findings.append(f"vba.py measures: draft speaks {m.group(1)} "
                            f"lines, the body carries {counted}")

    # (d) the spoken law-named unit test count vs test_vba.py
    # (the entry-24 class: a number spoken without its scope)
    m = re.search(r"(\d+) law-named unit tests", claims)
    if m:
        counted = len(re.findall(r"def test_", law_test_source))
        if int(m.group(1)) != counted:
            findings.append(f"law-named unit tests: draft speaks "
                            f"{m.group(1)}, test_vba.py carries {counted}")

    # (e) the scar heading counts its own block: v1.0–v1.(N-1)
    # (the heading falls of entries 19–22, ended)
    m_head = re.search(r"# Show HN — sealed draft v1\.(\d+)", claims)
    m_scar = re.search(r"## Scars of v1\.0–v1\.(\d+) ", claims)
    if m_head and m_scar:
        if int(m_scar.group(1)) != int(m_head.group(1)) - 1:
            findings.append(f"scar heading stops: the heading carries "
                            f"v1.0–v1.{m_scar.group(1)} while the header "
                            f"seals v1.{m_head.group(1)} — one short of "
                            "its own block")

    # (f) every register citation resolves against the register's body
    total = register_entry_count(register_text)
    for m in re.finditer(r"\b(?:entries|entry)\s+"
                         r"((?:\d+(?:\s*(?:,|and|–)\s*\d+)*))",
                         claims):
        cited = max(int(n) for n in re.findall(r"\d+", m.group(1)))
        if cited > total:
            findings.append(f"register carries: the draft cites entry "
                            f"{cited} but the register carries {total} "
                            "entries")

    # (g) quoted history names its witness: every number-bearing
    # double-quoted span lives in a paragraph that cites the register
    # (the entry-25 class: the exemption is verified, not trusted)
    for para in draft.split("\n\n"):
        spans = re.findall(r'"([^"]*)"', para)
        if any(QUOTE_NUMBER_RE.search(s) for s in spans) and \
                not re.search(r"\b(?:entries|entry)\s+\d+", para):
            findings.append("quoted history names no witness: a paragraph "
                            "quotes number-bearing history but carries no "
                            "register citation — an exemption is valid "
                            "only as scoping, never as silence")

    # (h) no number-bearing quote stands in the paste body —
    # history does not belong in what you post (the entry-25 class:
    # the mask's back door, closed)
    m_body = re.search(r'## Text \(paste into "text"\)\n\n(.+?)'
                       r"(?:\n\n---\n|\Z)", draft, re.DOTALL)
    if m_body:
        for span in re.findall(r'"([^"]*)"', m_body.group(1)):
            if QUOTE_NUMBER_RE.search(span):
                findings.append(f"quote in the paste body: history does "
                                f"not belong in what you post — the "
                                f"number-bearing quote '{span[:40]}' "
                                "stands where only present claims may")

    return findings


def main() -> int:
    draft = (ROOT / "outreach" / "show-hn-v1.0.md").read_text(encoding="utf-8")
    vba = (ROOT / "vba.py").read_text(encoding="utf-8")
    law = (ROOT / "test_vba.py").read_text(encoding="utf-8")
    register = (ROOT / "REGISTER-PADCEV.jsonl").read_text(encoding="utf-8")

    findings = findings_for(draft, vba, law, register)
    if findings:
        print("DRAFT GATE: FAIL — the sealed draft is stale against "
              "the repository's measured bodies:")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("DRAFT GATE: PASS — the sealed draft matches the medium and "
          "the repository's measured bodies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
