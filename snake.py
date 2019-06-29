import random
class Snake():
    
    def __init__(self,board_):
        self.eaten=False
        self.board=board_
        CELLWIDTH=self.board.cellwidth()
        CELLHEIGHT= self.board.cellheight()
        startx = random.randint(5,CELLWIDTH-6)
        starty = random.randint(5,CELLHEIGHT-6)
        self.coords = [{'x': startx,'y': starty},
                {'x': startx - 1, 'y': starty},
                {'x': startx - 2, 'y': starty}]
        self.direction=random.choice(['up','left','down','right'])
    
    def Coordinates(self):
        return self.coords
    def justeaten(self,check):
        self.eaten=check
    def Direction(self):
        return self.direction
    def move(self):
        CELLWIDTH=self.board.cellwidth()
        CELLHEIGHT= self.board.cellheight()
        HEAD = 0
        snakeCoords = self.coords
        if self.direction =='up':
            newhead={'x':snakeCoords[HEAD]['x'],'y':snakeCoords[HEAD]['y']-1}
        elif self.direction =='down':
            newhead={'x':snakeCoords[HEAD]['x'],'y':snakeCoords[HEAD]['y']+1}
        elif self.direction =='left':
            newhead={'x':snakeCoords[HEAD]['x']-1,'y':snakeCoords[HEAD]['y']}
        elif self.direction =='right':
            newhead={'x':snakeCoords[HEAD]['x']+1,'y':snakeCoords[HEAD]['y']}
        snakeCoords.insert(0,newhead)  
        if newhead['x']< 0:
            newhead['x']= CELLWIDTH-1
        if newhead['x']>=CELLWIDTH:
            newhead['x']= 0 

        if newhead['y']>CELLHEIGHT-1:
            newhead['y']= 0 
        if newhead['y']<0:
            newhead['y']=CELLHEIGHT-1
        
        if not self.eaten:
            del self.coords[-1]
        if self.eaten:
            self.eaten=False

    def Direct(self,direct):
        assert direct in ['up','left','down','right']
        self.direction=direct