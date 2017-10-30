import pygame
import time
import random
from Clases.Alien import Alien
from Clases.Config import Config
from Clases.Mensaje import Mensaje
from Clases.Constantes import *
from Niveles.Nivel_2 import *
from random import randint

pygame.init()

config = Config()
config.gameDisplay = pygame.display.set_mode((DISPLAY_ANCHO, DISPLAY_ALTURA), pygame.DOUBLEBUF)

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
    game_loop() 

def mensaje2(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    config.gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def mensaje_gano():
    mensaje2('Has ganado el juego!')

def mensaje_borde():
    mensaje1('Choque con el borde!')

def mensaje_colision():
    colision1('Has sido golpeado!')

def colision1(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    config.gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def agarraobjeto(aagarro,totalitenagarrado):
    Puntaje = 0
    if  aagarro==True:
        totalitenagarrado+=100
    return totalitenagarrado

def tronco1(trnc,x,y):
     config.gameDisplay.blit(trnc, (x,y))


def game_loop():
    
    x = 0
    y = 0

    # Mensajes Nuevos 
    nuevoMensaje = Mensaje()
    nuevoMensaje.Color = BLANCO
    nuevoMensaje.Posicion = "top-left"
    nuevoMensaje2 = Mensaje()
    nuevoMensaje2.Posicion = "bottom-left"
    nuevoMensaje2.Color = GRIS

    #Creamos el Alien
    iAlien = Alien("Alien")
    Puntaje = 0  
    #posicion de la tuerca
    x1 = 350
    y1 = 250
    x5=20
    y5=200
    
    #---------------
    vel = 10
    gameExit = False

    #pos del personaje principa7l
    x_var = 200
    y_var = 350

    #------------
    contador = 0 # contador para el cambio visual de imagenes
    agarratuerca = False
    contartuerca = 2
    agarratuerca1 = False
    contartuerca1 = 2

    #---pos de tornillos
    x2 = 300
    y2 = 300
    x4=150
    y4=150
    #-------
    agarratornillo = False
    contartornillo = 0
    agarratornillo1 = False
    contartornillo1 = 0

    #posicion nave
    x3 = 450
    y3 = 450
    #sonidos de personaje de movimiento y agarre
    sonidomover=pygame.mixer.Sound("Sonidos/mover.mp3")

    
    #posiciones del tronco Iniciales

    tron1x=random.randrange(randint(0, 60),randint(100, 460))
    tron1y=0
    tron2x=random.randrange(randint(0, 60),randint(100, 460))
    tron2y=0
    tron3x=random.randrange(randint(0, 60),randint(100, 460))
    tron3y=0
    
    while not gameExit:
             #pygame.display.update()
        for event in pygame.event.get():
            

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                   
            ###MOVIMIENTOS###
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    contador += 1
                    x =- vel
                    sonidomover.play()
 
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    contador += 1
                    x = vel
                    sonidomover.play()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    contador += 1
                    y =- vel
                    sonidomover.play()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    contador += 1
                    y = vel
                    sonidomover.play()
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
            
        #tronco
        tron1y+=10
        tron2y+=10
        tron3y+=10
 
        x_var += x
        y_var += y
        
               
        #lluvia 
        if tron1y==500:
            Puntaje = Puntaje + random.randrange(0,10)
            tron1y=0
            tron1x=random.randrange(randint(0, 60),randint(100, 460)) #devuelve una posicion aleatoria en el rango asignado
        if tron2y==550:
            Puntaje = Puntaje + random.randrange(0,10)
            tron2y=0
            tron2x=random.randrange(randint(0, 60),randint(100, 460))
        if tron3y==600:
            Puntaje = Puntaje + random.randrange(0,10)
            tron3y=0
            tron3x=random.randrange(randint(0, 60),randint(100, 460))

        #colision
        auxposx=x_var-66
        auxposy=y_var
        i=1
        col=False
                
        for i in range (1,130):
                auxposx=auxposx+1
                if  tron1x==auxposx and tron1y==auxposy:
                    col=True

                if  tron2x==auxposx and tron2y==auxposy:
                    col=True

                if  tron3x==auxposx and tron3y==auxposy:
                    col=True
        if col==True:
                    mensaje_colision()


        # si el perosonaje principal esta en esa posicion , va a agarrar la tuerca.
        if((x_var>=320 and x_var<=350)and (y_var >=210 and y_var<=265) ):
            agarratuerca=True
            if (contartuerca==2 and agarratuerca== True):
                Puntaje=agarraobjeto(agarratuerca,Puntaje)
                contartuerca=1
                agarratuerca= False
        if((x_var>=10 and x_var<=30)and (y_var >=170 and y_var<=210) ):
            agarratuerca1=True
            if (contartuerca1==2 and agarratuerca1== True):
                Puntaje=agarraobjeto(agarratuerca1,Puntaje)
                contartuerca1=1
                agarratuerca = False
        config.gameDisplay.fill(NEGRO)
        config.gameDisplay.blit(fondo2, (0, 0))
        
        #nuevoMensaje2.Print("Nombre:" + iAlien.name)

        iAlien.move(x_var, y_var,contador)

        #nuevoMensaje.Print("Puntaje:" + str(Puntaje))

        nave(x3, y3)
        tronco1(tronco,tron1x, tron1y)
        tronco1(tronco,tron2x, tron2y)
        tronco1(tronco,tron3x, tron3y)
            
     
        # si el perosonaje principal esta en esa posicion , va a agarrar la tuerca.

        #print (x_var,y_var,contartornillo,contartuerca)
        if((x_var>=280 and x_var<=290)and (y_var >267 and y_var<=310) ):
            agarratornillo=True
            if agarratornillo==True and contartornillo==0:
                Puntaje=agarraobjeto(agarratornillo,Puntaje)
                contartornillo=1
                agarratornillo = False
        
      
               
        #----------------------------------------
        if((x_var>=130 and x_var<=150)and (y_var >=120 and y_var<=160) ):
            agarratornillo1=True
            if agarratornillo1==True and contartornillo1==0:
                Puntaje=agarraobjeto(agarratornillo1,Puntaje)
                contartornillo1=1
                agarratornillo1=False
                           

    
        if agarratornillo1==False:
            tornillo(x4, y4)
        #------------------------
        if agarratuerca==False:
            tuerca(x1,y1)
            
        if agarratornillo==False:
            tornillo(x2, y2)
        if agarratuerca1==False:
            tuerca(x5,y5)
        #-----------------------------------------------------
            
        ###Colisiones
        if x_var >= COL_RIGHT or x_var <= 0:
            mensaje_borde()
            
        if y_var >= COL_BOTTOM or y_var <= 0:
            mensaje_borde()

            
        if contartornillo == contartuerca == contartornillo1 == contartuerca1:
            
            if ((x_var>=410 and x_var<=450) and (y_var>=400 and y_var<=450)):

                gameExit=True
                game_loop2(Puntaje)
                
                                   
        
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
