import laud as laua_meetodid
from random import choice

# globaalsed muutujad
suurus = 10
laevad = [5, 4, 3, 3, 2]


def mäng():
    global suurus
    global laevad
    # todo - tuleb mõelda, kuidas me kasutajale näitame, mida tema teab.
    laud1_mängija = laua_meetodid.laud_koos_laevadega(suurus, laevad)
    # laud1_info = laua_meetodid.loo_laud(suurus)

    laud2_mängija = laua_meetodid.loo_laud(suurus)
    # laud2_info = laua_meetodid.loo_laud(suurus)
    kasutaja_laevade_lisamine(laud2_mängija, laevad)


def kasutaja_laevade_lisamine(laud, laevad):
    global suurus
    for laev in laevad:
        suund = ""
        rida = -1
        veerg = -1
        while True:
            print("Laud on praegu selline:")
            väljasta_laud(laud)
            while suund not in ["N", "E", "S", "W"]:
                suund = input("Sisesta palun laeva suund (N, E, S, W): ").upper()
            while rida not in range(suurus):
                rida = int(input("Sisesta palun rea indeks vahemikus 0-" + str(suurus - 1) + ": "))
            while veerg not in range(suurus):
                veerg = int(input("Sisesta palun veeru indeks vahemikus 0-" + str(suurus - 1) + ": "))
            if laua_meetodid.lisa_laev(laev, suund, rida, veerg, laud):
                print("Laev lisatud!")
                break
            print("Lisamine ebaõnnestus, küsitakse uus sisend")
            suund = ""
            rida = -1
            veerg = -1
    print("Lõplik laud on selline")
    väljasta_laud(laud)
    #return laud


def mängu_mängimine(laud1, laud2):
    # kasutaja sisend ja arvuti käik
    return


def random_käik(laud):
    # seda ilmselt saaks efektiivsemaks teha kui võtta korra pommitamata kohad ja siis eemaldada sealt elemente, mitte iga kord uuesti leida.
    k = laua_meetodid.pommitamata_kohad(laud)
    ruut = choice(k)
    laua_meetodid.pommita(ruut[0], ruut[1], laud)


def väljasta_laud(laud):
    print(" ", end=" ")
    for i in range(suurus):
        print(str(i) + ".", end="\t")
    print()
    i = 0
    for rida in laud:
        print(str(i) + ".", end="\t")
        i += 1
        for ruut in rida:
            print(ruut, end="\t")
        # print()
        print()


def algoritm():
    # todo
    return
