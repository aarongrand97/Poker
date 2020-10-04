import random, sys, pygame, time, copy
from pygame.locals import *

pygame.init()
NAME_FONT = pygame.font.Font('freesansbold.ttf', 16)
MONEY_FONT= pygame.font.Font('freesansbold.ttf', 14)
BGGREEN    = (  5, 130,   0)

class Player:	
	def __init__(self, playernum):
		self.money = 1000
		self.isActive = True
		self.id = playernum
		##### Name text box #####
		self.name = "Player " + str(self.id) 
		self.nameText = NAME_FONT.render(self.name, True, (0,0,0), BGGREEN)
		self.nameRect = self.nameText.get_rect()
		self.nameRect.topleft = (10, self.id*120 + 40)
		##### Money text box #####
		self.moneyText = MONEY_FONT.render(u"\xA3"+str(self.money), True, (0,0,0), BGGREEN)
		self.moneyRect = self.moneyText.get_rect()
		self.moneyRect.topleft = (10, self.id*120 + 60)
		
	def draw(self, displaySurf):
		# draw player 'head'
		pygame.draw.circle(displaySurf, (0,0,0), (100, self.id*120 + 60), 20, 5)
		displaySurf.blit(self.nameText, self.nameRect)
		displaySurf.blit(self.moneyText, self.moneyRect)
		pygame.display.update()
