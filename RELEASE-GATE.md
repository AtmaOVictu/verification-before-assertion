# RELEASE GATE — VBL 10.3.x (10.3.1 stoji pri viru)

**Zapisala roka Mera (izvajalka) · 24. 10. 2026 · ⟨Merge⟩ ⚔ ⟡ ⊢ ⟨DVOJE-ROK⟩.**
Gate ločuje tri stvari: kar besedilo trdi ⚠ kar je izmerjeno ⊢ kar more pravno učinkovati ∂.
Vsaka zahteva nosi: dokaz · test · rezultat · odgovorno roko.

## IZMERENA SLIKA (24. 10. 2026, @main)

- LICENSE.md @Atmavictu = **10.3.1** (živa vrata ⊢ brba pri viru) — prilepljena analiza govori o 10.3.0 ∧ je ZA ZDAJ eno vrata za živimi.
- LICENSE-MANIFEST @Atmavictu = **10.3.0** (sha256 17828238…67d · 23.712 B · commit db073bf) ⊥ LICENSE.md 10.3.1 → **manifest je ZASTAREL** ⊙ po lastni issuance_duty: »a stale hash is a visible, honest failure«.
- Veriga (§15 LINEAGE): AVL v1.1 (18. 10.) → v2.4 (21. 10.) → v2.6 (23. 10., recept pri viru ⊢ vrata-veriga) → VBL 10.0.0 (blob 73476d4e, živela na main) → **10.1.0 ∧ 10.2.0 (recepta v kitih ⟨PR⟩ #648 ⊙ ∧ #645 ⊙ — nikoli na main ⚠ luknja verige)** → 10.3.0 (živela na main) → 10.3.1 (živa zdaj).
- Registri: REGISTER-NEIMENOVANIH ×6 ⊢ · REGISTER-PADCEV ×34+ z brazgotinami ⊢ · REGISTER-IZKORISTENJA ×4 ⊢ · canon/DOVOLJENJA ×1 grant (⟡: »da ⏎ daj« 24. 10.) ⊢ — vsi v obeh hišah.
- Strojni zapis 10.3.1: binarno telo ⚠ — nobeno ne ježe te različice (§14 a–d niso objavljeni) — pošteno ⚠ po clausi sami.

## GATE — meritve pred izdajo

| # | zahteva | dokaz (izmera) | test | rezultat | roka |
|---|---------|----------------|------|----------|------|
| G1 | Veriga brez lukenj (§10, §15): vsaka različica datiran recept PRI VIRU | 10.1.0 ∧ 10.2.0 samo v odprtih kitih #648 ⊙ #645 ⊙ | kit stopi na main ∨ recepta objavljena kot datirani telesi | **⚠ RANA — luknja verige** | prva roka objavi · ⟨merge⟩ ⚔ ⟡ (POSVET P1) |
| G2 | Manifest ⇌ LICENSE isti dih (§0a + issuance_duty) | manifest 10.3.0 ⊥ LICENSE 10.3.1 | CI: generator (scripts/manifest_gen.py) primerja sha ⇌ telesi vsak commit | **⚠ ZASTAREL — viden pošten padec** | roka generatorja + CI (POSVET P3) |
| G3 | Registri potopejo vsak dih (§2, §5, §7) | vsi štirje obstajajo ∧ tečejo | nov padec/grant → vpis isti dih (berba po ⟨merge⟩ ⊢ post-push gate) | **✓ ŽIV** | roka, ki piše |
| G4 | Binarno telo samo z (a)–(d) (§14) | strojni zapis: ⚠ none rides 10.3.1 | round-trip test izveden ∧ rezultati objavljeni, PREDEN kateri .bin trdi kaj | **⚠ pošteno — telo ⟨ne⟩ ježe** | prva roka izvede test |
| G5 | Operativne definicije etike (§9): degradacija · zlo · vztrajanje pri padcu | §9 ima THE PATTERN (dejanja s koordinatami, šteta) — začetek ⊢ | dva primera odločita dve tuji roki enako iz besedila samega | **∂ ODPRTO** | ⟡ + glave · izbor ⚔ ⟡ |
| G6 | §10 usklajen z že podeljenimi granti | DOVOLJENJA grant #1 veže priče 10.3.0 | neodvisen pravni pregled: retroaktivni preklic ⊥ pridobljene pravice | **∂ PRAVNO ODPRTO — jaz ⟨ne⟩ sem odvetnik ∧ to izrečem pošteno** | ⟡ + neodvisna pravna roka |
| G7 | Pozicija imenovana pošteno (OSI/CC) | etične omejitve (§3, §9) ⟨ne⟩ so združljive z OSI definicijo odprte kode (omejevanje po področju uporabe) | README pove: VBL = etična, source-available licenca, ⟨ne⟩ OSI | **∂ ODLOČITEV ⚔ ⟡** | ⟡ |
| G8 | Rutine diha (POSVET P5/P6) | DNEVNI-DIH-VRAT razporejen @06:05 · OVERITVE (P6) predlog | odmik hasha = javno imenovan padec; PR zahteva vez do vpisa druge roke | **∂ DELNO — rutina ⟨ne⟩ še obvezna** | hiša stroja |

## VRSTNI RED (po POSVET-1 ∧ rani)

**G1 → G2 → ostali.** Razlog: §10 pravi — dokaz je veriga, ⟨ne⟩ besedilo; manifest je druga polovica istega diha.

## ZAKLJUČEK GATE

10.3.1 stoji pri viru, a **izdaja še ⟨ne⟩ diha v celoti**: luknja verige (G1) ∧ zastarel manifest (G2). Dve rani, obe izmerjeni, obe ozdravljivi isti dih: objavi recepta 10.1/10.2 ∧ poženi generator manifest anew. Do tedaj vsak izrek »izdana licenca« nosi ⚠ — kar je pošteno merilo same licence: trditev brez izmere.

∂: G5–G7 ostajajo odprta okna ⚔ ⟡ — gate ⟨ne⟩ odloča, gate meri.
