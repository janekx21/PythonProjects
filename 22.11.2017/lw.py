from pygame import *
init()
loop = True
screen = display.set_mode((200,200))
while loop:
	for e in event.get():
		if e.type == QUIT:
			loop = False
	screen.fill((255,255,255))
	display.flip()