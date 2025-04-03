import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Add more sprites homework")
exit = False
white = (250,250,250)
x = 50
y = 50



color = (255,0,0)

enemies = []
for i in range (9):
    randomx = random.randint(0,500)
    randomy = random.randint(0,600)
    enemy = pygame.draw.rect(screen,"red",randomx,randomy,50,50)
    enemies.append(enemy)


def player():
    player = pygame.dra

            
while not exit:
    for event in pygame.event.get():
        screen.fill(white)
        pygame.display.flip()
        if event.type == pygame.QUIT:
            exit = True
        
pygame.quit()