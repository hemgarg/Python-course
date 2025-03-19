from tkinter import * 
import pygame

def startotrestart_tk():
    global root
    root = Tk()
    if 'screen' in globals():
        pygame.quit()
    root.mainloop()

def startorrestart_pg():
    if 'root' in globals():
        root.destroy()
    pygame.init()
    screen_width, screen_height = 500,500
    global screen
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("THE 2D PLATFORMER")



class Object:
    def __init__(self,length,height,x,y):
        self.length = length
        self.height = height
        self.x = x
        self.y = y
    def display(self):
        pygame.draw.rect(screen,"black",
                        (self.x,self.y,self.length,self.height))

class Player:
    def __init__(self,length,height,x,y):
        self.length = length
        self.height = height
        self.x = x
        self.y = y
    def display(self):
        pygame.draw.rect(screen,"red",
                        (self.x,self.y,self.length,self.height))


def level1():
    def frame1():
        l1ob1 = Object(100,10,20,30)
    frame1()
    level1player = Player()


def level2():
    pass

def level3():
    pass

def level4():
    pass

def level5():
    pass

def level6():
    pass

def level7():
    pass

def level8():
    pass

def level9():
    pass

def level10():
    pass

def levelselect():
    pass

