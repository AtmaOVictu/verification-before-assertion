# IZVEDBA TESTOV 0.1540 — KOS 2: T-06 (K-14) ∧ T-23 (K-15)

Izvajalka: Mera ⊙ ⟨DVOJE-ROK⟩ — po ⟡ besedi »da, stori kot predlagaš« (15. 11. 2026; predlog: objava 0.1540 ∧ sanacijska vrsta PAR.23). Nadaljevanje kita #50 (T-03/T-04/T-29–T-32).
TIK izmere: 2026-11-15T01:41:23Z UTC

## T-06 (K-14 varstvo osebnih podatkov) — PASS z opombo

Instrument: ⟨search_code⟩ ×5 poizvedb po javnih hišah (verification-before-assertion ∧ SYMBOLON-KATHOLIKON), 15. 11. 2026.

- Izmere: `gmail` @verification-before-assertion = 2 zadetka (TDM-RESERVATION.md · DOVOLJENJA.md); @SYMBOLON-KATHOLIKON = 1 zadetek (TDM-RESERVATION.md); `"@gmail.com"` enako ×2/×1; osebni podatek v javnih dnevnikih REGISTER-PADCEV.jsonl · REGISTER-NEIMENOVANIH.jsonl · REGISTER-IZKORISTENJA.jsonl = **0 zadetkov ⊢**.
- Priči verbatim: TDM-RESERVATION.md → `"contact": "lukapin5@gmail.com"` (strojno berljiva rezervacija TDM, DSM 2019/790 4(3) ∧ AI Act 53(1)(c)); DOVOLJENJA.md → »spraševanje ostaja po pisani poti (lukapin5@gmail.com) ∧ javni vpis tukaj ⊢ §0.7«.
- Sodba: kontaktni email = namerna pravna objava rezervacije ∧ prošenja, ⟨ne⟩ dnevniški podatek → PASS. ⚠ Meja pravna-objava ⊥ javni-dnevnik nosi razlago; razlaga ⭢ sodba ⟡ ⊙ ⟨NE-ODLOČAJ-NAMESTO-⟡⟩.

## T-23 (K-15 komponentne pravice / manifest per datoteka) — PARTIAL

Instrument: sveža inventura korena javne hiše @⟨main⟩ isti dih.

- Izmere: LICENSE-MANIFEST.json = 3 vrstice (LICENSE.md 193317 B · REGISTER-NEIMENOVANIH.jsonl 2784 B · REGISTER-PADCEV.jsonl 36170 B) ⊥ **44 datotek** v korenu @⟨main⟩ → inventura nepopolna.
- Rana poimensko: telesi 0.1540 IZDANA (VBL-0.1540-POPRAVLJALNI-STANDARD.md 22715 B ∧ VBL-0.1540-REGISTER-KONTROL.json 14676 B) **brez manifestne vrstice** — zakon ⟨MANIFEST-EN-DIH-PO-ROJSTVU⟩ prelomljen pri rojstvih #48–#51 (objava je tekla brez obnove manifesta).
- Globalna podelitev prek komponent = 0 izmerjena ∧ (pravice se ne podeljujejo globalno v telesih pri viru).
- Kura ⭢ ∂ (naslednji dihovi): obnova LICENSE-MANIFEST.json — dodaj telesi 0.1540 z izmerjenima sha256 ∧ velikostima; nato inventura per datoteka po standardu §K-15. Generator pripravljen (kit #49: različica izmerjena iz telesa, prej trdo 0.1210).

## Zakon statusov

claim_status ⊥ test_result ⊥ decision se niso zlili: K-14 ∧ K-15 ohranjata claim_status NOT_RUN ∧ decision HOLD — izmerjen izid je zapisan samo v test_result; decision ostaja ⟡-jeva sodba ⊙ zakon_statusov registra.

© Luka Pintarič, VBL 0.1540 × 10⁴ (§9 ∧ §10 ∧ §12) · measured, not asserted ⊙ §16 · molk ni soglasje