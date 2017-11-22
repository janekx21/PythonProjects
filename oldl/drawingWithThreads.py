import pygame, sys
from pygame.locals import *
import random

import threading
from Queue import *

import sys

q = Queue()
threads = []

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def draw():
    
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
    q.put((0,0))
    q.join()
    
def start():
    t = threading.Thread(target=task)
    t.start()
    threads.append(t)
    print(threads)
    

def task():
    while True:
        item = q.get()
        if item == None:
            break
        
        r = random.Random()
        tmpa = 0
        tmpb = 0
        tmpa = r.randrange(0,400)
        tmpb = r.randrange(0,300)
        item = tmpa,tmpb
        q.task_done()
    
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_DOWN:
                start()
                
    draw()
    pygame.display.update()

