import sys    # para usar exit()
import pygame

ANCHO = 640 # Ancho de la pantalla.
ALTO = 480  # Alto de la pantalla.

# Inicializando pantalla.
pantalla = pygame.display.set_mode((ANCHO, ALTO))
# Configurar título de pantalla.
pygame.display.set_caption('Juego de ladrillos')

while True:
    # Revisar todos los eventos.
    for evento in pygame.event.get():
        # Si se presiona la tachita de la barra de título,
        if evento.type == pygame.QUIT:
            # cerrar el videojuego.
            sys.exit()

    # Actualizar los elementos en pantalla.
    pygame.display.flip()
