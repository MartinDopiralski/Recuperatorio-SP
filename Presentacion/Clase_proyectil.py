import pygame

class Proyectil():
    def __init__(self, x, y, direccion):
        self.image = pygame.Surface((10, 10)) 
        self.image.fill('Black') 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direccion = direccion
        self.velocidad = 5  

    def update(self):
        if self.direccion == "derecha":
            self.rect.x += self.velocidad * -1
        elif self.direccion == "izquierda":
            self.rect.x += self.velocidad * 1

        #if self.rect.right < 0 or self.rect.left > self.pantalla_principal.get_width():
        #    self.kill()