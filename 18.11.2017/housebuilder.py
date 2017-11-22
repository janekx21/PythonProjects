data = "0,1,2,11,0,0,0,12,3,3"
data = data.split(",")
for i,x in enumerate(data):
	data[i] = int(x)
maxh = max(data)
st = ["" for x in range(maxh)]
for house in data:
	for etage in range(maxh):
		if int(house) > etage:
			st[etage] += "#"
		else:
			st[etage] += " "
for x in reversed(st):
	print(x)