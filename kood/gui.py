import pygame

# ~~~~~~~~~~~~~[suurused]~~~~~~~~~~~~~~~#
ekraaniLaius = 1180
ekraaniKõrgus = 750
ruuduLaius = 50
ruuduKõrgus = 50
# ~~~~~~~~~~~~~[menüü]~~~~~~~~~~~~~~~#
white = (255, 255, 255)
pas = (190, 190, 190)
akt = (230, 230, 230)
green = (48, 179, 83)
red = (222, 66, 42)
blue = (39, 153, 219)
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


def nupp(tekst, x, y, nl, nk, funktsioon=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + nl > mouse[0] > x and y + nk > mouse[1] > y:
        pygame.draw.rect(ekraan, akt, (x, y, nl, nk))
        if click[0] == 1 and funktsioon != None:
            funktsioon()
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
        TextRect.center = ((ekraaniLaius / 2), 100)
        ekraan.blit(TextSurf, TextRect)

        nupp("algoritm1", 300, 250, 150, 50)
        nupp("algoritm2", 300, 350, 150, 50)
        nupp("algoritm3", 300, 450, 150, 50)
        nupp("Välju", 300, 550, 150, 50, välju)

        pygame.display.update()


def mäng():
    tahed = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ekraan.fill(white)

        laud1 = pygame.draw.rect(ekraan, pas, (60, 100, 500, 500))
        laud2 = pygame.draw.rect(ekraan, pas, (620, 100, 500, 500))

        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont(pygame.font.get_default_font(), 30)

        # Esimesele lauale tähtede lisamine
        for i in range(10):
            textsurface = myfont.render(tahed[i], True, (0, 0, 0))
            ekraan.blit(textsurface, (35 - textsurface.get_width() / 2, i*50 + 125 - textsurface.get_height() / 2))

        # Teisele lauale tähtede lisamine
        for i in range(10):
            textsurface = myfont.render(tahed[i], True, (0, 0, 0))
            ekraan.blit(textsurface, (595 - textsurface.get_width() / 2, i*50 + 125 - textsurface.get_height() / 2))

        # Esimesele lauale numbrite lisamine
        for i in range(10):
            textsurface = myfont.render(str(i+1), True, (0, 0, 0))
            ekraan.blit(textsurface, (i*50 + 85 - textsurface.get_width() / 2, 75 - textsurface.get_height() / 2))

        # Teisele lauale numbrite lisamine
        for i in range(10):
            textsurface = myfont.render(str(i + 1), True, (0, 0, 0))
            ekraan.blit(textsurface, (i*50 + 645 - textsurface.get_width() / 2, 75 - textsurface.get_height() / 2))



        # Esimesele lauale ruutude joonistamine
        for i in range(10):
            for j in range(10):
                pygame.draw.rect(ekraan, blue, (i*50+60,j*50+100,50,50),0)
                pygame.draw.rect(ekraan, akt, (i*50+60,j*50+100,50,50),1)

        # Teisele lauale ruutude joonistamine
        for i in range(10):
            for j in range(10):
                pygame.draw.rect(ekraan, blue, (i * 50 + 620, j * 50 + 100, 50, 50),0)
                pygame.draw.rect(ekraan, akt, (i * 50 + 620, j * 50 + 100, 50, 50),1)

        pygame.display.update()


mäng()
