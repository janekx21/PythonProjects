import pygame,pygame.locals
pygame.init()








screen = pygame.display.set_mode((400,300))
loop = True
while loop:
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN: 
			if e.key == pygame.K_ESCAPE:
				loop = False

pygame.quit()


















