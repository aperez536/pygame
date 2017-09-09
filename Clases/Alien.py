import pygame
from Clases.Config import Config
from Clases.Constantes import *

class Alien():

    def __init__(self, gameDisplay, name):
        self.gameDisplay = gameDisplay
        self.name = name
        self.hp = 100
        self.inventary = [] #Para saber que herramientas tiene (?

    def move(self, x, y, contador):
        self.gameDisplay.blit(imagenes[contador], (x, y))
