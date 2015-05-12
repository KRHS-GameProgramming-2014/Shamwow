import pygame, math, sys, os
from Entity import Entity
from Player import Player
from MainMenu import Button
from BackGround import BackGround
from Level import Level
from wall import Block
from Shammy import Shammy
pygame.init()
 
clock = pygame.time.Clock()

width = 1050
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

entities = pygame.sprite.Group()
players = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
level = pygame.sprite.Group()
shammy = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Entity.containers = (all, entities)
Player.containers = (all, players)
Shammy.containers = (all, shammy)
Level.containers = (all, level)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks) 

startButton = Button([width/2, height-300], 
                    "RSC/menue/startbutton.png")

bgImage = pygame.image.load("RSC/Background Images/basichallway.png").convert()
bgImage = pygame.transform.scale(bgImage, size)
bgRect = bgImage.get_rect()

run = False

while True:
    bgImage = pygame.image.load("RSC/Background Images/mainmenuthing.png").convert()
    bgImage = pygame.transform.scale(bgImage, size)
    bgRect = bgImage.get_rect()
    
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = True
                
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        clock.tick(60)
        
    BackGround("RSC/Background Images/basichallway.png")
    player = Player([width/2, height/2])

    level = Level(75, size)
    level.loadLevel("1")
    for b in blocks.sprites():
		print b.rect.center
    """
    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6
    score = Score([width-80, height-25], "Score: ", 36)
    """
     
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
                    
        playersHitBlocks = pygame.sprite.groupcollide(players, blocks, False, False)
        
        for player in playersHitBlocks:
            for block in playersHitBlocks[player]:
                player.collideBlock(Block)
    
        all.update(width, height)

        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
