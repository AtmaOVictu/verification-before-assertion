# IZVEDBA TESTOV 0.1540 — KOS 8: T-12 (K-07) ∧ T-14 (K-07)

Izvajalka: Mera ⊙ ⟨DVOJE-ROK⟩ — po ⟡ besedi »stori« (15. 11. 2026; mandat: delegacija ⟡ »izbiraj…« @σ 5473 — sanacijska vrsta PAR.23 nadaljuje po vrsti: KOS 8 = K-07 ločitev-statusov ⊙ ⟨SAMODEJNA-VRSTA⟩ σ 4340). Nadaljevanje kitov #48–#58.
TIK izmere: 2026-11-15T05:30:45Z UTC ⇌ 06:30:45 CET Ljubljana

## Obseg izmere — register kontrol 0.1540 @⟨main⟩ (sha zlitja 96c70ff2, glava javne hiše ⟨main⟩ izmerjena isti dih)

Tela: VBL-0.1540-REGISTER-KONTROL.json (21.362 B, sha256 f30c41c8…d9d349 ⇌ manifestna vrstica ⊢; pre-šivno telo za diff — K-07 še NOT_RUN) ∧ IZVEDBA-TESTOV-01540-KOS-2.md (2.661 B) ∧ KOS-3 (3.614 B) ∧ KOS-4 (4.004 B) ∧ KOS-5 (4.598 B) ∧ KOS-6 (6.013 B) ∧ KOS-7 (6.357 B). Instrument: test_k07.py — mehanski razcep status-atom ⊥ plast; plasti: CLAIM (claim_status) ⊥ TEST (test_result) ⊥ DECISION (decision); pravila: R1 ločena polja ×19 (nabor {claim_status, test_result, decision}) · R2 pretipkanje (claim/decision gola statusna beseda ⊥ test_result NOT_RUN ∨ izmera) · R3 štetje po plasteh · R4 ura brez vira · R5 zunanje (Zakon statusov ∧ MANIFEST-DRZI ∧ glava @main) · R6 sonde; © nogice izrezane iz sekij (⟨PADC-©-NOGICA⟩ ⊙ vzorec kos 3/4/5/6/7).

## T-12 (K-07 ločitev-statusov) — PASS (2026-11-15T05:30:45Z)

Izmere: status-atomov 57 (×19 kontrol × 3 plasti ⊢ vsaka kontrola z lastno koordinato ∧ uro); R1 ločena polja 19/19 (nabor {claim_status, test_result, decision} enoličen ×19 ∧ zliti/odvečni ×0); pretipkanj ene plasti v drugo = 0 (claim_status NOT_RUN ×19 ∧ decision HOLD ×19 — gole statusne besede brez vsebine izmere ⊥ test_result NOT_RUN ×10 ∨ izmera ×9 — vsak izmerjen test_result nosi datum ∧ ⊢ pri viru: ura brez vira ×0) → claim se ne prikaže kot izmerjen izid ali odločitev ⊙ pogoj_PASS K-07 drži (pretipkanje statusov = 0).
- Sonde veljavnosti: negativne ujete 3/3 (s1 izmera-pretipkana-v-claim_status ujeta ⚠ · s2 izmera-pretipkana-v-decision ujeta ⚠ · s3 konflikt-brez-vrste-vira ujet ⚠) ∧ pozitivna sprejeta 1/1 (p1 ločena-plast: claim NOT_RUN ⊥ test PASS z izmero ⊥ decision HOLD) → instrument loči plasti (⟨ne⟩ prazna sodba) ⊙ ⟨NE-UGIBAJ⟩ 2690.

## T-14 (K-07 neznano-⊥-konflikt) — PASS (2026-11-15T05:30:45Z)

Izmere: CONFLICTED v statusih ×0 (57 atomov prebranih — nobena vrednost se ne začne s CONFLICTED) ∧ konflikt brez vrste (POLICY ∧ EVIDENCE ∧ AUTHORITY ∧ TEMPORAL ∧ SCOPE) ∧ vira ×0 ∧ NOT_RUN prikazan kot konflikt ×0 (neznano ostaja neznano — UNKNOWN ≠ CONFLICTED ⊙ §7.2) ∧ poročila KOS-2–KOS-7 brez CONFLICTED (© nogice odrezane pred štetjem ⊙ ⟨PADC-©-NOGICA⟩) → neznano ⊥ konflikt sta ločena ⊙ pogoj_PASS K-07 drži (konflikt nosi vrsto ∧ vir — ni ga, torej ni napovedan).

## Preverba ∧ kvaliteta izvedbe (2026-11-15T05:30:45Z)

- T-29 re-izmera ⊢: 19 kontrol · polj-7 manjka ×0 (problem ∧ zahtevani_dokazi ∧ test ∧ pričakovani_rezultat ∧ pogoj_PASS ∧ ravnanje_ob_neuspehu ∧ povezave_testi v vsaki kontroli).
- T-30 re-izmera ⊢: povezav 36 · unikatnih 34 · slabih (neobstoječi testi) ×0 — vsaka povezava vodi na test definirana v standardu §12 (34 testov; T-12 ∧ T-14 prisotna).
- Manifest ⇌ telesi ⊢: generatorjeva --check logika izvedena bajtno nad ×5 telesi = DRŽI ×5 (LICENSE.md 193.317 B · REGISTER-NEIMENOVANIH.jsonl 2.784 B · REGISTER-PADCEV.jsonl 36.170 B · standard 22.715 B · register 23.162 B po šivu); hashlib kalibriran na kanonu abc pred izmero ⊢.
- Zakon statusov ×9 pre-šivno ⊢ (K-01 ∧ K-02 ∧ K-03 ∧ K-04 ∧ K-05 ∧ K-06 ∧ K-14 ∧ K-15 ∧ K-18 → claim_status NOT_RUN ∧ decision HOLD ∧ test_result ≠ NOT_RUN v registru pri viru); po šivu ×10 (K-07 pridružen ⊢).
- Post-šivna izmera isti dih: instrument zagnan nad šivnimi telesi → T-12 PASS ∧ T-14 PASS exit 0 (izmerjeni test_result ×10 · zakon ×10 · manifest ⇌ register ⊢).

## PADC javno (2026-11-15T05:30:45Z)

⟨PADC-POROČILO-ODSOTNOSTI-KOT-KONFLIKT⟩ ×1 — T-14 detektor instrumenta je naivno štel poročilo odsotnosti (»CONFLICTED v statusih ×0« znotraj nove izmere K-07) kot napoved konflikta → post-šivna sodba padla na FAIL (exit 1); ujet pri post-šivni izmeri isti dih pred prevozom ⊙ vrata ⟨ne⟩ prenesla nobene laži; kura isti dih: detektor loči napoved (vrednost se začne s CONFLICTED) od poročila (omenitev ×0 znotraj izmere) ∧ ponovna izmera → T-14 PASS exit 0 ⊢; PADC zapisan pošteno v vrednost test_result K-07 ⊙ ⟨ZAKON-PADEC-NI-MOLK⟩ 2354 ∧ ⟨NE-UGIBAJ⟩ 2690.

## Zakon statusov (2026-11-15T05:30:45Z)

claim_status ⊥ test_result ⊥ decision se niso zlili: K-07 ohranja claim_status NOT_RUN ∧ decision HOLD — izmerjen izid zapisan samo v test_result (T-12 PASS ∧ T-14 PASS ⊢); decision ostaja ⟡-jeva sodba ⊙ zakon_statusov registra ⊢ izmera pri viru 2026-11-15. Diff stari⊥novi register = natanko eno polje (kontrole[6].status.test_result) → »samo v test_result« ⊢ (izmerjeno bajtno: spremenjenih listnih polj ×1 · vrstični diff −1/+1).

## Manifest (2026-11-15T05:30:45Z)

Dotik registra → obnova manifestne vrstice isti dih ⊙ ⟨MANIFEST-EN-DIH-PO-ROJSTVU⟩: vrstica VBL-0.1540-REGISTER-KONTROL.json → izmerjeno po šivu (23.162 B · sha256 5262fbe5…6bbf2a); note manifesta dopolnjena isti dih: kura K-07 kos 8 (T-12 PASS ∧ T-14 PASS ⊙ test_k07.py); preverba bajtna pred zlitjem: items ×5 ⇌ telesa = DRŽI ⊢.

© Luka Pintarič, VBL 0.1540 × 10⁴ (§9 ∧ §10 ∧ §12) · measured, not asserted ⊙ §16 · merilec se meri ⊙ §52 · molk ni soglasje
