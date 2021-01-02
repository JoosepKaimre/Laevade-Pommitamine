import sys
import time

import pygame
import laud as laua_meetodid
import mäng as mangu_meetodid
import algoritmid
import pildituvastus

# ~~~~~~~~~~~~~[suurused]~~~~~~~~~~~~~~~#
ekraaniLaius = 1180
ekraaniKõrgus = 650
ruuduLaius = 50
ruuduKõrgus = 50
# ~~~~~~~~~~~~~[menüü]~~~~~~~~~~~~~~~#
white = (255, 255, 255)
pas = (190, 190, 190)
akt = (230, 230, 230)
green = (48, 179, 83)  # mängija laeva sisaldava ruudu värv
red = (222, 66, 42)  # pommitatud laeva sisaldava ruudu värv
blue = (39, 153, 219)  # tühja või teadmata ruudu värv
yellow = (252, 223, 3)  # pommitatud, kuid tühja ruudu värv
b = pygame.image.load(".\\pildid\\valge.png")
b = pygame.transform.scale(b, (ruuduLaius, ruuduKõrgus))
# b1 = pygame.image.load("valge.png")
# b1 = pygame.transform.scale(b1, (ruuduLaius, ruuduKõrgus))
# b2 = pygame.image.load("valge.png")
# b2 = pygame.transform.scale(b2, (ruuduLaius, ruuduKõrgus))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
ekraan = pygame.display.set_mode((ekraaniLaius, ekraaniKõrgus))
pygame.display.set_caption('Laevade pommitamine')
gameIcon = pygame.image.load('.\\pildid\\laev_pommiga.png').convert_alpha()
pygame.display.set_icon(gameIcon)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
pygame.init()


def text_objects(text, font):
    black = (0, 0, 0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def nupp(tekst, x, y, nl, nk, algoritm=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + nl > mouse[0] > x and y + nk > mouse[1] > y:
        pygame.draw.rect(ekraan, akt, (x, y, nl, nk))
        if click[0] == 1 and algoritm is not None:
            if tekst == "Välju":
                välju()
            elif tekst == "Käsurealt":
                mäng(algoritm, False)
            elif tekst == "Pildilt":
                mäng(algoritm, True)
            else:
                time.sleep(0.3)
                lauaSisestamiseValik(algoritm)
    else:
        pygame.draw.rect(ekraan, pas, (x, y, nl, nk))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(tekst, smallText)
    textRect.center = ((x + (nl / 2)), (y + (nk / 2)))
    ekraan.blit(textSurf, textRect)


def välju():
    pygame.quit()
    quit()


def menüü():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ekraan.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Laevade pommitamine", largeText)
        TextRect.center = ((ekraaniLaius / 2), 50)
        ekraan.blit(TextSurf, TextRect)

        nupp("Random", 415, 150, 350, 50, algoritmid.random_käik)
        nupp("Hunt", 415, 250, 350, 50, algoritmid.hunt_algoritm)
        nupp("Hunt koos paarsusega", 415, 350, 350, 50, algoritmid.hunt_paarsus_algoritm)
        nupp("Tõenäosuslik", 415, 450, 350, 50, algoritmid.tõenäosuslik)
        nupp("Välju", 415, 550, 350, 50, välju)
        pygame.display.update()


def lauaSisestamiseValik(algoritm):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ekraan.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Vali laua sisestamise meetod", largeText)
        TextRect.center = ((ekraaniLaius / 2), 50)
        ekraan.blit(TextSurf, TextRect)

        nupp("Käsurealt", 415, 150, 350, 50, algoritm)
        nupp("Pildilt", 415, 250, 350, 50, algoritm)
        pygame.display.update()


def joonistaAlgsedLauad():
    pygame.font.init()
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 30)

    ekraan.fill(white)

    laud1 = pygame.draw.rect(ekraan, pas, (60, 100, 500, 500))
    textsurface = myfont.render("Vastase laud", True, (0, 0, 0))
    ekraan.blit(textsurface, (70, 25))

    laud2 = pygame.draw.rect(ekraan, pas, (620, 100, 500, 500))
    textsurface = myfont.render("Sinu laud", True, (0, 0, 0))
    ekraan.blit(textsurface, (630, 25))

    tahed = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    # Esimesele lauale tähtede lisamine
    for i in range(10):
        textsurface = myfont.render(tahed[i], True, (0, 0, 0))
        ekraan.blit(textsurface, (35 - textsurface.get_width() / 2, i * 50 + 125 - textsurface.get_height() / 2))

    # Teisele lauale tähtede lisamine
    for i in range(10):
        textsurface = myfont.render(tahed[i], True, (0, 0, 0))
        ekraan.blit(textsurface, (595 - textsurface.get_width() / 2, i * 50 + 125 - textsurface.get_height() / 2))

    # Esimesele lauale numbrite lisamine
    for i in range(10):
        textsurface = myfont.render(str(i), True, (0, 0, 0))
        ekraan.blit(textsurface, (i * 50 + 85 - textsurface.get_width() / 2, 75 - textsurface.get_height() / 2))

    # Teisele lauale numbrite lisamine
    for i in range(10):
        textsurface = myfont.render(str(i), True, (0, 0, 0))
        ekraan.blit(textsurface, (i * 50 + 645 - textsurface.get_width() / 2, 75 - textsurface.get_height() / 2))


def uuendaVastaseLauda(vastase_lauaseis):
    # " " tähistab tühja ruutu (sinine)
    # "-" tähistab pommitatud tühja ruutu (kollane)
    # "X" tähistab pommitatud laeva ruutu (punane)

    # Esimesele lauale ruutude joonistamine
    for i in range(10):
        for j in range(10):
            if vastase_lauaseis[j][i] == "-":
                color = yellow
            elif vastase_lauaseis[j][i] == "X":
                color = red
            else:
                color = blue
            pygame.draw.rect(ekraan, color, (i * 50 + 60, j * 50 + 100, 50, 50), 0)
            pygame.draw.rect(ekraan, white, (i * 50 + 60, j * 50 + 100, 50, 50), 1)
    pygame.display.update()
    pygame.event.pump()


def uuendaKasutajaLauda(kasutaja_lauaseis):
    # " " tähistab tühja ruutu (sinine)
    # "-" tähistab pommitatud tühja ruutu (kollane)
    # "O" tähistab laeva ruutu (roheline)
    # "X" tähistab pommitatud laeva ruutu (punane)

    # Teisele lauale ruutude joonistamine
    for i in range(10):
        for j in range(10):
            if kasutaja_lauaseis[j][i] == "-":
                color = yellow
            elif kasutaja_lauaseis[j][i] == "X":
                color = red
            elif kasutaja_lauaseis[j][i] == "O":
                color = green
            else:
                color = blue
            pygame.draw.rect(ekraan, color, (i * 50 + 620, j * 50 + 100, 50, 50), 0)
            pygame.draw.rect(ekraan, white, (i * 50 + 620, j * 50 + 100, 50, 50), 1)
    pygame.display.update()
    pygame.event.pump()


def joonistalauad(vastase_lauaseis, kasutaja_lauaseis):
    uuendaVastaseLauda(vastase_lauaseis)
    uuendaKasutajaLauda(kasutaja_lauaseis)


def mäng(algoritm, loeLaudPildilt):
    # Joonistame laudade indeksid ja pealkirjad
    joonistaAlgsedLauad()

    # Loome AI-le suvaliselt täidetud laua ja kasutajale tühja laua
    laevad = [5, 4, 3, 3, 2]
    vastase_lauaseis = laua_meetodid.laud_koos_laevadega(10, laevad)
    kasutaja_lauaseis = laua_meetodid.loo_laud(10)
    joonistalauad(vastase_lauaseis, kasutaja_lauaseis)

    # Loeme mängija laua sisse kas käsurealt või pildilt
    kasutaja_lauaseis = []
    if not loeLaudPildilt:
        kasutaja_lauaseis = laua_meetodid.loo_laud(10)
        # Laseme mängijal vajalikud laevad lauale lisada
        for laev in laevad:
            pygame.event.get()  # Seda läheb vaja, et GUI ei muutuks Not Responding'uks ja joonistaks laevu ühekaupa
            kasutaja_lauaseis = mangu_meetodid.kasutaja_laeva_lisamine(kasutaja_lauaseis, laev)
            # Uuendame kasutaja lauda GUI-s
            uuendaKasutajaLauda(kasutaja_lauaseis)
            pygame.event.get()
            pygame.display.update()
            pygame.event.pump()
        print()
    else:
        try:
            pildi_nimi = input("Sisestage laua pildi nimi: ")
            kasutaja_lauaseis = pildituvastus.kasutaja_laud_pildilt(pildi_nimi)
            print()
        except:
            input("Pildi sisse lugemine ebaõnnestus...")
            välju()

    # Joonistame mängija ja AI lauadade maatriksite põhjal lauad GUI-sse
    joonistalauad(vastase_lauaseis, kasutaja_lauaseis)
    pygame.display.update()
    pygame.event.pump()

    # Mängu main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.event.get()

        ############################
        # Mängijalt käigu küsimine #
        ############################
        print("\n--- Sinu käik ---")
        kasutaja_pommitamise_tulemus = 1
        # Laseme kasutajal korduvalt käike teha kui ta sai AI laevadele pihta
        while kasutaja_pommitamise_tulemus == 1:
            pygame.event.get()
            kasutaja_pommitamise_tulemus, vastase_lauaseis = laua_meetodid.kasutaja_pommitamine(vastase_lauaseis)
            uuendaVastaseLauda(vastase_lauaseis)
            pygame.event.get()
            # See on vajalik, et mäng ka siin lõppeks
            # (muidu jääb loopi kinni kuni tühjale ruudule käib)
            if laua_meetodid.mäng_läbi(vastase_lauaseis):
                print()
                print("Sinu võit!")
                input("Vajuta 'Enter', et lõpetada...")
                välju()
        if laua_meetodid.mäng_läbi(vastase_lauaseis):
            print()
            print("Sinu võit!")
            input("Vajuta 'Enter', et lõpetada...")
            välju()

        #####################
        # AI käigu tegemine #
        #####################
        print("\n--- Vastase käik ---")
        vastase_pommitamise_tulemus = 1
        # Laseme AI-l korduvalt käike teha kui ta sai kasutaja laevadele pihta
        while vastase_pommitamise_tulemus == 1:
            pygame.event.get()
            vastase_pommitamise_tulemus, kasutaja_lauaseis = algoritm(kasutaja_lauaseis)
            uuendaKasutajaLauda(kasutaja_lauaseis)
            pygame.event.get()
            # See on vajalik, et mäng ka siin lõppeks
            # (muidu jääb loopi kinni kuni tühjale ruudule käib)
            if laua_meetodid.mäng_läbi(kasutaja_lauaseis):
                print()
                print("Vastase võit!")
                input("Vajuta 'Enter', et lõpetada...")
                välju()
        if laua_meetodid.mäng_läbi(kasutaja_lauaseis):
            print()
            print("Vastase võit!")
            input("Vajuta 'Enter', et lõpetada...")
            välju()
        print()


menüü()
