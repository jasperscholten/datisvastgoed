# Readme van Amstelhaege case bij heuristieken
## Groep Datis Vastgoed
Nadav Baruch - 11427353</br>
Jelle Mul - 11402148</br>
Jasper Scholten - 11157887

## Logboek
**Week 1** - Voor ons eigen begrip een overzicht gemaakt van de case. Eerste regels code geschreven, waardoor een numpy array van de juiste grootte (maten van het veld) aangemaakt wordt; dit is de basis structuur waarop de huizen geplaatst kunnen worden. Daarnaast ook een manier van visualisatie gevonden en uitgetest (matplotlib.pyplot). Tevens contact gelegd met Wouter, onze code-interviseur.

**Week 2** - Structuur voor de code opgezet, waarin gewerkt wordt met classes; hiervoor inspiratie geput uit de Robots opdracht van programmeren 2. Uiteindelijk toegewerkt naar een code die ervoor zorgt dat huizen op het veld geplaatst worden, daarbij rekening houdend met de gestelde eisen (aantal huizen, aantal meters vrijstand, etc.). Dit tevens gevisualiseerd. Op donderdag de eerste presentatie gehouden, die positief werd ontvangen en waar we nuttige feedback uit terugkregen (zoals hoe om te gaan met floats/integers, type algoritme (hill-climbing), etc.)

**Week 3** - Gewerkt aan de scorefunctie. Dit omvatte vooral het creëren van variabelen waarin zaken als de waarde en de vrijstand kunnen worden opgeslagen per huis, en het maken van functies die de vrijstand en de waarde van een huis kunnen berekenen. Overlegd met de code-interviseur, die ons aanraadde om op een andere manier de berekening van de vrijstand te benaderen (door middel van standaard onderdelen van de Numpy library).

**Week 4** - Afgelopen week veel moeite moeten steken in App Studio, mede doordat de app van vorige week heel veel tijd heeft gekost en deze week nog afgemaakt moest worden. Donderdag hebben we desondanks wel kunnen presenteren, iets waar we achteraf heel blij mee kunnen zijn. Dit heeft er namelijk voor gezorgd, dat we nog redelijk op tijd achter een belangrijke denkfout zijn gekomen. Door de ontvangen feedback hebben we namelijk het inzicht gekregen, dat we de berekening van de vrijstand verkeerd benaderden (de vrijstand vanaf de hoeken is kleiner dan dat we in eerste instantie rekening mee hielden). We zijn daarom volledig opnieuw begonnen aan de scorefunctie, wat betekent dat we eerst een paar stappen terug moeten zetten, om vervolgens weer vooruit te kunnen.

**Week 5** - Deze week voor het eerst echt veel tijd aan Heuristieken kunnen besteden en daardoor een behoorlijke slag kunnen slaan. In eerste instantie aan de gang gegaan met het toevoegen van water aan de simulatie en het uitwerken van de scorefunctie. In een gesprek met (begeleider) Jelle, kregen we feedback dat we de scorefunctie veel te omslachtig en moeilijk aanpakten. Op basis hiervan weer redelijk opnieuw begonnen aan de scorefunctie, met als belangrijkste verschil dat er minder checks nodig waren en dat de input voor de berekening van de vrijstand bestaat uit twee huizen in plaats van 1 huis, gecombineerd met de hele lijst van huizen. In het weekend aan het verslag gewerkt, hier een basisopzet voor gemaakt en deze (oppervlakkig) ingevuld. Hierin zijn de resultaten verwerkt die voortkwamen uit een random algoritme, dat voor iedere huizenvariant 5000 keer een random configuratie van de wijk maakte en hier de totale waard evan berekende. Hiermee hebben we aan het einde van week 5 ons eerste 'echte' resultaat behaald.

**Week 6** - In week 6 is er vooral gewerkt aan het tweede algoritmte voor deze case, namelijk de hill-climber. Hier zijn goede stappen in gezet en is een fundamentale basis voor gelegd. Daarnaast is begonnen met het berekenen van de toestandsruimte van de case. Hiernaast is de scorefunctie nog geoptimaliseerd.

**Week 7** - Gedurende week 7 is er met name verder gewerkt aan het optimaliseren van het hill-climber algoritme. Hierin was veel sprake van debugging. Daarnaast is verder gegaan met het berekenen van de toestandsruimte. Hierin waren namelijk een paar problemen waar tegenaan gelopen werd, maar hier zijn inmiddels oplossingen voor gevonden.

**Week 8** -
