from pygame import *
SIZE = (200,200)
screen = display.set_mode(SIZE)

characters = ["a","b","c","d",
"e","f","g","h","i","j","k",
"l","m","n","o","p","q","r",
"s","t","u","v","w","x","y","z"," "]

indexes = [97,98,99,100,101,102,
103,104,105,106,107,108,109,110,
111,112,113,114,115,116,117,118,
119,120,121,122,32]
text = [[]]
select = 0,0
fontpix = image.load("font.png")

def main():
	init()
	loop()

def loop():
	global text,select
	while True:
		sx,sy = select
		for e in event.get():
			if e.type == QUIT:
				return
			if e.type == KEYDOWN:
				if e.key == K_BACKSPACE:
					if sx == 0:
						text.pop(sy)
						sy-=1
						sx = len(text[sy])
					else:
						text[sy].pop(sx-1)
						sx -=1
				elif e.key == K_RETURN:					
					zl = text[sy]
					text[sy]=zl[:sx]
					sy+=1
					#text[sy] = zl[sy][sx:]
					text.insert(sy,[])
					text[sy] = zl[sx:]
					sx = 0
				elif e.key == K_LEFT:
					sx-=1
					if sx <0:
						sy -=1
						sx=len(text[sy])
				elif e.key == K_RIGHT:
					sx+=1
					if sx>len(text[sy]):
						sx = 0
						sy +=1
				elif e.key == K_DOWN:
					sy+=1
					if sy > len(text)-1:
						sy = len(text)-1
					if sx > len(text[sy]):
						sx = len(text[sy])
				elif e.key ==K_UP:
					sy-=1
					if sx > len(text[sy]):
						sx = len(text[sy])
				else:
					try:
						i = indexes.index(e.key)
						text[sy].insert(sx,characters[i])
						sx+=1
					except:
						print("key {} not found".format(e.key))
				if sy > len(text)-1:
					sy = len(text)-1
				if sy < 0:
					sy =0
				print(sx,sy)
				print(len(text)-1)
				if sx > len(text[sy]):
					sx = len(text[sy])
				if sx < 0:
					sx = 0

		screen.fill((255,255,255))
		draw.rect(screen,(0,0,255),(sx*16,sy*16,16,16))
		for y,line in enumerate(text):
			for x,char in enumerate(line):
				index = characters.index(char)
				screen.blit(fontpix,(x*16,y*16),area=(index*16,0,16,16))
		display.flip()
		select = sx,sy

if __name__ == "__main__":
	main()