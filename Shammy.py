import pygame, math
from Entity import Entity
from Player import Player

class Shammy(pygame.sprite.Sprite):
	def __init__(self, image, speed = [0,0], pos = [0,0]):
		self.upImages = [pygame.image.load("RSC/Enemy Images/ththing/OH.png"),
 						 pygame.image.load("RSC/Enemy Images/ththing/OHNO.png"),
 						 pygame.image.load("RSC/Enemy Images/ththing/OH.png")]
 		self.downImages = [pygame.image.load("RSC/Enemy Images/ththing/OHNO.png"),
 						   pygame.image.load("RSC/Enemy Images/ththing/OH.png"),
 						   pygame.image.load("RSC/Enemy Images/ththing/OHNO.png")]
 		self.leftImages = [pygame.image.load("RSC/Enemy Images/ththing/OH.png"),
 						   pygame.image.load("RSC/Enemy Images/ththing/OHNO.png"),
 						   pygame.image.load("RSC/Enemy Images/ththing/OH.png")]
 		self.rightImages = [pygame.image.load("RSC/Enemy Images/ththing/OHNO.png"),
 						    pygame.image.load("RSC/Enemy Images/ththing/OH.png"),
 						    pygame.image.load("RSC/Enemy Images/ththing/OHNO.png")]
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
