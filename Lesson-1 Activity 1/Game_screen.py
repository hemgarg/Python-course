import pygame
pygame.init()
running = True
Screenwidth = 500
Screenheight = 500
display_surface = pygame.display.set_mode((Screenwidth,Screenheight))
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False

pygame.quit()