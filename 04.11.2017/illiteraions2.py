from timeit import *
def opperation(item):
	x,y = item
	if x %16 == 0:
		if y // 2==0:
			return x,y
	return 0,0



def thing():
	arr = [(x,y) for x in range(100)for y in range(100)]
	#a = map(opperation,arr)
	a = []
	for item in arr:
		a.append(opperation(item))
	return a
t = Timer(thing)
print(t.timeit(1000))
#21.3991959095
#36.1432909966 -x,-y
#29.3207800388 if