import socket
import thread
from pygame import *

BREAK = ";"

#print(socket.socket.__doc__)
server = socket.socket()
server.bind(("",8012))

server.listen(4)

def handle(sock,addr):
	global debug,screen
	while 1:
		r = sock.recv(1024)
		split = r.split(BREAK)
		if split[0] == "cls":
			screen.fill((int(split[1]),int(split[2]),int(split[3])))
		elif split[0] == "pix":
			screen.set_at()


def look(server):
	global debug
	while 1:
		sock,addr = server.accept()
		debug += repr(sock) + "\n"
		thread.start_new_thread(handle,(sock,addr))


debug = ""

thread.start_new_thread(look,(server,))
init()
screen = display.set_mode((400,300))
loop = True
while loop:
	for e in event.get():
		if e.type == QUIT:
			loop = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				loop = False
	display.flip()
	if debug != "":
		print(debug)
		debug = ""
server.shutdown(1)
server.clear()
