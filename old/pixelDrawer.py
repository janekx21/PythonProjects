import pygame as pygame
from pygame.locals import * 
import sys
from Tkinter import *
#import Tkinter
import tkFileDialog

pygame.init()
ROOT = Tk()
ROOT.withdraw()

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
PINK = (255,0,255)
WHITE = (255,255,255)
GRAY = (127,127,127)
BLACK = (0,0,0)
DARK = (40,40,40)
BROWN = (70,40,40)
TRANSPARENT = (0,0,0,0)

COLORS = [RED,GREEN,BLUE,YELLOW,CYAN,PINK,BROWN,BLACK,WHITE,GRAY]
CURRENTCOLOR  = 0

DISPLAYSIZE = (600,600)
DRAWSIZE = (32,32)
UISIZE = (16,16)
SCREEN = pygame.display.set_mode(DISPLAYSIZE,RESIZABLE)
DISPLAYSIZE = SCREEN.get_size()
UISURF = pygame.Surface(UISIZE, pygame.SRCALPHA)
DRAWSURF = pygame.Surface(DRAWSIZE, pygame.SRCALPHA)
DRAWSURF.fill(TRANSPARENT)
UISURF.fill(TRANSPARENT)
LASTMOUSEPOS = (0,0)
PINSELSIZE = 1

FLAG = True

def soroundPoint(x,y):
	global FLAG
	if DRAWSURF.get_at((x,y)) == COLORS[CURRENTCOLOR]:
		if x < DRAWSIZE[0]-1:
			if DRAWSURF.get_at((x+1,y)) == TRANSPARENT:
				DRAWSURF.set_at((x+1,y),COLORS[CURRENTCOLOR])
				FLAG = True
		if x > 0:
			if DRAWSURF.get_at((x-1,y)) == TRANSPARENT:
				DRAWSURF.set_at((x-1,y),COLORS[CURRENTCOLOR])
				FLAG = True
		if y < DRAWSIZE[1]-1:
			if DRAWSURF.get_at((x,y+1)) == TRANSPARENT:
				DRAWSURF.set_at((x,y+1),COLORS[CURRENTCOLOR])
				FLAG = True
		if y > 0:
			if DRAWSURF.get_at((x,y-1)) == TRANSPARENT:
				DRAWSURF.set_at((x,y-1),COLORS[CURRENTCOLOR])
				FLAG = True

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.key.get_mods() and pygame.KMOD_SHIFT:
				if event.button == 5:
					PINSELSIZE +=1
				if event.button == 4:
					PINSELSIZE -=1
				if PINSELSIZE<=0:
					PINSELSIZE = 1
			else:
				if event.button == 5:
					CURRENTCOLOR+=1
				if event.button == 4:
					CURRENTCOLOR-=1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSPACE:
				DRAWSURF.fill(TRANSPARENT)
			if event.key == pygame.K_F1:
				dir = tkFileDialog.asksaveasfilename(initialdir = "",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
				if dir:
					pygame.image.save(DRAWSURF,dir)

			if event.key == pygame.K_F2:
				dir = tkFileDialog.askopenfilename()
				if dir:
					DRAWSURF = pygame.image.load(dir)
	mouse_pos = pygame.mouse.get_pos()
	pix_pos = (mouse_pos[0]*DRAWSIZE[0]/DISPLAYSIZE[0],mouse_pos[1]*DRAWSIZE[1]/DISPLAYSIZE[1])
	ui_pos = (mouse_pos[0]*UISIZE[0]/DISPLAYSIZE[0],mouse_pos[1]*UISIZE[1]/DISPLAYSIZE[1])
	
	SCREEN.fill(DARK)
	
	if pygame.mouse.get_pressed()[0]:
		if pygame.key.get_pressed()[pygame.K_SPACE]:

			if ui_pos[1] < 1:
				CURRENTCOLOR =  ui_pos[0]
			elif ui_pos[0] < 1:
				PINSELSIZE = ui_pos[1]
		else:
			pygame.draw.line(DRAWSURF,COLORS[CURRENTCOLOR],pix_pos,LASTMOUSEPOS,PINSELSIZE)
			pygame.draw.circle(DRAWSURF,COLORS[CURRENTCOLOR],pix_pos,PINSELSIZE//2)
	FLAG = True
	while FLAG:
		FLAG = False
		if pygame.mouse.get_pressed()[1]:
			for x in range(0,DRAWSIZE[0]):
				for y in range(0,DRAWSIZE[1]):
					soroundPoint(x,y)
			for x in range(DRAWSIZE[0]-1,0,-1):
				for y in range(0,DRAWSIZE[1]):
					soroundPoint(x,y)
			for x in range(0,DRAWSIZE[0]):
				for y in range(DRAWSIZE[1]-1,0,-1):
					soroundPoint(x,y)
			for x in range(DRAWSIZE[0]-1,0,-1):
				for y in range(DRAWSIZE[1]-1,0,-1):
					soroundPoint(x,y)
	if CURRENTCOLOR > len(COLORS)-1:
		CURRENTCOLOR = 0
	if CURRENTCOLOR < 0:
		CURRENTCOLOR = len(COLORS)-1
	if pygame.mouse.get_pressed()[2]:
		DRAWSURF.set_at(pix_pos,TRANSPARENT)
	UISURF.fill((0,0,0,0))
	for i,color in enumerate(COLORS):
		UISURF.set_at((i,0),COLORS[i])
	UISURF.set_at((CURRENTCOLOR,1),WHITE)
	UISURF.set_at((0,PINSELSIZE),WHITE)
	buf = pygame.transform.scale(DRAWSURF, DISPLAYSIZE)
	SCREEN.blit(buf,(0,0))
	if pygame.key.get_pressed()[pygame.K_SPACE]:
		buf = pygame.transform.scale(UISURF, DISPLAYSIZE)
		SCREEN.blit(buf,(0,0))#,None, pygame.BLEND_RGBA_ADD)
	pygame.display.flip()
	if not pygame.key.get_mods() and pygame.KMOD_SHIFT:
		LASTMOUSEPOS = pix_pos
