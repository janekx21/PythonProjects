import pygame,pygame.locals,sys,os,math
SIZE = (400,300)
WHITE = (255,255,255)
BLACK = (0,0,0)


ill = 0
t = 0
class pos:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.s = 1
offset = pos()

def apperation(x,y,r,i):
	global ill,offset,t
	if r <=1 or r > 80:
		return
	color = pygame.Color(0,0,0,0)
	color.hsva = i*30%360,100,100,0
	pygame.draw.circle(screen,color,(int(x+SIZE[0]//2),int(y+SIZE[1]//2)),r,1)
	ill+=1
	if ill>100:
		pass
	apperation(x+offset.x+10+math.sin(t/4.0),y+offset.y-i*i,r-6,i+1)
	apperation(x-offset.x-10,y+offset.y-i*i+math.cos((t-i)/6.0)*15,r-10,i+1)
	apperation(x-offset.x*math.sin((t+i*2)/5.0),y+offset.y,r-10,i+2)
def loop():
	global ill,offset,t
	while True:
		clock.tick(60)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return
		mpos = pygame.mouse.get_pos()

		if pygame.mouse.get_pressed()[0]:
			pass
		if pygame.key.get_pressed()[pygame.K_DOWN]:offset.y+=1
		if pygame.key.get_pressed()[pygame.K_UP]:offset.y-=1
		if pygame.key.get_pressed()[pygame.K_RIGHT]:offset.x+=1
		if pygame.key.get_pressed()[pygame.K_LEFT]:offset.x-=1
		screen.fill(BLACK)
		ill = 0
		t+=1
		apperation(0,0,50,0)
		pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(SIZE)
	loop()
	pygame.quit()