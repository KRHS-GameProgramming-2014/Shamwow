import pygame
from Entity import Entity

class Player(Entity):
	def __init__(self,pos):
		Entity.__init__(self, "RSC/Player Images/player1.png", [0,0], pos)
		self.facing = "up"
		self.changed = False
		self.images = self.upImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 3
