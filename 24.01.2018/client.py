import socket
import thread
client = socket.socket()
client.connect(("localhost",8012))
print(client)
debug = ""
def recive(sock):
	global debug
	debug+=">"+sock.recv(1024) + " -\n"
thread.start_new_thread(recive,(client,))
#def send(sock):
#thread.start_new_thread(send,(client,))
while 1:
	if debug!="":
		print(debug)
		debug = ""
	client.sendall(raw_input())