from pygame import *
import random
init()
num = 0
loop=True
screen = display.set_mode((320,320))
while loop:
	for e in event.get():
		if e.type == QUIT:loop = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:loop = False
	screen.fill((0,0,0))
	for x in range(32):
		for y in range(32):
			if num & 1 << x+y*32:
				draw.rect(screen,(255,255,255),(x*10,y*10,10,10))	
	num+=1
	display.flip()