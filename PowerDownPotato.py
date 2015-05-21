import pygame
from Player import Player
from Entity import Entity

class PowerDownPotato(Entity):
    def __init__(self, pos):
        Entity.__init__(self, "RSC/Player Images/playerstep1.png", [0,0], pos)
        self.upImages = [pygame.image.load("RSC/Player Images/playerbackstep1.png"),
                            pygame.image.load("RSC/Player Images/playerbackstep2.png")]
        self.downImages = [pygame.image.load("RSC/Player Images/playerstep1.png"),
                            pygame.image.load("RSC/Player Images/playerstep2.png")]
        self.leftImages = [pygame.image.load("RSC/Player Images/player1side.png"),
                            pygame.image.load("RSC/Player Images/playerside1step.png")]
        self.rightImages = [pygame.image.load("RSC/Player Images/player2side.png"),
                            pygame.image.load("RSC/Player Images/playerside2step.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 4
            
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        Entity.update(self, width, height)
        self.animate()
        self.changed = False
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
    
    def collideBlock(self,block):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.speedy = 0
