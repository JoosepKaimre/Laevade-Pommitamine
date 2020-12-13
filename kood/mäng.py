import laud as laua_meetodid
from random import  choice

suurus = 10
def mäng():
    global suurus
    laud1 = laua_meetodid.laud_koos_laevadega(suurus)
    laud2 = laua_meetodid.loo_laud(suurus)
    
def random_käik(laud):
    k = laua_meetodid.pommitamata_kohad(laud)
    ruut = choice(k)
    pommita(ruut[0], ruut[1], laud)
    

def algoritm():
    #todo
    return