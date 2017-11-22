import pygame, sys
from pygame.locals import *
from vector import Vector

DEBUG = True
WIDTH = 200
HEIGHT = 150

class Obj(object):                              #Obj
    def __init__(self,pos):
        if type(pos) == type(Vector):
            self.pos = pos
        else:
            self.pos = Vector(pos[0],pos[1])         #Position
        self.canCollide = True  #Collision
        self.direction = Vector.ZERO() #Direction
        self.vel = Vector()
        self.acc = Vector()
        self.speed = 0.0          #Speed
        #Rect --
        self.size = Vector(0,0)
        self.rect = Rect(self.pos,self.size)
        #Appanding
        objects.append(self)
        self.create()           #Create

    def create(self):
        print("Obj createt")
 
    def draw(self):
        return True
        
    def update(self):
        return True

    def update_p(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector()
        
    def addForce(self,v):
        self.acc += v
    def move(self,direction,sp):
        if type(direction) != type(Vector):
            direction = Vector(direction[0],direction[1])
        direction = direction.normalize()
        self.pos += direction*sp


    def collide(self,other):
        if DEBUG:
            #print(self.__class__.__name__+"\t Coll \t"+other.__class__.__name__)
            #print(self.rect)
            #print(other.rect)
            return
    def getRect(self):
        return self.rect
        
class Player(Obj):                  #Player
    def create(self):
        self.rect = Rect(self.pos,(30,30))
        self.speed = 2
        self.shootTimer = 0
        
    def draw(self):
        if DEBUG:
            pygame.draw.rect(DISPLAYSURF,BLACK,self.rect,1)
        
        pygame.draw.circle(DISPLAYSURF, RED, (int(self.pos.x)+15,int(self.pos.y)+15),15, 0)

    def update(self):
        for key in keys:
            self.prosses(key)
        if self.shootTimer > 0:
            self.shootTimer -= 1
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.vel*=.8
        if self.vel.magnetude() > 2:
            
            self.vel.normalize()*2
        self.update_p()
    def prosses(self,key):
        mov = Vector(0.0,0.0)
        if key == K_UP:
            mov +=Vector(0.0,-1.0)
        elif key == K_DOWN:
            mov +=Vector(0.0,1.0)
        elif key == K_RIGHT:
            mov +=Vector(1.0,0.0)
        elif key == K_LEFT:
            mov +=Vector(-1.0,0.0)
        elif key == K_SPACE:
            if self.shootTimer <= 0:
                self.shoot()
        mov*=.6
        self.addForce(mov)
    def shoot(self):
        bullet = Bullet(self.rect.center)
        bullet.addForce(self.vel.normalize()*3)
        self.shootTimer = 20


class Bullet(Obj):                  #Bullet
    def create(self):
        self.speed = 1
        #self.direction = (1.0,.1)
        self.rect = Rect(self.pos.values,(8,8))
        
    def draw(self):
        if DEBUG:
            pygame.draw.rect(DISPLAYSURF,BLACK,self.rect,1)
        pygame.draw.circle(DISPLAYSURF,BLUE,(int(self.pos.values[0])+4,int(self.pos.values[1])+4),4,1)
    def update(self):
        self.update_p()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        if self.pos.values[0] > WIDTH +30:
            self.kill()
    def kill(self):
        objects.remove(self)

class Enemy(Obj):
    def create(self):
        self.hp = 100
        self.size = Vector(20,20)
        self.rect = Rect(self.pos,self.size)

    def draw(self):
        if DEBUG:
            pygame.draw.rect(DISPLAYSURF,BLACK,self.rect,1)
        pygame.draw.circle(DISPLAYSURF,GREEN,(int(self.pos.values[0])+10,int(self.pos.values[1])+10),10,3)
    def update(self):
        dira = player.pos - self.pos

        self.move(dira,.3)
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

# Code Beginns
pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Small Game')
clock = pygame.time.Clock()

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# draw on the surface object
"""
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 200, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[380][280] = BLACK
pixObj[382][282] = BLACK
pixObj[384][284] = BLACK
pixObj[386][286] = BLACK
pixObj[388][288] = BLACK
del pixObj
"""

objects = []
keys = []
enemys = [1]
player = Player((50,50))
enemys[0] = Enemy((2,3))

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key== K_ESCAPE:
                pygame.quit()
                sys.exit()
            keys.append(event.key)
            if DEBUG:
                print("down:"+pygame.key.name(event.key)+" id:"+str(event.key))
        elif event.type == KEYUP:
            keys.remove(event.key)
            if DEBUG:
                print("up:"+pygame.key.name(event.key)+" id:"+str(event.key))           
    DISPLAYSURF.fill(WHITE)
    for obj in objects:
        obj.update()
        obj.draw()
        if obj.canCollide:
            for other in objects:
                if other.__class__.__name__ != "Bullet":
                    if other.canCollide:
                        if other!=obj:
                            tmp=obj.getRect().colliderect(other.getRect())
                            #print(objects.index(obj))
                            #print(objects.index(other))
                            #print("a:"+obj.__class__.__name__+"+b:"+other.__class__.__name__+"="+str(tmp))
                            if tmp:
                                obj.collide(other)
                                #print(objects.index(obj))
                                #print(objects.index(other))
    pygame.display.update()
    clock.tick(60)
    pygame.display.set_caption("fps:"+str(clock.get_fps()))
