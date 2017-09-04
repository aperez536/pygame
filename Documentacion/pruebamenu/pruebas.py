import pygame
import time
import random
from logging import addLevelName
from test.pickletester import DATA0_DIS
from pygame.locals import *

pygame.init()

########DISPLAY SETTINGS########
display_ancho = 900
display_altura = 500
imagen_ancho= 50
imagen_alto= 50

#########COLORES#############

negro= (0,0,0)
blanco=(255,255,255)
BlancoViejo = (205,192,176)

#######IMAGENES########
imagen1= pygame.image.load('aliensinfondo.png')
imagen1= pygame.transform.scale(imagen1, (60,60))
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



###########################

class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500* paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 150
        self.x += (destino_x - self.x) / 10.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf', 50)
        x = 105
        y = 105
        paridad = 1

        self.cursor = Cursor(x - 80, y, 80) #CURSOR MOVIMIENTO

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 80 #DISTANCIA ENTRE PALABRAS
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                #función opción.
                self.opciones[self.seleccionado].activar()

        #opciones permitidas del cursor
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
     #IMPRIME OPCIONES DEL MENU

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

def comenzar_nuevo_juego():
    pygame.display.update()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.update()
    x=0
    y=0
    vel=10
    gameExit=False
    x_var=200
    y_var=200
      
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
            
      
    clock.tick(30)


def salir_del_programa():
   # import sys
    #sys.exit(0)
   for event in pygame.event.get():
    pygame.quit()
    quit()


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((500, 500))
    fondo = pygame.image.load("fondo.png").convert()
    fondo = pygame.transform.scale(fondo, (500, 500))
    
    menu = Menu(opciones)



######################


    while not salir:
        for event in pygame.event.get():

            if event.type == QUIT:
                salir = True
                
        screen.blit(fondo, (0,0)) 
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip ()
        pygame.time.delay(10)

"""        
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
"""



    

#game_loop()
pygame.quit()
quit()
