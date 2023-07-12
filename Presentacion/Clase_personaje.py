import pygame
from configuraciones import *
from Clase_plataforma import *
from Clase_proyectil import *

class Personaje:
    
    def __init__(self,tamaño, animaciones, posicion_inicial, velocidad, potencia_salto):
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1] 
        #ANIMACIONES
        self.contador_pasos = 0
        self.estado = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones['camina_izquierda'][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.apuntado = "izquierda"
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -potencia_salto
        self.limite_velocidad_caida = potencia_salto
        self.estado_salto = False
        #SISTEMA COMBATE
        self.proyectil = Proyectil(self.lados["main"].center[0], self.lados["main"].center[1], self.apuntado)
        self.vidas = 3
        self.atacar = False
        

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto))


    def animar(self, pantalla, que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self,velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def actualizar(self, pantalla, plataformas):
        if self.atacar:
            self.disparar(pantalla)

        match self.estado:
            case "derecha":
                if not self.estado_salto:
                    self.apuntado = "derecha"
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.estado_salto:
                    self.apuntado = "izquierda"
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad *-1)
            case "quieto":
                if not self.estado_salto:
                    if self.apuntado == "izquierda":
                        self.animar(pantalla, "quieto_izquierda")
                    else:
                        self.animar(pantalla, "quieto_derecha")
            case "salta":
                if not self.estado_salto:
                    self.estado_salto = True
                    self.desplazamiento_y = self.potencia_salto

            
        self.aplicar_gravedad(pantalla,plataformas)

    def aplicar_gravedad(self, pantalla, plataformas):
        if self.estado_salto:         
            self.animar(pantalla, f"salta_{self.apuntado}")
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            

        for piso in plataformas:
            if self.lados["bottom"].colliderect(piso.lados_rectangulo["top"]):
                self.desplazamiento_y = 0
                self.estado_salto = False
                self.lados["main"].bottom = piso.lados_rectangulo["main"].top
                break
            else:
                self.estado_salto = True

    def disparar(self,pantalla):
        pantalla.blit(self.proyectil.image, self.proyectil.rect)
        self.proyectil.update()
        self.atacar = False