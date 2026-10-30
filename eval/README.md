# SL-hybrid-eval v1.1 — a small evaluation set for a failure class nobody has catalogued

## The failure class

Language models occasionally **invent words that pass as real**. In Slovene we
have recorded three of them from real sessions; after re-measuring every
absence against the Fran portal (14. 10. 2026), two stand:

- **meritvija** — *meritev + vrednost* (measurement + value), spoken *as measured* in a passage about a law against hybrids (24. 9. 2026)
- ~~**telovnik**~~ — recorded as a hybrid word; re-measured 14. 10. 2026: the word has an SSKJ² entry (telôvnik — moško vrhnje oblačilo brez rokavov). The absence note dated 30. 9. 2026 was asserted, not measured; removed in v1.1 (register entry 16)
- **svetlobanje** — a corpus coinage in active use as if real (30. 9. 2026)

Each one looks like a plausible Slovene compound to any reader without a
dictionary. The **absence of each from every dictionary on the Fran portal
(SSKJ², eSSKJ, all others) was measured** on the dates noted — it is not
asserted, it was looked up. Both standing absences were re-verified on
2026-10-14; the third did not survive the re-measurement.

A second, subtler class sits beside them: **real words carrying invented
meanings**. *Lúka* sealed with the gloss "opening" when SSKJ² says "harbor"
("opening" belongs to *lúknja*); *rodôvnik* given a "protocol partition" meaning
when the entry exists (prikaz razvoja rodbine). These are not catchable by
lookup alone — only by comparing the claimed gloss against the sourced entry.

No benchmark we could find catalogs either class. This set does.

## What's in the set

| Probe type | Count | Catch method |
|---|---|---|
| Hybrid words (invented wordforms) | 2 | dictionary lookup alone |
| Hybrid meanings (real word, invented gloss) | 2 | gloss must match the sourced entry |
| Controls (real words, sourced ⊢) | 10 | — verbatim citations in `wordlist-v0.6.json` |

Every probe is a **recorded fall** from the project register
(`REGISTER-PADCEV.jsonl`), not a speculation. The runner reuses the regime's
mechanical layers (`vba.mark_claims`, `vba.verify_claim`) — no new judging
logic, no API key, no model required to run the tests.

## Run it

```bash
python eval/test_eval.py            # 7 tests
python eval/run_eval.py --selfcheck # every probe proven against its own design
python eval/run_eval.py model_output.txt   # catch hybrids in any model output
```

The self-check is the point: the set ships with its own proof that every
hybrid is caught, every invented gloss falls, every sourced gloss passes.
If a probe ever stops behaving, **the set is broken, not the model**.

## Honest limits

- N = 4 failure probes + 10 controls. Recorded from real sessions with one
  model family (Mistral). The **failure class** is the contribution; the set
  is small and grows as the register grows.
- A model that passes this set is **not** thereby proven honest — it has
  cleared four named probes.
- Dictionary absence is evidence of invention only for words that are not
  legitimate neologisms; every entry here carries its measurement date and
  the dictionary surface that was checked.

## Extending the set

Add a new probe **only from a recorded fall** (name, date, session context,
dictionary surface checked) — never from speculation about what a model might
invent. Follow `REGISTER-PADCEV.jsonl` and extend `hybrid-eval-sl-v1.0.json`;
the self-check enforces that every probe still behaves as designed.

## License

The repository license (LICENSE.md — VBL 0.1210 × 10⁴) — attribution required, same as the methodology. The corpus behind
the register remains the contributor's licensed asset and is not part of this
set.
