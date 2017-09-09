import pygame
from Clases.Constantes import *

#Clase de Configuracion

class Config():

    def __init__(self):
        pygame.display.set_caption(GAME_NOMBRE)
        self.gameDisplay = None
        self.clock = pygame.time.Clock()        
        pass

    def updateFPS(self):
        pygame.display.update()
        self.clock.tick(GAME_FPS)
