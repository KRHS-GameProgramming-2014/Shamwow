import pygame, math, sys

class Key():
    def __init__(self, image, pos = [0,0], blockSize=50, dest=""):
        self.baseImage = pygame.image.load(image)
        if size != None:
            self.resize(size)
        else:
            self.image = self.baseImage
        self.rect = self.imag.get_rect()
        self.place(pos)
        destinations = dest.split()
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos

    def resize (self, size):
        self.image = pygame.transform.scale 
    
    def distance (self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[0]
        y2 = pt[0]
        x2 = pt[0]
        return math.sqrt (((x2-x1)**2) + ((y2-y1)**2))
        
    def playerCollide (self, other):
        if (self.rect.right > other.rect.left
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top
            and self.rect.top < other.rect.bottom):
                self.living = False
            return True
        return False
