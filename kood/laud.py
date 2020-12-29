# " " tähistab tühja ruutu
# "-" tähistab pommitatud tühja ruutu
# "O" tähistab laeva ruutu
# "X" tähistab pommitatud laeva ruutu

from random import randint, choice
import pygame
import copy


# Erinevate laevade pommitamisega seotud vigade jaoks (võib ka uude faili tõsta)
class LaevadePommitamiseException(Exception):
    pass


# Tagastab etteantud suuruse järgi ruudukujulise tühja laua
def loo_laud(suurus):
    laud = []
    for i in range(suurus):
        laud.append(copy.deepcopy(suurus * [" "]))
    return laud


def lisa_laev(suurus, suund, rida, veerg, laud, teated=True):
    # suurus - laeva suurus
    # suund (N, E, S, W) - kuhu laev jääb stardiruudust
    # rida - stardiruudu reanumber
    # veerg - stardiruudu veerunumber
    # laud
    try:
        for i in range(suurus):
            if suund == "N":
                if (rida + 1 - suurus) < 0:
                    raise LaevadePommitamiseException
                if laud[rida - i][veerg] != " ":
                    if teated:
                        print("Need laeva kohad on juba võetud")
                    return False
            elif suund == "E":
                if laud[rida][veerg + i] != " ":
                    if teated:
                        print("Need laeva kohad on juba võetud")
                    return False
            elif suund == "S":
                if laud[rida + i][veerg] != " ":
                    if teated:
                        print("Need laeva kohad on juba võetud")
                    return False
            elif suund == "W":
                if (veerg + 1 - suurus) < 0:
                    raise LaevadePommitamiseException
                if laud[rida][veerg - i] != " ":
                    if teated:
                        print("Need laeva kohad on juba võetud")
                    return False
            else:
                if teated:
                    print("Sellist suunda ei saa olla")
                return False
        for i in range(suurus):
            if suund == "N":
                laud[rida - i][veerg] = "O"
            elif suund == "E":
                laud[rida][veerg + i] = "O"
            elif suund == "S":
                laud[rida + i][veerg] = "O"
            elif suund == "W":
                laud[rida][veerg - i] = "O"
            else:
                if teated:
                    print("Sellist suunda ei saa olla")
                return False
        return True
    except LaevadePommitamiseException:
        if teated:
            print("Laev jääb lauast välja")
        return False


# Tagastab False, kui laual leidub veel laevu, vastasel juhul tagastab True
def mäng_läbi(laud):
    return False if any("O" in rida for rida in laud) else True


def laud_koos_laevadega(suurus, laevad):
    laud = loo_laud(suurus)
    for laev in laevad:
        while True:
            suunad = []
            rida = randint(0, suurus - 1)
            veerg = randint(0, suurus - 1)
            if laev - 1 <= rida:
                suunad.append("N")
            if rida <= suurus - laev:
                suunad.append("S")
            if laev - 1 <= veerg:
                suunad.append("W")
            if veerg <= suurus - laev:
                suunad.append("E")
            if lisa_laev(laev, choice(suunad), rida, veerg, laud, False):
                break
    return laud


# Tagastab listi koordinaatide paaridest, millele vastavaid ruute pole veel pommitatud
def pommitamata_kohad(laud):
    return [(x, y) for x in range(len(laud)) for y in range(len(laud[x])) if laud[x][y] == " "]


# Etteantud ruudu pommitamise meetod mängija ja AI jaoks
def pommita(rida, veerg, laud):
    # rida - rea number
    # veerg - veeru number
    # laud - mängulaud
    try:
        sümbol = laud[rida][veerg]
        if sümbol == " ":
            laud[rida][veerg] = "-"
            print("Seal ruudul ei olnud laeva")
            return 0, laud
        elif sümbol == "O":
            print("Tabati laeva")
            laud[rida][veerg] = "X"
            return 1, laud
        else:
            print("Seda kohta on juba pommitatud! Proovige uuesti...")
            return -1, laud
    except LaevadePommitamiseException:
        print("Laual pole selliseid kohti")
        return -1, laud


def kasutaja_pommitamine(laud):
    tahed = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    while True:
        rida = -1
        veerg = -1
        while rida not in range(10) or veerg not in range(10):
            tulemus = input("Sisesta palun pommitatav ruut (kujul A0, A1 jne): ")
            try:
                rida = tahed.index(tulemus[0].upper())
                veerg = int(tulemus[1])
            except:
                print("Sisestasite ruudu koordinaadid valel kujul! Proovige uuesti...")
        pommitamise_tulemus, lauaseis = pommita(rida, veerg, laud)
        if pommitamise_tulemus == 1 or pommitamise_tulemus == 0:
            return pommitamise_tulemus, lauaseis
