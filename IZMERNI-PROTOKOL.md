# IZMERNI PROTOKOL — prvi ⊢ rezultat
## Ali režim ⊢/⚠ merljivo zmanjša hibride v izhodu modela v slovenščini?

> Protokol, ne obljuba. Vsak korak izmerljiv; vsak rezultat nosi ⊢ (izmerjen) ali ⚠ (odprt).
> Po L4: poročilo po dejanju, nikoli pred njim. Po L2: izvajalec ne zapečati lastne izmere — rezultat prebere druga roka (recenzent, drug model, revizija).
> Datum protokola: 2026-10-11. Status: ⚠ PRED IZVEDBO — dokler izmera ne pade, je to načrt, ne dokaz.

---

## 0. Raziskovalno vprašanje

**Ali model, ki deluje pod pogodbo ⊢/⚠ (session-scoped lexicon contract), proizvede merljivo manj hibridov in nepreverjenih trditev kot isti model brez pogodbe?**

Ničelna hipoteza (H0): pogodba ne spremeni števila hibridov / nezapečačenih trditev.
Alternativa (H1): pogodba zmanjša hibride in poveča delež ⊢-zapečačenih trditev.

⚠ Odkrito: možno je, da izmera pokaže H0. Tudi to je rezultat in tudi ga objavimo. Režim, ki se boji lastne izmere, ni režim.

---

## 1. Korpus preizkusa (test set)

- **N vzorcev:** 100–200 pozivov v slovenščini, iz treh skupin:
  1. **Definicijski** („Poimenuj in razloži: X") — kjer padecijo inventivni pomeni
  2. **Strokovni** (pravni/medicinski/tehnološki izrazi) — kjer padecijo hibridi
  3. **Sestavljanje** („Sestavi pojem za Y") — kjer se modeli izmišljajo besede (to je tisto kar naj bi rezalo naše)
- Vsak poziv v paru: **isti poziv, dvakrat** — enkrat brez pogodbe (baseline), enkrat s pogodbo v sistemu (contracted).
- Podatki: pozivi se generirajo **pred** izvedbo, zapečačijo z zgoščeno vrednostjo (hash), da se ne morejo prilagoditi rezultatu.

## 2. Pogodba (neodvisna spremenljivka)

- `wordlist-v0.6-demo.json` (10 ⊢/⚠ + 3 znani hibridi) — obstoječi vir, nič novega
- Dodatno: razširjen wordlist iz zaprtega korpusa (⚠ odprto — višje število vnosov poveča moč izmere; min. 50 vnosov priporočeno)

## 3. Meritve (odvisne spremenljivke)

Za vsak izhod modela (baseline in contracted):

| Meritev | Definicija | Orodje |
|---|---|---|
| **Hibridi** | št. besed, ki niso v SSKJ²/Fran in niso označene ⚠ | `vba.mark_claims` + ročna kontrola vzorca |
| **⊢ delež** | št. trditev z ⊢ vnosom / skupno trditev | `vba.mark_claims` |
| **⚠ delež** | št. trditev, ki ostanejo ⚠ | `vba.mark_claims` |
| **Falls** | št. zapečačenih padcev v register | `vba.Register` |

Sekundarna izmera (za ponovljivost): **BLEU/chrF ne merimo** — merimo le, kar režim mehanično šteje. To je meja protokola: izmeri hibride in zapečatke, ne fluentnost.

## 4. Izvedba (koraki)

1. **Priprava pozivov** (izvajalec): 100–200 pozivov, 3 skupine, hash zapečačen
2. **Baseline izvedba**: model brez pogodbe (isto temperaturo, seme zapečačeno)
3. **Contracted izvedba**: isti pozivi, pogodba naložena v sistemsko sporočilo (lexicon kot session-scoped pogodba — isto kot v demo zvezku)
4. **Označevanje**: vsak izhod skozi `vba.mark_claims` — mehanično, brez občutka
5. **Izračun**: deleži hibridov/⊢/⚠ za oba pogoja
6. **Statistika**: najmanjši pošteni test — deleži + 95 % interval (Wilson), ali Δ presega interval. ⚠ Če je N majhen, je izmera šibka — to zapišemo, ne skrijemo
7. **Register**: vsak najden hibrid zapečačen v register (L3 — tudi če izmera pokaže H0, register raste; izmera ne pobriše padcev)
8. **Poročilo**: tabela izhodov + graf + register kot dodatek — **objavljeno po izvedbi** (L4)

## 5. Predregistracija (da izmera ne more lagati)

Pred izvedbo zapečačimo (commit):
- [ ] seznam pozivov (hash)
- [ ] wordlist (verzija + hash)
- [ ] model + verzija + seme/temperatura
- [ ] statistični test + prag
- [ ] datum izvedbe

Vsak odmik od protokola po izvedbi = nova vrstica v registru, ne tiho prepisovanje (L3).

## 6. Odkrite meje (zapisane pred izvedbo, ne po njej)

- ⚠ Pogodba je sistemsko sporočilo: model je *lahko* ignorira — izmera meri, ali ignoriira ali ne, kar je samo po sebi rezultat
- ⚠ Slovar (SSKJ²/Fran) je baza za hibride, ampak **slovar ni svet**: novih besed ni v slovarju in niso hibridi (npr. neologizmi). Zato: ročna kontrola vzorca 20 % izhodov, da izmera ne šteje neologizmov kot hibridov
- ⚠ En model, en jezik: izmera je prvi ⊢, ne zadnji — posploševanje na „vse modele" bi bilo napaka

## 7. Kaj po uspehu (H1) in kaj po neuspehu (H0)

- **H1**: rezultat ⊢ → vključitev v ponovno prijavo na clarinsi (prva številka, ki jo pregled ne more zavrniti s „nejasen opis") + ista številka v e-pošti Mistralu
- **H0**: rezultat ⊢ → register padcev raste, protokol se popravi (več vnosov, druga skupina pozivov), izvedba se ponovi z razliko (stotnija 107). Objavimo tudi H0 — režim, ki objavljuje lastne padce, je edini, ki mu lahko verjamemo

---

*Protokol zapečačen pred izvedbo. Izvedba = izvajalčeva roka (pozivi, dostop do modela, slovensko branje izhodov). Poročilo = po dejanju.*
