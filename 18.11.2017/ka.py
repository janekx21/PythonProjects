from pygame import *
import sys
import random

SIZE = 100

init()
screen = display.set_mode((SIZE,SIZE))

bord = surfarray.array2d(screen)
newbord = surfarray.array2d(screen)
print("setupFinished")
bord[SIZE//2,SIZE//2] = 255
clock = time.Clock()
while True:
	clock.tick()
	for e in event.get():
		if e.type == QUIT:
			sys.exit()
	mx,my = mouse.get_pos()
#	for x in range(16):
#		for y in range(16):
#			if x+mx >= SIZE:
#				pass
#			elif y+my >= SIZE:
#				pass
#			else:
#				bord[mx+x,my+y] = 255
	#bord[mx,my] = 255
	for x in range(1,SIZE-2):
		for y in range(1,SIZE-2):
			av = 0
			av = bord[x+1,y] +av
			av = bord[x-1,y] +av
			av = bord[x,y+1] +av
			av = bord[x,y-1] +av 

#			av =+ bord[x+1,y+1]
#			av =+ bord[x-1,y+1]
#			av =+ bord[x+1,y-1]
#			av =+ bord[x-1,y-1]
			newbord[x,y] = av*.3
	screen.blit(surfarray.make_surface(newbord),(0,0))
	bord = newbord.copy()
	
	print("itter")
	display.flip()