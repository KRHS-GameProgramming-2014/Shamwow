import pygame, math, sys
from Player import Player

class Key(pygame.sprite.Sprite):
    def __init__(self, image, pos = [0,0], blockSize=50, dest=""):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = pos)
        self.destinations = dest.split()
        #print self.rect.center, self.destinations
