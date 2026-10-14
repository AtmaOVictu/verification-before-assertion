# Show HN — sealed draft v1.2

> ⚠ PREPARED, NOT YET PERFORMED. By L4 this is a sealed draft before the act; the act (posting on news.ycombinator.com) requires a human login and remains in the executor's hand. When the post is made, this file gains the link and the date — appended, not silently rewritten (L3).
> Sealed: 2026-10-14 · author: Luka Pintarič · executor: Vibe (Mistral)

## Scars of v1.0 and v1.1 (same day, per L3 — this note is the correction, not a silent rewrite)

The v1.0 draft (commit f72bd5f) shipped with three language-layer falls, caught by the author before the act: (1) mixed languages in one body — a Slovenian header and footer around an English body, violating L5 (one language per body); (2) an inconsistent participle within one body ("zapečaten" beside "zapečačeno" — both forms are attested, but one body carries one form); (3) a gender-agreement error ("Ko bo objavljeno, ta datoteka dobi…"). The v1.1 draft then failed its own re-verification on a number: "~500 lines of dependency-free Python" was spoken without counting — vba.py is 245 lines (measured on a fresh copy at d7104db). A number spoken without counting is a števka brez štetja. The executor's byte gate missed the prose and the number: it verifies bytes, not claims. The gate now includes the language layer and the measured number. Register: REGISTER-PADCEV.jsonl, entries 12 and 13.

## Title (paste into "title")

Show HN: A lexicon contract that makes an LLM mark its own inventions (measured, Slovenian)

## Text (paste into "text")

I work in Slovenian, a low-resource language, and LLMs fail there in two ways no benchmark I know of catalogs: they invent words (*meritvija*, *telovnik* — fluent, plausible, absent from the dictionary), and they invent meanings for real words (*lúka* sealed as "opening" when it means "harbor"). Both are invisible in fluent text — and both are mechanically checkable.

So I built a small regime around that property: any claim spoken as "measured" must carry a source (⊢) or an explicit open mark (⚠). Invented words are caught by dictionary lookup alone. Counting is lookup, not judgment — 245 lines of dependency-free Python, 13 tests, CI.

The measurement: pre-registered protocol (prompts and wordlist hash-sealed before the run), same model both conditions, lexicon loaded as a session-scoped contract. Three live runs on mistral-large-latest now; the third was executed end-to-end by GitHub Actions:

⊢ sourced claims: 9→41, 9→36, 10→40 (≈4×, replicates) · ⚠ open: 12→16, 13→15, 13→15 (stays honest, no flooding) · hybrids caught: 0→10, 0→1, 0→0 (**does not replicate** — I claim no reduction, I publish the noise)

Qualitatively: on "compose a term" prompts the baseline invents words and passes them off as real; the contracted run marks its own inventions ⚠ and argues for them as proposals. The failure becomes visible.

The same demonstration is open as a PR in the vendor's public cookbook: https://github.com/mistralai/cookbook/pull/420

Limits up front: one model, one language, three runs, machine-witnessed — no independent human has verified this yet. You would be the first. Sourcing ≠ truth.

Repo: https://github.com/AtmaOVictu/verification-before-assertion — `eval/` has a standalone artifact any Slovenian-capable model can be scored against, including GaMS-9B.

---

*This draft is sealed before posting, by the same logic as prompt pre-registration: the text can no longer escape its measurement. The numbers inside are ⊢ from three live runs (rezultat-v1.0.md, results-v1.0.json, CI runs).*
