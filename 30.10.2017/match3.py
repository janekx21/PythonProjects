import pygame,pygame.locals,sys,os,math

height = 10
width = 12
tilesize = 32
SIZE = (width*tilesize,height*tilesize)
WHITE = (255,255,255)

def basic(screen,pos):
	pygame.draw.rect(screen,(24,24,42),(pos,(tilesize,tilesize)))
def shroom(screen,pos):
	pygame.draw.rect(screen,(255,24,42),(pos,(tilesize,tilesize)))
def grass(screen,pos):
	pygame.draw.rect(screen,(12,255,42),(pos,(tilesize,tilesize)))
def berry(screen,pos):
	pygame.draw.rect(screen,(12,12,255),(pos,(tilesize,tilesize)))


draws = [basic,shroom,grass,berry]

def get(x,y):
	if x >= width:return -1
	if x < 0:return -1
	if y >= height:return -1
	if y < 0:return -1
	return bord[x][y]
def set(x,y,v):
	if x >= width:return -1
	if x < 0:return -1
	if y >= height:return -1
	if y < 0:return -1
	bord[x][y]=v
def flip(x,y,x2,y2):
	bord[x2][y2],bord[x][y]=bord[x][y],bord[x2][y2]


def loop():
	global selected,draw
	while True:
		clock.tick(60)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
		mpos = pygame.mouse.get_pos()

		if pygame.mouse.get_pressed()[0]:
			ix = mpos[0]//tilesize
			iy = mpos[1]//tilesize
			if not selected:
				selected = ix,iy
			else:
				if ix != selected[0] or iy != selected[1]:

					if abs(ix-selected[0])<=1 and abs(iy- selected[1])==0:
						print("Flip")
						flip(selected[0],selected[1],ix,iy)
						selected = None
					elif abs(iy- selected[1])<=1 and abs(ix-selected[0])==0:
						print("Flip")
						flip(selected[0],selected[1],ix,iy)
						selected = None
					else:
						selected = None

			turn(ix,iy)

		screen.fill(WHITE)
		for x,a in enumerate(bord):
			for y,b in enumerate(a):
				draws[b](screen,(x*tilesize,y*tilesize))
				v = get(x,y)
				if v!= 0:
					if get(x+1,y) == v and get(x-1,y)==v:
						set(x,y,0)
						set(x+1,y,0)
						set(x-1,y,0)
					if get(x,y+1) == v and get(x,y-1)==v:
						set(x,y,0)
						set(x,y+1,0)
						set(x,y-1,0)
				v = get(x,y)
				if v == 0:
					g = get(x,y-1)
					if g == -1:
						pass
					elif g != 0:
						set(x,y-1,0)
						set(x,y,g)
					#	pygame.draw.rect(screen,WHITE,(x*tilesize,y*tilesize,tilesize,tilesize),1)
		for x,a in enumerate(bord):
			for y,b in enumerate(a):
				if b == 0:
					set(x,0,random.randrange(0,len(draws)))
					
		if selected:
			ix = selected[0]
			iy = selected[1]
			pygame.draw.rect(screen,WHITE,(ix*tilesize,iy*tilesize,tilesize,tilesize),2)

		pygame.display.flip()
def turn(x,y):
	pass


if __name__ == '__main__':
	selected = None
	import random
	bord = [[random.randrange(0,len(draws)) for y in range(height)] for x in range(width)]
	bord[2][2] = 1
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(SIZE)
	loop()
	pygame.quit()