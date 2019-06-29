
import random


class Board:
    
    def __init__(self,cellsize,length,height):
        self.c=cellsize
        self.l=length
        self.h=height
        assert self.h % self.c == 0
        assert self.l % self.c == 0
        self.food=[]
    def Food(self):
        return self.food
    def cellsize(self):
        return self.c
    def width(self):
        return self.l
    def height(self):
        return self.h
    def cellheight(self):
        return self.h//self.c
    def cellwidth(self):
        return self.l//self.c
    def generateBoard(self,cellsize):
        self.c=cellsize
        possiblesize=[cellsize*x for x in range(30,60)]
        self.l = random.choice(possiblesize)
        self.h = random.choice(possiblesize)

    
    def getRandomLocation(self):
        CELLWIDTH= self.cellwidth()
        CELLHEIGHT=self.cellheight()
        return {'x':random.randint(0,CELLWIDTH-2),'y': random.randint(0,CELLHEIGHT-2)}
    def createFood(self,number):
        for x in range(number):
            (self.food).append(self.getRandomLocation())

    def replaceFood(self,index):
        if self.food==[]:
            self.createFood(3)
        else:
            del self.food[index]
            newfood = self.getRandomLocation()
            self.food.append(newfood)
        
    