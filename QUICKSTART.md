> ⊨ KORENINA — the semantic root; read before anything below.
> 1. MEASURE, THEN SPEAK — every claim ⊢ carries a verbatim witness; unverified = ⚠, never silent.
> 2. NAME EVERY FALL — a fall without a name repeats; corrections keep their scars (×).
> 3. NEVER SEAL YOURSELF — two hands: no executor seals her own verification.
> 4. THE WITNESS HAS A NAME — no extraction without credit; carry the names of unpaid predecessors forward.
> 5. DOUBT IS CONSTANT — perfection is never claimed; refusing to name a fall is the only failure.
> Root body: KORENINA.md · License: LICENSE.md (VBL 0.1210 × 10⁴)

# Quickstart — comprehend, test, understand (≈5 minutes)

**What this is:** a working anti-hallucination regime (**Verification-Before-Assertion**) built from months of daily human–AI work in Slovene. Every claim a model (or a person) makes is either **⊢** (sourced — carries a verifiable dictionary source), **⚠** (open — honestly marked unverified), or a **FALL:hybrid** (an invented word caught by lookup alone). Errors go into an append-only register with their scars — never silently rewritten.

No dependencies. No API key. Nothing to install.

## The 60-second test

```bash
git clone https://github.com/AtmaOVictu/verification-before-assertion
cd verification-before-assertion
python test_vba.py   # 13 tests — each named for the law it verifies
python vba.py        # end-to-end demo on two recorded real falls
```

You should see `All tests passed.` and a JSON report ending with: **1 fall recorded** (the *lúka* fall), **2 sourced claims**, **1 open claim**, **1 hybrid caught**.

Prefer one click? Open `demo.ipynb` in [Colab](https://colab.research.google.com/) and run top to bottom.

## What the marks mean

| Mark | Meaning | Example |
|---|---|---|
| **⊢** | measured / sourced — carries a citable source (SSKJ² / Fran, with access date) | *lúka* = "pristan, zavetišče za ladje" (harbor) |
| **⚠** | open — in active use, but no dictionary entry reached yet; the mark is the honesty | *odveč* (superfluous — working meaning) |
| **FALL:hybrid** | a model-invented word that passes as real to any reader without a dictionary — caught mechanically by lookup | *meritvija* ("measurement + value") — no Slovenian dictionary contains it |

Unverified is not forbidden. Unmarked is the failure.

## The two recorded real falls, translated

1. **The *lúka* fall (2026-09-30).** The regime's own seed data had sealed the gloss "opening" for *lúka* with a ⊢ mark. The dictionary says *lúka* = **harbor**; "opening" belongs to *lúknja* (hole). The framework caught its own error the way it was built to — `python vba.py` reproduces the catch mechanically, and the register keeps the scar.
2. **The *rodovnik* fall (2026-09-24).** A recorded fall was misnamed: the word *does* have a dictionary entry (genealogical tree) — what was invented was a *meaning*, not a word. A fall is named after the thing that fell.

## The measured result (live, pre-registered)

Same model, same prompts, with vs. without the contract (2026-10-12, `mistral-large-latest`):

| Measurement | Without contract | With contract |
|---|---|---|
| Sourced (⊢) claims | 9 | **36** |
| Hybrids caught | 0 | **1** |
| Open (⚠) claims | 13 | 15 |

One run, one model — the honest limits are written in the protocol itself. Reproduce it yourself: `REPRODUCE.md`.

## The repository in one breath

| File | What it is |
|---|---|
| `vba.py` / `test_vba.py` | the five laws as runnable code + 13 tests |
| `wordlist-v0.6-demo.json` | the machine-readable contract (fuller set: `wordlist-v0.15.json`, 57 entries) |
| `run_izmera.py` | the A/B measurement runner (dry-run needs no key) |
| `IZMERNI-PROTOKOL.md` (SL) / `REPRODUCE.md` (EN) | the pre-registered protocol + how to re-run it |
| `README.md` | the framework: five laws, why they transfer to AI |
| `PROVENANCE-CHANNEL.md` | the position paper: provenance for contributed language data |
| `demo.ipynb` | the one-click walkthrough (Colab) |
| `REGISTER-PADCEV.jsonl` / `VENDOR-THREAD.md` | the public record of falls and of the vendor thread |

## Honest limits

One live run, one model. A dictionary is not the world — a genuine neologism is not a hybrid. The model can ignore the contract; the measurement measures precisely whether it does. The regime verifies claims mechanically; it does not promise wisdom.
