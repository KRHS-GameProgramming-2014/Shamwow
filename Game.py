import pygame, math, sys, os
from Entity import Entity
from Player import Player
from MainMenu import Button
from BackGround import BackGround
from Level import Level
from wall import Block
from wall import BgBlock
from Shammy import ShammyTowel
from towelHead import ShamFlap
from levelChangeBlock import LevelChangeBlock
from key import Key
pygame.init()
 
clock = pygame.time.Clock()

width = 1050
height = 675
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

entities = pygame.sprite.Group()
players = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
keys = pygame.sprite.Group()
shammys = pygame.sprite.Group()
#towelHeads = pygame.sprite.Group()
levelBlocks = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Entity.containers = (all, entities)
Player.containers = (all, players)
ShammyTowel.containers = (all, shammys)
#towelHead = (all, towelHeads)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks) 
BgBlock.containers = (all, backgrounds) 
Key.containers = (all, keys) 
LevelChangeBlock.containers = (all, levelBlocks)



run = "start"

while True:
    bgImage = pygame.image.load("RSC/Background Images/mainmenuthing.png").convert()
    bgImage = pygame.transform.scale(bgImage, size)
    bgRect = bgImage.get_rect()
    
    startButton = Button([width/2, height-300], 
                    "RSC/menue/startbutton.png")
    
    while run == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = "game"
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = "game"
                
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        clock.tick(60)
        
    #BackGround("RSC/Background Images/basichallway.png")
    

    level = Level(75, size)
    level.loadLevel("01") 

    player = Player([width/3, height/2])
    """
    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6
    score = Score([width-80, height-25], "Score: ", 36)
    """
    enteredLevel = False
    
    keylist = []
    while run == "game" and player.living:
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
        for p in playersHitBlocks:
            for block in playersHitBlocks[p]:
                player.collideBlock(Block)
                
        playersHitLevelChangeBlocks = pygame.sprite.groupcollide(players, levelBlocks, False, False)
        if enteredLevel and playersHitLevelChangeBlocks == {}:
            enteredLevel = False
        for player in playersHitLevelChangeBlocks:
            for block in playersHitLevelChangeBlocks[player]:
                if not block.locked or block.curlev in keylist:
                    if not enteredLevel:
                        dest = block.newlev[5:]
                        for s in all.sprites():
                            s.kill()
                    #print dest
                        level.loadLevel(dest[:-1])
                        for block in levelBlocks.sprites():
                            if block.curlev[-1] == dest[-1]:
                                #print block.curlev
                                playerPos = block.rect.center
                                #print playerPos, ">>>>>>>>>>>>>", block.rect.center
                                player = Player(playerPos)
                                enteredLevel = True
                else:
                            player.collideBlock(Block)
                    
        keysHitPlayer = pygame.sprite.groupcollide(keys, players, True, False)
        for key in keysHitPlayer:
            for player in keysHitPlayer[key]:
                #print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                keylist += key.destinations  
                #print keylist          
        #shammysHitBlocks = pygame.sprite.groupcollide(shammys, blocks, False, False)
        #for shammy in shammysHitBlocks:
            #for block in shammysHitBlocks[shammy]:
                #shammy.collideBlock(Block)
        
        shammysHitPlayer = pygame.sprite.groupcollide(shammys, players, False, False)
        for shammy in shammysHitPlayer:
            for players in shammysHitPlayer[shammy]:
                player.collideShammy(shammy)
        #shammysHitBlock = pygame.sprite.groupcollide(shammys, blocks, False, False)
        #for shammy in shammysHitBlock:
            #for blocks in shammysHitBlock[shammy]:
                #shammy.collideBlock(shammy)
                        
        all.update(width, height)

        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    print "dead"
    for s in all.sprites():
        s.kill()
    run = "start"
