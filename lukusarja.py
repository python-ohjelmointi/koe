"""
Lukusarja

Tehtäväsi on toteuttaa funktio `lukusarja`, joka saa parametrinaan positiivisen kokonaisluvun ja
muodostaa sekä palauttaa listan kokonaislukuja alla kuvailtujen sääntöjen mukaisesti.

Muodostettavan listan täytyy alkaa funktiolle annetusta luvusta ja sen täytyy päättyä ykköseen.
Ensimmäisen luvun jälkeen seuraava luku asetetaan aina seuraavien sääntöjen mukaan:

1. jos edellinen luku on parillinen, se jaetaan kahdella ja tulos lisätään listalle
2. jos edellinen luku on pariton, se kerrotaan kolmella ja tuloon lisätään yksi, ja tulos lisätään listalle.

Tätä logiikkaa toistetaan, kunnes saavutetaan luku 1, jolloin kaikki käsitellyt luvut palautetaan listana.

# Esimerkki 1:

Esimerkiksi, jos funktio saa parametrinaan luvun 8, lukusarja on [8, 4, 2, 1]. Tässä lukusarjassa
on viimeistä lukua lukuun ottamatta vain parillisia lukuja, joten kaikki luvut on saatu jakamalla
edellinen luku kahdella.

# Esimerkki 2:

Jos puolestaan lukusarjan jokin luku on pariton, esimerkiksi 3, seuraava luku saadaan esitettyjen
sääntöjen perusteella kertomalla luku kolmella ja lisäämällä yksi: 3 * 3 + 1 = 10.

Kolmosesta aloitettaessa listan kaksi ensimmäistä lukua ovat siis [3, 10]. Koska luku 10 on parillinen,
sitä seuraava luku saadaan jakamalla se kahdella: 10 / 2 = 5. Listan kolme ensimmäistä lukua ovat siis
[3, 10, 5]. Koska luku 5 on pariton, seuraava luku saaadan taas kertomalla kolmella ja lisäämällä
yksi: 5 * 3 + 1 = 16. Nyt listan luvut ovat [3, 10, 5, 16].

Tätä logiikkaa jatketaan, kunnes lukusarja saavuttaa ykkösen:

[3, 10, 5, 16, 8, 4, 2, 1]


# Koodiesimerkit

Kun funktiota kutsutaan millä tahansa positiivisella luvulla, sen tulee palauttaa lista, joka on
muodostettu edellä esitettyjen sääntöjen ja esimerkkien mukaisesti.

    >>> lukusarja(8)                # esimerkki 1 (parilliset jaetaan kahdella)
    [8, 4, 2, 1]

    >>> lukusarja(3)                # esimerkki 2 (parittomat kerrotaan kolmella ja lisätään yksi)
    [3, 10, 5, 16, 8, 4, 2, 1]

    >>> lukusarja(7)                # hieman pidempi lukusarja
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


Huomaa, että funktio ei saa tulostaa listaa, vaan lista täytyy palauttaa paluuarvona:

    >>> lukusarja(2) == [2, 1]      # älä tulosta, vaan palauta!
    True


# Vinkit

Voit olettaa, että funktiolle annetaan aina jokin ykköstä suurempi kokonaisluku.

Tämä tehtävä perustuu matemaattiseen, toistaiseksi todistamatta olevaan väittämään nimelta
Collatzin konjektuuri. Sen mukaan lukujono saavuttaa aina ykkösen riippumatta siitä, mistä luvusta
aloitetaan. Voit lukea lisää aiheesta esimerkiksi sivulta https://fi.wikipedia.org/wiki/Collatzin_konjektuuri.
"""


# Toteuta funktioon tehtävänannon mukainen logiikka:
def lukusarja(alku: int) -> list:
    return []


if __name__ == "__main__":
    # Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään.
    # Voit myös halutessasi poistaa tämän if-lohkon.
    #
    # Lisäksi suosittelemme hyödyntämään yllä olevaan tehtäväkuvaukseen sisältyviä doctest-
    # testejä. Alla olevat rivit suorittavat tehtävänannon testit, kun tämä tiedosto ajetaan:

    import doctest
    doctest.testmod(verbose=True)
