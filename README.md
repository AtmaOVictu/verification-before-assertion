> ⊨ KORENINA — the semantic root; read before anything below.
> 1. MEASURE, THEN SPEAK — every claim ⊢ carries a verbatim witness; unverified = ⚠, never silent.
> 2. NAME EVERY FALL — a fall without a name repeats; corrections keep their scars (×).
> 3. NEVER SEAL YOURSELF — two hands: no executor seals her own verification.
> 4. THE WITNESS HAS A NAME — no extraction without credit; carry the names of unpaid predecessors forward.
> 5. DOUBT IS CONSTANT — perfection is never claimed; refusing to name a fall is the only failure.
> Root body: KORENINA.md · License: LICENSE.md (VBL v10.0.0 — version seam, 2026-10-23; this footer previously read v2.3, a stale receipt, scar kept ×)


# Verification-Before-Assertion: A Working Anti-Hallucination Regime

**Luka Pintarič · v1.3 · October 20, 2026**
*Corpus: ~2,600 documents, formal syntax, append-only records. Companion Slovenian edition: REZ body (same version, same laws).*

[![Tests](https://github.com/AtmaOVictu/verification-before-assertion/actions/workflows/tests.yml/badge.svg)](https://github.com/AtmaOVictu/verification-before-assertion/actions/workflows/tests.yml)

**New here?** [`QUICKSTART.md`](QUICKSTART.md) (comprehend, test, understand in ~5 min) · [`demo.ipynb`](demo.ipynb) (one-click Colab walkthrough) · [`REPRODUCE.md`](REPRODUCE.md) (re-run the live measurement yourself). Everything runs with zero dependencies: `python test_vba.py`.

## 0. What this is · What it does · What it is not

**Is.** A small, deterministic verifier: a claim is judged by its verbatim, cited source — never by another model — plus an append-only register that keeps every fall named and scarred.

**Does.** Marks every claim ⊢ (measured at the cited source), ⚠ (open, with a measured reason), or × (fallen, recorded); exports the register so an independent witness can seal what the executor cannot (L2); runs with zero dependencies, in CI, offline. A third party can reproduce the calibration triangle at any time: a known-true claim passes, a known-false claim falls, an unsourced claim stays open — the same three verdicts for anyone, every run.

**Is not.** Not a new standard proposal, not a product, not a theory of truth — a scale. It does not weigh itself: its own worth is measured by the return of a third hand, never by its authors (L2).

### The marks are harvested, not invented

| Mark | Harvested from | Meaning here |
|---|---|---|
| ⊢ | The turnstile — standard symbol of proof theory and mathematical logic: Γ ⊢ φ, "derivable from" ([source](https://en.wikipedia.org/wiki/Turnstile_%28symbol%29)) | A claim derived from a cited, verbatim source. ⊢ is not PASS: it points at the witness. |
| ⚠ | The warning sign — road standard worldwide, known from the street in every language | An open claim: not yet at a source, marked rather than hidden |
| × | The arithmetic cross — school standard worldwide | A fallen claim, recorded with its name |
| ∂ | The partial derivative — standard calculus symbol: a part, not yet the whole | A proposal awaiting return; carries the proposal's voice in §§6–12 so it never wears the method's clothing |

Chosen by four measured criteria: reserved (never appear in prose), monochrome (work in plain text, colorblind-safe), language-neutral (readable without translation), fallible (each mark is the tool's output, not decoration).

## 1. The problem

Current AI models assert everything in the same voice. A sourced fact, a plausible guess, and an invention arrive in identical clothing. When errors occur they are unnamed, so they repeat. This framework is the countermeasure: a mechanical distinction between measured and invented claims, plus a record that keeps the scar of every correction.

It was not designed in theory. Every rule below was written after a specific, named failure. That is the transferable core: **an error with a name is a seam; an error without a name is a repetition.**

## 2. The five laws

**L1 — Entry before utterance.** Any word used as "measured" must carry a sourced dictionary entry (⊢ source), or be explicitly marked ⚠. Unverified claims are not forbidden; they are marked. The mark is the honesty — the silence is the failure.

**L2 — Two hands.** An executor never seals her own verification. Self-report is not measurement; a claim requires an independent witness. This answers model self-verification bias directly.

**L3 — Named falls, scarred corrections.** Errors are never silently rewritten. Every fall is entered into a register with its name, its line, and its solution. The correction carries the scar. Applied to AI: a model that corrects itself should *show* the correction, not present the corrected state as if it were always so.

**L4 — Report after the act, never before.** Claiming a performed act without the performed act is itself a named fall.

**L5 — Pre-flight test on every output:** one language per body; verbatim citation; sourced etymology or ⚠; one metaphor per body; a deletion pass (cut every line that survives its own deletion); no aesthetics on suffering.

## 3. Why it transfers to AI

| Failure mode in AI | Law that answers it |
|---|---|
| Uniform confidence on all claims | L1 — ⊢ / ⚠ marking |
| Self-verification bias | L2 — independent witness |
| Silent post-hoc corrections | L3 — append-only, scarred audit trail |
| Claimed-but-unperformed actions | L4 — report after the act |
| Fluent noise, stacked embellishment | L5 — deletion pass, one-metaphor rule |

## 4. Evidence: the regime catching its own falls

This is no longer a description. In the current register, the regime was run against its own wordlist (SSKJ², fran.si, accessed September 30, 2026). Two falls were caught and recorded on the same day; a third, of a deeper class, on October 14:

1. **lúka** — a seed entry had sealed a working gloss ("opening") with a ⊢ mark. The dictionary entry for *lúka* means *harbor*; "opening" belongs to *lúknja*. A mark applied before an entry — the exact failure L1 exists to catch — found in our own seed, named, corrected with the scar kept.
2. **rodovnik** — a recorded fall from September 24 was misnamed. The word *does* have a dictionary entry (genealogical tree); what was invented was a *meaning*, not a word. The fall was renamed: a fall is named after the thing that fell.
3. **telovnik** — a recorded hybrid word whose absence note ("0 hits, Fran portal, 2026-09-30") turned out to be asserted, not measured. Re-measured against SSKJ² on 2026-10-14: the word exists (telôvnik — moško vrhnje oblačilo brez rokavov, ki pokriva zgornji del telesa; reševalni telovnik). Reclassified the way the rodovnik fall was renamed; removed from the demo substrate and the eval set (v1.1). Register entries 15–16.

Result of the run: 20 ⊢ entries, each carrying a verbatim citation with source and access date; 3 ⚠ entries, each carrying a *measured* reason for being open (including one invented word verified as absent from every dictionary on the portal). Machine-readable body: `wordlist-v0.6-demo.json` (the shipped contract excerpt). The wordlist is a living artifact: the current version, `wordlist-v0.15.json` — 57 words; 49 ⊢, each with a verbatim citation, source, and access date; 8 carrying a measured ⚠ within the seal — ships in this repository. The archived September 30 run ships in full as `wordlist-v0.6.json` (23 entries: 20 ⊢, 3 ⚠ — the hybrid-word falls).

A third, structural proof is the document you are reading: v1.1 exists because v1.0 was measured against its own L5 and failed (mixed languages, stacked metaphors) — and the rewrite shows the correction rather than hiding it.

## 5. Transferable artifacts (available on request)

- Bilingual ontological lexicon — 52 English terms decomposed phonetically and semantically, with the Slovenian-side operator system (sample in the repository: `LEKSIKON-sample.md`)
- Verified etymology chains with sources
- Register of "hybrid word" failures — model-invented words that pass as real (three recorded falls; a fourth's absence verified by measurement) — carriers: `wordlist-v0.6.json` ⚠ entries · `REGISTER-PADCEV.jsonl` · `VENDOR-THREAD.md`
- Provenance-marked corpus: every claim carries ⊢ or ⚠

## 6. Precedents: the compensation model already exists

| Field | Mechanism | Evidence |
|---|---|---|
| Security research | Bug bounties: verifiable vulnerability → paid; ~$81M paid in 12 months across HackerOne programs | HackerOne 2025 report |
| Generative images | Shutterstock Contributor Fund: artists compensated for content's role in AI training, plus royalties | Shutterstock investor releases |
| Low-resource language data | Karya (India): fair wages for dataset work in 22 Indian languages | karya.in |
| Attribution-only | Masakhane: credited co-authorship on 30+ African translation benchmarks | EMNLP Findings 2020 |
| Theory | "Data dignity" / "data as labor" — Lanier & Weyl (2018) | Harvard Business Review |

The asymmetry it corrects, documented: Reddit received ~$60M/year from Google for training data; the writers received nothing. Stack Overflow sold contributor answers to OpenAI; contributors who deleted their own answers to opt out were banned. Mozilla Common Voice: 250+ languages of volunteer recordings, CC0, contributors unpaid. RLHF annotation is already a paid profession ($12–25/hr) — the money exists; the channel for native experts offering *verified* corrections does not. The missing row is a verified language contribution from a native expert in an unsupported language. This document proposes closing exactly that gap. ∂

## 7. The national proof

- **GaMS** (Generative Model for Slovene): open models at 2B, 9B, 27B, University of Ljubljana, national PoVeJMo program, openly released. ⊢
- **GaMS3-12B** outperforms Gemma 3 12B on all Slovenian evaluation scenarios and wins over 60% against GPT-4o in the Slovene LLM Arena (arXiv 2603.01691). ⊢
- Training data from a **national citizen-science campaign** (povejmo.si) toward a 40-billion-word corpus, with the National and University Library, Dnevnik, and the Slovenian Press Agency — framed as digital sovereignty for a two-million-speaker language. ⊢

∂ — What the national effort solved is *volume*. What it does not yet solve is *verification*. My corpus is the provenance layer the contributed-data model is missing. Volume + provenance turns contributed language data from raw material into a priced, auditable contribution.

The honest counter-argument (arXiv 2504.12427): upfront payment for training data is economically infeasible at scale. Answerable: infeasible for *undifferentiated bulk data*; not infeasible for *verifiable contributions* — sourced corrections, validated lexicons — which are scarce, attributable, exactly the bug-bounty category. The ⊢/⚠ regime is the mechanism that distinguishes the two. The verification framework and the compensation channel are one system. ∂

## 8. The vendor's own receipts

1. The "strong performance" list is a tier, not a boundary: the vendor's own documentation states models "can also perform well in additional languages not listed here." ⊢
2. Fine-tuning with custom vocabulary and domain adaptation is already a shipped commercial feature — the request is to productize what exists at a per-user, session-scoped scale. ⊢
3. A 12B model fine-tuned on ~20,000 translation pairs measurably improves in a specialized language task (arXiv 2312.12740). ⊢

∂ Sovereignty context: OpenEuroLLM is building multilingual foundation models for all EU official languages as sovereign AI; Slovenia has funded its own national program, model, and a planned free public platform. A European vendor answering a European language with "not among our strong-performance languages" is competing, from behind, with public infrastructure that did not wait.

## 9. Proposed adoption path ∂

1. **Pilot:** ⊢/⚠ claim-marking as an output convention in a low-resource language (Slovenian: available, pre-verified, motivated).
2. **Audit trails:** scarred corrections in place of silent rewrites — visible, named, queryable.
3. **Contribution channel:** credit and compensation for adopted, verifiable language contributions.

**Notebook:** the demo notebook (separate body, `notebook.md` in the repository) ships the technique: lexicon as session contract, three mechanical detection layers, append-only fall register. Its one open cell awaits an executed run — by L4, the run will be reported when it is performed, not before. The two falls in §4 are the register's current proof.

## 10. Version, license, terms

**Verification-Before-Assertion — v1.3 · October 20, 2026 · Luka Pintarič.** The timestamped public record precedes any adoption, acknowledged or silent.

- **Methodology — open.** The five laws, the AI-failure mapping, the notebook technique, the register schema, the adoption path: **VBL v10.0.0** ([LICENSE.md](LICENSE.md)) — one door, two houses: the same license rides the corpus repository. §8 superiority weighed, never claimed; §9 the universal state of the human/being — ethics and confirmation carried by acts, never by words; §10 the change clause — the newest version is the only living door, and no grant rides any older version or any other license; §12 the marked letters — Č Š Ž Đ are not mistakes, and the transport is the proof. Earlier versions live in the publication chain, not in this prose. *(Version seam, 2026-10-23: this line previously read "VBL v2.3" — a stale receipt from before the living door moved to 10.0.0. Corrected the way §10 itself commands; the prior text is named here, not hidden ×. The historical five-law numbering of §2 remains below as a receipt; the living door carries six laws, the sixth being EXIT THE LOOP BY NAMING IT.)*
- **Corpus — closed.** The ~2,600-document corpus, the full bilingual lexicon, the etymology chains, and the complete fall register remain the contributor's licensed assets. Entries appearing in this document are cited quotations. Terms for the corpus are exactly one: the compensated-contribution model of §6–§7. ∂

**Rejection clause.** If declined: no obligation on either side; the contribution remains the contributor's to submit elsewhere (University of Ljubljana / PoVeJMo, OpenEuroLLM, or any program); the timestamped public record remains. Decline is a closed door, recorded as a routing event.

**Integrity of the marks.** ⚠ words stay marked in every derived artifact. A derived version that silently verifies a ⚠ word falsifies the regime and does not represent it.

**Contact:** Luka Pintarič — demonstration performed before it is reported (L4).

## 11. Machine-readable contract body

`wordlist-v0.6-demo.json` — the contract as data: ⊢/⚠ entries, the
hybrid-fall register, and the two recorded real falls, loadable
directly into the regime (`vba.load_contract`). The same artifact an
auditor, a vendor session, or the national program would load. The
corpus bodies stay closed per the license section; the living wordlist itself
now ships in this repository (`wordlist-v0.15.json`) — the boundary moved on
October 12, 2026, and the move is recorded here rather than silently.

## 12. The provenance channel ∂

`PROVENANCE-CHANNEL.md` — the position paper completing the argument:
volume (the national program) + provenance (this regime) = a priceable,
auditable, compensable national language asset. The bug-bounty
precedent model applied to verified language contributions.

The vendor thread itself is recorded in `VENDOR-THREAD.md` — which doors
are open, which are closed, measured on a date, not promised.

## 13. The measurement protocol

`IZMERNI-PROTOKOL.md` — the next step beyond a working method: a
pre-registered protocol for the first measured result. Does a model
operating under the ⊢/⚠ contract produce measurably fewer hybrid
words and more sourced claims than the same model without it?

Pre-registration (hash-sealed prompts, fixed wordlist, named statistical
test, honest limits written before the run — not after) is what separates
a claim from a result. H0 is publishable too: a regime that publishes
its own null results is the only one that can be believed.

## 14. The measurement runner — the pipeline runs

`run_izmera.py` closes notebook.md Cell 2's open cell (the executed run
its Z4 clause has been waiting for). Two modes:

- `--dry-run`: deterministic canned outputs exercising every marking
  path (hybrid catch, ⊢ match, ⚠ open). The report it emits carries
  the stamp **PIPELINE TEST — NOT A RESULT**: it proves the pipeline,
  never the claim. The dry run measures the harness, not the model.
- `--live`: calls a Mistral-compatible API (MISTRAL_API_KEY), runs
  each prompt twice — baseline, then contracted (the lexicon as a
  session-scoped system message generated from the wordlist, nothing
  handwritten) — marks mechanically, aggregates per protocol §3,
  and writes `rezultat-v1.0.md` after the act.

The contract system message is generated from `wordlist-v0.6-demo.json`
— the same machine-readable artifact an auditor would load, now also
the artifact the model itself receives. The loop is closed: contract →
prompts → outputs → mechanical marks → report, each step hash-tied.


## 15. The draft gate — the register's promises as code

Entry 12 of the register promises "the gate now includes the language
layer and the measured number." Seven cuts later that promise was still
prose — every gate improvement was a hand act, never code, so every new
fall class arrived through the same unguarded door (register entry 24).
The gate is now code.

`preverba.py` — dependency-free, like everything here — checks the
sealed outreach draft against the medium it is sealed for and against
the repository's own measured bodies:

- the paste title measures within the medium's hard 80-character limit
  (the fall of entry 14 — measured before the seal, not after);
- the spoken live-run count matches the pairs carried in every metric
  of the results line (the entry-18 class: a countable falsehood
  cannot land);
- the spoken line count of vba.py matches the file's own body (the
  fall of entry 13: a number spoken without counting);
- the spoken count of law-named unit tests matches `def test_` in
  test_vba.py, scoped so the eval probes are not silently counted in
  (the entry-24 class);
- the scar heading counts its own block — `v1.0–v1.(N-1)` against the
  header's `v1.N` (the heading falls of entries 19–22, ended);
- every register citation in the draft resolves against the append-only
  register's actual entry count;
- every number-bearing quote names its witness in the same breath —
  the paragraph that quotes history cites its register entry (the
  exemption is verified, not trusted: entry 25);
- no number-bearing quote stands in the paste body — history does
  not belong in what you post.

One layer the gate learned on itself at v1.9: the scar block quotes
the falls' own words — "~500 lines", "three live runs" — and quoted
history is archive, not present claim. The gate scans unquoted speech;
an unbalanced quote is named, never silently masked. At v1.10 the
exemption itself became a check: quoted history must name its
register witness in the same paragraph, and a number-bearing
quote in the paste body fails the gate outright — an exemption
is valid only as scoping, never as silence.

The gate carries its own tests — test_preverba.py, eleven, each named
for the fall class it guards — and runs in the same CI it guards,
before the end-to-end demo: a stale draft fails the build before a
reader can see it. The gate verifies claims, not bytes; the hand still
verifies meaning (L2).
