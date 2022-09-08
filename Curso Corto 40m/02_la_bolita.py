import sys    # para usar exit()
import pygame

ANCHO = 640 # Ancho de la pantalla.
ALTO = 480  # Alto de la pantalla.

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('imagenes/bolita.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla.
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2

# Inicializando pantalla.
pantalla = pygame.display.set_mode((ANCHO, ALTO))
# Configurar título de pantalla.
pygame.display.set_caption('Juego de ladrillos')

bolita = Bolita()

while True:
    # Revisar todos los eventos.
    for evento in pygame.event.get():
        # Si se presiona la tachita de la barra de título,
        if evento.type == pygame.QUIT:
            # cerrar el videojuego.
            sys.exit()

    # Dibujar bolita en pantalla.
    pantalla.blit(bolita.image, bolita.rect)
    # Actualizar los elementos en pantalla.
    pygame.display.flip()
