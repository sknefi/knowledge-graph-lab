# Kontrolný zoznam projektu

Kontrolný zoznam podľa aktualizovaného zadania semestrálneho projektu pre predmety 4IZ444/4IZ441, určený pre **dvojčlenný tím**. Odporúčania navyše sú oddelené na konci.

## 1. Téma a účel

- [x] Opísať doménu projektu: pracovné ponuky, zručnosti a vzdelávanie v IT.
- [x] Určiť konkrétny prípad použitia.
- [x] Vysvetliť, komu má znalostný graf slúžiť a čo mu umožní zistiť.
- [x] Vytvoriť **5–10 kompetenčných otázok**, na ktoré má graf odpovedať.

Dokumentácia: [Téma a účel projektu](01_TEMA_A_UCEL.md).

## 2. Návrh ontológie

- [ ] Odvodiť model od kompetenčných otázok.
- [ ] Definovať **5–15 tried**.
- [ ] Definovať **10–30 vlastností**.
- [ ] Zahrnúť axiómy alebo obmedzenia, napríklad domény a rozsahy vlastností či hierarchie tried.
- [ ] Každej triede a vlastnosti pridať **`rdfs:label` a `rdfs:comment`**.
- [ ] Zapísať ontológiu v **platnom formáte Turtle**.
- [ ] Overiť, že ontológia neobsahuje logické nekonzistentnosti.
- [ ] Vytvoriť **diagram tried a vlastností**.
- [ ] Model vysvetliť v texte.

## 3. Prieskum existujúcich ontológií a slovníkov

- [ ] Preskúmať existujúce pojmy, ktoré by sme mohli použiť.
- [ ] Rozhodnúť, čo prevezmeme a čo definujeme sami.
- [ ] **Zdôvodniť obe rozhodnutia** — prevzatie aj použitie vlastných definícií.

Pre našu tému môžeme preskúmať napríklad Schema.org a ESCO.

## 4. Dáta a znalostný graf

- [ ] Vytvoriť dáta podľa našej ontológie — generovaním alebo transformáciou existujúcich dát.
- [ ] Dosiahnuť orientačný rozsah **aspoň 50–100 RDF trojíc**. Zadanie to uvádza ako približný odhad.
- [ ] Dostatočne pokryť **všetky definované triedy a vlastnosti**.
- [ ] Pripraviť údaje, nad ktorými sa dá vykonať zmysluplná analýza.

Generované dáta sú povolené; zadanie výslovne pripúšťa použitie LLM na ich tvorbu.

## 5. SPARQL dotazy a výsledky

- [ ] Preložiť kompetenčné otázky do **SPARQL dotazov**.
- [ ] Dotazy spustiť a získať odpovede.
- [ ] Zahrnúť zložitejšie alebo analytické dotazy.
- [ ] Ak ich kompetenčné otázky nepokrývajú, pridať **tri ďalšie analytické dotazy**, napríklad s agregáciami, zoskupovaním či textovými operáciami.
- [ ] Do práce uviesť **všetky dotazy, ich opis a vysvetlenie výsledkov**.

## 6. SHACL validácia

- [ ] Vytvoriť **3–4 SHACL shapes**.
- [ ] Všetky uviesť v práci a vysvetliť ich význam.

Jedna shape môže obsahovať viacero kontrol, napríklad povinný názov kurzu aj nezápornú cenu.

## 7. Písomná práca

- [ ] Spracovať úplný text projektu do **PDF**.
- [ ] Zahrnúť opis domény a kompetenčné otázky.
- [ ] Zahrnúť opis ontológie, diagram a prieskum existujúcich slovníkov.
- [ ] Opísať vytvorenie dát.
- [ ] Uviesť SPARQL dotazy a výsledky.
- [ ] Uviesť SHACL shapes a vysvetlenia.

## 8. Odovzdanie a organizácia

- [ ] Overiť zápis tímu do zoznamu príslušného cvičenia. Termín v zadaní bol **24. októbra 2026**.
- [ ] Pripraviť **jeden ZIP**, ktorý obsahuje:
  - PDF práce,
  - ontológiu,
  - dátový súbor,
  - SPARQL dotazy,
  - SHACL shapes.
- [ ] Určiť jedného člena, ktorý odovzdá projekt za celý tím cez **InSIS**.
- [ ] Odovzdať do **4. decembra 2026 o 23:59**.

Konzultácie k projektu sú naplánované na **30. novembra a 1. decembra**.

## 9. Prezentácia

- [ ] Pripraviť prezentáciu na **maximálne 10 minút**.
- [ ] Predstaviť doménu a motiváciu.
- [ ] Ukázať konceptuálny model ontológie.
- [ ] Predviesť konkrétny prípad použitia s **jedným zaujímavým SPARQL dotazom a výsledkami**.
- [ ] Zhodnotiť spoluprácu a získané skúsenosti.

Prezentácie prebiehajú v **12. a 13. týždni výučby**.

**Hodnotenie:** projekt **35 bodov**, prezentácia **10 bodov**. Zadanie neuvádza podrobnejší rozpis bodov medzi jednotlivé časti.

## Naše odporúčania navyše

Tieto kroky pomôžu overiť kvalitu riešenia:

- [ ] Najprv overiť malý príklad s ručne vypočítanou očakávanou odpoveďou.
- [ ] Vyskúšať SHACL aj na úmyselne chybných dátach.
- [ ] Skontrolovať, že odporúčanie počíta iba nové ponuky a každú iba raz.
- [ ] Pridať návod, ako načítať dáta, spustiť dotazy a validáciu.

**Webová aplikácia, používateľské rozhranie ani živé sťahovanie pracovných ponúk nie sú v zadaní požadované.**
