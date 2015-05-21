import pygame, math, sys, time, os, random
from Entity import Entity
from levelChangeBlock import LevelChangeBlock
from Player import Player
from wall import Block
from wall import BgBlock

class Level():
    def __init__(self, blockSize, screenSize, linkFile = "RSC/Level/levels.link"):
        self.screenSize = screenSize
        self.blockSize = blockSize
        self.level = ""
        
        self.levelLinks = self.loadLevelLink(linkFile)
        print self.levelLinks
        
        #self.blockSize = 70
    
    def loadLevelLink(self, file):
        f = open(file, 'r')
        links = f.readlines()
        f.close()
        
        newLinks = []
        for link in links:
            if link[0] != '#' and link [0] != '\n':
                newLink = ""
                for c in link:
                    if c != '\n':
                        newLink += c
                newLinks += [newLink]
        links = newLinks
        
        newLinks = {}
        for link in links:
            link = link.split(',')
            newLinks[link[0]] = link[1]
        links = newLinks
        
        return links
        
    """ 
    def killOldLevels(self, timeInSeconds):
        for f in os.listdir("RSC/Level"):
            if f[-5:] == ".tngs":
                print f, time.time() - os.path.getmtime("RSC/Level/"+f), timeInSeconds
                if (time.time() - os.path.getmtime("RSC/Level/"+f)) > timeInSeconds:
                    print f
                    os.remove("RSC/Level/"+f)        
    """
    def loadLevel(self, level):  
        self.level = "Level"+level
        print self.level
        levelFile = "RSC/Level/" + "Level" + level +".lvl"
        print levelFile

        f = open(levelFile, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            print line
        """
        newlines = []
        #Clean up the file by stripping newlines!
        for line in lines:
            newline = ""
            for c in line:
                if c != "\n"
                    newline += c
                newlines += [newline]
        print len(newlines), len(lines)        
        lines = newlines
        
        """
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    #print "block", x, y
                    Block("RSC/Props/PLENT.png", 
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "@":
                    Block("RSC/Background Images/wlaklnra.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "!":
                    Block("RSC/Background Images/WELLBLEKC.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "$":
                    Block("RSC/Background Images/dfaesdfaesdfaesdfaesdfaesdfaesdfaesdfaesdfaesdfaes.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == " ":
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                       
                if c in "ABC": #Door from Top
                   LevelChangeBlock("RSC/Background Images/ANOTHER DOOR.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c])
                
                if c in "GHI": #Door from Bottom
                   LevelChangeBlock("RSC/Background Images/dor.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c])
                            
                if c in "MNO": #Stairs
                   LevelChangeBlock("RSC/Background Images/sterans.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c])
                
                if c in "STU": #Door from Side
                   LevelChangeBlock("RSC/Background Images/dorside.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c])
                               
                if c in "XYZ": #Stairs from Side
                   LevelChangeBlock("RSC/Background Images/steranside.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c])
                
