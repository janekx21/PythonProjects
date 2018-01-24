import thread
erg = []
num = 0
def thing(a):
	global num,erg
	for x in range(1000):
		x
	erg.append(a)
	num-=1
	return

print(dir(thread))
num += 1
thread.start_new_thread(thing,("abba",))
thread.start_new_thread(thing,("ajenj",))
thread.start_new_thread(thing,("ylil",))
while num >0:
	pass
print(erg)