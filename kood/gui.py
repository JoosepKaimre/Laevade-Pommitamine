import pygame

#~~~~~~~~~~~~~[suurused]~~~~~~~~~~~~~~~# 
ekraaniLaius = 750
ekraaniKõrgus = 750
ruuduLaius = 50
ruuduKõrgus = 50
#~~~~~~~~~~~~~[menüü]~~~~~~~~~~~~~~~# 
white = (255,255,255)
pas = (190, 190, 190)
akt = (230, 230, 230)
b = pygame.image.load(".\\pildid\\valge.png")
b = pygame.transform.scale(b, (ruuduLaius, ruuduKõrgus))
#b1 = pygame.image.load("valge.png")
#b1 = pygame.transform.scale(b1, (ruuduLaius, ruuduKõrgus))
#b2 = pygame.image.load("valge.png")
#b2 = pygame.transform.scale(b2, (ruuduLaius, ruuduKõrgus))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
ekraan = pygame.display.set_mode((ekraaniLaius, ekraaniKõrgus))
pygame.display.set_caption('Laevade pommitamine')
gameIcon = pygame.image.load('.\\pildid\\laev_pommiga.png').convert_alpha()
pygame.display.set_icon(gameIcon)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
pygame.init()

def text_objects(text, font):
    black=(0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def nupp(tekst, x, y, nl, nk, funktsioon=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+nl > mouse[0] > x and y+nk > mouse[1] > y:
        pygame.draw.rect(ekraan, akt,(x,y,nl,nk))
        if click[0] == 1 and funktsioon != None:
            funktsioon()
    else:
        pygame.draw.rect(ekraan, pas,(x,y,nl,nk))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(tekst, smallText)
    textRect.center = ( (x+(nl/2)), (y+(nk/2)) )
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
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Laevade pommitamine", largeText)
            TextRect.center = ((ekraaniLaius/2),100)
            ekraan.blit(TextSurf, TextRect)
            
            nupp("algoritm1", 300, 250, 150, 50)
            nupp("algoritm2", 300, 350, 150, 50)
            nupp("algoritm3", 300, 450, 150, 50)
            nupp("Välju", 300, 550, 150, 50, välju)

            pygame.display.update()
    
menüü()
