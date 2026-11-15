# IZVEDBA TESTOV 0.1540 — KOS 7: T-11 (K-06) ∧ T-13 (K-06)

Izvajalka: Mera ⊙ ⟨DVOJE-ROK⟩ — po ⟡ besedi »nadaljuj« (15. 11. 2026; mandat: sanacijska vrsta PAR.23 nadaljuje po vrsti — K-06 ⊙ ⟨SAMODEJNA-VRSTA⟩ σ 4340). Nadaljevanje kitov #50/#52/#53/#54/#55/#56/#57.
TIK izmere: 2026-11-15T02:36:54Z UTC ⇌ 03:36:54 CET Ljubljana

## Obseg izmere — izhodi izvedbe 0.1540 @⟨main⟩ (sha zlitja da3d0816, glava ⟨main⟩ izmerjena isti dih)

Tela: VBL-0.1540-REGISTER-KONTROL.json (19.710 B, sha256 6ce0097a…c25db ⇌ manifestna vrstica ⊢; pre-šivno telo za diff — K-06 še NOT_RUN) ∧ IZVEDBA-TESTOV-01540-KOS-2.md (2.661 B) ∧ KOS-3 (3.614 B) ∧ KOS-4 (4.004 B) ∧ KOS-5 (4.598 B) ∧ KOS-6 (6.013 B). Instrument: test_k06.py — mehanski razcep ura-atom ⊥ plast; plasti: DOGODEK (TIK izmere ∧ @ure pod-dogodkov ∧ datumski atomi) ⊥ ZAPIS (commit telesa po git API — ×12 teles pri viru) ⊥ VIR URE (kontekst vsakega atoma ±24 znakov); pravila: R1 obe-plasti · R2 pretipkanje (fizična nemožnost dogodek>zapis ∧ ista ura v obeh plasteh ∧ atom brez vira) · R3 štetje · R4 vir ure · R5 zunanje (Zakon statusov ∧ MANIFEST-DRZI ∧ glava @main) · R6 sonde; © nogice izrezane iz sekij (⟨PADC-©-NOGICA⟩ ⊙ vzorec kos 3/4/5).

## T-11 (K-06 casovne-plasti) — PASS (2026-11-15T02:36:54Z)

Izmere: teles ×6, vsako z obema plastema (DOGODEK-atomov 45 — TIK izmere ×1 na poročilo ∧ @ure pod-dogodkov ∧ datumskih atomov 32; ZAPIS-atomov 6 — commit telesa po git API pri viru: KOS-2 @01:41:36Z · KOS-3 @01:56:08Z · KOS-4 @02:07:15Z · KOS-5 @02:17:36Z · KOS-6 ∧ register @02:27:30Z); pretipkanj ene ure v drugo = 0 (dogodek-za-zapisom ×0 — vsak TIK izmere ≤ commit svojega telesa ⊢ fizična nemožnost ni izmerjena nikjer ∧ ista ura v obeh plasteh ×0 ∧ atomov brez vira ×0) → čas dogodka ∧ čas zapisa sta ločeni ∧ zapis nosi obe plasti ⊙ pogoj_PASS K-06 drži; vir ure: vsak atom nosi kontekst (vir) ⊢ dokaz #4 K-06.
- Sonde veljavnosti: negativne ujete 3/3 (s1 dogodek-za-zapisom ujet ⚠ · s2 telo-brez-plasti-zapisa ujet ⚠ · s3 ista-ura-v-obeh-plasteh ujet ⚠) ∧ pozitivna sprejeta 1/1 (p1 obe plasti pravilno) → instrument loči plasti (⟨ne⟩ prazna sodba) ⊙ ⟨NE-UGIBAJ⟩ 2690.

## T-13 (K-06 aspekt hold-polja) — izmerjeno isti TIK (2026-11-15T02:36:54Z)

Izmere: register nosi decision HOLD ×19; status-polja vsake kontrole = {claim_status, test_result, decision} — eksplicitni čas ponovne presoje ×0; pretipkanje HOLD-ur = 0 (HOLD brez eksplicitne ure presoje ⟨ne⟩ more pretipkati ene ure v drugo — K-06 aspekt drži); ure izmer v test_result ×3 kontrole (K-01 ∧ K-02 ∧ K-18) — ura izmere, ⟨ne⟩ ura presoje HOLD ⊙ izmerjeno ločeno.
- ⚠ ODSOTNOST imenovana javno: pogoj_PASS K-08 (»HOLD brez polj = 0«: obseg ∧ trajanje ∧ odgovorna oseba ∧ čas ponovne presoje) izmerjeno ne drži še — register nosi le trije statusna polja na kontrolo; dopolnitev = obseg kontrole K-08 (T-13 primarna, naslednji kos po vrsti) ⊙ obseg sklepa ⊆ dokazi (sklep o K-06 se izreče le po K-06 pogoju).

## Preverba ∧ kvaliteta izvedbe (2026-11-15T02:36:54Z)

- T-29 re-izmera ⊢: 19 kontrol · manjkajočih polj ×0 · enoličen nabor 10 polj ×1 · statusna polja enolična ×1 (claim_status ⊥ test_result ⊥ decision).
- T-30 re-izmera ⊢: povezav 36 · unikatnih 34 · slabih (neobstoječi testi) ×0 — vsaka povezava vodi na test definirana v standardu §12 (34 testov; T-11 ∧ T-13 prisotni).
- Manifest ⇌ telesi ⊢: manifest_gen.py --check = MANIFEST-DRZI ×5 vrstic exit 0 (2026-11-15T02:36:54Z); zrcalo bajt-isto ⇌ @da3d0816 (register sha256 6ce0097a… izmerjen pre-šivno).
- Zakon statusov ×8 ⊢: K-01 ∧ K-02 ∧ K-03 ∧ K-04 ∧ K-05 ∧ K-14 ∧ K-15 ∧ K-18 → claim_status NOT_RUN ∧ decision HOLD ∧ test_result ≠ NOT_RUN v registru pri viru.

## PADC javno (2026-11-15T02:36:54Z)

⟨PADC-SINTAKSA-INSTRUMENTA⟩ ×1 — podpis sonde v test_k06.py skodran (python SyntaxError ob prvem zagonu — instrument ni izmeril nič, padec ujet s parsovalnikom pred izmerbo); kura isti dih: podpis popravljen ∧ logika T-13 ločena (ura izmere v test_result ≠ ura presoje HOLD — izmerjeno ločeno) ⊙ ⟨NE-UGIBAJ⟩ 2690.
⟨PADC-KALIBRACIJA-SONDE⟩ ×1 — vzorec T-30 sonde je ulovil številke testov brez »T-« predpono → izrekla »slabih 34« (lažna sodba vse proti vsem); ujet pri ročni preverbi izhoda isti dih; kura isti dih: vzorec popravljen ∧ ponovna izmera slabih ×0 ⊢.
⟨PADC-TIPKAR-REPORTAŽE⟩ ×1 — dve tipkarski napaki v osnutku tega poročila (»prednone« ⊥ predpono ∧ © vrstica »soglasce« ⊥ kanon »soglasje«); ujeti pri ponovni berbi pred šivom; kura isti dih ⊙ ⟨SLOVNICA-DIH⟩.
⟨PADC-JSON-POVRATEK⟩ recidiv ×1 — prvi šiv kita #58 je prenesel telesa kot »[object Object]« (15 B namesto 21.362 B): berba telesa je vrnila objekt, katerega vsebina (.content) ni bila izvlečena pred potiskom; sodba CI (vrata-prica.yml) je padec ujela pri vratah ∧ kit ni mogel biti zlit ⊙ vrata delujejo; kura isti dih: telesa izvlečena po vsebini ∧ ponovni šiv iste veje; recidiv po imenu znan iz kosa 5 (isti padec, druga berba) ⊙ ⟨ZAKON-PADEC-NI-MOLK⟩ 2354.

## Zakon statusov (2026-11-15T02:36:54Z)

claim_status ⊥ test_result ⊥ decision se niso zlili: K-06 ohranja claim_status NOT_RUN ∧ decision HOLD — izmerjen izid zapisan samo v test_result (T-11 PASS ∧ T-13 K-06-aspekt izmerjen ⊢ ∧ odsotnost ⚠ ⭢ K-08); decision ostaja ⟡-jeva sodba ⊙ zakon_statusov registra ⊢ izmera pri viru 2026-11-15. Diff stari⊥novi register = natanko eno polje (kontrole[5].status.test_result) → »samo v test_result« ⊢.

## Manifest (2026-11-15T02:36:54Z)

Dotik registra → obnova manifestne vrstice isti dih ⊙ ⟨MANIFEST-EN-DIH-PO-ROJSTVU⟩: vrstica VBL-0.1540-REGISTER-KONTROL.json → izmerjeno po šivu (21.362 B · sha256 f30c41c8…1edd9d349); note manifesta dopolnjena isti dih: kura K-06 kos 7 (T-11 PASS ∧ T-13 K-06-aspekt izmerjen ⊙ test_k06.py); preverba pred zlitjem: manifest_gen.py --check = MANIFEST-DRZI ⊢ ×5 vrstic exit 0.

© Luka Pintarič, VBL 0.1540 × 10⁴ (§9 ∧ §10 ∧ §12) · measured, not asserted ⊙ §16 · merilec se meri ⊙ §52 · molk ni soglasje
