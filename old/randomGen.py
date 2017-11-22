s = 0
def random():
	global s
	n = (31583115313513153153511*s+315331313841315373)%10
	s=n
	print(n)
	return n

for i in range(50):
	random()#1