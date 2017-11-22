import pygame,pygame.locals,pygame.camera,sys

pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((400,300))

print(pygame.camera.list_cameras())
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])

cam.start()
print("start")

print(cam.get_image())

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			cam.stop()
			print("end")
			sys.exit()
	screen.blit(cam.get_image(),(0,0))
	pygame.display.flip()


