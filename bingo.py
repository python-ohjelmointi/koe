"""
BINGO!

> "Perinteisessä bingopelissä pelaajalla on pelattavanaan pelikortti, johon on merkitty tietty määrä
> ruudukkoja. Arvottujen numeroiden toivotaan muodostavan ruudukolla vaaka-, pysty- tai
> kulmasta kulmaan-rivejä."
>
> Bingo. https://fi.wikipedia.org/wiki/Bingo


Tehtäväsi on toteuttaa funktio `tarkista_bingo`, joka saa kaksi parametria: peliruudukon sekä
arvotut numerot. Funktion tulee tarkistaa, sisältääkö ruudukko numeroita siten, että jonkin pysty-,
vaaka- tai vinorivin kaikki numerot löytyvät arvotuista numeroista.

Jos annettu ruudukko sisältää bingon, funktiosi tulee palauttaa True. Muussa tapauksessa sen tulee
palauttaa False.

Ensimmäisenä parametrina annettava peliruudukko on kaksiulotteinen lista, joka sisältää kokonaislukuja.
Ruudukko koostuu numeroista 1-75, esimerkiksi seuraavasti:

   [[5, 10, 20, 30, 40],
    [1, 15, 25, 35, 45],
    [7, 12, 28, 33, 47],
    [3, 9, 18, 24, 50],
    [2, 13, 22, 31, 49]]

Toisena parametrina annettava arvottujen numeroiden lista on esimerkiksi seuraava:

   [5, 10, 20, 1, 15, 7, 12, 28, 33, 3, 9, 2, 13]

Näillä syötteillä funktiosi tulisi palauttaa True, koska ensimmäisen pystyrivin kaikki numerot
(5, 1, 7, 3 ja 2) löytyvät arvottujen numeroiden listalta. Huomaa, että arvotut numerot eivät ole
järjestyksessä, eikä niiden tarvitse olla.

Yksinkertaisuuden vuoksi lopuissa esimerkeissä käytetään seuraavaa ruudukkoa, jossa numerot kasvavat
aina vaakasuorassa yhdellä ja pystysuorassa kymmenellä, mikä helpottaa esimerkkien hahmottamista:

    >>> testiruudukko = [
    ...     [11, 12, 13, 14, 15],
    ...     [21, 22, 23, 24, 25],
    ...     [31, 32, 33, 34, 35],
    ...     [41, 42, 43, 44, 45],
    ...     [51, 52, 53, 54, 55]
    ... ]

Numerot voidaan arpoa missä tahansa järjestyksessä. Seuraavassa testiruudukolla bingo muodostuu
alimmasta vaakarivistä ([51, 52, 53, 54, 55]), kun arvottujen numeroiden lista on
[1, 2, 55, 54, 53, 3, 4, 51, 52]:

    >>> tarkista_bingo(testiruudukko, [1, 2, 55, 54, 53, 3, 4, 51, 52])
    True

Tässä esimerkissä bingo löytyy toiseksi viimeisestä pystyrivistä:

    >>> tarkista_bingo(testiruudukko, [14, 24, 34, 44, 54])
    True

Lopuksi, tässä esimerkissä bingo löytyy vinosti vasemmalta alhaalta oikealle ylös:

    >>> tarkista_bingo(testiruudukko, [51, 42, 33, 24, 15])
    True

Seuraavat ruudukot eivät puolestaan muodosta bingoa, joten funktio palauttaa False:

    >>> tarkista_bingo(testiruudukko, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    False

    >>> tarkista_bingo(testiruudukko, [11, 12, 13, 14, 21, 22, 23, 25, 31, 32, 34, 35, 41, 43, 44, 45, 52, 53, 54, 55])
    False


Voit olettaa, että ruudukko on aina 5x5-kokoinen ja että numeroiden arvot ovat välillä 1-75. Voit halutessasi
toteuttaa ratkaisusi toimimaan millä tahansa neliömuotoisilla ruudukoilla ja arvoväleillä. Arvottujen numeroiden
osalta voit olettaa, että lista sisältää aina vain sallittuja arvoja, mutta ratkaisusi ei saa kaatua, vaikka
yhtään lukua ei olisi vielä arvottu:

    >>> tarkista_bingo(testiruudukko, [])   # Ei arvottuja numeroita
    False

"""


# Toteuta funktioon tehtävänannon mukainen logiikka:
def tarkista_bingo(bingo_ruudukko: list, arvotut: list) -> bool:
    return False


if __name__ == "__main__":
    # Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään.
    # Voit myös halutessasi poistaa tämän if-lohkon.
    #
    # Lisäksi suosittelemme hyödyntämään yllä olevaan tehtäväkuvaukseen sisältyviä doctest-
    # testejä. Alla olevat rivit suorittavat tehtävänannon testit, kun tämä tiedosto ajetaan:

    import doctest
    doctest.testmod(verbose=True)
