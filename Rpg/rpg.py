import pygame,sys
from vector import *
class Entety(pygame.sprite.Sprite):
    def __init__(s,pos):
        pygame.sprite.Sprite.__init__(s)
        s.position = Vector(pos[0],pos[1])
        s.hp = 100
        s.damage = 10
        s.direction = Vector(0,0)
        s.velocity = Vector(0,0)
        s.friction = 0.0
        s.image = pygame.image.load("entety.png")
        s.rect = s.image.get_rect()
        s.add(sprites)
    def update(s):
        s.velocity *= 1.0 - s.friction
        s.position += s.velocity
        s.rect.x = s.position.x - offset.x
        s.rect.y = s.position.y - offset.y
    def addForce(s,force):
        s.velocity += force#
    def die(s):
        s.kill()
        del(s)
class Enemy(Entety):
    def __init__(s,position):
        Entety.__init__(s,position)
        s.image = pygame.image.load("cirlcle.png")
        s.rect = s.image.get_rect()
        s.addForce(Vector(1,10))
        s.friction = .1
        s.timer = 0
    def update(s):
        Entety.update(s)
        s.timer+=1
        if s.timer%40 == 0:
            s.addForce((player_position-s.position).normalize()*4.0)
        if s.timer > 500:
            print("defedet by time")
            s.die()
class SpriteEntety(Entety):
    def __init__(s,position):
        Entety.__init__(s,position)
        s.image = pygame.image.load("cirlcle.png")
        s.rect = s.image.get_rect()
    def update(s):
        Entety.update(s)

class Player(Entety):
    def __init__(s):
        Entety.__init__(s,Vector(0,0))
        s.image = pygame.image.load("cirlcle.png")
        s.rect = s.image.get_rect()
        s.position = player_position
    def update(s):
        s.position = player_position
        s.rect.x = s.position.x - offset.x - 16
        s.rect.y = s.position.y - offset.y - 16
def spawn(obj):
    global objects
    objects.append(obj)
def draw(offset):
    scale = 64
    for i in range(0,WIDTH/scale+scale):
        a = Vector(i*scale-offset.x%scale,0)
        b = Vector(i*scale-offset.x%scale,HEIGHT)
        pygame.draw.line(display,(200,2,3),a,b)
    for i in range(0,HEIGHT/scale+scale):
        a = Vector(0,i*scale-offset.y%scale)
        b = Vector(WIDTH,i*scale-offset.y%scale)
        pygame.draw.line(display,(200,2,3),a,b)
    #for i in range(0,WIDTH/scale):
            #   a = Vector(-offset.x+i*32,-offset.y)
            #    b = Vector.lerp(a,Vector(WIDTH/2,HEIGHT/2),.5)
                #    pygame.draw.line(display,(200,2,3),a,b)

        pos = player_position-offset
        pygame.draw.circle(display,(10,20,30),(int(pos.x),int(pos.y)),8)
        #for obj in objects:
         #   obj.draw(display,offset)
def update(events):
    global player_position,player_speed,keys
    #for event in events
    move = Vector(0,0)
    if pygame.K_LEFT in keys:
        move.x -= player_speed
    if pygame.K_RIGHT in keys:
        move.x += player_speed
    if pygame.K_UP in keys:
        move.y -= player_speed
    if pygame.K_DOWN in keys:
        move.y += player_speed
    #   print(event.key)
    cursor = move
    if move.x != 0 or move.y != 0:
        move = move.normalize()
    move *= player_speed
    player_position+= move
    #for obj in objects:
    #    obj.update(events)
WIDTH = 280
HEIGHT = 160

#player = {}
player_position = Vector(0,0)
player_speed = 5
#cam = {}
cam_position = Vector(0,0)

display = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('RPG')
clock = pygame.time.Clock()

keys = []
pressed = []
released = []
cursor = Vector(0,0)
mode = "play"
objects = []
sprites = pygame.sprite.Group()
offset = Vector(0,0)
player = Player()
"""
for x in range(0,100):
    se = SpriteEntety(Vector((x%5)*32,(x/5)*32))
"""
while mode == "play":
    clock.tick(60)
    print(clock.get_fps())
    #print(se)
    display.fill((255,255,255))
    events = pygame.event.get()
    relesed = []
    pressed = []
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key not in keys:
                keys.append(event.key)
            pressed.append(event.key)
            if event.key == pygame.K_ESCAPE:
                mode = "stop"
            if event.key == pygame.K_SPACE:
                spawn(Enemy((0,0)))
        if event.type == pygame.QUIT:
            mode = "stop"
        if event.type == pygame.KEYUP:
            if event.key in keys:
                keys.remove(event.key)
            relesed.append(event.key)
    update(events)
    if pygame.K_SPACE in keys:
        spawn(Enemy((0,0)))
    cam_position = Vector.lerp(cam_position,player_position,.1)
    offset = Vector(cam_position.x-WIDTH/2,cam_position.y-HEIGHT/2)
    #draw(offset)
    sprites.update()
    sprites.draw(display)
    pygame.display.update()
pygame.quit()
sys.exit()
