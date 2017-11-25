from pygame import *
SIZE = (600,400)
screen = display.set_mode(SIZE)

characters = ["a","b","c","d",
"e","f","g","h","i","j","k",
"l","m","n","o","p","q","r",
"s","t","u","v","w","x","y",
"z"," ","0","1","2","3","4",
"5","6","7","8","9",",",".",
"-","#","+","\t", # 41

"A","B","C","D",
"E","F","G","H","I","J","K",
"L","M","N","O","P","Q","R",
"S","T","U","V","W","X","Y",
"Z"," ","=","!","\"","-","$",
"%","&","/","(",")",";",":",
"_","\'","*","\t"]


indexes = [97,98,99,100,101,102,
103,104,105,106,107,108,109,110,
111,112,113,114,115,116,117,118,
119,120,121,122,32,48,49,50,51,52,53,54,55,56,57,
44,46,45,35,43,9
]

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
					if sy != 0 or sx !=0:
						if sx == 0:
							zl = text[sy]
							text.pop(sy)
							sy-=1
							sx = len(text[sy])
							text[sy].extend(zl)
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
						if sy > 0:
							sy -=1
							sx=len(text[sy])
				elif e.key == K_RIGHT:
					sx+=1
					if sx>len(text[sy]):
						if sy < len(text)-1:
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
				elif e.key == K_F1:
					#debug
					string = ""
					for s in characters:
						string+=s
					print(string)

					for l in text:
						for s in l:
							print(s,characters.index(s))
				else:
					try:
						i = indexes.index(e.key)
						if key.get_mods() and 1:
							text[sy].insert(sx,characters[i+43])
						else:
							text[sy].insert(sx,characters[i])

						sx+=1
					except:
						print("key {} not found".format(e.key))
				if sy > len(text)-1:
					sy = len(text)-1
				if sy < 0:
					sy =0
#				print(sx,sy)
				if sx > len(text[sy]):
					sx = len(text[sy])
				if sx < 0:
					sx = 0

		screen.fill((255,255,255))
		draw.rect(screen,(0,0,255),(sx*16,sy*16,16,16))
		for y,line in enumerate(text):
			for x,char in enumerate(line):
				index = characters.index(char)
				screen.blit(fontpix,(x*16,y*16),area=(index%32*16,index//32*16,16,16))
		display.flip()
		select = sx,sy

if __name__ == "__main__":
	main()