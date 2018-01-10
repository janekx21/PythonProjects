from pygame import *
import random
import sys

#Screen Size of the Window
WIDTH = 600
HEIGHT = 400
SIZE = (WIDTH,HEIGHT)
init() #init pygame
screen = display.set_mode(SIZE) #make window

class WorldBlock: #a Block in the world
	def __init__(self):
		self.color = (random.randrange(0,255),
			random.randrange(0,255),
			random.randrange(0,255))
		self.destcolor = None
	def update(self):
		pass
BLOCKSIZE = 64 #Block Side size
MAPWIDTH = WIDTH//BLOCKSIZE+1
MAPHEIGHT = HEIGHT//BLOCKSIZE+1

#init the world array with WorldBlocks
world = [[WorldBlock() for y in range(MAPHEIGHT)] for x in range(MAPWIDTH)]

def VecToTuple(vec):
	return vec.x,vec.y
def VecToIntT(vec):
	return int(vec.x),int(vec.y)
def clamp(ma,mi,v):
	max()

class Entety: #All doing Entety
	entetys = [] #Entety Batch
	dielist = [] #Dying EntetyBathc in the frame

	maxlivetime = -1

	def __init__(self, pos):
		if type(pos) == tuple: # Positioning ...
			self.pos = math.Vector2(pos[0],pos[1])
		elif type(pos) == math.Vector2:
			self.pos = pos
		else:
			print("default pos")
			self.pos = math.Vector2(0,0)
		self.time = 0 #Tim alive
		self.direction = 0 #facing dircetion
		self.entetys.append(self) #add this to entety batch
	def update(self):
		self.time += 1
		if self.time > self.maxlivetime and self.maxlivetime>0:
			self.die() #if live time is over
	def draw(self,screen):
		pass #stdDraw
	def die(self):
		self.dielist.append(self) #add to dying batch

class Sheep(Entety):
	def __init__(self, pos):
		Entety.__init__(self,pos)
	def update(self):
		Entety.update(self)
		mov = math.Vector2(1,0) #moving dirction as vector
		mov.rotate_ip(self.direction) #rotate the direction by degree
		self.pos+=math.Vector2(mov.x,mov.y)
		self.direction+=random.randrange(-5,6) #add a random direction
		if self.pos.x < 0 or self.pos.x > WIDTH: #if colliding with wall
			self.direction += 180 #turn arround
		if self.pos.y < 0 or self.pos.y > HEIGHT:
			self.direction += 180
	def draw(self,screen):
		draw.circle(screen,(255,0,0),VecToIntT(self.pos),20)

class Tree(Entety):
	def __init__(self,pos):
		Entety.__init__(self,pos)
	def draw(self,screen):
		draw.circle(screen,(0,255,0),VecToIntT(self.pos),10)
	def update(self):
		Entety.update(self)
		ix = int(self.pos.x // BLOCKSIZE)
		iy = int(self.pos.y // BLOCKSIZE)
		global world
		r,g,b = world[ix][iy].color
		r = math.clamp(r-1,0,255)
		world[ix][iy].color = (r,g,b) 
		#setting the unterliing block a color



Sheep((20,30))
looping = True #if game is looping (Played)
clock = time.Clock()
while looping:
	clock.tick(60) #60 fps lock
	for e in event.get():
		if e.type == QUIT:
			looping = False
		if e.type == KEYDOWN:
			if e.key == K_SPACE: #Space key pressed?
				if random.randrange(0,2)==0:
					#spawn sheep
					Sheep((WIDTH//2,HEIGHT//2))
				else:
					#spawn tree
					Tree((random.randrange(WIDTH),random.randrange(HEIGHT)))
	# update all Entetys
	for e in Entety.entetys:
		e.update() 
	screen.fill((255,255,255))
	# draw World Blocks
	for ix,xlist in enumerate(world):
		for iy,item in enumerate(xlist):
			draw.rect(screen,item.color,(ix*BLOCKSIZE,iy*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE))
	#draw all entetys
	for e in Entety.entetys:
		e.draw(screen)
	display.flip() # update display
	#remove dead entetys
	for e in Entety.dielist:
		Entety.entetys.remove(e)
	Entety.dielist = [] #reset dyed batch