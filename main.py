import pygame as pyg

# ------------- CONSTS

# ------------- VARS

# ------------- CLASSES
class Object:
    def __init__(self):
        pass

    def getPos(self):
        pass

    def drawObj(self):
        pass

    def addConnection(self):
        pass

    def getArea(self):
        pass

# ------------ GLOBAL FUNCS
def convert_pos(pos):
    pass

def create_id():
    pass



# ------------- PYGAME
pyg.init()
screen = pyg.display.set_mode((1280, 720))
clock = pyg.time.Clock()
dt = 0
running = True



# -------------- LOOP
while running:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.fill('white')
    #--------------------- DISPLAY




    #---------------------------
    pyg.display.flip()
    dt = clock.tick(60) / 1000
pyg.quit()