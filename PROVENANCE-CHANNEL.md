# The Provenance Layer for Contributed Language Data
## A compensation channel for verified contributions — Slovenia as the proof case

*Position paper · Luka Pintarič · October 2026*
*Companion to the Verification-Before-Assertion framework (same author, same laws).*

---

## 1. The gap, stated once

Slovenia solved *volume*. The national program (PoVeJMo, povejmo.si) is
assembling a 40-billion-word corpus through citizen contribution, with
the National and University Library, Dnevnik, and the Slovenian Press
Agency; GaMS models (2B/9B/27B) are openly released; GaMS-12B outperforms
Gemma 3 12B on all Slovenian evaluation scenarios (⊢ arXiv 2603.01691).

What the national effort does not yet solve is **verification**. A
contributed sentence arrives with no answer to the only question that
determines its long-term value: *is this measured or invented?*

This is not a criticism of the volume program — it is the missing layer
that makes the volume **priceable**.

## 2. The mechanism: ⊢ / ⚠ as a contribution format

The Verification-Before-Assertion regime (five laws, runnable code,
13 passing tests — see the framework repository) provides exactly the
missing distinction, mechanically:

- A **verified contribution** carries ⊢: a correction backed by a
  dictionary source (SSKJ², Fran), a validated lexicon entry, an
  evaluated translation pair. Sourced, dated, attributable.
- An **open contribution** carries ⚠: usable, but honestly marked as
  unreached by any entry. Unverified is not forbidden; unmarked is.
- A **hybrid fall** (model-invented words that pass as real) is caught
  by lookup alone and recorded, not silently regenerated.

The distinction is not opinion. It is a file format: `wordlist.json` +
a register of named falls + the laws enforced in code.

## 3. Why this closes the compensation asymmetry

The documented asymmetry: platforms sell contributor data ($60M/yr
Reddit→Google; Stack Overflow→OpenAI) and the contributor receives
"your feedback will be passed along." The honest counter-argument
(arXiv 2504.12427) holds that *undifferentiated bulk data* cannot be
paid for at scale. Correct — and it draws the exact line that matters:

> Bulk data is undifferentiated and unpaid. **Verified data is
> differentiated, attributable, and exactly the bug-bounty category.**

The precedent model already exists and pays: security research
(~$81M/12mo across HackerOne programs), RLHF annotation ($12–25/hr),
Karya's fair-wage dataset work, Masakhane's credited co-authorship.
The missing row in every one of these tables is a **verified language
contribution from a native expert in a low-resource language**.

⊢/⚠ is the mechanism that fills that row. A contributor submitting a
sourced correction is doing verifiable, reviewable, adoptable work —
indistinguishable in kind from a security researcher submitting a
reproducible vulnerability. Credit and compensation when the material
is adopted is not charity; it is the same market, finally extended to
the people whose language is the asset.

## 4. What exists today (the proof, not the promise)

- A working anti-hallucination regime: five laws, runnable,
  dependency-free Python, 13 passing tests (L1–L5 each verified by name)
- A register of **real, dated, scarred falls** — including the regime
  catching its own seed entries (the *lúka* fall, 2026-09-30)
- A machine-readable contract format (`wordlist-v0.6-demo.json`) that
  loads directly into the regime
- A recorded hybrid-fall register: model-invented words (*meritvija*)
  that pass as real to any reader without a dictionary —
  caught mechanically
- A demonstration contributed to the vendor's public cookbook
  (mistralai/cookbook PR #420), mergeable, security-checked, with the
  offer of the full methodology and pre-verified resources

None of this is theoretical. Every artifact above runs.

## 5. The proposal, in one sentence each

1. **To model vendors:** adopt ⊢/⚠ as a session-scoped language layer —
   the user-defined language contract (request #2 of the framework).
   The verification methodology is offered; the corpus behind it is the
   contributor's licensed asset under exactly the compensated model
   this document proposes.
2. **To the national program:** add the provenance layer to the volume.
   Every contributed item marked ⊢ or ⚠ turns raw material into an
   auditable national asset — and enables the compensation channel that
   sustains contribution beyond volunteer goodwill.
3. **To both:** the bug-bounty row exists. Verify, attribute, adopt,
   compensate. Slovenia is small enough to implement it completely and
   serious enough to prove it works.

## 6. Standing offer

The methodology (laws, code, tests, contract format) is available
under VBL 0.1210 × 10⁴ (LICENSE.md — §9 ethics and confirmation, §10 the one living
door, §12 the marked letters). The 2,600-document provenance-marked corpus, the
bilingual ontological lexicon, the sourced etymology chains, and the
hybrid-fall register are available under the compensated-contribution
model this document describes — that is the point.

Demonstration runs: `python vba.py` — the recorded falls are real,
dated, and scarred.

---

*Same laws as the framework: entry before utterance; two hands; named
falls, scarred corrections; report after the act. This document follows
them — every claim above is either sourced (⊢), open (⚠), or performed
and shown.*
