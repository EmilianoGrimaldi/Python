import pygame, sys

ANCHO = 800
ALTURA = 600
CENTRO = ANCHO//2, ALTURA//2
TITULO = "Primer aplicacion"
BLANCO = (255,255,255)
ROJO = (255, 0, 0)
VELOCIDAD = 5
FPS = 60

pygame.init()


resolucion = pygame.display.set_mode((ANCHO,ALTURA))
pygame.display.set_caption(TITULO)

#FONDO
fondo = pygame.image.load("PyGame_Repaso\src\img\galaxia.jpg").convert() #JPG
fondo = pygame.transform.scale(fondo,(ANCHO,ALTURA))

reloj = pygame.time.Clock()
#arriba y abajo
sup_mundo = pygame.image.load("PyGame_Repaso\src\img\mundo.png").convert_alpha() #PNG para que mantenga la transparencia
sup_mundo = pygame.transform.scale(sup_mundo,(100,100) )
rect_mundo = sup_mundo.get_rect()
rect_mundo.center = CENTRO
# izq a der
sup_mundo_x = pygame.image.load("PyGame_Repaso\src\img\mundo.png").convert_alpha() #PNG para que mantenga la transparencia
sup_mundo_x = pygame.transform.scale(sup_mundo,(100,100) )
rect_mundo_x = sup_mundo.get_rect()
rect_mundo_x.center = CENTRO
#fuente
# fuente = pygame.font.get_fonts()
# print(fuente)
fuente = pygame.font.SysFont("superfunky", 50)
texto = fuente.render("PUMM!!!", True, ROJO)
#------------
#EXPLOSION
sup_explosion = pygame.image.load("PyGame_Repaso\src\img\explosion.png").convert_alpha() #PNG para que mantenga la transparencia
sup_explosion = pygame.transform.scale(sup_explosion,(rect_mundo.width, rect_mundo.height))
#SOUNDS
sonido = pygame.mixer.Sound("PyGame_Repaso\src\sounds\\fatality.mp3")

#MOV IMG
caida = False
x_mundo = False

while True:
    
    reloj.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    resolucion.blit(fondo, (0,0))
    
    resolucion.blit(sup_mundo, rect_mundo)
    
    if not caida:
        if rect_mundo.bottom <= ALTURA:
            rect_mundo.y += VELOCIDAD
        else:
            caida = True
    else:
        if rect_mundo.top >= 0:
            rect_mundo.y -= VELOCIDAD
        else:
            caida = False
            
    resolucion.blit(sup_mundo_x, rect_mundo_x)
    if not x_mundo:
        if rect_mundo_x.right <= ANCHO:
            rect_mundo_x.x += VELOCIDAD
        else:
            x_mundo = True
    else:
        if rect_mundo_x.left >= 0:
            rect_mundo_x.x -= VELOCIDAD
        else:
            x_mundo = False
    #CHOCARON
    if rect_mundo.colliderect(rect_mundo_x):
        resolucion.blit(texto, (0, 0))
        resolucion.blit(sup_explosion, rect_mundo)
        resolucion.blit(sup_explosion, rect_mundo_x)
        sonido.play()
        
    #---------------------------------------
    pygame.display.flip()