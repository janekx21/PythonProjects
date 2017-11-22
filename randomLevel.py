import time
import random
import sys
import array

import pygame as pygame
from pygame.locals import *

WIDTH = 400
HEIGHT = 400

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),RESIZABLE)# and pygame.FULLSCREEN)
SCREEN.fill((0,0,0))
WHITE = (255,255,255)
SCALE = 20

MAZE = []

ALPHA = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def drawMaze():
	global MAZE
	MAZE = []
	SCREEN.fill((0,0,0))
	for x in range(0,WIDTH//SCALE+1):
		for y in range(0,HEIGHT//SCALE+1):
			if random.randint(0,1) == 0:
				pygame.draw.line(SCREEN,WHITE,(x*SCALE,y*SCALE),(x*SCALE+SCALE,y*SCALE+SCALE))
				MAZE.append(True)
			else:
				pygame.draw.line(SCREEN,WHITE,(x*SCALE+SCALE,y*SCALE),(x*SCALE,y*SCALE+SCALE))
				MAZE.append(False)

def printMaze():
	st =""#= array.array("B")
	abstand = 6
	for i in range(len(MAZE)//abstand):
		tmp = ""
		for x in range(abstand):
			if MAZE[i*abstand+x]:
				tmp += "1"
			else:
				tmp += "0"
		index = int(tmp,2)
		if index > len(ALPHA)-1:
			index = 0
		#index = index % len(ALPHA)
		sys.stdout.write(ALPHA[index])
	print("->")
	#print(MAZE)



drawMaze()
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_F10:
				drawMaze()
			if event.key == pygame.K_F11:
				printMaze()
	
	pygame.display.flip()