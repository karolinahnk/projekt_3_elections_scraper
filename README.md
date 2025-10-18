Engeto projekt Elections Scraper
Toto je třetí projekt pro Datový analytik s Python

Popis projektu:
Tento projekt slouží ke stažení výsledků do parlamentních voleb 2017 z webu [volby.cz](https://volby.cz).  
Program stahuje výsledky pro všechny obce vybraného územního celku (např. okres Benešov) a ukládá je do CSV souboru.

Instalace knihoven
Všechny knihovny, které jsou v kódu použity, jsou uloženy v requirements.txt. 
Pro instalaci je dobré, použít nové virtuální prostředí a následně takto spustit:
$ pip --version                       #overeni verze
$ pip install -r requirements.txt     #nainstalovani knihoven

Spuštění projektu
Spuštění souboru main.py v rámci příkazového řádku požaduje dva argumenty:
python main <odkaz-uzemniho-celku> <vysledny-soubor>
Následně se výsledky stáhnou do souboru s příponou .csv

Ukázka projektu
Výsledky hlasování pro okres Benešov:
1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2. argument:vysledky_benesov.csv

Spuštění programu:
python main.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' 'vysledky_benesov.csv'

Průběh stahování:
Downloading data from: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
The data was saved to: vysledky_benesov.csv
Ending the election-scraper.

