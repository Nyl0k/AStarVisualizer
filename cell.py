import pygame

class Cell:
    color = (100,100,100)
    x = 0
    y = 0
    g = 0
    h = 0
    surf = None
    wall = False
    occupied = False
    parent = None

    def __init__(self, X, Y, window, isWall=False):
        self.x = X
        self.y = Y
        self.surf = window
        self.wall =  isWall

    def create(self):
        pygame.draw.rect(self.surf, self.color, pygame.Rect(self.x, self.y, 25, 25))

    def block(self):
        self.color = (0,0,0)
        self.wall = True
        self.create()

    def occupy(self):
        self.color = (255,0,0)
        self.occupied = True
        self.create()
