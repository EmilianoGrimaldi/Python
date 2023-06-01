import pygame, sys
#configuracion

ANCHO = 800
ALTO = 600
CENTRO = ANCHO // 2, ALTO // 2
FPS = 30


clock = pygame.time.Clock()
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Primer aplicacion")
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CUSTOM = (157, 123, 236)



rectangulo = pygame.rect.Rect(100, 50, 120, 70)

rect_1 = pygame.rect.Rect(100, 50, 120, 70)
rect_1.center = CENTRO

superficie_1 = pygame.surface.Surface((100,70))
superficie_1.fill(ROJO)
rect_sup_1 = superficie_1.get_rect()
rect_sup_1.center = CENTRO

superficie_2 = pygame.surface.Surface((70,100))
superficie_2.fill(AZUL)
rect_sup_2 = superficie_2.get_rect()
rect_sup_2.center = CENTRO

while True:
    clock.tick(FPS)
    #configuramos el tamaño de la pantalla
    #manejar eventos -> si se presiono un boton o se dio una instruccion
    #dibujar pantalla
    #actualizar la pantalla (buffer)
    #fin de la aplicacion
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pantalla.fill(CUSTOM)
      
    # pygame.draw.rect(pantalla, VERDE, rectangulo)
    # rectangulo_dos = pygame.draw.rect(pantalla, AZUL, (200, 200, 120, 70))
    # pygame.draw.circle(pantalla, ROJO, (300, 250), 50, 2)
    # pygame.draw.line(pantalla, NEGRO, CENTRO, (0,ALTO))
    # pygame.draw.rect(pantalla, AMARILLO, (50, 70, 120, 120), 1)
    # pygame.draw.ellipse(pantalla, CYAN, (200,300,120,70), 3)
    
    # pygame.draw.rect(pantalla, AMARILLO, rect_1, 1)
    
        
    pantalla.blit(superficie_1, rect_sup_1)
    
    pygame.draw.line(pantalla, NEGRO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))
    pygame.draw.line(pantalla, NEGRO, (0, ALTO // 2, 0), (ANCHO, ALTO // 2))
    pygame.display.flip()
    