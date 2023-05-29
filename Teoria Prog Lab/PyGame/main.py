import pygame, sys
#configuracion

ancho = 800
alto = 600
pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Primer aplicacion")
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CUSTOM = (157, 123, 236)

pantalla.fill(CUSTOM)

while True:
    
    #configuramos el tamaño de la pantalla
    #manejar eventos -> si se presiono un boton o se dio una instruccion
    #dibujar pantalla
    #actualizar la pantalla (buffer)
    #fin de la aplicacion
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    