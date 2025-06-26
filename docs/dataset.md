<style>
code {
    color:rgb(255, 0, 0);
}
</style>
# Formule 1 Data-analyse: Dataset & Preprocessing
Een diepgaande analyse van Formule 1 prestaties van 1994-2022, met focus op de invloed van startposities en pitstopstrategieën op raceresultaten.

---
## Dataset Beschrijving

Voor een robuuste analyse van startposities, pitstopstrategieën en eindresultaten combineerden we **vier open source-datasets** met officiële Formule 1 gegevens: 

### 1. Startposities
> Per race bevat deze set de kwalificatie­klasseringen van alle coureurs.

### 2. Eindresultaten  
> Hierin staan de uiteindelijke posities, het team, het aantal voltooide ronden en de uitval redenen (DNF, DNS).

### 3. Pitstopgegevens
> Per pitstop-actie worden het tijdstip, de duur (in seconden) en het aantal stops per coureur geregistreerd.

### 4. Overtakes
> Per seizoen en per race wordt er gekeken naar de totale hoeveelheid overtakes.

> **Tijdsperiode:** Omdat pitstopgegevens pas vanaf 1994 volledig en betrouwbaar worden vastgelegd, stelden we onze studieperiode in op 1994–2022. Zo ontstaat een grote, consistente dataset van bijna drie decennia Formule 1-geschiedenis, waarin zowel dominante seizoenen als strategisch spannende periodes zijn vertegenwoordigd.

---
## Harmonisatie en samenvoegen
Allereerst richtten we ons op het harmoniseren van labels: over alle datasets heen hebben we de coureur- en Grand Prix-benamingen gestandaardiseerd. Vervolgens voegden we de datasets samen met een samengestelde sleutel: (Grand Prix naam + seizoen + coureur). Elk resulterend record bevat vanaf dat moment één rij met:

- `Startpositie` uit de kwalificatie
- `Team- en rondeninformatie` uit de race-uitslag  
- `Gedetailleerde pitstopdata`
- `Totaal aantal on-track overtakes`

Dankzij deze koppeling is iedere rij een samenhangend overzicht van een race met een unieke ID.

---
## Data kwaliteit
Om de betrouwbaarheid te waarborgen, zochten we actief naar onvolledige of niet-geclassificeerde gevallen (`NC` of `Not Classified`). Zulke records markeerden we of verwijderden we, afhankelijk van de analysebehoefte. Ook zorgden we ervoor dat pitstop-tijden altijd als numerieke seconden werden opgeslagen, zodat we moeiteloos gemiddelden, varianties en relatieve scores konden berekenen. Tot slot implementeerden we parameteriseerbare filters op seizoen en circuit, zodat we eenvoudig subgroepanalyses kunnen uitvoeren.

---
## Technische implementatie
De dataverwerking vond volledig in Python plaats, waarin we:
- `pandas` gebruikten voor het inlezen, hernoemen en samenvoegen van tabellen,
- `numpy` voor efficiënte numerieke conversies en aggregaties,
- `functies` bouwden om seizoenen en circuits dynamisch te selecteren,
- `automatische validatiechecks` toevoegden voor controle op dubbele rijen of afwijkende tijdseenheden,
- `matplotlib` inzetten voor statische visualisaties,
- `plotly` gebruiken voor interactieve grafieken.

Deze aanpak garandeert reproduceerbaarheid en maakt het eenvoudig om later nieuwe data in te laden én direct te visualiseren.

---
## Variabelen van onze dataset
Ons eindresultaat is één slimme tabel met per coureur–racecombinatie de volgende hoofdvariabelen:

- `start_pos`: beginpositie / kwalificatieresultaat
- `end_pos`: eindpositie na de finish
- `pitstop_count`: totaal aantal pitstops
- `pit_avg`: gemiddelde pitstopduur in seconden
- `pit_rel_score`: relatieve score van pitstoptijd (snelste = 1,0; anderen als fractie)
- `pos_change`: netto posities gewonnen of verloren
- `season`
- `circuit`

Door al deze gegevens in één overzicht samen te brengen, kunnen we zowel losse verbanden als gecombineerde patronen ontdekken.

---
## Kernindicatoren
Op basis van de ruwe data berekenden we twee kernindicatoren:

**1. Relatieve pitstopscore**
> `Pit_rel_score = pit_avg_driver / min_pit_time_race`

Zo zetten we pitstop-efficiëntie per race om in een eerlijk vergelijkingsmaat.

**2. Netto positieverandering**
> `Pos_change = start_pos - end_pos`

Positief als een coureur terrein wint, negatief bij verlies. Met deze aggregaten leggen we de basis voor al onze visualisaties.