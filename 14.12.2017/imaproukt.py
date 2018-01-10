from pygame import *
import pygame.camera
import math as mathf

SIZE = (128,128)
REALSIZE = (400,400)

init()
pygame.camera.init()
cams = pygame.camera.list_cameras()
print(cams)
if len(cams) > 0:
	cam = pygame.camera.Camera(cams[0],SIZE)
	print(cam.get_size())
	cam.start()

# \_____/
#    |
#    |
#    |
#    V
#=========
#---------



screen = display.set_mode(REALSIZE)
 
drawer = Surface(SIZE)
urface = Surface((32,32))
loop = True
t = 0
clock = time.Clock()

cursor = 0
lastshoot = 0
dots = []

while loop:
	t+=1
	lastshoot+=1
	clock.tick(60)
	for e in event.get():
		if e.type == QUIT:
			loop = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				loop = False
			else:
				if lastshoot > 30:
					dots.append((cursor,32+4))
					lastshoot=0
	for i,d in enumerate(dots):
		x,y = d
		if y < 64:
			dots[i] = x,y+2
		elif y < 64+42:
			dots[i] = x,y+1
		else:
			dots[i] = x+1,y

	drawer.fill((0,0,0))
	if t % 10 == 0:
		b = transform.scale(cam.get_image(),(128,128))
		urface.blit(b,(-64+16,-64+16))
	cursor = mathf.sin(t/100.0)*32+64
	draw.circle(drawer,(255,255,255),(int(cursor),8),32)
	draw.rect(drawer,(255,255,255),(cursor-8,0,16,32+16))
	for i in range(16):
		ntime = t//1.15
		x = i*128//8 + (ntime)%(128//4)-16
		od = i%2==0
		if od:
			draw.line(drawer,(255,255,255),(x//.8-8,128),(x,128-32))
		else:
			for j in range(128//8):
				draw.line(drawer,(255,255,255),((x-j)//.8-8,128),((x-j),128-32))

	for d in dots:
		x,y = d
		#draw.circle(drawer,(255,255,255),(int(x),int(y)),6)
		drawer.blit(urface,(int(x)-16,int(y)-16))
		draw.rect(drawer,(255,255,255),(int(x)-16,int(y)-16,32,32),1)
	screen.blit(transform.scale(drawer,REALSIZE),(0,0))
	display.flip()