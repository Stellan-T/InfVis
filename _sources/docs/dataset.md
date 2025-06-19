# Formule 1 Data-analyse: Dataset & Preprocessing

> **Project Overview**
> 
> Een diepgaande analyse van Formule 1 prestaties van 1994-2022, met focus op de invloed van startposities en pitstopstrategieën op raceresultaten.

---

## Dataset Beschrijving

Voor deze analyse gebruikten we **vier open source-datasets** met officiële Formule 1-gegevens:

### 1. Startposities
> Per race bevat deze set de **kwalificatie­klasseringen** van alle coureurs.

### 2. Eindresultaten  
> Hierin staan de **uiteindelijke posities**, het team, het aantal voltooide ronden en de uitval redenen (DNF, DNS).

### 3. Pitstopgegevens
> Per pitstop-actie worden het **tijdstip, de duur** (in seconden) en het aantal stops per coureur geregistreerd.

### 4. Overtakes
> Per seizoen en per race wordt er gekeken naar de **totale hoeveelheid overtakes**.

> **Tijdsperiode:** We kozen de periode **1994 tot en met 2022**, omdat vanaf 1994 de pitstopgegevens volledig en betrouwbaar beschikbaar zijn.

---

## Preprocessing Methodologie

### Perspective 1 preprocessing

Tijdens de preprocessing brachten we coureursnamen en Grand Prix-benamingen in alle bestanden op één lijn en voegden we de data op basis van Grand Prix, jaar en coureursnaam samen. Zo bevat elke rij zowel startpositie- als pitstop- en resultaatinformatie.

Vervolgens verwijderden of markeerden we onvolledige of niet-geclassificeerde records ('NC' voor Not Classified). Pitstoptijden werden omgezet naar numerieke waarden, zodat we gemiddelden en varianties konden berekenen. We voegden bovendien extra filters toe, zoals op seizoen of circuit, om gerichte analyses mogelijk te maken.

Alle dataverwerking gebeurde in Python, met behulp van onder andere pandas en numpy. Voor de visualisaties maakten we gebruik van matplotlib en Plotly, zodat we de invloed van startpositie en pitstopstrategie zowel statistisch onderbouwd als visueel overtuigend in kaart konden brengen.

---

### Perspective 2 preprocessing

Voor onze analyse combineren we drie open F1-datasets: de startgrid (starting_grids.csv), de race-uitslagen (race_details.csv) en de pitstop-samenvatting (pitstops.csv). Allereerst laden we de bestanden in en beperken we ons tot de seizoenen van 1994 tot en met 2022, zodat we een evenwichtige en vergelijkbare periode bekijken.

Vervolgens koppelen we elke sessie aan een eenduidige race-ID door de Grand Prix-naam te combineren met het jaartal. Zo kunnen we in één lijn zien wie waar is begonnen, wie waar is geëindigd en hoe lang de pitstops duurden. De grid-bijdrage ('Pos') geven we een leesbare naam (start_pos), de eindpositie hetzelfde (end_pos), en de pitstop-duur (Total) zetten we om naar seconden. Eventuele ontbrekende of onleesbare waarden worden weggefilterd, zodat alleen complete records overblijven.

Tot slot berekenen we per coureur én per race de gemiddelde pitstop-tijd, en zetten we die om in een relatieve score waarbij de snelste stop in elke race 1,0 wordt en langzamere stops een fractie daarvan. Door de start- en eindposities van elkaar af te trekken, krijgen we het aantal gewonnen of verloren plekken. Het resultaat is één compacte tabel met per rij één coureur-racecombinatie: startpositie, eindpositie, gemiddelde pitstoptijd, relatieve pit-score en posities gewonnen. Daarmee hebben we een schone, uniforme basis voor al onze visualisaties.