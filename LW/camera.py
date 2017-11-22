import pygame
import sys
import pygame.locals
import pygame.camera

pygame.init()
pygame.camera.init()

lis = pygame.camera.list_cameras()

cam = pygame.camera.Camera(lis[0])
cam.start()
SIZE = cam.get_size()
OWNSIZE = (200,150)
screen = pygame.display.set_mode(OWNSIZE)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	camimage = cam.get_image()
	b = pygame.transform.scale(camimage,OWNSIZE)
	pix = pygame.PixelArray(b)
	for x in range(len(pix)):
		for y in range(len(pix[0])):
			pix[x,y]=pix[x,y]>>7
	screen.blit(pix.make_surface(),(0,0))
	pygame.display.flip()