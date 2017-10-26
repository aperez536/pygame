import pygame

GAME_NOMBRE = "Space Full of Aliens" 
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
fondo2 = pygame.image.load('Imagenes/fondo_posible.png')
fondo2 = pygame.transform.scale(fondo2, (DISPLAY_ANCHO, DISPLAY_ALTURA))
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
imagenes = [imagen1, imagen2, imagen3, imagen4, imagen5]

imagen6 = pygame.image.load("Imagenes/cog.png")
imagen6 = pygame.transform.scale(imagen6, (24, 24))
imagen7 = pygame.image.load("Imagenes/wrench.png")
imagen7 = pygame.transform.scale(imagen7, (24, 24))
imagen8 = pygame.image.load("Imagenes/nave.png")
imagen8 = pygame.transform.scale(imagen8, (35, 35))
imagen9= pygame.image.load("Imagenes/Creadores.png")
meteoro = pygame.image.load("Imagenes/meteoro.png")
imagen9 = pygame.transform.scale(imagen9, (250, 250))
meteoro = pygame.transform.scale(meteoro, (60, 60))
tronco = pygame.image.load("Imagenes/tronco2.png")
tronco = pygame.transform.scale(tronco, (66, 66))


ImagenActual = 0
imagenes[ImagenActual]



#background = pygame.transform.scale(background,(500,800)) #Ajuste de la imagen al tamao del display
