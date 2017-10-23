import os  #ver si en todas las pc esta
import pygame
import time
import random
import sys

from logging import addLevelName
from test.pickletester import DATA0_DIS
from pygame.locals import *
from Clases.Mensaje import *
from Clases.Constantes import *
from Aliens import *

pygame.init()

NEGRO = (0,0,0)
pygame.mixer.music.load("Sonidos\\bg.ogg")
reloj= pygame.time.Clock()
pygame.mixer.music.play(-1, 0.0)

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
        destino_x = 100 # ubicacion palabras
        self.x += (destino_x - self.x) / 8.0 #rapidez de movimiento
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
        self.image = pygame.image.load('Imagenes\\menu\\cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 8.0 #rapidez movimiento cursor
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('Font\\Oxin.ttf', 50)
        x = 150 #Ubicacion palabras
        y = 150 #same
        paridad = 1

        self.cursor = Cursor(x - 95, y, 95) #CURSOR MOVIMIENTO

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 70 #DISTANCIA ENTRE PALABRAS
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
                #funcion opcion 
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
    game_loop() # Funciona pero no es como se debe  

def salir_del_programa():
    pygame.quit()
    quit()

def los_creditos():
    gameExit = False
    salir=False
    while not gameExit:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #pygame.KEYDOWN (Cuando se Aprienta) (Principio) Depende que se necesite
            #pygame.KEYUP (Cuando se suelta la tecla) (Final) En este caso KEYUP cuando soltas que mande al menu
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    #No se como llamar a que reinicie el programa
                    os.execv(sys.executable, ['python'] + sys.argv)
                    # ^ Funciona pero no es como se debe (Reinicia el programa en vez de ir al menu anterior)
                    
        #screen = pygame.display.set_mode((500,500))
        #screen.fill(NEGRO) --- BORRAR ! SIEMPRE PONE LA PANTALLA NEGRA SINO
        pygame.display.update()
        creditos = Mensaje()
        creditos.Color = BLANCO
        creditos.Posicion = "middle"
        config.gameDisplay.blit(imagen9, (100,100))
  


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("juego nuevo", comenzar_nuevo_juego),
        ("salir", salir_del_programa),
        ("creditos", los_creditos)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((500, 500))
    fondo = pygame.image.load("Imagenes\\menu\\fondo.png").convert()
    fondo = pygame.transform.scale(fondo, (500, 500))
    
    menu = Menu(opciones)



######################


    while not salir:
        
        #pygame.mixer.music.play()
        for event in pygame.event.get():

            if event.type == QUIT:
                salir = True
                
        screen.blit(fondo, (0,0)) 
        menu.actualizar()
        menu.imprimir(screen)
        reloj.tick(20)
        pygame.display.update()

        pygame.display.flip ()
        pygame.time.delay(10)
    
pygame.quit()
quit()
