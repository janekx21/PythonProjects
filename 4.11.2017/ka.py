import pygame,sys

SIZE = (480,320)

def loop():
	while True:
		for e in pygame.event.get():
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					return
		screen.fill((24,52,52))
		pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode(SIZE)
	loop()
	pygame.quit()