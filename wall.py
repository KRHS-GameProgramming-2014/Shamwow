import pygame, math

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos = [0,0], blockSize=50):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [blockSize, blockSize])
        self.rect = self.image.get_rect()
        self.place(pos)
        #self.living = true
        #print pos
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(*args):
        self = args[0]
