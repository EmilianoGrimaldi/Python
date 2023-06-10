import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir los colores
WHITE = (255, 255, 255)

# Configurar la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moviendo un cuadrado en diagonal")

# Definir las coordenadas y la velocidad del cuadrado
x = 0
y = 0
speed = 1

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el cuadrado en diagonal
    x += speed
    y += speed

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar el cuadrado en la nueva posición
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))

    # Actualizar la pantalla
    pygame.display.update()

    # Establecer la velocidad del bucle
    pygame.time.Clock().tick(60)
