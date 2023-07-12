import pygame
from configuraciones import *

class Plataforma:
    def __init__(self, path, tamaño: tuple, posicion_inicial: tuple):
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,(tamaño[0], tamaño[1]))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados_rectangulo = obtener_rectangulos(self.rectangulo)
        
   
        
