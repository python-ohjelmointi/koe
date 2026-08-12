"""
Tervehdys

Toteuta funktio tervehdys, joka saa parametrinaan merkkijonomuotoisen nimen ja tulostaa
tervehdyksen. Tervehdys on muotoa "Hei nimi!" ja se tulee tulostaa, eikä palauttaa.

Esimerkki:

    >>> tervehdys('Lauri')
    Hei Lauri!

    >>> tervehdys('Mirella')
    Hei Mirella!


Erityistapauksissa, joissa funktiolle annetaan joko tyhjä merkkijono tai None, funktion
tulee tulostaa teksti "Hei tuntematon!".

    >>> tervehdys('')
    Hei tuntematon!

    >>> tervehdys(None)
    Hei tuntematon!

"""

# Toteuta oma tervehdys-funktiosi tänne


if __name__ == "__main__":
    # Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään.
    # Voit myös halutessasi poistaa tämän if-lohkon.
    #
    # Lisäksi suosittelemme hyödyntämään yllä olevaan tehtäväkuvaukseen sisältyviä doctest-
    # testejä. Alla olevat rivit suorittavat tehtävänannon testit, kun tämä tiedosto ajetaan:

    import doctest
    doctest.testmod(verbose=True)
