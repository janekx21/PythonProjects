import random
konsonants = ["b","d","f","g","h","j","k","l","m","n","p",
"r","s","t","v","w","z"] # x q c
vocale = ["a","e","i","o","u",]
namen = []
for x in range(1000):
	st = ""
	for i in range(random.randrange(3,10)):
		if i %2==0:
			st+=konsonants[random.randrange(0,len(konsonants))]
		else:
			st+=vocale[random.randrange(0,len(vocale))]
		if random.randrange(0,5)==0:
			i-=1
	namen.append(st)
print(namen)