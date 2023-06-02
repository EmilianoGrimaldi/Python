import pygame, sys

ANCHO = 1280
ALTURA = 720
TITULO = "Primer aplicacion"
COLOR = (255,0,0)
COLOR_LINE = (0,0,0)
AMARILLO = (255,255,0)
pygame.init()
# print(pygame.get_init())

resolucion = pygame.display.set_mode((ANCHO,ALTURA))
pygame.display.set_caption(TITULO)
rectangulo  = pygame.rect.Rect(ANCHO//2, ALTURA//2, 120, 70)

# in_game = True

while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # in_game = False
    resolucion.fill(COLOR)
    pygame.draw.line(resolucion,COLOR_LINE, (ANCHO // 2, 0), (ANCHO // 2, ALTURA))
    pygame.draw.line(resolucion,COLOR_LINE, (0, ALTURA // 2), (ANCHO, ALTURA // 2))
    # pygame.draw.ellipse(resolucion, COLOR_RECT, (200,120,120,70), 5)
    # pygame.draw.polygon(resolucion, AMARILLO, [(20,20),(200,75),(170, 300)], 4)
    pygame.display.flip()