import pygame as pygame
from pygame.locals import *
import sys
import random

class Worker:
	def __init__(self,x,y):
		self.x=x;self.y=y
		self.dir = 0 # right,up,left,down
		self.steeps = 0
	def draw(self,app):
		pygame.draw.circle(app.screen,(255,0,0),(self.x,self.y),5)
		app.map.set_at((self.x,self.y),(0,255,0))
	def update(self,app):
		if self.steeps == 0:
			ndir = self.dir
			while ndir == self.dir:
				ndir = random.randrange(0,4)
			self.dir = ndir
			self.steeps = random.randrange(0,20)
		else:
			self.steeps-=1
			if self.dir == 0:
				self.x += 1
			elif self.dir == 1:
				self.y -= 1
			elif self.dir == 2:
				self.x -= 1
			else:
				self.y += 1
	def split(self,app): 
		app.workers.append(Worker(self.x,self.y))
class app:
	SIZE = (400,400)
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.SIZE)
		self.map = pygame.Surface(self.SIZE)
		self.workers = []
		for x in range(40):
			for y in range(40):
				self.workers.append(Worker(x*10,y*10))
		self.loop()
	def loop(self):
		clock = pygame.time.Clock()
		while True:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					elif event.key == pygame.K_t:
						self.workers = []
			self.screen.fill((255,255,255))
			self.screen.blit(self.map,(0,0))
			for worker in self.workers:
				worker.update(self)
			for worker in self.workers:
				worker.draw(self)
			pygame.display.flip()

if __name__ == "__main__":
	app()