# Readme Amstelhaege case bij heuristieken
## Groep Datis Vastgoed B.V.
Nadav Baruch - 11427353</br>
Jelle Mul - 11402148</br>
Jasper Scholten - 11157887

## Doel van de Amstelhaege case
De gemeente Ouder-Amstel heeft Datis Vastgoed B.V. de planologisch uitdagende klus gegeven, een geheel nieuwe woonwijk te ontwikkelen op een locatie in de Duivendrechtse Polder ter grootte van 150 bij 160 meter. De wijk zal de naam ‘Amstelhaege’ gaan dragen en heeft als voornaamste doelgroep expats en hoogopgeleide werknemers actief op de Amsterdamse Zuidas.
Het planologisch proces zal worden gebaseerd op een vernieuwend concept, waarin de indeling van de wijk bepaald wordt met behulp van een computeralgoritme. Dit algoritme zal de indeling van de wijk proberen te optimaliseren op basis van een aantal wensen van de gemeente. Zo moeten er uiteindelijk drie varianten onderzocht worden, die respectievelijk de opties voor twintig, veertig en zestig huizen uitwerken.

## Het programma
Met behulp van dit programma is het mogelijk om huizen op een bepaalde oppervlakte te optimaliseren op twee doelen, namelijk op zo een groot mogelijke vrijstand en een zo hoog mogelijke prijs. Hoe dit bepaald wordt is terug te vinden in het verslag. Door middel van command-line arguments is het programma te runnen. Allereerst wordt gevraagd welke variant er gerund er dient te worden. Voor elke variant zijn er verschillende inputs van de gebruiker nodig, zoals de naam voor het .csv bestand, het aantal keer dat het programma moet runnen, of er een visualisatie wordt laten zien aan het eind en voorwaarden voor bepaalde varianten. 

## Het runnen van het programma
De repository datisvastgoed bevat het programma genaamd Amstelhaege.py. Door in de terminal naar de map datisvastgoed te gaan, kan het programma gerund worden door python Amstelhaege.py aan te roepen. Hierna verschijnt het volgende.
![Image of my screenshot]
(/startScreen.png)

## Gemaakt met
Atom (Python)

## Logboek
**Week 1** - Voor ons eigen begrip een overzicht gemaakt van de case. Eerste regels code geschreven, waardoor een numpy array van de juiste grootte (maten van het veld) aangemaakt wordt; dit is de basis structuur waarop de huizen geplaatst kunnen worden. Daarnaast ook een manier van visualisatie gevonden en uitgetest (matplotlib.pyplot). Tevens contact gelegd met Wouter, onze code-interviseur.

**Week 2** - Structuur voor de code opgezet, waarin gewerkt wordt met classes; hiervoor inspiratie geput uit de Robots opdracht van programmeren 2. Uiteindelijk toegewerkt naar een code die ervoor zorgt dat huizen op het veld geplaatst worden, daarbij rekening houdend met de gestelde eisen (aantal huizen, aantal meters vrijstand, etc.). Dit tevens gevisualiseerd. Op donderdag de eerste presentatie gehouden, die positief werd ontvangen en waar we nuttige feedback uit terugkregen (zoals hoe om te gaan met floats/integers, type algoritme (hill-climbing), etc.)

**Week 3** - Gewerkt aan de scorefunctie. Dit omvatte vooral het creëren van variabelen waarin zaken als de waarde en de vrijstand kunnen worden opgeslagen per huis, en het maken van functies die de vrijstand en de waarde van een huis kunnen berekenen. Overlegd met de code-interviseur, die ons aanraadde om op een andere manier de berekening van de vrijstand te benaderen (door middel van standaard onderdelen van de Numpy library).

**Week 4** - Afgelopen week veel moeite moeten steken in App Studio, mede doordat de app van vorige week heel veel tijd heeft gekost en deze week nog afgemaakt moest worden. Donderdag hebben we desondanks wel kunnen presenteren, iets waar we achteraf heel blij mee kunnen zijn. Dit heeft er namelijk voor gezorgd, dat we nog redelijk op tijd achter een belangrijke denkfout zijn gekomen. Door de ontvangen feedback hebben we namelijk het inzicht gekregen, dat we de berekening van de vrijstand verkeerd benaderden (de vrijstand vanaf de hoeken is kleiner dan dat we in eerste instantie rekening mee hielden). We zijn daarom volledig opnieuw begonnen aan de scorefunctie, wat betekent dat we eerst een paar stappen terug moeten zetten, om vervolgens weer vooruit te kunnen.

**Week 5** - Deze week voor het eerst echt veel tijd aan Heuristieken kunnen besteden en daardoor een behoorlijke slag kunnen slaan. In eerste instantie aan de gang gegaan met het toevoegen van water aan de simulatie en het uitwerken van de scorefunctie. In een gesprek met (begeleider) Jelle, kregen we feedback dat we de scorefunctie veel te omslachtig en moeilijk aanpakten. Op basis hiervan weer redelijk opnieuw begonnen aan de scorefunctie, met als belangrijkste verschil dat er minder checks nodig waren en dat de input voor de berekening van de vrijstand bestaat uit twee huizen in plaats van 1 huis, gecombineerd met de hele lijst van huizen. In het weekend aan het verslag gewerkt, hier een basisopzet voor gemaakt en deze (oppervlakkig) ingevuld. Hierin zijn de resultaten verwerkt die voortkwamen uit een random algoritme, dat voor iedere huizenvariant 5000 keer een random configuratie van de wijk maakte en hier de totale waard evan berekende. Hiermee hebben we aan het einde van week 5 ons eerste 'echte' resultaat behaald.

**Week 6** - In week 6 is er vooral gewerkt aan het tweede algoritmte voor deze case, namelijk de hill-climber. Hier zijn goede stappen in gezet en is een fundamentale basis voor gelegd. Daarnaast is begonnen met het berekenen van de toestandsruimte van de case. Hiernaast is de scorefunctie nog geoptimaliseerd.

**Week 7** - Gedurende week 7 is er met name verder gewerkt aan het optimaliseren van het hill-climber algoritme. Hierin was veel sprake van debugging. Daarnaast is verder gegaan met het berekenen van de toestandsruimte. Hierin waren namelijk een paar problemen waar tegenaan gelopen werd, maar hier zijn inmiddels oplossingen voor gevonden.

**Week 8** - De laatste week van het project is aangebroken en de laatste stappen worden gezet. Het random algoritme en de hill-climber waren nog gelukkig nog snel gelukt. Toen werd het tijd voor het laatste algoritme, de Simulated Annealing. Deze is inmiddels ook af en nu zijn het nog de laatste dingen die geperfectioneerd moeten worden. Bijvoorbeeld het opschonen van de code, het verslag, de presentatie, de README file en het logboek. Toch zien wij een rooskleurig einde tegemoet.
