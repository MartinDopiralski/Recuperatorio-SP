import pygame,sys
from pygame.locals import *
from Clase_nivel import *
from Clase_personaje import *
from Clase_plataforma import *
from configuraciones import *

class NivelUno(Nivel):
    def __init__(slef, pantalla: pygame.Surface):
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load("Presentacion/Recursos/FondoJuego.png")
        fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

        posicion_inicial = (150, 640)
        tamaño = (50,65)

        animaciones = {}
        animaciones["quieto_izquierda"] = quieto_izquierda
        animaciones["quieto_derecha"] = quieto_derecha
        animaciones["salta_izquierda"] = salta_izquierda
        animaciones["salta_derecha"] = salta_derecha
        animaciones["camina_derecha"] = camina_derecha
        animaciones["camina_izquierda"] = camina_izquierda

        #Plataformas 
        piso = Plataforma("Presentacion/Recursos/Plataformas/0.png",(2000,150), (-100, 800))
        plataforma_uno = Plataforma("Presentacion/Recursos/Plataformas/0.png",(200, 20), (10, 700))
        plataforma_dos = Plataforma("Presentacion/Recursos/Plataformas/0.png",(200, 20), (340, 580))
        plataforma_tres = Plataforma("Presentacion/Recursos/Plataformas/0.png",(200, 20), (670, 460))
        plataforma_cuatro = Plataforma("Presentacion/Recursos/Plataformas/0.png",(200, 20), (1000, 460))
        lista_plataformas = [piso, plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro]

        mi_personaje = Personaje(tamaño, animaciones, posicion_inicial, 10, 15)

        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo)