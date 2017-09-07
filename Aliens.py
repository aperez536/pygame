import pygame
import time
import random
from logging import addLevelName
from test.pickletester import DATA0_DIS

pygame.init()

########DISPLAY SETTINGS########
DISPLAY_ANCHO = 500
DISPLAY_ALTURA = 500
ALIEN_ANCHO = 50
ALIEN_ALTO = 50

#########COLORES#############

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
BLANCOVIEJO = (205, 192, 176)

#######IMAGENES########
imagen1 = pygame.image.load('aliensinfondo.png')
imagen1 = pygame.transform.scale(imagen1, (50,50))
imagen2= pygame.image.load("Imagenes/alien2.png")
imagen2 = pygame.transform.scale(imagen2, (50,50))
imagen3= pygame.image.load("Imagenes/alien3.png")
imagen3 = pygame.transform.scale(imagen3, (50,50))
imagen4= pygame.image.load("Imagenes/alien4.png")
imagen4 = pygame.transform.scale(imagen4, (50,50))
imagen5= pygame.image.load("Imagenes/alien5.png")
imagen5 = pygame.transform.scale(imagen5, (50,50))
imagenes=[imagen1,imagen2,imagen3,imagen4,imagen5]
ImagenActual=0
imagenes[ImagenActual]
#background =  pygame.image.load()
#background = pygame.transform.scale(background,(500,800)) #Ajuste de la imagen al tamao del display

##########AJUSTES VARIOS############

gameDisplay = pygame.display.set_mode((DISPLAY_ANCHO, DISPLAY_ALTURA)) #Tamao del display
pygame.display.set_caption("Space full of aliens") #Nombre del juego
clock = pygame.time.Clock()

def alien(x,y,contador):
    gameDisplay.blit(imagenes[contador], (x,y))

def texto(text, font):
    textSurface = font.render(text, True, BLANCO)
    return textSurface, textSurface.get_rect()

def mensaje1(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto (text, largeText)
    TextRect.center= ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
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
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def game_loop():
    x = 0
    y = 0
    vel = 10
    gameExit = False
    x_var = 200
    y_var = 200
    contador=0 # contador
    # para ver si la tecla sigue apretada
    while not gameExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            ###MOVIMIENTOS###
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    contador+=1
                    x =- vel     
                if event.key == pygame.K_RIGHT:
                    contador+=1
                    x = vel
                if event.key == pygame.K_UP:
                    contador+=1
                    y =- vel
                if event.key == pygame.K_DOWN:
                    contador+=1
                    y = vel
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:  
                    x = 0
                if event.key == pygame.K_RIGHT:
                    x = 0
                if event.key == pygame.K_UP:
                    y = 0
                if event.key == pygame.K_DOWN:
                    y = 0
            
        if(contador>4):
            contador=0
        
        x_var += x
        y_var += y

        gameDisplay.fill(NEGRO)
        alien(x_var, y_var,contador)
       
        ###Colisiones
        if x_var > DISPLAY_ANCHO-ALIEN_ANCHO or x_var < 0:
            mensaje_borde()
        if y_var > DISPLAY_ALTURA-ALIEN_ALTO or y_var < 0:
            gameExit = True
        if x_var > DISPLAY_ALTURA or x_var < 0:
            gameExit = True
            
        
        pygame.display.update()   ##actualiza display
        clock.tick(20)


game_loop()
pygame.quit()
quit()
