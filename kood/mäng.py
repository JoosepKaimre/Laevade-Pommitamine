import laud as laua_meetodid

# globaalsed muutujad
suurus = 10
laevad = [5, 4, 3, 3, 2]


def kasutaja_laeva_lisamine(laud, laev):
    global suurus
    suund = ""
    rida = -1
    veerg = -1

    tahed = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    while True:
        print("Lisa laev pikkusega " + str(laev))
        while suund not in ["N", "E", "S", "W"]:
            suund = input("Sisesta palun laeva suund (N, E, S, W): ").upper()
        while rida not in range(suurus) or veerg not in range(suurus):
            tulemus = input("Sisesta palun alguspunkt (kujul A0, A1 jne): ")
            try:
                rida = tahed.index(tulemus[0].upper())
                veerg = int(tulemus[1])
            except:
                print("Sisestasite alguspunkti valel kujul! Proovige uuesti...")
        if laua_meetodid.lisa_laev(laev, suund, rida, veerg, laud):
            print("Laev lisatud!")
            break
        print("Lisamine ebaõnnestus, küsitakse uus sisend.")
        suund = ""
        rida = -1
        veerg = -1
    return laud


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
    return laud


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
