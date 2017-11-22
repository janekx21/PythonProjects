class a:
	def __init__(self):
		self.name = "a"
class b:
	def __init__(self):
		self.name = "b"

classes = [a,b,a]

c = classes[2]()

print(c.name)