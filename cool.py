import pygame
import sys
import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()


SCREEN = None
SCREENR = None
text = []
selector = 0
lastChar = "None"

#COLORS
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

#RESELOTIONS
SURFACERES = (200,200)
WINDOWRES = (800,800)

#-------------------#
keydown = []
keyup = []
keypress = []

pixFont = None
pixFontIndexs = ["\l","","","","","","","","","","","","","","","",
				 "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
				 "q","r","s","t","u","v","w","x","y","z","","","","","","",
				 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
				 "Q","R","S","T","U","V","W","X","Y","Z","","","","","","",
				 "0","1","2","3","4","5","6","7","8","9","\xc3","\xc2","","","","",
				 "!","\"","\xc2","$","%","&","/","(",")","=","?","\xc2","","","","",
				 " ","\xc2","\xc2","","","","","","{","[","]","}","\\","","","",
				 ",",".","-","+","#","~","<","|","^","","","","","","","",
				 ";",":","_","*","\'","",">","","\xc2","","","","","","",""]


def main():
	global SCREEN,font,pixFont,SCREENR
	pygame.init()
	pixFont = pygame.image.load("fontwhite.png")

	SCREENR = pygame.display.set_mode(WINDOWRES)
	SCREEN = pygame.Surface(SURFACERES)
	mainLoop()
	pygame.quit()


def mainLoop():
	global SCREEN,font,selector,text,pixFont,pixFontIndexs,SCREENR
	LOOP = True
	while LOOP:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				LOOP = False
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					LOOP = False
					return
				if event.key == pygame.K_LEFT:
					if selector >0:
						selector -=1
				if event.key == pygame.K_UP:
					zeil = 0
					lastEnter = 0
					for i,char in enumerate(text):
						if i == selector:
							selector = lastEnter
							
						if char == "\n":
							zeil += 1
							lastEnter = i
				if event.key == pygame.K_DOWN:
					zeil = 0
					last = False
					for i,char in enumerate(text):
						if i > selector:
							last = True
						if char == "\n" and last:
							selector = i
							break

				if event.key == pygame.K_RIGHT:
					if selector <len(text):
						selector +=1
				if event.key == pygame.K_F10:
					try:
						global playCall,playStart
						exec("global playCall,playStart,keydown,keyup,keypress\n" + arrayToString(text))
						playInit()
					except  Exception as inst:
						print(inst)
				if event.key == pygame.K_F12:
					file_path = tkFileDialog.askopenfilename()
					if file_path:
						with open(file_path,"w") as f:
							f.write(arrayToString(text))
				if event.key == pygame.K_F11:
					file_path = tkFileDialog.askopenfilename()
					if file_path:
						with open(file_path,"r") as f:
							selector = 0
							text = []
							for item in f.read():
								tAdd(item)

				inputting(event.key)
		SCREEN.fill((28,20,20))
		x = 0
		y = 0
		sx = 8
		sy = 8
		for i,item in enumerate(text):
			if item != "\n":
				if item != "\t":
					#font.render_to(SCREEN, ((x)*sx,(y+1)*sy), item, (255,255,255))
					index = pixFontIndexs.index(item)
					SCREEN.blit(pixFont,((x)*sx,y*sy),(index%16*8,index/16*8,8,8))
					x += 1
				else:
					x += 3
			else:
				x = 0
				y += 1
			if i+1 == selector:
				pygame.draw.rect(SCREEN,(20,0,200),(x*sx,y*sy,3,sy))
		pygame.display.flip()
		d = pygame.transform.scale(SCREEN,WINDOWRES,SCREENR)
		#SCREENR.blit(d,(0,0))

def playInit():
	playStart()
	playLoop()
	print("End DEMO")

def playLoop():
	global keydown,keyup,keypress,SCREENR,SCREEN
	while True:
		keydown = []
		keyup = []

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			if event.type == pygame.KEYDOWN:
				if event.key not in keydown:
					keydown.append(event.key)
				if event.key not in keypress:
					keypress.append(event.key)
				if event.key == pygame.K_ESCAPE:
					return
			if event.type == pygame.KEYUP:
				if event.key in keyup:
					keyup.remove(event.key)
				if event.key in keypress:
					keypress.remove(event.key)
		playCall()
		pygame.display.flip()
		d = pygame.transform.scale(SCREEN,WINDOWRES,SCREENR)
		#SCREENR.blit(d,(0,0))

def playStart():
	print("Start Empty")

def playCall():
	global SCREEN
	SCREEN.fill((0,0,0))
	print("Loop Empty")

## THE DRAW FUNCTIONS

def circ(x,y,rad,color):
	global SCREEN
	pygame.draw.circle(SCREEN,color,(x,y),rad)
def cls(color):
	global SCREEN
	SCREEN.fill(color)
def rect(x,y,x2,y2,color):
	global SCREEN
	pygame.draw.rect(SCREEN,color,(x,y,x2,x2))
def line(x,y,x2,y2,color):
	global SCREEN
	pygame.draw.line(SCREEN, color, (x,y), (x2,y2))

def inputting(id):
	global text,selector,lastChar
	#print(id)
	if not pygame.key.get_mods() & pygame.KMOD_SHIFT and not pygame.key.get_mods() & pygame.KMOD_CTRL:
		if id == pygame.K_SPACE:
			tAdd(" ");return
		if id == pygame.K_TAB:
			tAdd("\t");return
		if id == pygame.K_RETURN:
			if lastChar == ":":
				tAdd("\n")
				tAdd("\t")
			else:
				tAdd("\n")
			return
		if id == pygame.K_BACKSPACE:
			if len(text)>0:
				text.pop(selector-1)
				selector -=1
			return
		if id == pygame.K_LEFT:
			return
		if id == pygame.K_RIGHT:
			return
		if id == pygame.K_UP:
			return
		if id == pygame.K_DOWN:
			return
		if id == pygame.K_LSHIFT:
			return
		if id == pygame.K_RSHIFT:
			return
		if id == pygame.K_a:
			tAdd("a");return
		if id == pygame.K_b:
			tAdd("b");return
		if id == pygame.K_c:
			tAdd("c");return
		if id == pygame.K_d:
			tAdd("d");return
		if id == pygame.K_e:
			tAdd("e");return
		if id == pygame.K_f:
			tAdd("f");return
		if id == pygame.K_g:
			tAdd("g");return
		if id == pygame.K_h:
			tAdd("h");return
		if id == pygame.K_i:
			tAdd("i");return
		if id == pygame.K_j:
			tAdd("j");return
		if id == pygame.K_k:
			tAdd("k");return
		if id == pygame.K_l:
			tAdd("l");return
		if id == pygame.K_m:
			tAdd("m");return
		if id == pygame.K_n:
			tAdd("n");return
		if id == pygame.K_o:
			tAdd("o");return
		if id == pygame.K_p:
			tAdd("p");return
		if id == pygame.K_q:
			tAdd("q");return
		if id == pygame.K_r:
			tAdd("r");return
		if id == pygame.K_s:
			tAdd("s");return
		if id == pygame.K_t:
			tAdd("t");return
		if id == pygame.K_u:
			tAdd("u");return
		if id == pygame.K_v:
			tAdd("v");return
		if id == pygame.K_w:
			tAdd("w");return
		if id == pygame.K_x:
			tAdd("x");return
		if id == pygame.K_y:
			tAdd("z");return
		if id == pygame.K_z:
			tAdd("y");return
		if id == pygame.K_1:
			tAdd("1");return
		if id == pygame.K_2:
			tAdd("2");return
		if id == pygame.K_3:
			tAdd("3");return
		if id == pygame.K_4:
			tAdd("4");return
		if id == pygame.K_5:
			tAdd("5");return
		if id == pygame.K_6:
			tAdd("6");return
		if id == pygame.K_7:
			tAdd("7");return
		if id == pygame.K_8:
			tAdd("8");return
		if id == pygame.K_9:
			tAdd("9");return
		if id == pygame.K_0:
			tAdd("0");return
		if id == pygame.K_PERIOD:
			tAdd(".");return
		if id == pygame.K_COMMA:
			tAdd(",");return
		if id == 47:
			tAdd("-");return
		if id == 93:
			tAdd("+");return
	if pygame.key.get_mods() & pygame.KMOD_SHIFT and not pygame.key.get_mods() & pygame.KMOD_CTRL:
		if id == pygame.K_a:
			tAdd("A");return
		if id == pygame.K_b:
			tAdd("B");return
		if id == pygame.K_c:
			tAdd("C");return
		if id == pygame.K_d:
			tAdd("D");return
		if id == pygame.K_e:
			tAdd("E");return
		if id == pygame.K_f:
			tAdd("F");return
		if id == pygame.K_g:
			tAdd("G");return
		if id == pygame.K_h:
			tAdd("H");return
		if id == pygame.K_i:
			tAdd("I");return
		if id == pygame.K_j:
			tAdd("J");return
		if id == pygame.K_k:
			tAdd("K");return
		if id == pygame.K_l:
			tAdd("L");return
		if id == pygame.K_m:
			tAdd("M");return
		if id == pygame.K_n:
			tAdd("N");return
		if id == pygame.K_o:
			tAdd("O");return
		if id == pygame.K_p:
			tAdd("P");return
		if id == pygame.K_q:
			tAdd("Q");return
		if id == pygame.K_r:
			tAdd("R");return
		if id == pygame.K_s:
			tAdd("S");return
		if id == pygame.K_t:
			tAdd("T");return
		if id == pygame.K_u:
			tAdd("U");return
		if id == pygame.K_v:
			tAdd("V");return
		if id == pygame.K_w:
			tAdd("W");return
		if id == pygame.K_x:
			tAdd("X");return
		if id == pygame.K_y:
			tAdd("Z");return
		if id == pygame.K_z:
			tAdd("Y");return
		if id == pygame.K_1:
			tAdd("!");return
		if id == pygame.K_2:
			tAdd("\"");return
		if id == pygame.K_3:
			tAdd("e")
			tAdd("a")
			tAdd("s")
			tAdd("t")
			tAdd("e")
			tAdd("r")
			tAdd("\n")
			return
		if id == pygame.K_4:
			tAdd("$");return
		if id == pygame.K_5:
			tAdd("%");return
		if id == pygame.K_6:
			tAdd("&");return
		if id == pygame.K_7:
			tAdd("/");return
		if id == pygame.K_8:
			tAdd("(");return
		if id == pygame.K_9:
			tAdd(")");return
		if id == pygame.K_0:
			tAdd("=");return
		if id == pygame.K_PERIOD:
			tAdd(":");return
		if id == pygame.K_COMMA:
			tAdd(";");return
		if id == 47:
			tAdd("_");return
		if id == 93:
			tAdd("*");return
		if id == 45:
			tAdd("?");return
	if pygame.key.get_mods() & pygame.KMOD_CTRL and pygame.key.get_mods() & pygame.KMOD_ALT:
		if id == 45:
			tAdd("\\");return

def tAdd(x):
	global text,selector,lastChar
	text.insert(selector,x)
	lastChar = x
	selector +=1
	


def arrayToString(array):
	string = ""
	for item in array:
		string += item
	return string

if __name__ == "__main__":
	main()