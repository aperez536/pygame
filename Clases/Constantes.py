import pygame

GAME_NOMBRE = "Space Full of Aliens" #Buscar nombre copado?!
GAME_FPS = 30

########DISPLAY SETTINGS########
DISPLAY_ANCHO = 500
DISPLAY_ALTURA = 500
ALIEN_ANCHO = 50
ALIEN_ALTO = 50

########COLISSION DISPLAY########

COL_TOP = 150
COL_BOTTOM = DISPLAY_ALTURA - ALIEN_ALTO
COL_LEFT = 0
COL_RIGHT = DISPLAY_ANCHO - ALIEN_ANCHO

#########COLORES#############

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
BLANCOVIEJO = (205, 192, 176)
CELESTE = (0, 99, 255)
AMARILLO = (255, 255, 0)
GRIS = (60, 60, 60)

#######IMAGENES########
fondo = pygame.image.load('Imagenes/fondo.png')
fondo = pygame.transform.scale(fondo, (DISPLAY_ANCHO, DISPLAY_ALTURA))

imagen1 = pygame.image.load('aliensinfondo.png')
imagen1 = pygame.transform.scale(imagen1, (50, 50))
imagen2 = pygame.image.load("Imagenes/alien2.png")
imagen2 = pygame.transform.scale(imagen2, (50, 50))
imagen3 = pygame.image.load("Imagenes/alien3.png")
imagen3 = pygame.transform.scale(imagen3, (50, 50))
imagen4 = pygame.image.load("Imagenes/alien4.png")
imagen4 = pygame.transform.scale(imagen4, (50, 50))
imagen5 = pygame.image.load("Imagenes/alien5.png")
imagen5 = pygame.transform.scale(imagen5, (50, 50))
imagen6 = pygame.image.load("Imagenes/tuerca.png")
imagen6 = pygame.transform.scale(imagen6, (25, 25))
imagen7 = pygame.image.load("Imagenes/tornillo.png")
imagen7 = pygame.transform.scale(imagen7, (25, 25))
imagen8 = pygame.image.load("Imagenes/nave.png")
imagen8 = pygame.transform.scale(imagen8, (35, 35))
imagenes = [imagen1, imagen2, imagen3, imagen4, imagen5]
meteoro = pygame.image.load("Imagenes/meteoro.png")
meteoro = pygame.transform.scale(meteoro, (60, 60))
########################imagen trono y variables de posicion
tronco = pygame.image.load("Imagenes/tronco2.png")


ImagenActual = 0
imagenes[ImagenActual]



#background = pygame.transform.scale(background,(500,800)) #Ajuste de la imagen al tamao del display
