from pygame import *
import time as Time
import math
import random
init()
screen = display.set_mode((0,0))
width,height = screen.get_size()
x = width//2
y = height//2
looping = True
clock = time.Clock()
while looping:
	clock.tick(60)
	width,height = screen.get_size()
	for e in event.get():
		if e.type == QUIT:
			looping = False
		if e.type == KEYDOWN:
			looping = False
	color = Color(0,0,0)
	color.hsva = int(Time.time()*100)%360,100,100,100
	screen.fill(color)

	color.hsva = int(Time.time()*100+90)%360,100,100,100
	draw.circle(screen,color,(x,y),int((math.sin(Time.time())+1)*width/4)+1)
	color.hsva = int(Time.time()*100+180)%360,100,100,100
	x+=random.randrange(-1,2)
	y+=random.randrange(-1,2)
	s = Surface((width,height),SRCALPHA)
	liste = [(width//2,0),(width,height),(0,height)]
	draw.polygon(s,color,liste)
	s = transform.rotozoom(s,Time.time()*100%360,(math.sin(Time.time())*-.4))
	screen.blit(s,(0,0))
	display.flip()