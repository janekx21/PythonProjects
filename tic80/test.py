class Go:
	def __init__(s,x,y):
		s.x = x
		s.y = y
	def update(s):
		s.x+=1


def init():
	go = Go(0,0)
init()

def TIC():
	go.update()
	print(go.x)