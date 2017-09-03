import pygame
import time
import random
from logging import addLevelName
from test.pickletester import DATA0_DIS

pygame.init()

########DISPLAY SETTINGS########
display_ancho = 500
display_altura = 500
imagen_ancho= 50
imagen_alto= 50

#########COLORES#############

negro= (0,0,0)
blanco=(255,255,255)
BlancoViejo = (205,192,176)

#######IMAGENES########
imagen1= pygame.image.load('aliensinfondo.png')
imagen1= pygame.transform.scale(imagen1, (50,50))
#background =  pygame.image.load()
#background= pygame.transform.scale(background,(500,800)) #Ajuste de la imagen al tamao del display

##########AJUSTES VARIOS############

gameDisplay= pygame.display.set_mode((display_ancho, display_altura)) #Tamao del display
pygame.display.set_caption("Space full of aliens") #Nombre del juego
clock=pygame.time.Clock()

def alien(x,y):
    gameDisplay.blit(imagen1, (x,y))

def texto(text, font):
    textSurface = font.render(text, True, blanco)
    return textSurface, textSurface.get_rect()

def mensaje1(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto (text, largeText)
    TextRect.center= ((display_ancho/2), (display_altura/2))
    gameDisplay.blit (TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()
    
def mensaje_borde():
    mensaje1('Choque con el borde!')
def mensaje_colision():
    colision1('Choque!')

def colision1(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto (text, largeText)
    TextRect.center= ((display_ancho/2), (display_altura/2))
    gameDisplay.blit (TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def game_loop():
    x=0
    y=0
    vel=10
    gameExit=False
    x_var=200
    y_var=200

    while not gameExit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                
               ###MOVIMIENTOS###
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x=-vel
                if event.key == pygame.K_RIGHT:
                    x=vel
                if event.key == pygame.K_UP:
                    y=-vel
                if event.key == pygame.K_DOWN:
                    y=vel
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x=0
                if event.key == pygame.K_RIGHT:
                    x=0
                if event.key == pygame.K_UP:
                    y=0
                if event.key == pygame.K_DOWN:
                    y=0


        x_var+=x
        y_var+=y
        gameDisplay.fill(negro)
        alien(x_var,y_var)

        
                       ###Colisiones
        if x_var > display_ancho-imagen_ancho or x_var < 0:
            mensaje_borde()
        if y_var > display_altura-imagen_alto or y_var < 0:
            gameExit=True
        if x_var > display_altura or x_var < 0:
            gameExit=True
        


        pygame.display.update()   ##actualiza display
        clock.tick(30)

game_loop()
pygame.quit()
quit()
