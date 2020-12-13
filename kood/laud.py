# " " tähistab tühja ruutu
# "-" tähistab pommitatud tühja ruutu
# "O" tähistab laeva ruutu
# "X" tähistab pommitatud laeva ruutu

from random import randint, choice

def loo_laud(suurus):
    # võtab sisse laua suuruse argumendina
    # loob tühja laua.
    tulemus = []
    for i in range(suurus):
        tulemus.append(suurus*[" "])
    return tulemus

def pommita(rida, veerg, laud):
    # rida - rea number
    # veerg - veeru number
    # laud - mänguload
    try:
        sümbol = laud[rida][veerg]
        if sümbol == " ":
            laud[rida][veerg] = "-"
            print("Seal ruudul ei olnud laeva")
            return 0
        elif sümbol == "O":
            print("Tabati laeva")
            laud[rida][veerg] = "X"
            return 1
        else:
            print("Seda kohta on juba pommitatud")
            return -1
        
    except:
        print("Laual pole selliseid kohti")
        return -1

def lisa_laev(suurus, suund, rida, veerg, laud):
    # suurus - laeva suurus
    # suund (N,W,E,S) - kuhu laev jääb stardiruutust
    # rida - stardiruudu reanumber
    # veerg - stardiruudu veerunumber
    # laud
    try:
        for i in range(suurus):
            if suund == "N":
                if laud[rida-i][veerg] != " ":
                    print("Need laeva kohad on juba võetud")
                    return False
            elif suund =="E":
                if laud[rida][veerg+i] != " ":
                    print("Need laeva kohad on juba võetud")
                    return False
            elif suund =="S":
                if laud[rida+i][veerg] != " ":
                    print("Need laeva kohad on juba võetud")
                    return False
            elif suund == "W":
                if laud[rida][veerg-i] != " ":
                    print("Need laeva kohad on juba võetud")
                    return False
            else:
                print("Sellist suunda ei saa olla")
                return False
        for i in range(suurus):
            if suund == "N":
                laud[rida-i][veerg] = "O"
                
            elif suund =="E":
                laud[rida][veerg+i] = "O"
            elif suund =="S":
                laud[rida+i][veerg] = "O"
            elif suund == "W":
                laud[rida][veerg-i] = "O"
            else:
                print("Sellist suunda ei saa olla")
                return False
        return True
            
    except:
        print("Laev jääb lauast välja")
        return False
    
def mäng_läbi(laud):
    for rida in laud:
        for ruut in rida:
            if ruut == "O":
                return False
    return True

def laud_koos_laevadega(suurus):
    laud = loo_laud(suurus)
    laevad = [5,4,3,3,2]
    for laev in laevad:
        while True:
            suunad = []
            rida = randint(0,suurus-1)
            veerg = randint(0,suurus-1)
            if laev-1 <=rida:
                suunad.append("N")
            if rida <= suurus-laev:
                suunad.append("S")
            if laev-1 <= veerg:
                suunad.append("W")
            if veerg <= suurus-laev:
                suunad.append("E")
            if lisa_laev(laev, choice(suunad), rida, veerg, laud):
                break
    return laud


def pommitamata_kohad(laud):
    tulem = []
    for i in range(len(laud)):
        for j in range(len(laud)):
            if laud[i][j] == " ":
                tulem.add((i,j))
    return tulem
            
        
        
        
    