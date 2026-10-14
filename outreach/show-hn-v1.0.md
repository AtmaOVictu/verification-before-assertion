# Show HN — sealed draft v1.8

> ⚠ PREPARED, NOT YET PERFORMED. By L4 this is a sealed draft before the act; the act (posting on news.ycombinator.com) requires a human login and remains in the executor's hand. When the post is made, this file gains the link and the date — appended, not silently rewritten (L3).
> Sealed: 2026-10-14 · author: Luka Pintarič · executor: Vibe (Mistral)

## Scars of v1.0–v1.7 (same day, per L3 — this note is the correction, not a silent rewrite)

The v1.0 draft (commit f72bd5f) shipped with three language-layer falls, caught by the author before the act: (1) mixed languages in one body — a Slovenian header and footer around an English body, violating L5 (one language per body); (2) an inconsistent participle within one body ("zapečaten" beside "zapečačeno" — both forms are attested, but one body carries one form); (3) a gender-agreement error ("Ko bo objavljeno, ta datoteka dobi…"). The v1.1 draft then failed its own re-verification on a number: "~500 lines of dependency-free Python" was spoken without counting — vba.py is 245 lines (measured on a fresh copy at d7104db). A number spoken without counting is a števka brez štetja. The executor's byte gate missed the prose and the number: it verifies bytes, not claims. The gate now includes the language layer and the measured number. Register: REGISTER-PADCEV.jsonl, entries 12 and 13.

The v1.2 draft then failed a third full re-verification on the act's medium: its title measured 91 characters, and the Hacker News submission field carries a hard 80-character limit — the seal was cut without measuring the constraint of the place it was sealed for, and the medium would have truncated it silently. The title is re-cut to 69 characters (measured); the qualifiers it carried — measured, Slovenian — already live in the body's first sentence. The gate now measures the medium's constraints before the seal. Register: REGISTER-PADCEV.jsonl, entry 14.

The v1.3 draft then fell on a claim, not on bytes: its example named telovnik as a word "absent from the dictionary" — and the dictionary contains it (SSKJ²: telôvnik — moško vrhnje oblačilo brez rokavov, ki pokriva zgornji del telesa; reševalni telovnik; measured against the Fran portal, 2026-10-14). The byte gate cannot see this: it verifies bytes, not claims about the world — suspicion is its own layer, and this re-measurement was ordered by the author, not automated. The same pass found the word still carried in the project's own substrate with an "absence measured" note that had been asserted, not performed; the substrate is corrected in the same act (register entries 15–16). The example keeps meritvija, whose absence was re-measured the same day (Fran portal, all dictionaries: 0 hits). The gate now re-measures every dictionary claim against the source before the seal — and the medium is measured against its own doc (news.ycombinator.com/formatdoc): asterisks italicize, there is no bold, and URLs in a submission's text field do not become links. The body below therefore carries plain words and bare URLs — what you read is what was sealed.

The v1.4 seal then went stale on an event, not on an error: a fourth live run landed after the seal (izmera-bot, 2026-10-14T16:10:31Z) — baseline 9 ⊢ / 12 ⚠ / 0 hybrids, contracted 43 ⊢ / 15 ⚠ / 0 hybrids — carrying the same sealed prompts hash (09395ef0…) and a different wordlist hash (e0aeec2a…: the re-cut contract after the telovnik reclassification). A body posted saying "three live runs" while the repository carries four would speak a countable falsehood into a medium whose readers count commits; the count is re-measured from the run's results body before the act. What the fourth run adds: the effect replicates on the corrected contract too — sourced claims ≈4–5×, ⚠ stays honest, hybrids do not replicate (the noise is published either way). Register: REGISTER-PADCEV.jsonl, entry 18.

The v1.5 cut then fell on its own scope marker and on its reader: the scar block's heading still read "Scars of v1.0–v1.3" while carrying the v1.4 scar (a heading that undercounts its own contents — the fall class this regime names), and the paste body carried three terms it never defined for the reader: "hybrids" (used in the numbers line before any definition), "the telovnik reclassification" (a name the body never introduces), and the project verb "sealed" (in lúka "sealed as"). Ordered by the author — no undefined word or concept may stand in the posted body — v1.6 fixes them: the heading counts v1.0–v1.4; "hybrids" is defined at first mention ("I call them hybrids"); telovnik is introduced inline (re-measured, found in the dictionary, reclassified); "sealed" became "glossed"; "re-cut" became "corrected"; the bot is named by its measured role (the izmera workflow configures its own commit identity). Register: REGISTER-PADCEV.jsonl, entry 19.

The v1.6 cut then fell on the same scope marker it had just fixed: the re-counted heading ('Scars of v1.0–v1.4') still undercounted — the v1.5 scar paragraph now lives under a heading that stops one scar short of its own block. A heading counted once, at the cut that fixes it, and not re-counted at the next cut, is a place, not a sweep — the lesson register entry 20 names. v1.7 counts the heading from the block's own paragraphs (v1.0 through v1.6 — this paragraph is the v1.6 scar), the way a number is counted before it is spoken. Register: REGISTER-PADCEV.jsonl, entry 22.

The v1.7 seal was then refused by the medium itself, not by a reader: Hacker News is temporarily restricting Show HNs from accounts without community standing (news.ycombinator.com/showlim, read 2026-10-14 — a blanket flood-control gate, keyed to the account, not to the content; the draft's body was never read by anyone, and the empty url field was not the cause). The v1.3 pass measured the medium's formatdoc constraints — title length, formatting, bare URLs — and did not measure the standing gate: the same class as v1.2, one layer upstream, standing instead of format. v1.8 adds the standing gate to the pre-act check the way v1.2 added the title length: the act waits for standing — substantive comments, karma, time, or a direct word with the moderators (hn@ycombinator.com). The draft stays sealed; nothing in its paste body changes. Register: REGISTER-PADCEV.jsonl, entry 23.

## Title (paste into "title")

Show HN: A lexicon contract that makes an LLM mark its own inventions

## Text (paste into "text")

I work in Slovenian, a low-resource language, and LLMs fail there in two ways no benchmark I know of catalogs: they invent words (I call them hybrids: meritvija — fluent, plausible, absent from every dictionary), and they invent meanings for real words (lúka glossed as "opening" when it means "harbor"). Both are invisible in fluent text — and both are mechanically checkable.

So I built a small regime around that property: any claim spoken as "measured" must carry a source (⊢) or an explicit open mark (⚠). Invented words are caught by dictionary lookup alone. Counting is lookup, not judgment — 245 lines of dependency-free Python, 13 tests, CI.

The measurement: pre-registered protocol (prompts and wordlist hash-sealed before the run), same model both conditions, lexicon loaded as a session-scoped contract. Four live runs on mistral-large-latest now; the third was executed end-to-end by GitHub Actions, and the fourth (the repository's measurement bot, izmera-bot, 2026-10-14 16:10 UTC) ran on the corrected wordlist — one listed hybrid, telovnik, had been re-measured and found in the dictionary, so it was reclassified — with the same sealed prompts:

⊢ sourced claims: 9→41, 9→36, 10→40, 9→43 (≈4–5×, replicates) · ⚠ open: 12→16, 13→15, 13→15, 12→15 (stays honest, no flooding) · hybrids caught: 0→10, 0→1, 0→0, 0→0 (does not replicate — I claim no reduction, I publish the noise)

Qualitatively: on "compose a term" prompts the baseline invents words and passes them off as real; the contracted run marks its own inventions ⚠ and argues for them as proposals. The failure becomes visible.

The same demonstration is open as a PR in the vendor's public cookbook: https://github.com/mistralai/cookbook/pull/420

Limits up front: one model, one language, four runs, machine-witnessed — no independent human has verified this yet. You would be the first. Sourcing ≠ truth.

Repo: https://github.com/AtmaOVictu/verification-before-assertion — eval/ has a standalone artifact any Slovenian-capable model can be scored against, including GaMS-9B.

---

*This draft is sealed before posting, by the same logic as prompt pre-registration: the text can no longer escape its measurement. The numbers inside are ⊢ from four live runs (rezultat-v1.0.md, results-v1.0.json, CI runs).*
