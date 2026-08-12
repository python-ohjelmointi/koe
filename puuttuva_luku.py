"""
Puuttuva luku

Tehtäväsi on toteuttaa funktio, joka etsii ja palauttaa puuttuvan luvun annetusta
kokonaislukujen listasta. Annettu lista koostuu peräkkäisistä luvuista, mutta yksi
luku puuttuu aina listalta. Lista voi alkaa ja päättyä mihin tahansa numeroon, eikä
lista ole välttämättä järjestyksessä.

Esimerkiksi seuraava lista sisältää luvut väliltä 1-5, mutta välistä puuttuu luku 4:

    >>> etsi_puuttuva_luku([1, 2, 3, 5])
    4

Lista ei välttämättä ala luvusta 1. Esimerkiksi seuraava lista alkaa luvusta 10 ja
siitä puuttuu luku 12:

    >>> etsi_puuttuva_luku([10, 11, 13, 14, 15])
    12

Listan luvut voivat olla epäjärjestyksessä, kuten tässä esimerkissä:

    >>> etsi_puuttuva_luku([2, 6, 5, 3])
    4

Voit olettaa, että annetulla listalla on aina vähintään kaksi lukua ja että annetut
listat noudattavat tehtävänannossa kuvailtua logiikkaa. Sama luku ei koskaan esiinny
kahdesti ja yksi luku puuttuu aina.

"""



def etsi_puuttuva_luku(lista: list) -> int:
    """
    Etsi puuttuva luku annetusta kokonaislukujen listasta ja palauta se.
    """
    return -1


if __name__ == "__main__":
    # Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään.
    # Voit myös halutessasi poistaa tämän if-lohkon.
    #
    # Lisäksi suosittelemme hyödyntämään yllä olevaan tehtäväkuvaukseen sisältyviä doctest-
    # testejä. Alla olevat rivit suorittavat tehtävänannon testit, kun tämä tiedosto ajetaan:

    import doctest
    doctest.testmod(verbose=True)
