from pygame import *
import math
import time as Time
SIZE = (500,400)
screen = display.set_mode(SIZE)

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

clock = time.Clock()

def main():
	init()
	loop()

def loop():
	global clock
	clock.tick()
	while True:
		width,height = SIZE
		for e in event.get():
			if e.type == QUIT:
				return
			if e.type == KEYDOWN:
				pass
		#screen.fill(BLACK)
		for x in range(width):
			y = int(math.sin(float(x+Time.time()*100)/(width//10))*height/2)+height//2
			color = Color(0,0,0)
			if x%2==0:
				y = height-y
#				color =BLUE
#			if y > height//2:
#				if color == BLUE:
#					color = RED
#				else:
#					color = BLUE
			hsva = color.hsva
			color.hsva = (-x-int(Time.time()*200))%360,100,100,100
			#draw.circle(screen,color,(x,y),8)
			#draw.rect(screen,color,(x,y,64,64),1)
			draw.line(screen,color,(x,y),(x,y+32))
			#screen.set_at((x,y),color)
		display.flip()
if __name__ == "__main__":
	main()