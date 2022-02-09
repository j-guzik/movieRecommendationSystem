# System rekomendacji filmów
https://github.com/j-guzik/movieRecommendationSystem

## Spis treści
* [Podstawowe informacje](#podstawowe-informacje)
* [Technologie i architektura](#technologie-i-architektura)
* [Uruchomienie](#uruchomienie)
* [Odwołania](#odwołania)

## Podstawowe informacje
Projekt przedstawia aplikację webową służącą do rekomendacji filmów. Rekomendacja odbywa się za pomocą tzw. content-based filtering i opiera się na porównywaniu podobieństwa między słowami kluczowymi, gatunkami, najlepszymi aktorami oraz reżyserze. 

![](https://github.com/j-guzik/movieRecommendationSystem/blob/master/media/Recommender.gif) 

## Technologie i architektura
Projekt utworzono przy pomocy:
* Angular CLI: 12.2.10
* Node: 14.18.1
* Package Manager: npm 6.14.15
* Python 3.10
* MySQL 8.0

<img height="400" alt="architecture" src="https://github.com/j-guzik/movieRecommendationSystem/blob/master/media/architektura.PNG">

## Uruchomienie

* baza danych

Należy utworzyć bazę o następującej strukturze:

<img height="400" alt="architecture" src="https://github.com/j-guzik/movieRecommendationSystem/blob/master/media/baza.PNG">

Następny krok to wczytanie do tabeli movies wartości z pliku:

https://github.com/j-guzik/movieRecommendationSystem/blob/master/media/movies.csv


* backend

W pliku databaseCon.py należy połączyć się z lokalną bazą danych.
Pakiety do zainstalowania: pandas 1.3.4, pyodbc 4.0.32, flask 2.0.2.

* frontend

```
$ git clone https://github.com/j-guzik/movieRecommendationSystem
$ cd movieRecommendationSystem/aplikacja/RecommenderFront/recommender-front
$ npm install
$ npm start
```

Aplikacja powinna uruchomić się pod adresem http://localhost:4200.




## Odwołania
W projekcie korzystano z danych pobranych ze strony https://www.themoviedb.org. Aplikacja powstała na bazie silnika rekomendacji opisanego na stronie https://machinemantra.in/content-based-recommender-system/. 
