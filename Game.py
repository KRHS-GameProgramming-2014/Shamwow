import pygame, math, sys, os
from Player import Player
pygame.init()
win = False

clock = pygame.time.Clock()
width = 800
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0
screen = pygame.display.set_mode(size)
