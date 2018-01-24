import random
from pygame import *
def lerp(a,b,t):
	return a*(1-t)+b*t
def index(x,y):
	return x+y*width
def set_random(x,y):
	data[x+y*width] = random.randrange(0,10)/10.0

width = 20
height = 20
scale = 16
data = [(0) for x in range(width*height)]
set_random(0,0)
set_random(width-1,0)
set_random(0,height-1)
set_random(width-1,height-1)
for x in range(1,width-1):
	data[index(x,0)] = lerp(data[index(0,0)],data[index(width-1,0)],float(x)/width)


init()
screen = display.set_mode((scale*width,scale*height))
loop = True
screen.fill((0,0,0))
for x in range(width):
	for y in range(height):
		color = data[x+y*width]
		draw.rect(screen,(color*255,color*255,color*255),(x*scale,y*scale,scale,scale))

while loop:
	for e in event.get():
		if e.type == QUIT:loop=False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:loop=False
	display.flip()