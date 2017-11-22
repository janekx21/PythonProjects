class app:
	mode = "a"
	def __init__(self):
		print("start main")
		class P:
			def __init__(self,x):
				self.x = x
		self.player = P(10)
		print(self.player.x)
		self.loop()
	def loop(self):
		for x in range(0):
			if self.mode == "a":
				self.mainloop(x)
			elif self.mode == "b":
				self.subloop(x)
	def mainloop(self,x):
		print(x)
		if x == 40:
			self.mode = "b"
	def subloop(self,x):
		print("janek")
		if x == 60:
			self.mode = "a"

if __name__ == "__main__":
	app()