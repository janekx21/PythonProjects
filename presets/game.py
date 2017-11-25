from pygame import *
SIZE = (200,200)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

init()
sceen = display.set_mode(SIZE)
SIZE = sceen.get_size()
loop = True
clock = time.Clock()
while loop:
	clock.tick(60)
	for e in event.get():
		if e.type == QUIT:
			loop = False
	sceen.fill(WHITE)
	display.flip()