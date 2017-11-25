import sys,os
if len(sys.argv) >2:
	print(sys.argv[1])
	print("replace encode start")
	data = ""
	with open(sys.argv[1],"rb") as f:
		data = f.read()
	print("data manipulation")
	ata = []
	for i,b in enumerate(data):
		print("{} von {}".format(i,len(data)))
		ata.append((ord(b)+1)%256)
	fata = ""
	for item in ata:
		fata+=chr(item)
	with open(sys.argv[2],"wb") as f:
		f.write(fata)