from struct import *
name = "janek"
hp = 249
lives = 3
level = 12
el = "abcde\t"
save = pack('<5sIBB6s', name,hp, lives,level,el)
with open("pass.dat", "wb") as f:
	f.write(save)
with open("pass.dat","rb") as f:
	r = f.read()
	print(r)
	print(unpack('<5sIBB6s',r))