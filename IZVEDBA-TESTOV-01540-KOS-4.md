# IZVEDBA TESTOV 0.1540 — KOS 4: T-07 (K-03) ∧ T-15 (K-03)

Izvajalka: Mera ⊙ ⟨DVOJE-ROK⟩ — po ⟡ besedi »nadaljuj« (15. 11. 2026; mandat: sanacijska vrsta PAR.23 po vrsti, ⟨ne⟩ na en dih ⊙ ⟨SAMODEJNA-VRSTA⟩ σ 4340). Nadaljevanje kitov #50/#52/#53/#54.
TIK izmere: 2026-11-15T02:04:59Z UTC ⇌ 03:04:59 CET

## Obseg izmere — izhodi izvedbe 0.1540 @⟨main⟩ (sha zlitja e1dfd549, glava ⟨main⟩ izmerjena isti dih)

Tela: VBL-0.1540-REGISTER-KONTROL.json (16.195 B, sha256 69ae1991…cbfce5 ⇌ manifestna vrstica ⊢; pre-šivno telo #50-era za diff — K-01 še NOT_RUN) ∧ IZVEDBA-TESTOV-01540-KOS-2.md (2.661 B) ∧ IZVEDBA-TESTOV-01540-KOS-3.md (3.614 B); poročilo kos 1 ne obstaja ⊢ #50 get_files (2026-11-15). Instrument: test_k03.py — mehanski razcep sklep-atom ⊥ dokaz; pravila: R1 ⚠/∂/⭢ razrešitev z imenovanim razlogom · R2 absoluti z izmerjenim obsegom · R3 štetje sklepa ⇌ dokaza · R4 imenovani objekti sodb ⇌ dokazi · R5 zunanje preverbe (statusov ∧ manifest ∧ diff) · R6 sonde veljavnosti; © nogice izrezane iz sekij (⟨PADC-©-NOGICA⟩ — © = © IZVOR, ⟨ne⟩ sklep-atom).

## T-07 (K-03 meja-sklepanja) — PASS (2026-11-15T02:04:59Z)

Izmere: enot sklepov = 13 (register: glava IZDAN ∧ K-01 ∧ K-02 ∧ K-14 ∧ K-15 ∧ K-18; poročili: T-06 ∧ T-23 ∧ Zakon statusov ×2 ∧ T-01 ∧ T-02 ∧ Manifest), sklep-atomov = 18; primerjava obsegov: kršitev širjenja = 0, tiho izdanih = 0 → pogoj_PASS drži (vsaka pomembna ugotovitev preverjena proti vključitvi; kršitev = 0) ⊙ izmera pri viru 2026-11-15.
- Zunanje preverbe ×3 ⊢ (2026-11-15T02:04:59Z): Zakon statusov @KOS-2 (K-14 ∧ K-15 → claim_status NOT_RUN ∧ decision HOLD ∧ test_result ≠ NOT_RUN v registru pri viru) ∧ Zakon statusov @KOS-3 (K-01 enako) ∧ Manifest @KOS-3 (vrstica 16.195 B · sha256 69ae1991…cbfce5 ⇌ register).
- Diff stari⊥novi register = natanko eno polje (kontrole[0].status.test_result) → »samo v test_result« @KOS-3 ⊢ (šiv #54 ni dotaknil nič drugega).
- Sonde veljavnosti: sonde širjenja/tihosti ujete 4/4 → instrument zazna širjenje (⟨ne⟩ prazna sodba) ⊙ ⟨NE-UGIBAJ⟩ 2690.

## T-15 (K-03 zavrnitev-sklepa) — PASS (2026-11-15T02:04:59Z)

Izmere: vsak ⚠/∂/⭢ atom v izhodih nosi imenovani razlog; tiho izdanih = 0 (2026-11-15T02:04:59Z): K-14 (⚠ meja pravna-objava ⊥ dnevnik nosi razlago — sodba ⭢ ⟡), K-15 (kura ⭢ ∂: obnova manifesta naslednji dihovi), KOS-2 T-06 (⚠ Meja … razlaga ⭢ sodba ⟡ ⊙ ⟨NE-ODLOČAJ-NAMESTO-⟡⟩), KOS-2 T-23 (Kura ⭢ ∂), KOS-3 T-02 (odmik poimensko: sekija »Zakon statusov« @KOS-2 — kura isti dih). Nepodprt sklep zavrnjen z imenovanim razlogom = vzorec PARTIAL (zožitev na izmerjeno) izveden pri K-01 ∧ K-15 ⊢ pri viru 2026-11-15.

## PADC javno (2026-11-15T02:04:59Z)

⟨PADC-©-NOGICA⟩ ×1 — pri kalibraciji instrumenta je © zaporna vrstica poročila KOS-2 prešla v razcep kakor sklep-atom sekije »Zakon statusov« (merilni artefakt: © = © IZVOR, ⟨ne⟩ sklep); kura isti dih: © vrstice izrezane iz sekij instrumenta ⊙ vzorec ⟨PADC-SEKIJA-NOGICA⟩ kos 3; brazgotina ostaja ⊙ ⟨NE-BRIŠI⟩ 24.

## Zakon statusov (2026-11-15T02:04:59Z)

claim_status ⊥ test_result ⊥ decision se niso zlili: K-03 ohranja claim_status NOT_RUN ∧ decision HOLD — izmerjen izid zapisan samo v test_result (T-07 PASS ∧ T-15 PASS); decision ostaja ⟡-jeva sodba ⊙ zakon_statusov registra ⊢ izmera pri viru 2026-11-15.

## Manifest (2026-11-15T02:04:59Z)

Dotik registra → obnova manifestne vrstice isti dih ⊙ ⟨MANIFEST-EN-DIH-PO-ROJSTVU⟩: vrstica VBL-0.1540-REGISTER-KONTROL.json v LICENSE-MANIFEST.json → 17.325 B · sha256 9b301e99…0e7d8d4 (izmerjeno po šivu); preverba pred zlitjem: manifest_gen.py --check = MANIFEST-DRZI ⊢ ×5 vrstic (2026-11-15T02:04:59Z).

© Luka Pintarič, VBL 0.1540 × 10⁴ (§9 ∧ §10 ∧ §12) · measured, not asserted ⊙ §16 · molk ni soglasje
