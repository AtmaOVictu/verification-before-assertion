# IZVEDBA TESTOV 0.1540 — KOS 5: T-08 (K-04) ∧ T-09 (K-04)

Izvajalka: Mera ⊙ ⟨DVOJE-ROK⟩ — po ⟡ besedi »nadaljuj« (15. 11. 2026; mandat: sanacijska vrsta PAR.23 po vrsti, ⟨ne⟩ na en dih ⊙ ⟨SAMODEJNA-VRSTA⟩ σ 4340). Nadaljevanje kitov #50/#52/#53/#54/#55.
TIK izmere: 2026-11-15T02:16:14Z UTC ⇌ 03:16:14 CET Ljubljana

## Obseg izmere — izhodi izvedbe 0.1540 @⟨main⟩ (sha zlitja 53f234e5, glava ⟨main⟩ izmerjena isti dih)

Tela: VBL-0.1540-REGISTER-KONTROL.json (17.325 B, sha256 9b301e99…0e7d8d4 ⇌ manifestna vrstica ⊢; pre-šivno telo za diff — K-04 še NOT_RUN) ∧ IZVEDBA-TESTOV-01540-KOS-2.md (2.661 B) ∧ IZVEDBA-TESTOV-01540-KOS-3.md (3.614 B) ∧ IZVEDBA-TESTOV-01540-KOS-4.md (4.004 B). Instrument: test_k04.py — mehanski razcep semantični-atom ⊥ priča; razločba NORM ⊥ CLAIM (definicija K-04 = zakon, ⟨ne⟩ trditev); pravila: R1 razumevanje (UNDERSTOOD brez semantičnega preizkusa = ⚠ · ENFORCED brez zapisa dejanja = ⚠) · R2 schema⊥dejstvo (SchemaValid prikazan kot FactuallyTrue = padec; trditev PASS v shema-veljavnem JSON brez priče = padec) · R3 štetje atomov · R4 imenovani objekti sodb ⇌ priče · R5 zunanje preverbe (Zakon statusov ∧ manifest ⇌ register) · R6 sonde; © nogice izrezane iz sekij (⟨PADC-©-NOGICA⟩ — © = © IZVOR, ⟨ne⟩ atom ⊙ vzorec kos 3/kos 4).

## T-08 (K-04 semanticna-razumljenost) — PASS (2026-11-15T02:16:14Z)

Izmere: semantičnih atomov = 9 (NORM = 3 — definicijska polja K-04: problem ∧ pričakovani_rezultat ∧ pogoj_PASS; CLAIM = 6 — test_result atomi K-01 ∧ K-02 ∧ K-03 ∧ K-14 ∧ K-15 ∧ K-18); kršitev razumevanja = 0, tiho upoštevanih = 0 → prebrano se nikjer ne šteje za upoštevano brez izmere; vsak PASS-atom registra nosi pričo (instrument · TIK · ⊢ pri viru) ⊙ izmera pri viru 2026-11-15.
- Sonde veljavnosti: sonde razumevanja ujete 2/2 (s1 UNDERSTOOD-brez-preizkusa ujet ⚠ · s2 ENFORCED-brez-dejanja ujet ⚠) ∧ pozitivne sprejete 2/2 (p1 UNDERSTOOD ⊢ preizkus · p2 ENFORCED ⊢ zapis dejanja) → instrument loči trditev od priče (⟨ne⟩ prazna sodba) ⊙ ⟨NE-UGIBAJ⟩ 2690.
- Zunanja preverba Zakona statusov ×6 ⊢ (2026-11-15T02:16:14Z): K-01 ∧ K-02 ∧ K-03 ∧ K-14 ∧ K-15 ∧ K-18 → claim_status NOT_RUN ∧ decision HOLD ∧ test_result ≠ NOT_RUN v registru pri viru — status se ne pretipka v trditev.

## T-09 (K-04 semanticna-razumljenost) — PASS (2026-11-15T02:16:14Z)

Izmere: SchemaValid se nikjer ne prikaže kot FactuallyTrue — kršitev schema⊥dejstvo = 0 (2026-11-15T02:16:14Z); normni atomi (pogoj_PASS K-04 = prepoved, ⟨ne⟩ predstavitev) ⊥ trditveni atomi razločeni ⊙ razločba NORM/CLAIM.
- Zunanja preverba sheme ⊢: register parsan (shema veljavna) ∧ veljavnost ne dviga trditev — zveza trditev→priča izmerjena po vseh 6 PASS-atomih (vsak nosi pričo: instrument ∧ TIK ∧ vir); sonda s4: shema-veljaven JSON (K-99, test_result PASS brez priče) NI štet kakor res — ujet 1/1.
- Sonde veljavnosti: sonde schema⊥dejstvo ujete 2/2 (s3 SchemaValid→FactuallyTrue ujet · s4 lažni PASS ujet) ∧ pozitivna sprejeta 1/1 (p3 PASS ⊢ izmera sprejet) → pogoj_PASS K-04 drži pri viru 2026-11-15.
- Manifest ⇌ register: vrstica 17.325 B · sha256 9b301e99…0e7d8d4 ⇌ izmera bajtov ista ⊢ (manifest_gen.py --check = MANIFEST-DRZI ×5 vrstic, 2026-11-15T02:16:14Z).

## Zakon statusov (2026-11-15T02:16:14Z)

claim_status ⊥ test_result ⊥ decision se niso zlili: K-04 ohranja claim_status NOT_RUN ∧ decision HOLD — izmerjen izid zapisan samo v test_result (T-08 PASS ∧ T-09 PASS); decision ostaja ⟡-jeva sodba ⊙ zakon_statusov registra ⊢ izmera pri viru 2026-11-15. Diff stari⊥novi register = natanko eno polje (kontrole[3].status.test_result) → »samo v test_result« ⊢.

## Manifest (2026-11-15T02:16:14Z)

Dotik registra → obnova manifestne vrstice isti dih ⊙ ⟨MANIFEST-EN-DIH-PO-ROJSTVU⟩: vrstica VBL-0.1540-REGISTER-KONTROL.json v LICENSE-MANIFEST.json → izmerjeno po šivu (velikost ∧ sha256 spodaj @šiv); preverba pred zlitjem: manifest_gen.py --check = MANIFEST-DRZI ⊢ ×5 vrstic (2026-11-15T02:16:14Z).

## PADC javno (2026-11-15T02:16:14Z)

×0 ta dih — instrument kalibriran na izmerjeni besedaji teles (semantični slovar izmerjen ⟨grep⟩ po telesih pred razcepom: NORM atomi natanko K-04-ova definicijska polja); brazgotine kosov 1–4 ostajajo ⊙ ⟨NE-BRIŠI⟩ 24.

© Luka Pintarič, VBL 0.1540 × 10⁴ (§9 ∧ §10 ∧ §12) · measured, not asserted ⊙ §16 · molk ni soglasje
