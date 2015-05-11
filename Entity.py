import pygame, math

class Entity(pygame.sprite.Sprite):
    def __init__(self, image, speed = [0,0], pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
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
        
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
        if self.frame < self.maxFrame:
            self.frame += 1
        else:
            self.frame = 0

        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
                
                self.image = self.images[self.frame]
        
        if self.changed:    
            if self.facing == "up":
                if self.shooting:
                    self.images = self.upRangedImages
                elif self.stabbing:
                    self.images = self.upKnifeImages
                else:
                    self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
                    
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True

        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                
        
    def collideBlock(self, other):
        if self != other:
            if (self.radius + other.radius) > self.distance(other.rect.center):
                if not self.didBounceX:
                    self.speedx = -self.speedx
                    self.didBouncex = True
            if not self.didBounceY:
                    self.speedy = -self.speedy
                    self.didBounceY = True
