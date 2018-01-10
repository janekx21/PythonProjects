from pygame import *
SIZE = (200,200)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

class Entety:
	entetys = []
	dielist = []
	def __init__(self,pos):
		self.pos = pos
		self.entetys.append(self)
		self.hp = 8
		self.orginal_hp = self.hp
		self.time = 0
	def update(self):
		self.time+=1
	def draw(self,sceen):
		pass
	def draw_hp(self,sceen):
		x,y =self.pos
		p = float(self.hp) / self.orginal_hp
		draw.line(sceen,RED,(x,y),(x+int(p*32),y))
	def on_start(self):
		pass
	def on_end(self):
		pass
	def die(self):
		self.dielist.append(self)

	def check_collision(self):
		rect = Rect(self.pos,(32,32))
		for e in Entety.entetys:
			if e != self:
				if rect.colliderect(Rect(e.pos,(32,32))):
					self.collide(e)
					e.collide(self)

	def collide(self,other):
		pass

	@staticmethod
	def die_list():
		for e in Entety.dielist:
			Entety.entetys.remove(e)
		Entety.dielist = []
	@staticmethod
	def sort_by_y(a,b):
		return cmp(a.pos[1] , b.pos[1])


class Player(Entety):
	sprite = image.load("player.png")
	weaponsprite = image.load("sword.png")
	def __init__(self,pos):
		Entety.__init__(self,pos)
		self.swings = False
		self.swingTimer = 0
		self.dir = 0
		self.mov = 0,0
	def draw(self,sceen):
		x,y = self.pos
		sceen.blit(self.sprite,self.pos)
		if self.swings:
			if self.mov != (0,0):
				mx,my = self.mov
				b = transform.rotate(self.weaponsprite,self.dir*90)
				sceen.blit(b,(x+32*mx,y+32*my))
		self.draw_hp(sceen)
	def update(self):
		x,y = self.pos
		Entety.update(self)
		mx,my = 0,0
		if key.get_pressed()[K_LEFT]:
			mx-=1
			self.dir = 2
		if key.get_pressed()[K_RIGHT]:
			mx+=1
			self.dir = 0
		if key.get_pressed()[K_UP]:
			my-=1
			self.dir = 1
		if key.get_pressed()[K_DOWN]:
			my+=1
			self.dir = 3
		self.pos = x+mx,y+my
		self.mov = mx,my
		if key.get_pressed()[K_SPACE] and not self.swings:
			self.swing()
		if self.swingTimer >0:
			self.swingTimer-=1
		if self.swingTimer == 0:
			self.swings = False
			swingTimer = -1
		self.check_collision()
	def swing(self):
		self.swings = True
		self.swingTimer = 60
	def collide(self,other):
		print(other)
class Enemy(Entety):
	sprite = {}
	sprite[0] = image.load("enemy0.png")
	sprite[1] = image.load("enemy1.png")
	sprite["dead"] = image.load("enemydead.png")
	def __init__(self,pos):
		Entety.__init__(self,pos)
	def update(self):
		Entety.update(self)
	def draw(self,sceen):
		x,y = self.pos
		sceen.blit(self.sprite[self.time//15%2],self.pos)
		self.draw_hp(sceen)

class Tree(Entety):
	sprite = {}
	sprite[0] = image.load("tree0.png")
	sprite[1] = image.load("tree1.png")
	seeding = 0
	def __init__(self,pos):
		Entety.__init__(self,pos)
		self.seed = self.seeding%2
		Tree.seeding += 1
		self.hp = 160
		self.orginal_hp = self.hp
	def draw(self,sceen):
		sceen.blit(self.sprite[self.seed],self.pos)
		if self.hp != self.orginal_hp:
			self.draw_hp(sceen)
	def collide(self,other):
		if self.hp >0:
			self.hp-=1
		else:
			self.die()

init()
sceen = display.set_mode(SIZE)
SIZE = sceen.get_size()
loop = True
clock = time.Clock()

player = Player((0,0))
Enemy((64,64))
Tree((128,64))
Tree((92,32))
Tree((64,32))
Tree((92,64))
while loop:
	clock.tick(60)
	for e in event.get():
		if e.type == QUIT:
			loop = False
	for e in Entety.entetys:
		e.update()
	sceen.fill(WHITE)
	Entety.entetys.sort(Entety.sort_by_y)
	for e in Entety.entetys:
		e.draw(sceen)
	#print(Entety.entetys,"normal list")
	display.flip()
	Entety.die_list()