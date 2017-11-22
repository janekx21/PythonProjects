import time,math

def add():
	a.append(10/1.0)
class test:
	def __init__(s):
		pass

t = time.time()
a = []
for i in range(1,100000):
	"""
	string = ""
	if i%3==0:
		string += "Fizz"
	if i%5==0:
		string += "Bizz"
	if string == "":
		string = str(i)
	print(string)
	"""
	#add()										#0.0285186767578125
	#a.append(10/1.0)							#0.016010284423828125
	#a.append(1/10)								#0.016510486602783203
	#b = 1/10									#0.01000833511352539
	#b = 10/1									#0.011006832122802734
	#b = math.pow(42,4)							#0.04353022575378418
	#if "oyo" == "maggi":						#0.008005380630493164
	#if "oyoyoyoyoyoyo" == "magimagimagimagu":	#0.008505582809448242
	#if 123 == 123:								#0.010007143020629883
	#if 123 < 123:								#0.008005380630493164
	#if 123 > 123:								#0.008006095886230469
	#pass										#0.005002737045288086
	#test()										#0.031520843505859375
	#b = "Guten Tag"							#0.010006427764892578
print(time.time()-t)

