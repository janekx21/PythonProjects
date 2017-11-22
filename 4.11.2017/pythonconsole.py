import pygame,pygame.locals,sys,time
from subprocess import Popen,PIPE,STDOUT

py = Popen(["python","-i"],stdin=PIPE,stdout=PIPE,stderr=STDOUT)
print(dir(py.stdin))
py.stdin.write("a = 126;")
py.stdin.flush()
py.stdin.write("print(a);")
py.stdin.flush()
time.sleep(.1)
py.stdin.close()

#print(py.communicate(""))
print(py.stdout.read())


while True:
	c = raw_input("->")
	if c == "exit":
		break
	print(py.communicate(c)[0])
	#print(py.stdin.write(c+"\n"))
	#py.stdin.flush()
	#print(py.stdout.read())
#py.stdout.flush()
#print(py.stdout.read())

#print(py.stdout.flush())
#print(py.stdout.readline())
#print(py.poll())
#if py.poll ==None:
#	py.kill()
print(py.poll())
print("FINISHED")
#print(py.stdout.read())