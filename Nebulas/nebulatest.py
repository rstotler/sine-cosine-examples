import pygame, math, random
from pygame import *

class start:
	
	def __init__(self):
		
		pygame.init()
		pygame.display.set_caption("Nebulousness")
		
		self.tick  = 0
		self.clock = pygame.time.Clock()
		self.win   = pygame.display.set_mode((640,480),0,32)
		self.bg    = pygame.Surface((640,480)) ; self.bg.fill((11,11,11))
		self.mouse = [0,0]
		
		self.nebula = [] ; self.load_nebula()
		
		self.main()
		
	def main(self):
		
		while True:
			
			self.clock.tick(60)
			self.tick += 1
			self.get_input()
			
			self.win.blit(self.bg,(0,0))
			for pix in self.nebula : pix.update(self.win,self.mouse)
			
			pygame.display.update()
			
	def get_input(self):
		
		self.mouse[0], self.mouse[1] = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			
			if event.type == QUIT : raise SystemExit
			if event.type == KEYDOWN and event.key == K_ESCAPE : raise SystemExit
		
	def load_nebula(self):
		
		for x in range(3000):
			self.nebula.append(pixel())
				
class pixel:
	
	def __init__(self):
		
		self.dis = random.randrange(1,150)
		self.x   = 0
		self.y   = 0
		
		self.orbit_num  = 25 * self.dis
		self.orbit_tick = random.randrange(0,self.orbit_num)
			
	def update(self,win,mouse):
		
		self.orbit_tick += 1
		if self.orbit_tick >= self.orbit_num : self.orbit_tick = 0
		import math
		self.x = 320 + int(math.cos(math.radians(((self.orbit_tick+.0)/self.orbit_num)*360)) * self.dis)
		self.y = 240 + int(math.sin(math.radians(((self.orbit_tick+.0)/self.orbit_num)*360)) * self.dis) * -1
		
		#self.x = mouse[0] + int(math.cos(math.radians(((self.orbit_tick+.0)/self.orbit_num)*360)) * self.dis)
		#self.y = mouse[1] + int(math.sin(math.radians(((self.orbit_tick+.0)/self.orbit_num)*360)) * self.dis)
		
		r = random.randrange(140,222) + (self.dis*-1)
		g = random.randrange(140,222) + (self.dis*-1)
		b = random.randrange(180,255) + (self.dis*-1)
		clist = [r,g,b] ; color = []
		for c in clist:
			if c < 0   : c = 0
			if c > 255 : c = 255
			color.append(c)
		
		win.set_at((self.x,self.y),color)
			
start()
