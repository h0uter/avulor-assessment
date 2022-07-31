# Assessment 1

Dit assessment bestaat uit twee delen. In het eerste deel vragen we je een zelf-gemaakte oplossing toe te lichten. Dit zou weinig voorbereiding moeten kosten. Het tweede deel is een programmeer opdracht gebaseerd op de drone zwerm die bij Avalor AI gebouwd wordt.

Als je vragen hebt kun je ons gerust bellen of mailen.


## Opdracht 1: SE Review

We zouden graag een toelichting zien op een software design dat je zelf ontworpen hebt. Gebruik hiervoor een persoonlijk/professioneel project dat je in zoverre kan delen. Dit kan het design van een stuk code zijn, communicatie-flow of een architectuur zijn. Het hoeft niet het design van een heel project te zijn, maar mag ook een gedeelte zijn. Graag horen we van je welke afwegingen je hebt gemaakt en waar je uiteindelijk bij de implementatie tegenaan bent gelopen. Je kiest zelf hoe je het aan ons presenteert, maar gelieve wel schematisch/visueel en niet in code.

Tijdens het assessment praat je ons door je design heen, waarbij wij wat vragen zullen stellen. We zullen hier kijken naar de requirements, het ontwerp, je afwegingen en jouw toelichting daarop. Duur: +/- 20 min.


## Opdracht 2: Technische opdracht

Om een zwerm drones aan te sturen dienen alle drones te communiceren met een grond-station. Drones registreren zich bij een grond-station, waarna het grondstation waypoints naar de verschillende drones stuurt om naar toe te vliegen. Elke drone stuurt het grondstation zijn positie elke 5 seconden.

Er zijn verschillende communicatieprotocollen mogelijk om dit te implementeren. Een mogelijkheid is gRPC. gRPC is snel, robuust, en alle data wordt gestructureerd opgeslagen in het protobuf formaat.

Opdracht: Schrijf een grondstation dat communiceert met _1_ drone cfm bovenstaand scenario.

Graag ontvangen we uiterlijk een dag voor het begin van de assessment een link naar je projectcode. Tijdens de assessment praat je ons door je code heen en zullen we wat vragen stellen. Duur: +/- 30 min.

Voorwaarden:

- Je bent vrij in het kiezen van een programmeertaal.
- Voor de communicatie dien je gebruik te maken van gRPC. https://grpc.io/
- Het grondstation en de drone dienen apart van elkaar gedraaid te worden (ze hebben elk hun eigen "main").
- De volgende gRPC berichten dienen gestuurd te worden:
  - _register_: De drone registreert zich bij het grondstation.
  - _listen_waypoint_: De drone luistert naar waypoints die het grondstation stuurt.
  - _send_position_: De drone stuurt elke 5 seconden zijn positie naar het grondstation.
- De protobuf berichten dienen (minimaal) de volgende data te bevatten:
  - registration bevat de naam van de drone die zich registreert.
  - Een waypoint bevat een latitude en longitude.
  - Een position bevat een latitude, longitude en altitude.
- Voor deze opdracht is het niet nodig een realistische positie terug te sturen. Ga er van uit dat een drone na 10 seconden altijd op het gestuurde waypoint is aangekomen.
- Verzin zelf zinnige waardes of eigenschappen voor zover die hier niet beschreven staan.

Tips:

- Het grondstation is de gRPC server, de drone de gRPC client.
- Een protobuf bestand is als voorbeeld meegestuurd.

Extra: Mocht je nog wat tijd over hebben dan kun je je zelf uitdagen door:

- De code uit te breiden zodat meerdere drones kunnen verbinden met het grondstation
- Geef de drones een realistische snelheid en laat ze realistische posities terug sturen (de voorwaarde dat een drone altijd na 10 sec op zijn waypoint aankomt vervalt hiermee).
- Voeg zelf berichten toe met mogelijk handige functionaliteit.
- Unit tests en/of een opzetje voor CI/CD.
- De server en client in twee verschillende talen te programmeren (wij gebruiken Rust en Python).

