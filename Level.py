import pygame, math, sys, time, os, random
from Entity import Entity
from levelChangeBlock import LevelChangeBlock
from Player import Player
from wall import Block

class Level():
    def __init__(self, blockSize, screenSize):
        self.screenSize = screenSize
        self.blockSize = blockSize
        self.level = ""
        
        self.levelChangeBlocks = []
        self.Entity = []
        
        self.blockSize = 70
        
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
    
    def loadLevel(self, level):  
        self.level = level
        print self.level
        levelFile = "RSC/Level/" + "Level" + level +".lvl"
        print levelFile

        f = open(levelFile, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
			print line
        """"
        newlines = []
        #Clean up the file by stripping newlines!
        for line in lines:
            newline = ""
            for c in line:
                if c != "\n":
                    newline += c
                newlines += [newline]
        print len(newlines), len(lines)        
        lines = newlines
        
        """
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    print "block", x, y
                    Block("RSC/Background Images/WELLBLEKC.png", 
                          )

#[(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
 #                         (self.blockSize,self.blockSize)
