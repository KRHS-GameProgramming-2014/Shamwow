import pygame, math, sys, time, os, random
from Entity import Entity
from levelChangeBlock import LevelChangeBlock
from Player import Player
from wall import Block

class Level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.blocks = []
        self.hardBlocks = []
        
        self.levelChangeBlocks = []
        self.Entity = []
        
        self.blockSize = 70
        self.level = level
        self.load(level)
        
    def killOldLevels(self, timeInSeconds):
        for f in os.listdir("RSC/Level"):
            if f[-5:] == ".tngs":
                print f, time.time() - os.path.getmtime("RSC/Level/"+f), timeInSeconds
                if (time.time() - os.path.getmtime("RSC/Level/"+f)) > timeInSeconds:
                    print f
                    os.remove("RSC/Level/"+f)
            

    def unload(self):
        things = []
        line = []
        for y in range(14):
            for x in range(20):
                line += [" "]
            things += [line]
            line = []
        #print len(things), len(things[0])
        
        for Entity in self.Entity:
            things[Entity.rect.center[1]/50][Entity.rect.center[0]/50] = "G"
        for lc in self.levelChangeBlocks:
            things[lc.rect.center[1]/50][lc.rect.center[0]/50] = lc.kind
        
        thingString = ""
        for line in things:
            for c in line:
                thingString += c
            thingString += "\n"
        #print thingString
        
        thingMap="RSC/Level/"+ self.level +".tngs"
        savedThingfile = open(thingMap, "w")
        savedThingfile.write(thingString)
        savedThingfile.close()
            
        while len(self.blocks) > 0:
            self.blocks.remove(self.blocks[0])
        while len(self.hardBlocks) > 0:
            self.hardBlocks.remove(self.hardBlocks[0])
        while len(self.levelChangeBlocks) > 0:
            self.levelChangeBlocks.remove(self.levelChangeBlocks[0])
        while len(self.Entity) > 0:
            self.Entity.remove(self.Entity[0])
    
    def load(self, level):  
        self.level = level
        print self.level
        geoMap="RSC/Levels/"+ level +".lvl"
        thingMap="RSC/Levels/"+ level +".tng"

        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        

        #Clean up the file by stripping newlines!
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]

        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "#":
                    self.hardBlocks += [Block("RSC/Background Images/mapblock2.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]
                    self.blocks += [self.hardBlocks[-1]]
                if c == "*":
                    self.blocks += [Block("RSC/Background Images/block.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]

        
        thingfile = open(thingMap, "r")
        lines = thingfile.readlines()
        thingfile.close()

        newlines = []

        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]

        for y, line in enumerate(newlines):
            for x, c in enumerate(line): 
                if c == "@":
                    self.player = Player([(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])
                if c == "j":
                    speeds = [[0,-5], [5,0], [0,5], [-5,0]]
                    self.Entity += [Entity("RSC/Enemy/", 
                                        speeds[random.randint(0,3)],
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)]
                                    )]
