import pygame, sys

ANCHO = 600
ALTURA = 300
TITULO = "Primer aplicacion"
COLOR = (255,0,0)


pygame.init()
# print(pygame.get_init())

resolucion = pygame.display.set_mode((ANCHO,ALTURA))
pygame.display.set_caption(TITULO)
# in_game = True

while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # in_game = False
    resolucion.fill(COLOR)
    
    pygame.display.flip()
    