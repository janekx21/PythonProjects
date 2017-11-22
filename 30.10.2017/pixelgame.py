import pygame,pygame.locals,sys,os

class player:
	sprite = pygame.image.load("pics/player.png")
	def __init__(self):
		self.x = 0
		self.y = 0
	def draw(self,app):
		speed = 2
		if pygame.key.get_pressed()[pygame.K_UP]:
			self.y -= speed
		if pygame.key.get_pressed()[pygame.K_DOWN]:
			self.y += speed
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			self.x -= speed
		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.x += speed
		if pygame.key.get_pressed()[pygame.K_SPACE]:
			enemy()
		#pygame.draw.circle(app.draw,(255,255,255),(self.x,self.y),16)
		app.draw.blit(self.sprite,(self.x,self.y))

class enemy:
	enemys = []
	sprite = pygame.image.load("pics/enemy.png")
	def __init__(self):
		self.x = -16
		self.y = 64
		self.enemys.append(self)
	def draw(self,app):
		self.x+=1
		#pygame.draw.circle(app.draw,(100,100,100),(int(self.x),int(self.y)),8)
		app.draw.blit(self.sprite,((int(self.x),int(self.y))))
		if self.x > app.width:
			self.die()
	def die(self):
		if self in self.enemys:
			self.enemys.remove(self)
	@staticmethod
	def loop(app):
		for enem in enemy.enemys:
			enem.draw(app)

class app:
	screen = None
	width = 256
	height = 144
	def loop(self):
		while True:
			self.clock.tick(60)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:return
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_ESCAPE:return
			self.draw.fill((20,20,20))
			enemy.loop(self)
			self.player.draw(self)
			b = pygame.transform.scale(self.draw,(self.size))
			self.screen.blit(b,(0,0))
			pygame.display.flip()
			self.time += 1
	def __init__(self):
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.size = self.screen.get_size()
		self.draw = pygame.Surface((self.width,self.height))
		self.player = player()
		self.time = 0
		self.clock = pygame.time.Clock()
		self.loop()

if __name__ == '__main__':
	lis =os.listdir("mods")
	print(lis)
	for mod in lis:
		execfile(os.path.join("mods",mod))
	pygame.init()
	app()
	pygame.quit()