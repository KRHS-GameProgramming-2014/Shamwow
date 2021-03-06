import pygame, math, sys, time, os, random
from Entity import Entity
from levelChangeBlock import LevelChangeBlock
from Player import Player
from wall import Block
from wall import BgBlock
from Shammy import ShammyTowel
from key import Key
from towelHead import ShamFlap

class Level():
    def __init__(self, blockSize, screenSize, levelLinkFile = "RSC/Level/levels.link", keyLinkFile = "RSC/Level/keys.link"):
        self.screenSize = screenSize
        self.blockSize = blockSize
        self.level = ""
        self.shammy = []
        self.levelLinks = self.loadLinks(levelLinkFile)
        self.keyLinks = self.loadLinks(keyLinkFile)
        self.lockedDoors = []
        for v in self.keyLinks.values():
            self.lockedDoors += v.split()
        #print self.lockedDoors
        #print self.levelLinks
        
        #self.blockSize = 70
    
    def loadLinks(self, file):
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
        #print self.level
        levelFile = "RSC/Level/" + "Level" + level +".lvl"
        #print levelFile
        monsters = {"shammy": [],
                    "shamflap": []}
        f = open(levelFile, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            pass
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
                #print level+c
                if "Level"+level+c in self.lockedDoors:
                    locked = True
                    #print level+c, "is locked"
                else:
                    locked = False
                if c == "#": #Plant
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/Props/PLENT.png",
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
                       
                if c in "AB": #Door from Top
                    LevelChangeBlock("RSC/Background Images/ANOTHER DOOR.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                
                if c in "CD": #Door from Bottom
                    LevelChangeBlock("RSC/Background Images/AH.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                            
                if c in "EF": #Down Stairs
                    LevelChangeBlock("RSC/Background Images/dhjnsb99.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                
                if c in "GH": #Door from Left Side
                   LevelChangeBlock("RSC/Background Images/drfsejdfsennjfyu3.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                               
                if c in "IJ": #Up Stairs from Side
                   LevelChangeBlock("RSC/Background Images/a not so stupid nam.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                if c in "KL": #Door from Right Side
                   LevelChangeBlock("RSC/Background Images/hhhhhhhhhhhhhhhhhhhhhhhhhhhhh.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                if c in "MN": #Up Stairs
                   LevelChangeBlock("RSC/Background Images/sterans.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                if c in "OP": #Down Stairs from Side
                   LevelChangeBlock("RSC/Background Images/steranside.png",
                               [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                               self.blockSize,
                               self.level+c,
                               self.levelLinks[self.level+c],
                               locked)
                if c == "/": #dead Cheyenne
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/deadchey.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)               
                if c == "%": #shammytowelblock
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    monsters["shammy"] += [[(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)]]
                if c == ".": #shamflapblock
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    monsters["shamflap"] += [[(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)]]
                if c in "abcdefghijklmno": #KEYS
                    #print "KEY!!!!!!!!!!!!!!!!!!!!!!!!"
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Key("RSC/Props/Key Images/okey.png",
                       [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                        self.blockSize,
                        self.keyLinks["Key"+self.level[-2:]+c])
                if c == "`": #Bed
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/bed.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "~": #Robot
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/benedict.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "^": #Bathtub
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/beth.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "&": #Carpet
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/Props/bloody triangle.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "*": #Chair
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/Props/chair.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "(": #Fridge
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/frigersat.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == ")": #Counter
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/ketchnicounter.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "-": #Giraffe
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/Props/rutherford.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "_": #Shelf
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/shelf.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "+": #Sofa
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/Props/sofa.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "=": #Table
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/table.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "[": #Toilet
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    Block("RSC/Props/toi lit.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "]": #Dead Zoe
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/deadzoe.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                if c == "{": #Dead Ellie
                    BgBlock("RSC/Background Images/basichallway.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
                    BgBlock("RSC/deadellie.png",
                          [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                          self.blockSize)
        for shammy in monsters["shammy"]:
            ShammyTowel(shammy)
        for shamflap in monsters["shamflap"]:
            ShamFlap(shamflap)
