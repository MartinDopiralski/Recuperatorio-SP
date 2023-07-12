import pygame,sys
from pygame.locals import *
from nivel_uno import *
from modo import *

ANCHO, ALTO = 1800, 900
TAMAÑO_PANTALLA = (ANCHO, ALTO)
FPS = 30
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Presentacion/Recursos/audioJuego.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

nombre_juego = "Pac-Man: Rescate en Ooo"
pygame.display.set_caption(nombre_juego)

logo = pygame.image.load("Presentacion/Recursos/icono_juego.png")
pygame.display.set_icon(logo)

nivel_uno = NivelUno(PANTALLA)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    fondo = pygame.image.load("Presentacion/Recursos/PantallaDeInicio.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))
    PANTALLA.blit(fondo, (0,0))
    
    nivel_uno.actualizar(eventos)
  
    pygame.display.update()