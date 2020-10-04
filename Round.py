import pygame

BGGREEN = (5,130,0)


class Round:
	isComplete = False
	
	def __init__(self, players, dispsurf, bigBlind, smlBlind):
		self.players = players
		self.activePlayers = players
		self.currentPlayer = self.players[0]
		self.DISPLAYSURF = dispsurf
		self.DISPLAYSURF.fill(BGGREEN)
		
	def makeNextMove(self):
		for player in self.players:
			player.draw(self.DISPLAYSURF)
		  
