import laud as laua_meetodid
from random import choice

def random_käik(laud):
    # seda ilmselt saaks efektiivsemaks teha kui võtta korra pommitamata kohad ja siis eemaldada sealt elemente, mitte iga kord uuesti leida.
    k = laua_meetodid.pommitamata_kohad(laud)
    ruut = choice(k)
    print("Random algoritm: pommitan " + str(ruut))
    pommitamise_tulemus, lauaseis = laua_meetodid.pommita(ruut[0], ruut[1], laud)
    return pommitamise_tulemus, lauaseis
