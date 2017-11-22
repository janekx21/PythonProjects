from timeit import *
from pygame import *
init()
screen = display.set_mode((200,200))
dec = [(0,0),(1,1),(2,2),(3,3)]
def opperation(item):
	x,y = item
	screen.set_at(item,(x%255,y%255,255))
	display.flip()
	

def thing():
	arr = [(x,y) for x in range(100)for y in range(100)]
	a = map(opperation,arr)
	#return a
t = Timer(thing)
print(t.timeit(1))
#15.1629209518 pass
#27.8554160595 -x,-y
#23.8336319923 if
#49.5885369778 arr inner 
#39.541834116 arr outer


#1 mal draw pix 4.81446814537
#1 mal pix in for 5.33459496498
#1 mal pix in map 5.44678997993