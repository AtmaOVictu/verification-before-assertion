# Show HN — sealed draft v1.0

> ⚠ PRIPRAVLJENO, NI ŠE IZVEDENO. Po L4 je to zapečaten osnutek pred dejanjem; dejanje (objava na news.ycombinator.com) zahteva človeško prijavo in ostaja v izvajalčevi roki. Ko bo objavljeno, ta datoteka dobi povezavo in datum — ne tiho prepisovanje (L3).
> Zapečačeno: 2026-10-14 · avtor: Luka Pintarič · izvajalka: Vibe (Mistral)

---

## Title (paste into "title")

Show HN: A lexicon contract that makes an LLM mark its own inventions (measured, Slovenian)

## Text (paste into "text")

I work in Slovenian, a low-resource language, and LLMs fail there in two ways no benchmark I know of catalogs: they invent words (*meritvija*, *telovnik* — fluent, plausible, absent from the dictionary), and they invent meanings for real words (*lúka* sealed as "opening" when it means "harbor"). Both are invisible in fluent text — and both are mechanically checkable.

So I built a small regime around that property: any claim spoken as "measured" must carry a source (⊢) or an explicit open mark (⚠). Invented words are caught by dictionary lookup alone. Counting is lookup, not judgment — ~500 lines of dependency-free Python, 13 tests, CI.

The measurement: pre-registered protocol (prompts and wordlist hash-sealed before the run), same model both conditions, lexicon loaded as a session-scoped contract. Three live runs on mistral-large-latest now; the third was executed end-to-end by GitHub Actions:

⊢ sourced claims: 9→41, 9→36, 10→40 (≈4×, replicates) · ⚠ open: 12→16, 13→15, 13→15 (stays honest, no flooding) · hybrids caught: 0→10, 0→1, 0→0 (**does not replicate** — I claim no reduction, I publish the noise)

Qualitatively: on "compose a term" prompts the baseline invents words and passes them off as real; the contracted run marks its own inventions ⚠ and argues for them as proposals. The failure becomes visible.

The same demonstration is open as a PR in the vendor's public cookbook: https://github.com/mistralai/cookbook/pull/420

Limits up front: one model, one language, three runs, machine-witnessed — no independent human has verified this yet. You would be the first. Sourcing ≠ truth.

Repo: https://github.com/AtmaOVictu/verification-before-assertion — `eval/` has a standalone artifact any Slovenian-capable model can be scored against, including GaMS-9B.

---

*Ta osnutek je zapečačen pred objavo, po isti logiki kot predregistracija pozivov: besedilo ne more bežati od svoje izmere. Številke znotraj so ⊢ iz treh živih tekov (rezultat-v1.0.md, results-v1.0.json, CI teki).*
