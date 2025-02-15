import pygame

pygame.init()

Screenwidth = 400
Screenheight = 500
Color = (255,0,0)
Blue = (0,255,0)

screen = pygame.display.set_mode((Screenwidth,Screenheight))

class Sprite(pygame.sprite.Sprite):
    def __init__(self,height,width,color,x,y):
        super().__init__()
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.width = width
        self.color = color
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: self.rect.x-=1
        if pressed[pygame.K_RIGHT]: self.rect.x+=1
        if pressed[pygame.K_UP]: self.rect.y-=1
        if pressed[pygame.K_DOWN]: self.rect.y+=1

running = True
ob = Sprite(50,50,Color,0,0)
while running:
    screen.fill((200,200,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ob.move()
    screen.blit(ob.image,ob.rect)
    pygame.draw.rect(screen,Blue,(200,200,30,30),)
    pygame.display.flip()
    pygame.time.delay(5)

pygame.quit()