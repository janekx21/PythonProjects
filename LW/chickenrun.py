import pygame,pygame.locals,sys,random,time
pygame.init()
SIZE = (400,300)
screen = pygame.display.set_mode(SIZE)

class Block(object):
	blocks = []
	sidespeed = 2
	def __init__(self,y):
		self.y = y
		self.x = 400
		self.rect = pygame.Rect(400,y,32,32)
		self.blocks.append(self)
	def draw(self,screen):
		pygame.draw.rect(screen,(0,255,255),self.rect)
	def update(self):
		self.rect.x -= self.sidespeed
		if self.rect.x +64 < 0:
			self.blocks.remove(self)
		if self.rect.colliderect(chicken.rect):
			self.blocks.clear()
	def updateall(screen):
		for block in Block.blocks:
			block.update()
			block.draw(screen)
	def spawn():
		rnd = random.randrange(0,3)
		Block(200-rnd*50)

class chicken:
	rect = pygame.Rect(50,200,32,32)
	vx =0
	vy =0
	canjump = False
	def update():
		if chicken.vy < 0:
			chicken.vy += .18
		else:
			chicken.vy += .22
		if chicken.rect.y+chicken.vy >= 200:
			chicken.vy = 0
			chicken.rect.y = 200
			chicken.canjump = True
		chicken.rect.x+=chicken.vx
		chicken.rect.y+=chicken.vy
	def draw(screen):
		pygame.draw.rect(screen,(244,0,0),chicken.rect)
	def jump():
		if chicken.canjump:
			chicken.vy = -8
			chicken.rect.y -=1
			chicken.canjump = False

def key(k):
	if k == pygame.K_SPACE:
		chicken.jump()
clock = pygame.time.Clock()
ltime = time.time()+2
while True:
	clock.tick(120)#------<<<<
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			key(event.key)
	if time.time()>ltime:
		Block.spawn()
		ltime = time.time()+random.uniform(.3,1.6)
	chicken.update()
	screen.fill((255,255,255))
	Block.updateall(screen)
	chicken.draw(screen)
	pygame.display.flip()