import pygame
from Clases.Config import Config
from Clases.Constantes import *

class Alien():

    def __init__(self, name):
        self.gameDisplay = pygame.display.set_mode((DISPLAY_ANCHO, DISPLAY_ALTURA))
        self.name = name
        self.hp = 100
        self.inventary = [] #Para saber que herramientas tiene (?

    # Funcion que mueve al Alien
    def move(self, x, y, contador):
        self.gameDisplay.blit(imagenes[contador], (x, y))

    # Funcion que le saca vida al Alien
    def getHit(self, damage):
        self.hp = self.hp - damage
        return #ver si return es necesario

    # Funcion que cura la vida al Alien
    def getHeal(self, heal):
        self.hp = self.hp + heal

    # Funcion cuando se queda sin vida
    def die(self):
        pass #Pass hace que quede vacia -> hay que mostrar el cartel de Game Over y Reintentar

    # Funcion que recolecta Herramientas
    def agregarItem(self, itemID):
        self.inventary.append(itemID)
        return #ver si return es necesario

    # Funcion que elimina Herramientas (Cuando las Usa)
        self.inventary.remove(itemID)
        #Ordenar el Inventario?
        return #ver si return es necesario
