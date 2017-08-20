import pygame
import time
import random

pygame.init()

########DISPLAY SETTINGS########
display_ancho = 500
display_altura = 500

#########COLORES#############

negro= (0,0,0)
white=(255,255,255)
BlancoViejo = (205,192,176)

#######IMAGENES########
#imagen1= pygame.image.load()
#imagen1= pygame.transform.scale(imagen1, (50,50))
#background =  pygame.image.load()
#background= pygame.transform.scale(background,(500,800)) #Ajuste de la imagen al tamaño del display

##########AJUSTES VARIOS############

display= pygame.display.set_mode((display_ancho, display_altura)) #Tamaño del display
pygame.display.set_caption("Space full of aliens") #Nombre del juego
reloj=pygame.time.Clock()

pygame.quit()
