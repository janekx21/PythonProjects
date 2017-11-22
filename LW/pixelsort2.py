import pygame
import sys
import math
import pygame.locals
import pygame.camera

pygame.init()
pygame.camera.init()

image = pygame.image.load("/home/janek/Bilder/camera/hand1.jpg")
SIZE = (400,300)
screen = pygame.display.set_mode(SIZE)
SIZE = screen.get_size()
b = pygame.transform.scale(image,SIZE)
image = pygame.Surface(SIZE)
image.blit(b,(0,0))
WIDTH = image.get_width()
HEIGHT = image.get_height()

SIZE = image.get_size()
image.set_alpha(255)
pix = pygame.PixelArray(image)
i = 0
render = True

print(len(pix))
print(len(pix[0]))
#pix.replace((0,0,0),(0,0,0),.1)

def want():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

for x in range(WIDTH):
	for y in range(HEIGHT):
		want()
		color = pygame.Color(pix[x,y]<<8)
		hsva = color.hsva
		hsva = hsva[0],100-hsva[2],100-hsva[1],hsva[3]
		color.hsva = hsva
		pix[x,y] = color
	screen.blit(pix.make_surface(),(0,0))
	pygame.display.flip()
	want()
pygame.image.save(pix.make_surface(),"new.png")
while True:
	want()
	pygame.display.flip()




"""
		rec = color.r + color.g + color.b
		reci = -1
		for i in range(x+y*WIDTH,WIDTH*HEIGHT):
			
			c2 =pygame.Color(pix[i%WIDTH,i//WIDTH])
			br =c2.r+c2.g+c2.b 
			if br > rec:
				rec = br
				reci = i
		pix[x,y],pix[reci%WIDTH,reci//HEIGHT]=pix[reci%WIDTH,reci//HEIGHT],pix[x,y]
"""