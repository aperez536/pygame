# BREVE DESCRIPCION DEL JUEGO:
# En una primera instancia del juego, un alien
# se pierde en el espacio y aterriza accidentalmente en XXXXXXXX y en esta
# maniobra se le rompe la nave. Por lo que debera juntar las piezas para
# armarla nuevamente y poder regresar a su hogar. En el segundo nivel
# debera esquivar meteoros en el espacio para poder llegar a destino.
#
# MANUAL DE USUARIO: El personaje principal solo se mueve con las flechas
# ARRIBA (W), ABAJO (S), DERECHA (A) e IZQUIERDA (D).
#
#
# OBJETIVOS: 1 nivel: juntar todas las piezas
#            2 nivel: esquivar cierta cantidad de meteoritos para llegar al hogar
#
# CREADORES: Alan Perez, Nicolas Ojeda, Micaela Peralta.

import pygame
import time
import random
from Clases.Alien import Alien
from Clases.Config import Config
from Clases.Constantes import *

pygame.init()

config = Config()
config.gameDisplay = pygame.display.set_mode((DISPLAY_ANCHO, DISPLAY_ALTURA)) #Tamano del display

def tuerca(x, y):
    config.gameDisplay.blit(imagen6, (x, y))

def tornillo(x, y):
    config.gameDisplay.blit(imagen7, (x, y))

def nave(x, y):
    config.gameDisplay.blit(imagen8, (x, y))

def texto(text, font):
    textSurface = font.render(text, True, BLANCO)
    return textSurface, textSurface.get_rect()

def mensaje1(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    config.gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop() #No tiene que volver a empezar

def mensaje2(text): # es igual que mensaje 1?????
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    config.gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def mensaje_gano():
    mensaje2('gano el juego')

def mensaje_borde():
    mensaje1('Choque con el borde!')

def mensaje_colision():
    colision1('Choque!')

def colision1(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    config.gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def game_loop():
    x = 0
    y = 0

    #Creamos el Alien
    iAlien = Alien("JuanCarlosNoveno")

    #posicion de la tuerca
    x1 = 350
    y1 = 250

    #---------------
    vel = 10
    gameExit = False

    #pos del personaje principal
    x_var = 200
    y_var = 200

    #------------
    contador = 0 # contador para el cambio visual de imagenes
    agarratuerca = False
    contartuerca = -1

    #---pos del tornillo
    x2 = 300
    y2 = 300

    #-------
    agarratornillo = False
    contartornillo = 0

    #posicion nave
    x3 = 450
    y3 = 450

    # para ver si la tecla sigue apretada
    while not gameExit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            ###MOVIMIENTOS###
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    contador += 1
                    x =- vel
 
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    contador += 1
                    x = vel
                    
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    contador += 1
                    y =- vel

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    contador += 1
                    y = vel
                    
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:  
                    x = 0
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x = 0
                    
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y = 0
                    
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y = 0
            
        if(contador > 4):
            contador = 0
        
        x_var += x
        y_var += y
        
        # si el perosonaje principal esta en esa pocision , va a agarrar la tuerca.
        if((x_var>=330 and x_var<=340)and (y_var >=220 and y_var<=250) ):
            agarratuerca=True
            contartuerca=1
            
        config.gameDisplay.fill(NEGRO)
        config.gameDisplay.blit(fondo, (0, 0))
        
        iAlien.move(x_var, y_var,contador)
        nave(x3, y3)
        
        # si el perosonaje principal esta en esa pocision , va a agarrar la tuerca.

        #print (x_var,y_var,contartornillo,contartuerca)
        if((x_var>=280 and x_var<=290)and (y_var >267 and y_var<=290) ):
            agarratornillo=True
            contartornillo=1
        #----------------------------------------
        
        
        #------------------------
        if agarratuerca==False:
            tuerca(x1,y1)
            
        if agarratornillo==False:
            tornillo(x2, y2)
        #-----------------------------------------------------
            
        ###Colisiones
        if x_var >= COL_RIGHT or x_var <= 0:
            mensaje_borde()
            
        if y_var >= COL_BOTTOM or y_var <= 0:
            mensaje_borde()

            
        if contartornillo == contartuerca:
            if ((x_var>=410 and x_var<=450) and (y_var>=400 and y_var<=450)):
                mensaje_gano()
        
        config.updateFPS() #Actualiza el Display

def game_main_menu():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        config.gameDisplay.fill(NEGRO)
        config.updateFPS() #Actualiza el Display

def main():
    #game_main_menu()
    game_loop()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
