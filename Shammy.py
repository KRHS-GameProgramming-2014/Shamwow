import pygame, math, random
from Entity import Entity
from Player import Player

class ShammyTowel(pygame.sprite.Sprite):
    def __init__(self, pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Enemy Images/ththing/OH.png"),
                         pygame.image.load("RSC/Enemy Images/ththing/OHNO.png")]
        self.changed = False
        self.images = self.upImages
        self.speedx = random.randint(-4,4)
        self.speedy = random.randint(-4,4)
        self.speed = [self.speedx, self.speedy]
        self.didBounceX = False
        self.didBounceY = False
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.place(pos)
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
        self.animate()
        self.changed = False
        
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
    
    def collideBlock(self, block):
        self.speedx = random.randint(-4,4)
        self.speedy = random.randint(-4,4)
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 2
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        self.image = self.images[self.frame]
    
    def detect(self, Player):
        if self.distToPoint(player.rect.center) < self.detectionRadius:
            pX = Player.rect.center[0]
            pY = Player.rect.center[1]
            zX = self.rect.center[0]
            zY = self.rect.center[1]
           
            if pX > zX:
                self.speedx = self.maxSpeed
            elif pX < zX:
                self.speedx = -self.maxSpeed
            else:
                self.speedx = 0
       
            if pY > zY:
                self.speedy = self.maxSpeed
            elif pY < zY:
                self.speedy = -self.maxSpeed
            else:
                self.speedy = 0                
