import timeit
dic = {}
arr = [0 for x in range(10)]
for x in range(10):
	dic["".join([str(x),"hay"])]=x
	arr[x] = x
print(dir(dic))
def t():
	for k,i in dic.iteritems():
		pass
def t2():
	for i in arr:
		pass
print(timeit.timeit(t))
print(timeit.timeit(t2))