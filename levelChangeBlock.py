import pygame, math, sys
from wall import Block

class LevelChangeBlock(Block):
    def __init__(self, pos, size, newlev, kind):
        Block.__init__(self, "RSC/Block/LevelChangeBlock.png", pos, size)
        print newlev
        self.newlev = newlev
        self.kind = kind


    def playerCollide(self, other):
        if (self.rect.right > other.rect.left
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and
                self.rect.top < other.rect.bottom):
                print "I'm going to ", self.newlev
                return True
        return False
