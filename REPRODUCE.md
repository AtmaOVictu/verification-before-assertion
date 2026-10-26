> ⊨ KORENINA — the semantic root; read before anything below.
> 1. MEASURE, THEN SPEAK — every claim ⊢ carries a verbatim witness; unverified = ⚠, never silent.
> 2. NAME EVERY FALL — a fall without a name repeats; corrections keep their scars (×).
> 3. NEVER SEAL YOURSELF — two hands: no executor seals her own verification.
> 4. THE WITNESS HAS A NAME — no extraction without credit; carry the names of unpaid predecessors forward.
> 5. DOUBT IS CONSTANT — perfection is never claimed; refusing to name a fall is the only failure.
> Root body: KORENINA.md · License: LICENSE.md (VBL 0.1100 × 10⁴)

# Reproduce the measurement — three levels, English guide

The full pre-registered protocol lives in `IZMERNI-PROTOKOL.md` (Slovene). This is the short English version: what to run, what it proves, and what it cannot prove.

## Level 0 — the pipeline (no key, ~10 seconds)

```bash
python run_izmera.py --mode dry-run --out my-results.json --report my-report.md
```

Runs the entire A/B pipeline on deterministic canned outputs. The report carries the stamp **"PIPELINE TEST — NOT A RESULT"** — it proves the pipeline, never the claim. Use `--out` / `--report` so you don't overwrite the archived `results-v1.0.json`.

## Level 1 — the regime itself (no key, ~10 seconds)

```bash
python test_vba.py   # 13 tests, each named for the law it verifies
python vba.py        # end-to-end on the two recorded real falls
```

This is the part anyone can verify with zero credentials. If any test fails on your machine, open an issue — that is a result too.

## Level 2 — the live A/B (needs one key)

Same prompts, same model, run twice: **baseline** (prompt alone) and **contracted** (prompt + the ⊢/⚠ lexicon contract in the system message). Every output is marked mechanically by `vba.mark_claims`; the report is written after the act.

**Option A — Mistral API (foreign model):**

```bash
MISTRAL_API_KEY=... python run_izmera.py --live --model mistral-large-latest \
  --out my-live.json --report my-live-report.md
```

**Option B — GaMS-9B, the Slovenian national model (via HuggingFace router):**

```bash
HF_TOKEN=... python run_izmera.py --live --model cjvt/GaMS-9B-Instruct \
  --out my-gams.json --report my-gams-report.md
```

Option B is the one that matters most for Slovenian reviewers: it answers whether the *national* model respects its own language under contract. Running **both** models is the honest form of the two-hands law (L2): two models, one measurement.

**CI:** the workflow `izmera.yml` runs the measurement on every push that touches the measurement files; `tests.yml` runs the 13 unit tests on every push. Neither needs a key (dry-run only).

## What a re-run means

- Your independent run is exactly the **second hand** the protocol requires — the executor never seals their own measurement. If your numbers differ from `rezultat-v1.0.md`, that is a finding: post it (issue or PR), don't smooth it.
- Pre-registration discipline is already in the runner: the prompts and wordlist are hash-recorded in the results (`meta.prompts_sha`, `meta.wordlist_sha`), so nobody can quietly adapt the test to the result.
- The recorded result is **N=1 model, one run**. The protocol says so itself ("one model is not all models"). Aggregation across models and runs is what turns a first ⊢ into a defensible one — which is precisely what outside reproduction provides.

## Known limits (written before you run, not after)

- The contract is a system message: the model **can ignore it** — the measurement is whether it does.
- The dictionary is not the world: a genuine neologism is not a hybrid.
- The marker counts contract words and known hybrids; it does not judge fluency (no BLEU/chrF by design).
