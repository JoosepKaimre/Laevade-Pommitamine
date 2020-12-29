import laud as laua_meetodid
from random import choice, shuffle

global viimati_pommitatud

def kõrvuti_ruudud(käik, laud):
    global targad_käigud
    rida = käik[0]
    veerg = käik[1]
    vrida = rida-1 
    prida = rida +1 
    üveerg = veerg -1
    aveerg = veerg + 1
    if (vrida >= 0 and (laud[vrida][veerg] == " " or laud[vrida][veerg] == "O")):
        targad_käigud.append((vrida,veerg))
    if (prida < len(laud) and (laud[prida][veerg] == " " or laud[prida][veerg] == "O")):
        targad_käigud.append((prida,veerg))
    if (üveerg >= 0 and (laud[rida][üveerg] == " " or laud[rida][üveerg] == "O")):
        targad_käigud.append((rida,üveerg))
    if (aveerg < len(laud) and (laud[rida][aveerg] == " " or laud[rida][aveerg] == "O")):
        targad_käigud.append((rida,aveerg))
        

def random_käik(laud):
    # seda ilmselt saaks efektiivsemaks teha kui võtta korra pommitamata kohad ja siis eemaldada sealt elemente, mitte iga kord uuesti leida.
    k = laua_meetodid.pommitamata_kohad(laud)
    ruut = choice(k)
    viimati_pommitatud = ruut
    print("Random algoritm: pommitan " + str(ruut))
    pommitamise_tulemus, lauaseis = laua_meetodid.pommita(ruut[0], ruut[1], laud)
    return pommitamise_tulemus, lauaseis


# algoritm, mis laeva tabamisel otsib lähedusest laevu (ülevalt, alt, kõrvalt, paremalt)
targad_käigud = []
def hunt_algoritm(laud):
    global targad_käigud
    global viimati_pommitatud
    if len(targad_käigud) != 0:
        shuffle(targad_käigud)
        viimati_pommitatud = targad_käigud.pop()
        tulem, laud = laua_meetodid.pommita(viimati_pommitatud[0],viimati_pommitatud[1],laud)
        if tulem == 1:
            kõrvuti_ruudud(viimati_pommitatud,laud)
        return tulem, laud
    else:
        tulem, laud = random_käik(laud)
        if tulem == 1:
            kõrvuti_ruudud(viimati_pommitatud,laud)
        return tulem, laud
            


# Hunti algoritmi edasiarendus. Siin ei kasutata randomit, vaid läbitakse ruute üle ühe
def hunt_paarsus_algoritm(laud):
    global targad_käigud
    global viimati_pommitatud
    if len(targad_käigud) != 0:
        shuffle(targad_käigud)
        viimati_pommitatud = targad_käigud.pop()
        tulem, laud = laua_meetodid.pommita(viimati_pommitatud[0],viimati_pommitatud[1],laud)
        if tulem == 1:
            kõrvuti_ruudud(viimati_pommitatud,laud)
        return tulem, laud
    else:
        tulem, laud = paarsus_käik(laud)
        if tulem == 1:
            kõrvuti_ruudud(viimati_pommitatud,laud)
            
def paarsus_käik(laud):
    #todo
    for i in range(len(laud)):
        for j in range(len(laud)):
            # siin tuleb teha kontroll, et kõik külgedel olevad ruudud on pommitamata
            return (0,0),laud
            
            
        
