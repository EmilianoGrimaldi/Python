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



reloj = pygame.time.Clock()



while True:
    
    reloj.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #teclado
        # if evento.type == pygame.KEYDOWN:
        #     match evento.key:
        #         case pygame.K_a:
        #             print("izq")
        #         case pygame.K_s:
        #             print("abajo")
        #         case pygame.K_d:
        #             print("der")
        #         case pygame.K_w:
        #             print("arriba")
           
            # if evento.key == pygame.K_a:
            #     print("a")
        #mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
    
            if evento.button == 1:
                print("click izq", evento.pos)
            if evento.button == 2:
                print("ruedita")
            if evento.button == 3:
                print("click der")
            if evento.button == 4:
                print("rued arriba")
            if evento.button == 5:
                print("rue abajo")
            if evento.button == 6:
                print("boton lat ab")
            if evento.button == 7:
                print("boton lat ar")


        #mantengo presionado se mueve sino no
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_a]:
        #     print("izquierda")
        
    resolucion.fill(BLANCO)
    
    pygame.display.flip()