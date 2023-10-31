# Captic-technisch-luik

## Technisch luik

Schrijf een python scriptje waar je een bestandsnaam van een afbeelding kan aan meegeven.
Het script gaat dan voor die afbeeldingen een JSON-file uitschrijven met de metadata van de afbeelding.
Gebruik hierbij de opencv package.

Dockerize het script zodat je een container hebt met de functionaliteit zoals hierboven beschreven.
Probeer te vermijden dat de afbeelding in de container image zelf zit.

Gedurende de test verwachten we dat je gebruik maakt van GitHub.
Met deze test willen we nagaan of je Python, Docker en GitHub beheerst.
Daarnaast kijken we ook naar je manier van werken en de kwaliteit van de code.

## Oplossing technisch luik

De commandos die nodig zijn om de docker container aan te maken en te laten runnen (template):

```console
docker build -t my_container .

docker run -v /path/to/external/file:/app/external_file -v /path/to/output/directory:/app/output my_container
```

De commandos die ik gebruikt heb om de docker container aan te maken en te laten runnen (ingevuld):

```console
docker build -t metadata .

docker run -v "C:\Users\maxit\Documents\HOGent\3e Jaar\Stage\Captic-technisch-luik\images\pil1.png":/app/external_file -v "C:\Users\maxit\Documents\HOGent\3e Jaar\Stage\Captic-technisch-luik\output":/app/output metadata
```

## Inzichtelijk luik

Maak een README aan in de waarin je in het kort beschrijft hoe je te werk om een dataset te clusteren.

Veronderstel dat de dataset bestaat uit afbeeldingen zoals:

 ![Pil1](./images/pil1.png) en  ![Pil2](./images/pil2.png)

Verschillen zijn dus minimaal.
Het doel van het clusteren is om uiteindelijk te bepalen welke types defecten er allemaal kunnen voorkomen.
Je weet dus niet op voorhand hoeveel clusters je mag verwachten.

## Oplossing inzichtelijk luik

De images gaan omgezet moeten worden naar feature vectoren, ze gaan best geresized worden zodat het model beter getraind kan worden.
Dit kan door het gebruiken van een pre-trained model convulition neural network ResNet.
Dan moeten we een maat van similariteit kiezen dit kan door het gebruiken van cosinus similariteit of de afstand van elkaar te berekenen.
De gekozen maat van similariteit kan dan gebruikt worden om de afbeeldingen te clusteren.
Het clusteren kan gebeuren door verschillende algoritmes zoals K-means of DBSCAN, best meerdere proberen om het beste algoritme uit te komen.
Het aantal clusters kan geschat worden door het gebruiken van de elbow method, het plotten van het aantal clusters tegen over de variantie.
