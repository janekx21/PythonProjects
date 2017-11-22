import time


def countdown():
	for i in range(10,0,-1):
		print(i)
		time.sleep(.5)

def start():
	print("JUHU")
	time.sleep(1)

def phase1():
	for x in range(1,1000):
		print("|||||")
		time.sleep(.01)
def phase2():
	for x in range(1,1000):
		print("|||")
		time.sleep(.01)

def endphase():
	print("^^")
	print("|o|")
	print("__")


countdown()
start()

phase1()

phase2()

phase1()

endphase()
