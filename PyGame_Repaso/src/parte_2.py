import pygame, sys

ANCHO = 800
ALTURA = 600
CENTRO = ANCHO//2, ALTURA//2
TITULO = "Primer aplicacion"
COLOR = (255,255,255)
COLOR_LINE = (0,0,0)
AMARILLO = (255,255,0)
VERDE = (128, 255, 0)
NARANJA = (255, 128, 0)
CYAN = (0,255,255)
AZUL = (0, 0, 255)
CELESTE = (0,128,255)
VELOCIDAD = 5
FPS = 60

pygame.init()
# print(pygame.get_init())

resolucion = pygame.display.set_mode((ANCHO,ALTURA))
pygame.display.set_caption(TITULO)

reloj = pygame.time.Clock()
# cuadrado 1
cyan = pygame.surface.Surface((50,50))
cyan.fill(CYAN)
rect_cyan = cyan.get_rect()
rect_cyan.center = CENTRO
# cuadrado 2
sup_cuadrado = pygame.surface.Surface((50,50))
sup_cuadrado.fill(VERDE)
rect_verde = sup_cuadrado.get_rect()
rect_verde.center = CENTRO 
#cuadrado 3
cuadrado_3 = pygame.surface.Surface((50,50))
cuadrado_3.fill(NARANJA)
cuadrado_naranja = cuadrado_3.get_rect()
cuadrado_naranja.topleft = 0,0
#cuadrado 4
cuadrado_4 = pygame.surface.Surface((50, 38))
cuadrado_4.fill(AZUL)
cuadrado_azul = cuadrado_4.get_rect()
cuadrado_azul.topleft = 0,0
#cuadrado 5
cuadrado_5 = pygame.surface.Surface((50, 38))
cuadrado_5.fill(CELESTE)
cuadrado_celeste = cuadrado_5.get_rect()
cuadrado_celeste.bottomleft = 0,ALTURA

# in_game = True
y_rect_cyan = False
x_rect_verde = False
x_rect_naranja = False
y_rect_naranja = False
diagonal = False
diagonal_2 = False

while True:
    
    reloj.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # in_game = False
    
    resolucion.fill(COLOR)
    pygame.draw.line(resolucion,COLOR_LINE, (ANCHO // 2, 0), (ANCHO // 2, ALTURA))
    pygame.draw.line(resolucion,COLOR_LINE, (0, ALTURA // 2), (ANCHO, ALTURA // 2))
    pygame.draw.line(resolucion,COLOR_LINE, (0, 0), (ANCHO, ALTURA))
    pygame.draw.line(resolucion,COLOR_LINE, (0, ALTURA), (ANCHO, 0))

    resolucion.blit(cyan, rect_cyan)
    if not y_rect_cyan:
        if rect_cyan.bottom <= ALTURA:
            rect_cyan.y += VELOCIDAD
        else:
            y_rect_cyan = True
    else:
        if rect_cyan.top >= 0:
            rect_cyan.y -= VELOCIDAD
        else:
            y_rect_cyan = False

    resolucion.blit(sup_cuadrado, rect_verde)
    if not x_rect_verde:
        if rect_verde.right <= ANCHO:
            rect_verde.x += VELOCIDAD
        else:
            x_rect_verde = True
    else:
        if rect_verde.left >= 0:
            rect_verde.x -= VELOCIDAD
        else:
            x_rect_verde = False

    resolucion.blit(cuadrado_3, cuadrado_naranja)
    if not y_rect_naranja:
        if cuadrado_naranja.bottom <= ALTURA:
            cuadrado_naranja.y += VELOCIDAD
        else:
            y_rect_naranja = True

    if y_rect_naranja and not x_rect_naranja:
        if cuadrado_naranja.right <= ANCHO:
            cuadrado_naranja.x += VELOCIDAD
        else:
            x_rect_naranja = True
    
    if x_rect_naranja:
        if cuadrado_naranja.top >= 0:
            cuadrado_naranja.y -= VELOCIDAD
        else:
            y_rect_naranja = False
    
    if not y_rect_naranja and x_rect_naranja:
        if cuadrado_naranja.left >= 0:
            cuadrado_naranja.x -= VELOCIDAD
        else:
            x_rect_naranja = False
    
    resolucion.blit(cuadrado_4, cuadrado_azul)
    if not diagonal:
        if cuadrado_azul.bottomright <= (ANCHO, ALTURA):
            cuadrado_azul.x += 4
            cuadrado_azul.y += 3
        else:
            diagonal = True
    
    if diagonal:
        if cuadrado_azul.topleft >= (0,0):
            cuadrado_azul.x -= 4
            cuadrado_azul.y -= 3
        else:
            diagonal = False

    resolucion.blit(cuadrado_5, cuadrado_celeste)
    if not diagonal_2:
        if cuadrado_celeste.topright <= (ANCHO,0):
            cuadrado_celeste.x += 4
            cuadrado_celeste.y -= 3
        else:
            diagonal_2 = True
    
    if diagonal_2:
        if cuadrado_celeste.bottomleft >= (0,0):
            cuadrado_celeste.x -= 4
            cuadrado_celeste.y += 3
        else:
            diagonal_2 = False

    # pygame.draw.ellipse(resolucion, COLOR_RECT, (200,120,120,70), 5)
    # pygame.draw.polygon(resolucion, AMARILLO, [(20,20),(200,75),(170, 300)], 4)
    pygame.display.flip()