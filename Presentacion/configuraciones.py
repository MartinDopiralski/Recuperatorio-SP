import pygame
def reescalar_imagen(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],tamaño)


def girar_imagenes(lista_original_, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original_:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))

    return lista_girada

def obtener_rectangulos(principal) -> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

quieto_izquierda = [pygame.image.load("Presentacion/Recursos/Quieto/0.png")]
quieto_derecha = girar_imagenes(quieto_izquierda, True, False)


camina_izquierda = [pygame.image.load("Presentacion/Recursos/Camina/7.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/9.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/10.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/11.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/12.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/13.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/14.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/15.png"),
                    pygame.image.load("Presentacion/Recursos/Camina/16.png")]

camina_derecha = girar_imagenes(camina_izquierda, True, False)

salta_izquierda = [pygame.image.load("Presentacion/Recursos/Salta/19.png")]
salta_derecha = girar_imagenes(salta_izquierda, True, False)