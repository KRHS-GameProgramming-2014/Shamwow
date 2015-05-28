import pygame, math
from Entity import Entity
from Player import Player

class ShamFlap(pygame.sprite.Sprite):
    def __init__(self, pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("images/Player/pballru.png"),
                         pygame.image.load("images/Player/pballgu.png"),
                         pygame.image.load("images/Player/pballbu.png")]
        self.downImages = [pygame.image.load("images/Player/pballrd.png"),
                           pygame.image.load("images/Player/pballgd.png"),
                           pygame.image.load("images/Player/pballbd.png")]
        self.leftImages = [pygame.image.load("images/Player/pballrl.png"),
                           pygame.image.load("images/Player/pballgl.png"),
                           pygame.image.load("images/Player/pballbl.png")]
        self.rightImages = [pygame.image.load("images/Player/pballrr.png"),
                            pygame.image.load("images/Player/pballgr.png"),
                            pygame.image.load("images/Player/pballbr.png")]
        
        self.images = self.upImages
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.speedx = random.randint(-4,4)
        self.speedy = random.randint(-4,4)
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos

    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                #print "hit xWall"
        
    def collidePlayer(self, other):
        if self != other:
            if (self.radius + other.radius) > self.distance(other.rect.center):
                if not self.didBounceX:
                    self.speedx = -self.speedx
                    self.didBouncex = True
            if not self.didBounceY:
                    self.speedy = -self.speedy
                    self.didBounceY = True
