import pygame, sys, random
from pygame.locals import *
from board import *
from snake import *
FPS = 15
##set up syntactic sugar
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   50, 255)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
DARKBLUE = (0,50,200)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 #snake's head


##quit game

def terminate():
    pygame.quit()
    sys.exit()   
##set up grid
grid = Board(20,1800,1000)
WINDOWHEIGHT=grid.height()
WINDOWWIDTH= grid.width()
CELLWIDTH= grid.cellwidth()
CELLHEIGHT=grid.cellheight()
CELLSIZE=grid.cellsize()





def runGame():
    snake1=Snake(grid)
    snake2 = Snake(grid)
    if grid.Food() == []:
        grid.createFood(10)
    food=grid.Food()
    snake1Coords=snake1.Coordinates()
    snake2Coords=snake2.Coordinates()
    while True:
        food=grid.Food()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type==KEYDOWN:
                if (event.key==K_LEFT) and snake1.Direction() !=RIGHT:

                    snake1.Direct(LEFT)

                elif (event.key == K_RIGHT) and snake1.Direction() != LEFT:

                    snake1.Direct(RIGHT)

                elif (event.key == K_UP ) and snake1.Direction() != DOWN:

                    snake1.Direct(UP)

                elif (event.key == K_DOWN) and snake1.Direction() != UP:

                    snake1.Direct(DOWN)


                elif (event.key==K_a) and snake2.Direction() !=RIGHT:

                    snake2.Direct(LEFT)

                elif (event.key == K_d) and snake2.Direction() != LEFT:

                    snake2.Direct(RIGHT)

                elif (event.key == K_w) and snake2.Direction() != DOWN:

                    snake2.Direct(UP)

                elif ( event.key == K_s) and snake2.Direction() != UP:

                    snake2.Direct(DOWN)

                elif event.key == K_ESCAPE:

                    terminate()
        ##check if snake head hits other snake's body
        for segment in snake1Coords[1:]:
            if segment==snake2Coords[HEAD]:
                return
        for segment in snake2Coords[1:]:
            if segment==snake1Coords[HEAD]:
                return
        for count,meal in enumerate(food):
            if snake1Coords[HEAD]['x']==meal['x'] and snake1Coords[HEAD]['y']==meal['y']:
                grid.replaceFood(count)
                
                snake1.justeaten(True)
            if snake2Coords[HEAD]['x']==meal['x'] and snake2Coords[HEAD]['y']==meal['y']:
                grid.replaceFood(count)
                snake2.justeaten(True)
        snake1.move()
        snake2.move()
        DISPLAYSURF.fill(BGCOLOR)
        drawSnake1(snake1Coords)
        drawSnake2(snake2Coords)
        drawfood(food)
        drawFirstScore(len(snake1Coords)-3)
        drawSecondScore(len(snake2Coords)-3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


##FUNCTIONS TO DRAW EVERYTHING

##draw all the food
def drawfood(food):
    for meal in food:
        x = meal['x'] * CELLSIZE
        y = meal['y'] * CELLSIZE
        appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, RED, appleRect)
##draw start screen "press a key to play."
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True,
    DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()

    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


##check to see if key is pressed.
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)

    if len(keyUpEvents) == 0:

        return None

    if keyUpEvents[0].key == K_ESCAPE:

        terminate()

    return keyUpEvents[0].key

#draw start screen  before game runs
def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    cover=titleFont.render('snake fight!', True, WHITE, DARKGREEN)
    Rect = cover.get_rect()
    DISPLAYSURF.blit(cover, Rect)
    drawPressKeyMsg()
   
    if checkForKeyPress():
        pygame.event.get() # clear event queue
        return

    
##when you lose
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurface = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurface.get_rect()
    gameRect.midtop = (WINDOWWIDTH // 2, 10)

    overRect.midtop = (WINDOWWIDTH // 2, gameRect.height + 10 + 25)
    DISPLAYSURF.blit(gameSurf, gameRect)

    DISPLAYSURF.blit(overSurface, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()
    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
##keep track of score on topright of screen
def drawSecondScore(score):

    scoreSurf = BASICFONT.render('Score 2: %s' % (score), True, WHITE)

    scoreRect = scoreSurf.get_rect()

    scoreRect.topleft = (WINDOWWIDTH - 120, 10)

    DISPLAYSURF.blit(scoreSurf, scoreRect)
def drawFirstScore(score):

    scoreSurf = BASICFONT.render('Score 1: %s' % (score), True, WHITE)

    scoreRect = scoreSurf.get_rect()

    scoreRect.topleft = (10, 10)

    DISPLAYSURF.blit(scoreSurf, scoreRect)

##draw the snake
def drawSnake1(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8,CELLSIZE-8)
        pygame.draw.rect(DISPLAYSURF, GREEN, snakeInnerSegmentRect)
def drawSnake2(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKBLUE, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8,CELLSIZE-8)
        pygame.draw.rect(DISPLAYSURF, BLUE, snakeInnerSegmentRect)
        




def main():
    
    global FPSCLOCK,DISPLAYSURF,BASICFONT
    
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)
    pygame.display.set_caption('snake')
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()
        
if __name__ == '__main__':
    main()