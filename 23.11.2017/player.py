from pygame import *
class Player:
	def __init__(self):
		self.pos = 0,0
		self.hp = 100
	def update(self):
		pass
	def draw(self,screen):
		draw.circle(screen,(255,0,0),self.pos,10)