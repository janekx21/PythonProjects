import pygame, sys
from pygame.locals import *

from gameobject import *
from vector import *

class Brick(GameObject):
	def draw(s,display):
		pygame.draw.rect(display, (255,20,20), (s.position.x, s.position.y, 64, 32),)
		pygame.draw.rect(display, BLACK, (s.position.x, s.position.y, 64, 32),1)
	def update(s):
		#s.position += Vector(0,1)
		pass
class Select(GameObject):
	def draw(s,display):
		pygame.draw.rect(display, (20,20,255,127), (s.position.x, s.position.y, 64, 32))
	def update(s):
		global objMng
		pos = pygame.mouse.get_pos()
		#print pos
		s.position = Vector(pos[0] / 32 * 32,pos[1]/32*32)
		if pygame.mouse.get_pressed()[0]:
			objMng.add(Brick(position=s.position))

pygame.init()
objMng = ObjectManager()
objMng.add(Brick(position=Vector(32,32)))
objMng.add(Select())

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0,32)#pygame.FULLSCREEN, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

keys = []

# run the game loop
while True:
	DISPLAYSURF.fill(WHITE);
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key not in keys:
				keys.append(event.key)
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == KEYUP:
			if event.key in keys:
				keys.remove(event.key)
	pygame.draw
	objMng.update(DISPLAYSURF)
	pygame.display.update()
