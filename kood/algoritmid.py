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
        return tulem, laud
            
def paarsus_käik(laud):
    #todo
    rida = -1
    veerg = -1
    for i in range(len(laud)):
        for j in range(len(laud)):
            if laud[i][j] == "-" or laud[i][j] == "X":
                continue
            else:
                rida = i
                veerg = j
            # kui kuskil küljel on pommitatud ruut, siis ta ei vali seda randomiks
            if i > 0 and (laud[i-1][j] == '-' or laud[i-1][j] == 'X'):
                continue
            if i < len(laud) and (laud[i+1][j] == '-' or laud[i+1][j] == 'X'):
                continue
            if j > 0 and (laud[i][j-1] == '-' or laud[i][j-1] == 'X'):
                continue
            if j < len(laud) and (laud[i][j+1] == '-' or laud[i][j+1] == 'X'):
                continue
            return laua_meetodid.pommita(i,j,laud)
    # kui ei leidu ruutu, millel poleks mingi naaber pommitamata, siis pommitame viimase vaba ruudu
    return laua_meetodid.pommita(rida,veerg,laud)
            
def hunt_tõenäosuslik(laud):
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
        tulem, laud = tõenäosuslik(laud)
        if tulem == 1:
            kõrvuti_ruudud(viimati_pommitatud,laud)
        return tulem, laud


def tõenäosuslik(laud):
    tühi_maatriks = [[0]*10]*10
    laevad = [5,4,3,3,2]
    # vasakult paremale kontrollid
    for laev in laevad:
        for rida in range(len(laud)):
            for veerg in range(len(laud)+1-laev):
                if tühjuse_kontroll_rida(rida,veerg,laev,laud):
                    for i in range(laev):
                        tühi_maatriks[rida][veerg+i] +=1
                if tühjuse_kontroll_veerg(veerg,rida,laev,laud):
                    for i in range(laev):
                        tühi_maatriks[rida+1][veerg] +=1
    max = -1
    rida = -1
    veerg = -1
    for i in range(10):
        for j in range(10):
            if tühi_maatriks[i][j] > max:
                rida = i
                veerg = j
    return laua_meetodid.pommita(rida,veerg,laud)
                        
                    
    
def tühjuse_kontroll_rida(rida,veerg,laev,laud):
    for i in range(laev):
        if (laud[rida][veerg+i] == "-" or laud[rida][veerg+i] == "X"):
            return False
    return True

def tühjuse_kontroll_veerg(rida,veerg,laev,laud):
    for i in range(laev):
        if (laud[rida+i][veerg] == "-" or laud[rida+i][veerg] == "X"):
            return False
    return True
                    
    
