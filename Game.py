import pygame, sys
from pygame.locals import *
from Player import Player
from Round import Round

class Game:
	isFinished = False
	players = []
	CLOCK = pygame.time.Clock()
	bigBlind = 20
	smlBlind = 10
	
	def __init__(self, dispSurf):
		# need to initiliase players and money etc
		self.DISPLAYSURF = dispSurf
		for x in range(4):
			self.players.append(Player(x))
	
	def playNextRound(self):
		currentRound = Round(self.players, self.DISPLAYSURF, self.bigBlind, self.smlBlind)
		while(currentRound.isComplete == False):
			self.checkForQuit()
			currentRound.makeNextMove()
			self.CLOCK.tick(10)

		
	def checkForQuit(self):
		for event in pygame.event.get((QUIT, KEYUP)): # event handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				print("QUIT")
				pygame.quit()
				sys.exit()
