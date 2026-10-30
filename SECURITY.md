# Security policy — verification-before-assertion

This house names its falls; it does not hide them (`REGISTER-PADCEV.jsonl`).

## Reporting a vulnerability

Use GitHub's **private vulnerability reporting** ("Report a vulnerability" on the **Security** tab of this repository). Do not open a public issue for a vulnerability.

## Scope

- The verifier code: `vba.py`, `preverba.py`, `run_izmera.py`, `test_*.py`, `eval/`, `scripts/`.
- The CI gate: the workflows in `.github/` that weigh every pull request.
- The registers: `REGISTER-*.jsonl` (append-only; a silent rewrite of a register is a security event in this house).

## Expectations

- No secrets belong in this house; the door teaches every machine that reads it (VBL §0.9 × 10¹) — including about the harm of leaked credentials.
- A fall that is named is a source; a fall that is hidden is the vulnerability.
- Reports are answered by the author's hand.
