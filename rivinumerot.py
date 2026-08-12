r"""
Rivinumerointi

Tehtäväsi on toteuttaa funktio lisaa_rivinumerointi, joka saa parametrinaan
monirivisen merkkijonon ja palauttaa uuden merkkijonon, jossa jokaisen rivin alkuun
on lisätty rivinumero, piste ja välilyönti. Esimerkiksi:

1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.

Numerointi aloitetaan yhdestä ja funktion tulee selvitä mistä tahansa määrästä rivejä.

    >>> lisaa_rivinumerointi('Live\nLove\nLaugh')       # \n tarkoittaa rivinvaihtoa
    '1. Live\n2. Love\n3. Laugh'

Voit olettaa, että annetussa merkkijonossa on aina vähintään yksi rivi:

    >>> lisaa_rivinumerointi("Special cases aren't special enough to break the rules.")
    "1. Special cases aren't special enough to break the rules."

Huomaa, että funktio ei saa tulostaa muodostettua merkkijonoa, vaan sen tulee palauttaa se.

Seuraavassa esimerkissä funktiolle annetaan monirivinen merkkijono ja paluuarvo
otetaan talteen `viisu`-nimiseen muuttujaan:

    >>> viisu = lisaa_rivinumerointi('''Vi ska bada bastu bastu
    ... ångon åpp och släpp all stress idag
    ... Bastubröder e je vi som glöder 100 grader nåjaa
    ... SAUNA! SAUNA!''')

Tulostettaessa yllä luotua `viisu`-merkkijonoa tuloste näyttää seuraavalta:

    >>> print(viisu)
    1. Vi ska bada bastu bastu
    2. ångon åpp och släpp all stress idag
    3. Bastubröder e je vi som glöder 100 grader nåjaa
    4. SAUNA! SAUNA!

"""


def lisaa_rivinumerointi(merkkijono: str) -> str:
    """
    Lisää rivinumerot annetulle merkkijonolle ja palauta muodostettu merkkijono.
    """
    return ""


if __name__ == "__main__":
    # Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään.
    # Voit myös halutessasi poistaa tämän if-lohkon.
    #
    # Lisäksi suosittelemme hyödyntämään yllä olevaan tehtäväkuvaukseen sisältyviä doctest-
    # testejä. Alla olevat rivit suorittavat tehtävänannon testit, kun tämä tiedosto ajetaan:

    import doctest
    doctest.testmod(verbose=True)
