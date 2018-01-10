from pygame import *
init()
WIDTH = 600
HEIGHT = 400
screen = display.set_mode((WIDTH,HEIGHT))

mixer.init()

s = mixer.Sound("ui.wav")
raw = s.get_raw()
l = list(raw)
print(chr(0xFF))
"""
for i in range(92160//2):
	if i %100>50:
		l[i] = chr(255)
	else:
		l[i] = chr(127)
"""
raw = "".join(l)
n = mixer.Sound(raw)

for x in range(WIDTH):
	breite = len(l)//WIDTH
	avr = 0
	anz = 0
	avr2 = 0
	anz2 = 0
	for i in range(breite):
		o = ord(l[x*breite+i])
		if o>127:
			avr += o
			anz+=1
		else:
			avr2 += o
			anz2+=1
	if anz != 0:
		h = avr//anz
	else:
		h = 0
	if anz2 != 0:
		h2 = avr2//anz2
	else:
		h2 = 0
	#index=len(l)*x//WIDTH
	draw.line(screen,(255,255,255),(x,h2//2+HEIGHT//2),(x,HEIGHT//2-h//2))
	#screen.set_at((x,h*HEIGHT//255),(255,255,255))

looping=True
while looping:
	for e in event.get():
		if e.type == QUIT:
			looping=False
		if e.type == KEYDOWN:
			n.play()
	display.flip()