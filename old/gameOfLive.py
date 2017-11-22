import pygame as pygame
from pygame.locals import *
import sys
import random
import array

class app:
	SIZE = (400,400)
	WIDTH = 400
	HEIGHT = 400
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.SIZE)
		self.map = array.array("B",[0x00 for x in range(400*400//8+1)])
		print(self.setAt(267,0,1))
		print(self.getAt(267,0))
		print(self.getAt(269,0))
		print(self.getAt(270,0))
		self.loop()
	def getAt(self,x,y):
		index = x+y*(self.WIDTH//8)
		if x<0:return 0
		if y<0:return 0
		if x>self.WIDTH:return 0
		if y>self.HEIGHT:return 0
		return self.map[index//8]>>index%8 & 1
	def setAt(self,x,y,b):
		index = x+y*self.WIDTH
		self.map[index//8] = b << index%8 | self.map[index//8]
	def loop(self):
		clock = pygame.time.Clock()
		while True:
			clock.tick()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
			mpos = pygame.mouse.get_pos()
			self.setAt(mpos[0],mpos[1],1)
			self.screen.fill((100,100,100))
			for x in range(self.WIDTH):
				for y in range(self.HEIGHT):
					b = self.getAt(x,y)
					i=0
					if self.getAt(x+1,y) == 0:i+=1
					if self.getAt(x+1,y-1) == 0:i+=1
					if self.getAt(x,y-1) == 0:i+=1
					if self.getAt(x-1,y-1) == 0:i+=1
					if self.getAt(x-1,y) == 0:i+=1
					if self.getAt(x-1,y+1) == 0:i+=1
					if self.getAt(x,y+1) == 0:i+=1
					if self.getAt(x+1,y+1) == 0:i+=1

					if i == 2:
						pass
					elif i == 3:
						self.setAt(x,y,1)
					else:
						self.setAt(x,y,0)


					if b==1:
					 	self.screen.set_at((x,y),(255,255,0))
			pygame.display.flip()

if __name__ == "__main__":
	app()