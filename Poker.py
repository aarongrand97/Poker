import random, sys, pygame, time, copy
from pygame.locals import *
from Game import Game

FPS = 10
WINDOWWIDTH = 640;
WINDOWHEIGHT = 480;

#              R    G    B
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
GREEN      = (  0, 155,   0)
BRIGHTBLUE = (  0,  50, 255)
BROWN      = (174,  94,   0)
BGGREEN    = (  5, 130,   0)

TEXTBGCOLOR1 = BRIGHTBLUE
TEXTBGCOLOR2 = GREEN
GRIDLINECOLOR = BLACK
TEXTCOLOR = WHITE
HINTCOLOR = BROWN

def main():
    global MAINCLOCK, DISPLAYSURF, FONT, BIGFONT
    
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Poker')
    FONT = pygame.font.Font('freesansbold.ttf', 16)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 32)
    
    while True:
	if(runGame() == False):
	    break

def runGame():
    if(checkLoadGame() == False):
	game = Game(DISPLAYSURF)
	while (game.isFinished == False):
	    game.playNextRound()
	return False
	
	

def checkLoadGame():
    newGameSurf = BIGFONT.render('New Game', True, TEXTCOLOR, BGGREEN)
    newGameRect = newGameSurf.get_rect()
    newGameRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) - 40)
    while True:
	checkForQuit()
	for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if newGameRect.collidepoint( (mousex, mousey) ):
                    return False
	DISPLAYSURF.fill(BGGREEN)
	DISPLAYSURF.blit(newGameSurf, newGameRect)
	pygame.display.update()
	MAINCLOCK.tick(FPS)

def checkForQuit():
    for event in pygame.event.get((QUIT, KEYUP)): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
