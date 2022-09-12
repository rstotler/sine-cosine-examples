import pygame, math
from pygame import *

class load:

	def __init__(self):
	
		self.player = player()
		
		self.bg = pygame.Surface((640,480)) ; self.bg.fill((0,0,0))
		
	def update(self,window,mouse):
	
		self.get_input(mouse)
		
		window.blit(self.bg,(0,0))
		self.player.update(window,mouse)
		
	def get_input(self,mouse):
	
		mouse.x, mouse.y = pygame.mouse.get_pos()
		import math
		mouse.angle = math.atan2((mouse.y-self.player.y),(mouse.x-self.player.x))
		print(mouse.angle)
		
		for event in pygame.event.get():
		
			if   event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) : raise SystemExit
			elif event.type == MOUSEBUTTONDOWN and event.button == 1 : self.player.fire(mouse)
			elif event.type == MOUSEBUTTONDOWN and event.button == 3 and not mouse.right_clicking : mouse.right_clicking = True
			elif event.type == MOUSEBUTTONUP   and event.button == 3 and     mouse.right_clicking : mouse.right_clicking = False
			
		if mouse.right_clicking : self.player.move(mouse)
		
class player:

	def __init__(self):
	
		self.bullets = []
	
		self.x = 320
		self.y = 240
		
		self.micro_x = 0.0
		self.micro_y = 0.0
		
		self.color = [200,0,0]
		
		self.speed = 3
		
	def update(self,window,mouse):
	
		#pygame.draw.line(window,self.color,[self.x,self.y],[mouse.x,mouse.y])
		pygame.draw.circle(window,self.color,[self.x,self.y],10)
		
		del_list = []
		for bnum, b in enumerate(self.bullets):
			b.update(window)
			if b.life == 0 : del_list.append(bnum)
		del_list.reverse()
		for bnum in del_list : del self.bullets[bnum]
		
	def fire(self,mouse):

		# CREATE NEW BULLET #
		import math
		mx = math.cos(mouse.angle)
		my = math.sin(mouse.angle)
		x  = self.x + mx * 10
		y  = self.y + my * 10
		
		b = bullet(mx,my,x,y)
		self.bullets.append(b)
	
	def move(self,mouse):
		
		import math
		xx  = mouse.x - self.x ; xx = xx * xx
		yy  = mouse.y - self.y ; yy = yy * yy
		dis = math.sqrt(xx+yy)
		
		if dis > 2:
			mx = math.cos(mouse.angle)
			my = math.sin(mouse.angle)
			
			speed = self.speed
			if dis > 70 : speed = 3
			
			self.micro_x += mx * speed
			self.micro_y += my * speed
			
		while self.micro_x >= 1  : self.x += 1 ; self.micro_x -= 1
		while self.micro_x <= -1 : self.x -= 1 ; self.micro_x += 1
		while self.micro_y >= 1  : self.y += 1 ; self.micro_y -= 1
		while self.micro_y <= -1 : self.y -= 1 ; self.micro_y += 1
			
class bullet:

	def __init__(self,mx,my,x,y):
	
		self.mx = mx
		self.my = my
		self.x  = x
		self.y  = y
		
		self.speed = 10
		self.life  = 50
		
	def update(self,window):
	
		self.x = self.x + self.mx * self.speed
		self.y = self.y + self.my * self.speed
		self.life -= 1
	
		if self.life > 0:
			pygame.draw.circle(window,[250,250,250],[int(self.x),int(self.y)],4)
		