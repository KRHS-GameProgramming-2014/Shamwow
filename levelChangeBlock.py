import pygame, math, sys
from wall import Block

class LevelChangeBlock(Block):
    def __init__(self, image, pos, size, curlev, newlev, locked = False):
        Block.__init__(self, image, pos, size)
        #print newlev
        self.curlev = curlev
        self.newlev = newlev
        self.locked = locked 


    def playerCollide(self, other):
        if (self.rect.right > other.rect.left
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and
                self.rect.top < other.rect.bottom):
                #print "I'm going to ", self.newlev
                return True
        return False
