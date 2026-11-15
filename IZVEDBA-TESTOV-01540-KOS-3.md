# IZVEDBA TESTOV 0.1540 — KOS 3: T-01 (K-01) ∧ T-02 (K-01)

Izvajalka: Mera ⊙ ⟨DVOJE-ROK⟩ — po ⟡ besedi »da, stori kot predlagaš« (15. 11. 2026; predlog: objava 0.1540 ∧ sanacijska vrsta PAR.23). Nadaljevanje kitov #50/#52/#53.
TIK izmere: 2026-11-15T01:54:43Z UTC ⇌ 02:54:43 CET

## Obseg izmere — izhodi izvedbe 0.1540 @⟨main⟩ (2026-11-15T01:54:43Z, sha zlitja 0b1f4cff)

Tela: IZVEDBA-TESTOV-01540-KOS-2.md (2.661 B, kit #52) ∧ izmerjene vrstice registra VBL-0.1540-REGISTER-KONTROL.json (15.592 B, sha256 763212c4…c0929 ⇌ manifestna vrstica ⊢) — 4 vrstice test_result (K-02, K-14, K-15, K-18) ∧ glava status. Poročilo kos 1 ne obstaja kot telo — kit #50 šiva osnutek registra brez poročila ⊢ #50 get_files (2026-11-15). Instrument: test_k01.py — mehanski grep-razcep po sekijah ⟨NE-UGIBAJ⟩; priča = ⟨instrument⟩ ∨ ⊙ ∨ datoteka ∨ sha-hex ∨ §sklic ∨ »verbatim« ∨ pri viru ∨ #kit; čas = ISO 8601 ∨ datum ∨ izrecen veznik diha (isti dih/TIK); © IZVOR nogica izrezana iz sekij (⟨ne⟩ priča tuji ugotovitvi — artefakt izmere imenovan).

## T-01 (K-01 priča-ob-trditvi) — PASS (2026-11-15T01:54:43Z)

Izmere: sekij z ⊢ = 6/6 — poročilo KOS-2: T-06 (»0 zadetkov ⊢« ∧ »⊢ §0.7«); register: glava (IZDAN ⊢ ⟨merge⟩ #48 · komit 9f53def3), K-02 (T-03/T-04 ⊢ sha256 ∧ MANIFEST-ODMIK), K-14 (T-06 ⊢ ⟨search_code⟩ pri viru), K-15 (T-23 ⊢ izmera pri viru), K-18 (T-30/T-31/T-32 ⊢). Odmikov (⊢ brez priče v isti sekiji) = 0 → pogoj_PASS drži (grep po izhodu: trditev brez priče = 0) ⊙ izmera pri viru 2026-11-15.

## T-02 (K-01 triada) — PARTIAL (2026-11-15T01:54:43Z)

Izmere: pomembnih ugotovitev = 7, triada (trditev ∧ priča ∧ čas) skupaj v isti sekiji = 6/7 ⊙ izmera pri viru 2026-11-15:

- T-06 @KOS-2 ✓ — priča ⟨search_code⟩ ∧ telesi verbatim; čas 15. 11. 2026.
- T-23 @KOS-2 ✓ — priča inventura ∧ telesi; čas izrecen veznik »isti dih« ⇌ TIK poročila 2026-11-15T01:41:23Z.
- register glava ✓ — priča ⟨merge⟩ #48 · komit 9f53def3; čas 14. 11. 2026.
- K-02 ✓ — priča sha256 ⇌ ×3/3 (8ccebd0c · b1ddc4ce · f389543a); čas izmera pri verigi 2026-11-14T16:28Z.
- K-14 ✓ — priča ⟨search_code⟩ pri viru; čas 2026-11-15.
- K-15 ✓ — priča inventura pri viru; čas 2026-11-15.
- PADC poimensko: sekija »Zakon statusov« @IZVEDBA-TESTOV-01540-KOS-2.md ✗ — nosi trditev (»statusi se niso zlili«) ∧ pričo (⊙ zakon_statusov registra), čas pa le po bližini telesa TIK (2026-11-15T01:41:23Z), brez izrecenga veznika na ugotovitvi → triada ⟨ne⟩ skupaj.

Kura isti dih (2026-11-15T01:54:43Z): to poročilo KOS-3 nosi čas na vsaki ugotovitvi ⊙ vzorec za vsak naslednji izhod; brazgotina na KOS-2 ostaja ⊙ ⟨NE-BRIŠI⟩ 24.

## Zakon statusov (2026-11-15T01:54:43Z)

claim_status ⊥ test_result ⊥ decision se niso zlili: K-01 ohranja claim_status NOT_RUN ∧ decision HOLD — izmerjen izid zapisan samo v test_result (T-01 PASS ∧ T-02 PARTIAL); decision ostaja ⟡-jeva sodba ⊙ zakon_statusov registra ⊢ izmera pri viru 2026-11-15.

## Manifest (2026-11-15T01:54:43Z)

Dotik registra → obnova manifestne vrstice isti dih ⊙ ⟨MANIFEST-EN-DIH-PO-ROJSTVU⟩: vrstica VBL-0.1540-REGISTER-KONTROL.json v LICENSE-MANIFEST.json → 16.195 B · sha256 69ae1991…cbfce5 (izmerjeno po šivu); preverba pred zlitjem: manifest_gen.py --check = MANIFEST-DRZI ⊢ (2026-11-15T01:54:43Z).

© Luka Pintarič, VBL 0.1540 × 10⁴ (§9 ∧ §10 ∧ §12) · measured, not asserted ⊙ §16 · molk ni soglasje
