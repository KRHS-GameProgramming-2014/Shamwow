import pygame, math, sys, time, os, random

class Block():
    def __init__ (self, image, pos, size):
        self.baseImage = pygame.image.load(image)
        if size != None:
            self.resize(size)
        else:
            self.image = self.baseImage
        self.rect = self.image.get_rect()
        self.place(pos)
    def place(self, pos):
        self.rect.center = pos
        
    def resize (self, size):
        self.image = pygame.transform.scale(self.baseImage, size)
        
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[0]
        y2 = pt[0]
        x2 = pt[0]
        return math.sqrt (((x2-x1)**2) + ((y2-y1)**2))
        
    def EntityCollide(self, other):
        if (self.rect.right > other.rect.left
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and
                self.rect.top < other.rect.bottom):
                #print "Collide With: ", other
                return True
        return False
                
    def update(self):
        pass
