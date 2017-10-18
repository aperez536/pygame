import pygame
import time
import random
from Clases.Alien import Alien
from Clases.Config import Config
from Clases.Mensaje import Mensaje
from Clases.Constantes import *

pygame.init()



config = Config()
config.gameDisplay = pygame.display.set_mode((DISPLAY_ANCHO, DISPLAY_ALTURA), pygame.DOUBLEBUF)


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

def mensaje2(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    config.gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

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

def meteorito(trnc,x,y):
     config.gameDisplay.blit(trnc, (x,y))


def game_loop():
    
    x = 0
    y = 0

    #Prueba de Mensajes Nuevos (Falta hacerles un timer para que desaparescan con el tiempo??)
    nuevoMensaje = Mensaje()
    nuevoMensaje.Color = CELESTE
    nuevoMensaje.Posicion = "top-left"
    nuevoMensaje2 = Mensaje()
    nuevoMensaje2.Posicion = "bottom-left"
    nuevoMensaje2.Color = GRIS
    #posicion de la tuerca
    x1 = 350
    y1 = 250

    #---------------
    vel = 10
    gameExit = False

    #pos de la nave
    x_var = 200
    y_var = 400

    #sonidos de personaje de movimiento y agarre
    sonidomover=pygame.mixer.Sound("Sonidos/mover.mp3")
    pygame.mixer.music.load("Sonidos/win.mp3")
    
    #posiciones del meteoro
    meteoro1x= random.randrange(0,400)
    meteoro1y=0
    meteoro2x=random.randrange(0,400)
    meteoro2y=0
    meteoro3x=random.randrange(0,400)
    meteoro3y=0
    meteoro4x=random.randrange(0,500)
    meteoro4y=0
    meteoro5x=random.randrange(0,500)
    meteoro5y=0
    meteoro6x=random.randrange(0,500)
    meteoro6y=0
    
    while not gameExit:
             #pygame.display.update()
        for event in pygame.event.get():
            

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                   
            ###MOVIMIENTOS###
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x =- vel
                    sonidomover.play()
 
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x = vel
                    sonidomover.play()
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:  
                    x = 0
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x = 0

        #meteoro
        meteoro1y+=10
        meteoro2y+=10
        meteoro3y+=10
        meteoro4y+=10
        meteoro5y+=10
        meteoro6y+=10
 
        x_var += x
        y_var += y
    
               
        #lluvia  de meteoros
        if meteoro1y==500:
            meteoro1y=0
            meteoro1x=random.randrange(0,400)#devuelve una posicion aleatoria en el rango asignado
        if meteoro2y==550:
            meteoro2y=0
            meteoro2x=random.randrange(0,400)
        if meteoro3y==600:
            meteoro3y=0
            meteoro3x=random.randrange(0,400)   
            
        if meteoro4y==600:
            meteoro4y=0
            meteoro4x=random.randrange(0,400)   
        
        if meteoro5y==600:
            meteoro5y=0
            meteoro5x=random.randrange(0,400)   
            
        if meteoro6y==600:
            meteoro6y=0
            meteoro6x=random.randrange(0,400)   

        #colision
        auxposx=x_var-50
        auxposy=y_var
        i=1
        col=False
        print(meteoro1x,meteoro1y)
                # colision del meteoro
        for i in range (1,70):
                auxposx=auxposx+1
                if  meteoro1x==auxposx and meteoro1y==auxposy:
        
                    col=True

                if  meteoro2x==auxposx and meteoro2y==auxposy:
                    col=True

                if  meteoro3x==auxposx and meteoro3y==auxposy:
                    col=True
                    
                if  meteoro4x==auxposx and meteoro4y==auxposy:
                    col=True
                if  meteoro5x==auxposx and meteoro5y==auxposy:
                    col=True
                if  meteoro6x==auxposx and meteoro6y==auxposy:
                    col=True
        if col==True:
                    mensaje_colision()
                    game_loop()




        ##
        # si el perosonaje principal esta en esa pocision , va a agarrar la tuerca.
        config.gameDisplay.fill(NEGRO)
        config.gameDisplay.blit(fondo, (0, 0))
        #---------------------------------------------------
        #dezplazamiento de la nave--
        nave(x_var, y_var)
        # caida de meteoro 
        meteorito(meteoro, meteoro1x, meteoro1y)
        meteorito(meteoro, meteoro2x, meteoro2y)
        meteorito(meteoro, meteoro3x, meteoro3y)
        meteorito(meteoro, meteoro4x, meteoro4y)
        meteorito(meteoro, meteoro5x, meteoro5y)
        meteorito(meteoro, meteoro6x, meteoro6y)
           
        ###Colisiones
        if x_var >= COL_RIGHT or x_var <= 0:
            mensaje_borde()
            
        if y_var >= COL_BOTTOM or y_var <= 0:
            mensaje_borde()
        
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