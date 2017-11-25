import sys,os
from pygame import *

if len(sys.argv) == 1:
	print("wrong args")
	print("arg1: dir to combine")
	#sys.exit()
	dire = ""
else:
	dire = sys.argv[1]
print("dir name: {}".format(dire))

lis = os.listdir(os.path.join("./",dire))
print(lis)
pics = []
for f in lis:
	post = os.path.basename(f).split(".")[-1]
	if post == "png":
		print(f)
		try:
			pics.append(image.load(f))
		except:
			pass
rx,ry = 0,0
rec = None
for p in pics:
	x,y = p.get_size()
	print(x,y)
	if x > rx:
		rec = p
		rx = x
	if y > ry:
		rec = p
		ry = y
print("record:",rx,ry)

s = Surface((rx*len(pics),ry))
for x,p in enumerate(pics):
	s.blit(p,(x*rx,0))

image.save(s,"global.png")

