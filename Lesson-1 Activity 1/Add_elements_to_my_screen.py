import pygame

pygame.init()

#add colours and centres
GOLD = (255,215,0)
CENTREY = 200
CENTREX = 250
WHITE = (220,220,220)

#set screen and font
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("My first game screen")
font = pygame.font.SysFont("timesnewroman", 36)


#Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #FILL the screen white white
    screen.fill(WHITE)
    #Draw the rectangle
    pygame.draw.rect(screen,GOLD,(CENTREX, CENTREY, 200,100))
    #Print the text
    text = font.render("Hello! This is a rectangle", True, (0,0,0))
    screen.blit(text,(CENTREX - 70, CENTREY - 36))
    #Update the screen
    pygame.display.flip()
#Quit Pygame
pygame.quit()
