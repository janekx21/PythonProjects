import pygame ,pygame.locals, sys
pygame.init()

WIDTH = 400
HEIGHT = 300
DWIDHT = 40
DHEIGHT = 30
screen = pygame.display.set_mode((WIDTH,HEIGHT))
checker = pygame.Surface((WIDTH,HEIGHT))
draw = pygame.Surface((DWIDHT,DHEIGHT),pygame.SRCALPHA)
draw.set_alpha(0)

for x in range(WIDTH):
	for y in range(HEIGHT):
		if (y*WIDTH+x+y)%2==0:
			checker.set_at((x,y),(50,50,50))
		else:
			checker.set_at((x,y),(200,200,200))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	mpos = pygame.mouse.get_pos()
	screen.blit(checker,(0,0))
	if pygame.mouse.get_pressed()[0]:
		drawpos = (mpos[0]*DWIDHT//WIDTH,mpos[1]*DHEIGHT//HEIGHT)
		pygame.draw.circle(draw,(255,255,255),drawpos,0)
	if pygame.mouse.get_pressed()[2]:
		old = pygame.Surface((DWIDHT,DHEIGHT))
		old.blit(draw,(0,0))
		for x in range(DWIDHT):
			for y in range(DHEIGHT):
				if old.get_at((x,y)) == (255,255,255):
					pygame.draw.circle(draw,(0,0,0),(x,y),3 )
	tmp = pygame.transform.scale(draw,(WIDTH,HEIGHT))
	screen.blit(tmp,(0,0))
	pygame.display.flip()