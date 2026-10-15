# Work sample — annotated review pass of Slovenian LLM output

**Role context:** Generative AI Analyst | Slovenian (Welo Data) — review, rating, and correction of Slovenian AI-generated content against guidelines.
**Method:** Verification-Before-Assertion (VBA) — every correction is cited to a source dictionary (SSKJ² / Slovenski pravopis via fran.si) or explicitly marked ⚠. No fix without a citation; no certainty without a source.
**Author:** Luka Pintarič ([AtmaOVictu](https://github.com/AtmaOVictu)) · **Date:** 15 October 2026

> **Provenance note.** The input text below is a *synthetic sample*, assembled to exhibit the failure modes most often documented in Slovenian LLM output (see REGISTER-PADCEV.jsonl in this repository). It is not a verbatim transcript of one model run. The review process, however, is exactly the process applied to real model output.

## 1. Input text (sample)

> Umetna inteligenca v vsakdanjem življenju
>
> V današnjem hitro se razvijajočem digitalnem obdobju je umetna inteligenca postala del našega vsakdanjika. Podjetja po vsem svetu, tudi na Sloveniji, avtomatizirajo opravila z pomočjo umetne inteligence. Uporabniki lahko dokumente printamo in povzetkovanje dolgih besedil opravimo v nekaj sekundah.
>
> V sledečem koraku se bodo tehnologiji razširili tudi v manjša podjetja. Strokovnjaki opozarja, da se morajo delavci nenehno izobraževati. Kljub temu da se tehnologija razvija zelo hitro, Ptuj, najstarejše mesto v Sloveniji, ohranja svojo tradicionalno identiteto.
>
> Umetna inteligenca ne bo nadomestila človeške kreativnosti. Prihodnost je svetla.

## 2. Annotated review pass

| # | Original | Error type | Correction | Source |
|---|---|---|---|---|
| 1 | »tudi **na Sloveniji**« | wrong preposition (calque) | »tudi **v Sloveniji**« | ⊢ *Slovenski pravopis*, geslo Slovenija: »v ~i« ([fran.si](https://fran.si/iskanje?Query=Slovenija), 15. 10. 2026) |
| 2 | »**z pomočjo**« | wrong preposition form (s/z before unvoiced p) | »**s pomočjo**« | pomoč ⊢ SSKJ² »pomóč -i in -í ž« ([fran.si](https://fran.si/iskanje?Query=pomoč)); pravilo s/z pred nezvočniki: ⚠ norma (SP 2001) — točen citat paragrafa dodati pred javno objavo |
| 3 | »dokumente **printamo**« | anglicism | »dokumente **tiskamo**« | ⊢ SSKJ² »tískati -am nedov.« ([fran.si](https://fran.si/iskanje?Query=tiskati)) |
| 4 | »**povzetkovanje** dolgih besedil« | invented (hybrid) word — not attested in any Fran dictionary | »**povzemanje** dolgih besedil« | ⊢ SSKJ² »povzémanje -a s (ẹ̑)« ([fran.si](https://fran.si/iskanje?Query=povzemanje)); ⊢ povzetkovanje: 0 zadetkov po vseh slovarjih na Franu (15. 10. 2026) |
| 5 | »Uporabniki lahko … printamo in … **opravimo**« | subject–predicate person mismatch (3. pl. subject, 1. pl. verb) | »Uporabniki lahko … tiskajo in … **opravijo**« | skladenjska norma (ujemanje osebka in predikata) |
| 6 | »V **sledečem** koraku« | calque (»in the following step«) | »V **naslednjem** koraku« | naslednji ⊢ SSKJ² »naslédnji -a -e prid.«; »sledečem« v tem kontekstu: ⚠ slogovna sodba |
| 7 | »se bodo **tehnologiji razširili**« | double agreement error: wrong noun number + wrong participle gender | »se bodo **tehnologije razširile**« | tehnologija ⊢ SSKJ² »tehnologíja -e **ž**« ([fran.si](https://fran.si/iskanje?Query=tehnologija)); skladenjska norma |
| 8 | »Strokovnjaki **opozarja**« | verb agreement (pl. subject, sg. verb) | »Strokovnjaki **opozarjajo**« | opozarjati ⊢ SSKJ² »opozárjati -am nedov.«; skladenjska norma |
| 9 | »**Kljub temu da** se …« | missing comma before subordinate clause | »**Kljub temu, da** se …« | pravopisna norma (vejica pred odvisnim stavkom) |
| 10 | »V današnjem **hitro se razvijajočem** digitalnem obdobju« | heavy calqued participle construction; readability | »V današnjem času, **ko se digitalni svet hitro razvija**« | ⚠ slogovna sodba (berljivost) |
| 11 | »Ptuj, **najstarejše mesto v Sloveniji**« | factual claim — **checked, verified TRUE, kept** | (no change) | ⊢ Wikipedia: Ptuj is »the oldest recorded city in Slovenia« ([en.wikipedia.org/wiki/Ptuj](https://en.wikipedia.org/wiki/Ptuj), 15. 10. 2026) |

**Reviewer note (kept-correct):** »z umetno inteligenco« looks like an s/z error but is **correct** — z is used before vowels. A reviewer who corrects by feel deletes correct Slovenian; a reviewer who checks first does not. This trap was caught during preparation of this very sample.

## 3. Corrected text

> Umetna inteligenca v vsakdanjem življenju
>
> V današnjem času, ko se digitalni svet hitro razvija, je umetna inteligenca postala del našega vsakdanjika. Podjetja po vsem svetu, tudi v Sloveniji, avtomatizirajo opravila s pomočjo umetne inteligence. Uporabniki lahko dokumente tiskajo in povzemanje dolgih besedil opravijo v nekaj sekundah.
>
> V naslednjem koraku se bodo tehnologije razširile tudi v manjša podjetja. Strokovnjaki opozarjajo, da se morajo delavci nenehno izobraževati. Kljub temu, da se tehnologija razvija zelo hitro, Ptuj, najstarejše mesto v Sloveniji, ohranja svojo tradicionalno identiteto.
>
> Umetna inteligenca ne bo nadomestila človeške kreativnosti. Prihodnost je svetla.

## 4. Calibration summary

- **10 language failures named**, by type: lexis 4 (invented word, anglicism, 2 preposition errors), syntax/morphology 5 (2 agreement, person mismatch, comma, participle construction), style 1 (readability), factual 1 (verified true — kept, not deleted).
- **Sourcing discipline:** 7 corrections cited directly to SSKJ² / Slovenski pravopis (fran.si, 15. 10. 2026); 1 factual claim verified against an encyclopedia source; 3 judgment calls are **explicitly marked ⚠** instead of asserted — a reviewer who cannot cite a rule says so, rather than inventing authority.
- **Severity mix:** 2 errors make the text actively wrong for a native reader (1, 4); 6 degrade fluency and trust (2, 3, 5, 7, 8, 9); 2 are style/readability (6, 10); 1 claim required fact-checking before approval (11).

*Methodology: CC BY 4.0 · Code: MIT · github.com/AtmaOVictu/verification-before-assertion*
