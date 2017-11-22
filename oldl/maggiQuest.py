import pygame, sys
from pygame.locals import *

pygame.init()

#DISPLAYSURF = pygame.display.set_mode((0, 0),0,32)# pygame.FULLSCREEN, 32)
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32)
pygame.display.set_caption('Maggi Quest')
INFO = pygame.display.Info()
WIDTH =INFO.current_w
HEIGTH =INFO.current_h

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def inter(a,b,val):
	assert type(a) == type(b)
	if type(a) == type((0,0)):
		return (b[0]-a[0])*val+a[0],(b[1]-a[1])*val+a[1]

class Point(object):
	def __init__(s,pos):
		s.x = pos[0]
		s.y = pos[1]
		#print "new Point at" + str(pos)
	def draw(s,display):
		pygame.draw.circle(display, BLUE, (int(s.x), int(s.y)), 20, 0)
	def drawSmall(s,display):
		pygame.draw.circle(display, GREEN, (int(s.x), int(s.y)), 2, 0)
def draw():
	
	lastPoint = False
	points2 = []
	for point in points:
		point.draw(DISPLAYSURF)
		if lastPoint:
			pygame.draw.line(DISPLAYSURF, RED,(point.x,point.y), (lastPoint.x,lastPoint.y), 4)
			pos2 = inter((point.x,point.y), (lastPoint.x,lastPoint.y),polateVal)
			points2.append(Point(pos2))
		lastPoint = point
	lastPoint = False
	points3 = []
	for point in points2:
		#point.draw(DISPLAYSURF)
		if lastPoint:
			#pygame.draw.line(DISPLAYSURF, RED,(point.x,point.y), (lastPoint.x,lastPoint.y), 4)
			pos2 = inter((point.x,point.y), (lastPoint.x,lastPoint.y),polateVal)
			points3.append(Point(pos2))
		lastPoint = point
	lastPoint = False
	pointsStay = []
	for point in points3:
		#point.draw(DISPLAYSURF)
		if lastPoint:
			#pygame.draw.line(DISPLAYSURF, RED,(point.x,point.y), (lastPoint.x,lastPoint.y), 4)
			pos2 = inter((point.x,point.y), (lastPoint.x,lastPoint.y),polateVal)
			#pygame.draw.circle(DISPLAYSURF, GREEN, (int(pos2[0]),int(pos2[1])), 2, 0)

			pointsStay.append(Point(pos2))
		lastPoint = point
	lp = False
	for poi in pointsStay:
		if type(lp) !=bool:
			pass
		#	pygame.draw.line(DISPLAYSURF, GREEN,(0,0), (lastPoint.x,lastPoint.y), 2)
			#pygame.draw.circle(DISPLAYSURF, RED, (int(lp.x), int(lp.y)), 2, 0)
		lp = poi
		poi.drawSmall(DISPLAYSURF)
		
############################
loops = True
points = []
pointsStay = []
polateVal = .5
keys = []
grabing = False
points.append(Point((WIDTH/6,HEIGTH/5)))
points.append(Point((WIDTH*.8,HEIGTH/5)))
points.append(Point((WIDTH/6,HEIGTH*.8)))
points.append(Point((WIDTH*.8,HEIGTH*.9)))

if __name__ == "__main__":
	while loops:
		DISPLAYSURF.fill(WHITE)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	 		if event.type == KEYDOWN:
	 			if not event.key in keys:
	 				keys.append(event.key)
	 			if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == KEYUP:
				if event.key in keys:
	 				keys.remove(event.key)
			if event.type == MOUSEBUTTONDOWN:
				pass
				#points.append(Point(pygame.mouse.get_pos()))
		if K_1 in keys:
			polateVal+=.01
		if K_2 in keys:
			polateVal-=.01
		if pygame.mouse.get_pressed()[0]:
			if grabing:
				grabing.x = pygame.mouse.get_pos()[0] 
				grabing.y = pygame.mouse.get_pos()[1] 
			else:
				for point in points:
					if pygame.mouse.get_pos()[0] > point.x-16 and pygame.mouse.get_pos()[0] <point.x+16:
						if pygame.mouse.get_pos()[1] > point.y-16 and pygame.mouse.get_pos()[1] <point.y+16:
							grabing = point
		else:
			grabing = False
		MAX = 100
		val = .0
		for i in xrange(0,MAX):
			val = float(i)/float(MAX)
			#print val
			polateVal = val
			draw()
		pygame.display.update()