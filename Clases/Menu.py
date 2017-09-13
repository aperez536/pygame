# -*- coding: cp1252 -*-
import pygame
import time
import random
from logging import addLevelName
from test.pickletester import DATA0_DIS
from pygame.locals import *

pygame.init()

pygame.mixer.music.load("Music1.mp3")
reloj= pygame.time.Clock()
#pygame.mixer.music.play(1)


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
        fuente = pygame.font.Font('Oxin.ttf', 50)
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
      

def salir_del_programa():
    import sys
    sys.exit(0)


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("jugar", comenzar_nuevo_juego),
        ("salir", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((500, 500))
    fondo = pygame.image.load("fondo.png").convert()
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
