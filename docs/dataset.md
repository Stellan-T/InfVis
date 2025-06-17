# Dataset en preprocessing
Voor deze analyse gebruikten we drie open source-datasets met officiële Formule 1-gegevens:
[1.	Startposities]
Per race bevat deze set de kwalificatie¬klasseringen van alle coureurs.
[2.	Eindresultaten]
Hierin staan de uiteindelijke posities, het team, het aantal voltooide ronden en de uitval redenen (DNF, DNS).
[3.	Pitstopgegevens]
Per pitstop-actie worden het tijdstip, de duur (in seconden) en het aantal stops per coureur geregistreerd.
We kozen de periode 1994 tot en met 2022, omdat vanaf 1994 de pitstop gegevens volledig en betrouwbaar beschikbaar zijn. Tijdens de preprocessing brachten we coureursnamen en Grand Prix-benamingen in alle bestanden op één lijn en voegden we de data op basis van Grand Prix, jaar en coureursnaam samen. Zo bevat elke rij zowel startpositie- als pitstop- en resultaatinformatie. 

Vervolgens verwijderden of markeerden we onvolledige of niet-geclassificeerde records (‘NC’ voor Not Classified). Pitstoptijden werden omgezet naar numerieke waarden, zodat we gemiddelden en varianties konden berekenen. We voegden bovendien extra filters toe, zoals op seizoen of circuit, om gerichte analyses mogelijk te maken.
Alle dataverwerking gebeurde in Python, met behulp van onder andere pandas en numpy. Voor de visualisaties maakten we gebruik van matplotlib en Plotly, zodat we de invloed van startpositie en pitstopstrategie zowel statistisch onderbouwd als visueel overtuigend in kaart konden brengen.
