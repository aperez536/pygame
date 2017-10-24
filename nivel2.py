import pygame
import time
import random
from Clases.Config import Config
from Clases.Mensaje import Mensaje
from Clases.Constantes import *
from Aliens import *



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
    time.sleep(2)
    

def mensaje_borde():
    mensaje1('Choque con el borde!')


def termina(vida):
    mensaje1('el juego se acabo')
    if vida == 0:
        game_Exit=True;
        return game_Exit

def mensaje_colision():
    colision1('Choque!')

def colision1(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = texto(text, largeText)
    TextRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))
    config.gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)

def meteorito(trnc,x,y):
     config.gameDisplay.blit(trnc, (x,y))


def game_loop2():

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

    #--------------
    
    choque1=False;
    choque2=False;
    choque3=False;
    choque4=False;
    choque5=False;
    choque6=False;
    
    vel = 10 # lo uso para el dezplazamiento de la nave
    gameExit = False

    #pos de la nave
    x_var = 200
    y_var = 400
    #vida que tendra la nave
    vida=3
    #sonidos de personaje de movimiento y agarre
    sonidomover=pygame.mixer.Sound("Sonidos/mover.mp3")
    pygame.mixer.music.load("Sonidos/win.mp3")
    
    #posiciones del meteoro
    meteoro1x= random.randrange(0,400)
    meteoro1y=-150
    meteoro2x=random.randrange(0,400)
    meteoro2y=-10
    meteoro3x=random.randrange(0,400)
    meteoro3y=-100
    meteoro4x=random.randrange(0,400)
    meteoro4y=0
    meteoro5x=random.randrange(0,100)
    meteoro5y=-50
    meteoro6x=random.randrange(0,400)
    meteoro6y=-30
    
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
        if choque1==False:
            if meteoro1y==500:
                meteoro1y=0
                meteoro1x=random.randrange(0,400)#devuelve una posicion aleatoria en el rango asignado
        if choque2==False:
            if meteoro2y==500:
                meteoro2y=0
                meteoro2x=random.randrange(0,400)
        if choque3==False:
            if meteoro3y==500:
                meteoro3y=0
                meteoro3x=random.randrange(0,400)   
            
        if choque4==False:
            if meteoro4y==600:
                meteoro4y=0
                meteoro4x=random.randrange(0,400)   
        
        if choque5==False:
            if meteoro5y==500:
                meteoro5y=0
                meteoro5x=random.randrange(0,400)   
           
        if choque6==False:   
            if meteoro6y==850:
                meteoro6y=0
                meteoro6x=random.randrange(0,400)   

        #colision
        auxposx=x_var-50
        auxposy=y_var
        i=1
        col=False

            
                # colision del meteoro
        for i in range (1,70):
                auxposx=auxposx+1
                if  meteoro1x==auxposx and meteoro1y==auxposy:
                    choque1=True
                    col=True

                if  meteoro2x==auxposx and meteoro2y==auxposy:
                    choque2=True
                    col=True

                if  meteoro3x==auxposx and meteoro3y==auxposy:
                    choque3=True
                    col=True
                    
                if  meteoro4x==auxposx and meteoro4y==auxposy:
                    choque4=True
                    col=True
                if  meteoro5x==auxposx and meteoro5y==auxposy:
                    choque5=True
                    col=True
                if  meteoro6x==auxposx and meteoro6y==auxposy:
                    choque6=True
                    col=True
                
        if col==True:
            vida=vida-1
            if vida>=1 and vida <=3:
            #termina el juego
                mensaje_colision()
            else:
                
                #col = False        
                gameExit=termina(vida)
                
                
        
        #vuelven a caer el meteorito
            choque1=False
            choque2=False
            choque3=False
            choque4=False
            choque5=False
            choque6=False
        ##
        # si el perosonaje principal esta en esa pocision , va a agarrar la tuerca.
        config.gameDisplay.fill(NEGRO)
        config.gameDisplay.blit(fondo, (0, 0))
        # MUESTRA LA VIDA DEL PERSONAJE
        nuevoMensaje.Print("vidae:" + str(vida))
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
        if x_var <= 0:
            vida-=1
            if vida>=1 and vida <=3:
            #termina el juego
                mensaje_borde()
            else:
                
                #col = False        
                gameExit=termina(vida)
                
            x_var=10
            if vida== 0:
                gameExit=termina(vida)
          
            
        if x_var >= COL_RIGHT+15:
            vida-=1
            if vida>=1 and vida <=3:
            #termina el juego
                mensaje_borde()
            else:
                
                #col = False        
                gameExit=termina(vida)
                
            x_var=450
            if vida==0:
                gameExit=termina(vida)

        
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
    game_loop2()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()