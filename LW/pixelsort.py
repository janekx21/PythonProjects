import pygame
import sys
import math
import pygame.locals
import pygame.camera

pygame.init()
pygame.camera.init()

image = pygame.image.load("/home/pi/Pictures/camera/stand1.png")
WIDTH = image.get_width()
HEIGHT = image.get_height()

SIZE = image.get_size()
screen = pygame.display.set_mode(SIZE)
pix = pygame.PixelArray(image)
i = 0
render = True

print(len(pix))
print(len(pix[0]))
#pix.replace((0,0,0),(0,0,0),.1)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	for b in range(1000):
		if render:
			x,y = i//WIDTH,i%HEIGHT
			x2,y2 = i%WIDTH,i//HEIGHT
			color = pygame.Color(pix[x,y])
			color2 = pygame.Color(pix[x2,y2])
			pix[x,y] = pix[x,y]#(color.r,color.g,color.b)
			
			i+=1
			if x == WIDTH-1 and y == HEIGHT-1:
				i=0
				pygame.image.save(pix.make_surface(),"new.png")
	screen.blit(pix.make_surface(),(0,0))
	pygame.display.flip()