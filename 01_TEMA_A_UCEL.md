# 1. Téma a účel projektu

## Doména

Projekt sa venuje pracovným ponukám, zručnostiam a vzdelávaniu naprieč IT. Zahŕňa rôzne pracovné oblasti, napríklad vývoj softvéru, testovanie, analytiku, správu systémov a kybernetickú bezpečnosť.

Znalostný graf prepojí uchádzačov a ich zručnosti s pracovnými ponukami, požiadavkami zamestnávateľov a kurzmi, ktoré učia konkrétne zručnosti. Súčasťou domény sú aj firmy zverejňujúce ponuky a poskytovatelia kurzov.

## Cieľový používateľ

Cieľovým používateľom je človek, ktorý sa chce uplatniť v IT, posunúť sa v kariére alebo zmeniť špecializáciu. Môže ísť o študenta, začínajúceho uchádzača aj skúseného pracovníka, napríklad testera so záujmom o automatizované testovanie.

Projekt nie je obmedzený iba na juniorské alebo dátové pozície. Ukážkový scenár môžeme postaviť na študentovi.

## Účel projektu

Cieľom je pomôcť uchádzačovi porovnať svoje zručnosti s požiadavkami pracovných ponúk, identifikovať chýbajúce zručnosti a vybrať kurz, ktorý mu umožní splniť zručnostné požiadavky ďalších ponúk.

**Hlavná otázka projektu:** Ktorý kurz umožní uchádzačovi splniť požiadavky najväčšieho počtu nových pracovných ponúk vzhľadom na jeho súčasné zručnosti?

Odporúčanie má byť vysvetliteľné: okrem kurzu má ukázať doplnené zručnosti aj konkrétne nové ponuky, ktorých zručnostné požiadavky uchádzač následne pokryje.

## Prípad použitia

1. Poznáme zoznam zručností uchádzača.
2. Porovnáme ho s povinnými zručnosťami pracovných ponúk.
3. Určíme ponuky, ktorým už zodpovedá, a zručnosti, ktoré mu pri ostatných chýbajú.
4. Vyhodnotíme, ako by získanie zručností z jednotlivých kurzov zmenilo jeho situáciu.
5. Porovnáme kurzy podľa počtu nových ponúk a zobrazíme vysvetlenie výsledkov.

## Dohodnuté pravidlá a rozsah

- **Zručnosti bez úrovní:** evidujeme konkrétne zručnosti, napríklad Python, SQL alebo Git, bez rozlíšenia začiatočníckej a pokročilej úrovne.
- **Povinné zručnosti:** pri ponukách vyhodnocujeme zoznam povinných zručností. Uchádzač spĺňa zručnostné požiadavky ponuky, keď pokrýva všetky uvedené povinné zručnosti.
- **Jeden kurz naraz:** každý kurz hodnotíme samostatne vzhľadom na pôvodné zručnosti uchádzača.
- **Úspešné absolvovanie:** pri posudzovaní prínosu predpokladáme získanie všetkých zručností, ktoré vybraný kurz učí. Pridávajú sa k pôvodným zručnostiam uchádzača.
- **Iba nové ponuky:** do prínosu kurzu nezapočítavame ponuky, ktorých požiadavky uchádzač pokrýval už pred kurzom. Každú novú ponuku počítame iba raz.
- **Hlavné kritérium:** odporúčanie vychádza z počtu nových ponúk, ktorých všetky povinné zručnosti uchádzač po kurze pokryje.
- **Doplnkové údaje:** cenu a dĺžku kurzu evidujeme na ďalšie porovnávanie; nemenia hlavné kritérium odporúčania.

Vyhodnocovanie vychádza zo zručností a požiadaviek evidovaných v dátach. „Sprístupnenie ponuky“ znamená splnenie jej evidovaných zručnostných požiadaviek; nepredstavuje záruku prijatia do zamestnania.

## Ilustračný príklad

Uchádzač ovláda SQL. Posudzovaný kurz učí Python.

| Ponuka | Povinné zručnosti | Pred kurzom | Po kurze |
| --- | --- | --- | --- |
| A | SQL | Spĺňa | Spĺňa |
| B | SQL, Python | Nespĺňa | Spĺňa |
| C | Python, Git | Nespĺňa | Nespĺňa — chýba Git |

**Prínos kurzu je jedna nová ponuka: B.** Ponuka A bola dostupná už pred kurzom a pri ponuke C stále chýba povinná zručnosť.

## Kompetenčné otázky

| ID | Otázka |
| --- | --- |
| CQ1 | Pri ktorých pracovných ponukách uchádzač už spĺňa všetky požadované zručnosti? |
| CQ2 | Ktoré zručnosti mu chýbajú pri konkrétnej ponuke? |
| CQ3 | Ktoré kurzy učia zručnosti, ktoré uchádzačovi chýbajú pri vybranej ponuke? |
| CQ4 | Ktorý kurz umožní uchádzačovi splniť požiadavky najväčšieho počtu nových ponúk? |
| CQ5 | Ktoré konkrétne nové ponuky by uchádzačovi sprístupnil vybraný kurz? |
| CQ6 | Ktoré zručnosti vyžaduje najväčší počet pracovných ponúk? |
| CQ7 | Ktorý kurz má najnižšiu cenu na jednu novú sprístupnenú ponuku? |
| CQ8 | Koľko požadovaných zručností uchádzačovi priemerne chýba pri ponukách jednotlivých firiem? |

**CQ4 je hlavná otázka projektu.** CQ2, CQ3 a CQ5 pomáhajú odporúčanie vysvetliť. CQ6–CQ8 dopĺňajú analytické pohľady: početnosť, pomer ceny a prínosu a priemerný počet chýbajúcich zručností.

Pri CQ7 porovnávame iba kurzy, ktoré uchádzačovi sprístupnia aspoň jednu novú ponuku.
