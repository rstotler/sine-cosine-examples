import pygame, game
from pygame import *

class start:

	def __init__(self):
	
		pygame.init()
		self.window = pygame.display.set_mode((640,480),0,32)
		self.clock  = pygame.time.Clock()
		self.game   = game.load()
		self.mouse  = mouse()
		
		self.main()
		
	def main(self):
	
		while True:
		
			self.clock.tick(60)
			self.game.update(self.window,self.mouse)
			pygame.display.update()
			
class mouse:
	
	def __init__(self):
	
		self.x = 0
		self.y = 0
		
		self.angle = 0
		
		self.right_clicking = False
			
start()