from pygame import *
import random
SIZE = (640,640)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

init()
sceen = display.set_mode(SIZE)
SIZE = sceen.get_size()
DRAWSIZE = (64,64)
drawsurf = Surface(DRAWSIZE)
loop = True
clock = time.Clock()
data = [0 for x in range(DRAWSIZE[0]*DRAWSIZE[1])]
px = 0
py = 0
vy = 0

def chk(x,y):
	try:
		return data[x+y*DRAWSIZE[0]]==1
	except Exception as e:
		return False
	

for i in range(DRAWSIZE[0]*DRAWSIZE[1]):
	x = i%DRAWSIZE[0]
	y = i//DRAWSIZE[1]
	if y > 50-random.randrange(0,10):
		data[i] = 1
while loop:
	clock.tick(20)
	for e in event.get():
		if e.type == QUIT:loop = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:loop = False
	######
	keys = key.get_pressed()
	if keys[K_RIGHT] and not chk(px+1,py):
		px+=1
	if keys[K_LEFT] and not chk(px-1,py):
		px-=1
#	if chk(px,py):
#		py -=1
#		vy = 0
	if not chk(px,py+1):
		if vy < 2:
			vy+=1
	if vy > 0:
		for i in range(vy):
			if not chk(px,py+1):
				py +=1
			else:
				vy = 0;break
	if vy < 0:
		for i in range(-vy):
			if not chk(px,py-1):
				py -=1
			else:
				vy = 0;break
	if keys[K_UP] and chk(px,py+1):
		vy = -3
		#py -=1

	if mouse.get_pressed()[0]:
		x,y = mouse.get_pos()
		ix = x*DRAWSIZE[0]//SIZE[0]
		iy = y*DRAWSIZE[1]//SIZE[1]
		data[ix+iy*DRAWSIZE[0]] = 1
	######
	drawsurf.fill(BLACK)
	for i in range(DRAWSIZE[0]*DRAWSIZE[1]):
		if data[i] == 1:
			drawsurf.set_at((i%DRAWSIZE[0],i//DRAWSIZE[1]),WHITE)
	drawsurf.set_at((px,py),RED)
	sceen.blit(transform.scale(drawsurf,SIZE),(0,0))
	display.flip()