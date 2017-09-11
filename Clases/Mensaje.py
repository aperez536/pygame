# Clase que Muestra Los Mensajes en la Pantalla
# Como se Usa (Pseudo)
# Para Iniciarlizarlo
# --------------------------
# Mensaje = Nuevo Mensaje()
# Mensaje.Color = "255,255,255"
# Mensaje.Posicion = "center" o "top-left" o "top-right" "bottom-left" "bottom-right"
# Mensaje.Tamano = 20
# Mensaje.Fuente = "freesansbold.ttf"
# ^ Todo es Default no es necesario usar esa configuracion salvo que quiera cambiarse
# --------------------------
# Para Usarlo
# --------------------------
# Mensaje.Print("Texto a Imprimir con las configuraciones ya hechas")
# Mensaje.Borrar() para sacarlo de la pantalla cuando quieran
# ^ Facil?

import pygame
import time
from Clases.Constantes import *

class Mensaje():
    def __init__(self):
        #Default
        self.Color = BLANCO #(255,255,255) sera string?
        self.Fuente = "Font\\wowsers.ttf"
        self.Tamano = 20
        self.Posicion = "center"
        self.Padding = 10
        self.GameDisplay = pygame.display.set_mode((DISPLAY_ANCHO, DISPLAY_ALTURA))

    def Print(self, msg):
        #Configuracion
        self.fontConfig = pygame.font.Font(self.Fuente, self.Tamano, bold=False, italic=False)

        #Necesito un TextSurface y TextRectangulo
        msgSurface = self.fontConfig.render(msg, True, self.Color)
        msgSurfaceRect = msgSurface.get_rect()
        msgHeight = msgSurface.get_height()
        msgWidth = msgSurface.get_width()

        #Posicionar el texto segun la configuracion (Hay que hacerlo)
        if self.Posicion == "top-left":
            msgSurfaceRect.center = ((0 + (msgWidth / 2)) + self.Padding, (0 + msgHeight))
        elif self.Posicion == "top-center":
            msgSurfaceRect.center = ((DISPLAY_ANCHO/2), (0 + msgHeight))
        elif self.Posicion == "top-right":
            msgSurfaceRect.center = (DISPLAY_ANCHO, (0 + msgHeight) + self.Padding)
        elif self.Posicion == "bottom-left":
            msgSurfaceRect.center = ((0 + (msgWidth / 2)) + self.Padding, (DISPLAY_ALTURA - msgHeight))
        elif self.Posicion == "bottom-center":
            msgSurfaceRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA - msgHeight))
        elif self.Posicion == "bottom-right":
            msgSurfaceRect.center = (DISPLAY_ANCHO, (DISPLAY_ALTURA - msgHeight) - self.Padding)
        else:
            #Centro - Centro
            msgSurfaceRect.center = ((DISPLAY_ANCHO/2), (DISPLAY_ALTURA/2))

        #Ponerlo en el Display
        self.GameDisplay.blit(msgSurface, msgSurfaceRect)

    def Borrar(self):
        msgSurface = self.fontConfig.render("", True, self.Color)
        msgSurfaceRect = msgSurface.get_rect()
        self.GameDisplay.blit(msgSurface, msgSurfaceRect)
