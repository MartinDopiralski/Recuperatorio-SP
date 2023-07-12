import pygame
from modo import *
from Clase_personaje import *
from Clase_plataforma import *

class Nivel:
    def __init__(self, pantalla, personaje_principal: Personaje, lista_plataformas: list[Plataforma], imagen_fondo):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.fondo = imagen_fondo


    def actualizar(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN: 
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        
        self.leer_inputs()
        self.actualizar_pantalla()
        self.dibujar_rectangulos()

    def actualizar_pantalla(self):
        self._slave.blit(self.fondo, (0,0))
        for piso in self.plataformas:
           self._slave.blit(piso.imagen, piso.rectangulo)

        self.jugador.actualizar(self._slave, self.plataformas)

    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.jugador.atacar = True
        
        if keys[pygame.K_RIGHT]:
            self.jugador.estado = "derecha"
        elif keys[pygame.K_LEFT]:
            self.jugador.estado = "izquierda"
        elif keys[pygame.K_UP]:
            self.jugador.estado = "salta"
        elif keys[pygame.K_LSHIFT]:
            self.jugador.estado = "disparar"
        else:
            self.jugador.estado = "quieto"
        
         


    def dibujar_rectangulos(self):
        if get_modo():
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Blue", self.jugador.lados[lado], 2)

            for plataforma in self.plataformas:
                for lado in plataforma.lados_rectangulo:
                    pygame.draw.rect(self._slave, "Red", plataforma.lados_rectangulo[lado], 2)
            
            
