import pygame,pygame.locals,sys,os,random

SIZE = (64*8,48*8)
TILESIZE = 4
WIDHT = SIZE[0]/TILESIZE
HEIGHT = SIZE[1]/TILESIZE

bord = [[random.randrange(0,2) for x in range(-1,HEIGHT+1)]for y in range(-1,WIDHT+1)]
newbord = [[random.randrange(0,2) for x in range(-1,HEIGHT+1)]for y in range(-1,WIDHT+1)]

def loop():
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					return
		for x in range(WIDHT):
			for y in range(HEIGHT):
				v = bord[x-1][y-1] + bord[x][y-1] + bord[x+1][y-1] + bord[x-1][y]   +                bord[x+1][y]   +bord[x-1][y+1] + bord[x][y+1] + bord[x+1][y+1]
				if bord[x][y]:
					if v < 2 or v > 3:
						newbord[x][y]=0
				else:
					if v == 3:
						newbord[x][y]=1
		screen.fill((0,0,0))
		for x in range(WIDHT):
			for y in range(HEIGHT):
				bord[x][y] = newbord[x][y]
				if bord[x][y]:
					pygame.draw.rect(screen,(255,255,255),(x*TILESIZE,y*TILESIZE,TILESIZE,TILESIZE))

		pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode(SIZE)
	loop()
	pygame.quit()