from pygame import *
import random
SIZE = (600,400)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

def dubble(surf):
	x,y = surf.get_size()
	return transform.scale(surf,(x*2,y*2))

init()
sceen = display.set_mode(SIZE)
SIZE = sceen.get_size()
loop = True
clock = time.Clock()
px = SIZE[0]//2-16
py = 0
pspeed = 10
playersurf = [None,None]
playersurf[0] = image.load("player.png")
playersurf[1] = image.load("player2.png")
for i,surf in enumerate(playersurf):
	playersurf[i] = dubble(surf)
platformsurf = image.load("platform.png")
platformsurf = dubble(platformsurf)
enemys = []
dielist = []
t = 0
class Enemy:
	def __init__(self):
		self.x = random.randrange(0,SIZE[0])
		self.y = SIZE[1]
		self.speed = 5
		self.t = 0
		enemys.append(self)
	def draw(self,sceen):
		self.y -=self.speed
		sceen.blit(platformsurf,(self.x,self.y))
		self.t+=1
		if self.t > 120:
			self.die()
	def die(self):
		dielist.append(self)
while loop:
	clock.tick(60)
	for e in event.get():
		if e.type == QUIT:
			loop = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				loop = False
			if e.key == K_SPACE:
				pass
	if key.get_pressed()[K_SPACE]:
		px-=pspeed
	else:
		px+=pspeed
	if px > SIZE[0]-playersurf[0].get_size()[0]:
		px = SIZE[0]-playersurf[0].get_size()[0]
	if px < 0:
		px = 0
	if t %20==0:
		Enemy()
	sceen.fill(BLUE)
	for enemy in enemys:
		enemy.draw(sceen)
	sceen.blit(playersurf[t//30%2],(px,py))
	for obj in dielist:
		enemys.remove(obj)
	dielist = []
	display.flip()
	t+=1