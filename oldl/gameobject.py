from vector import *
class GameObject(object):
	def __init__(s,**options):
		if type(options.get("position")) == Vector:
			s.position = options.get("position")
		else:
			s.position = Vector.ZERO()
		s.Velocity = Vector.ZERO()
		s.rotation = 0.0
		s.size = Vector(1.0,1.0)
		s.name = "New "+str(s.__class__.__name__)
		s.init()
	def init(s):
		print( "#New "+str(s.__class__.__name__))
	def draw(s,display):
		pass
	def update(s):
		pass
class ObjectManager:
	def __init__(s):
		s.objects = []
		print("#Object Manager Init")
	def add(s,object):
		s.objects.append(object)
	def __repr__(s):
		return "<Object Manager , Objects.len:" + str(len(s.objects)) + " >"
	def update(s,display):
		for obj in s.objects:
			obj.update()
		for obj in s.objects:
			obj.draw(display)
if __name__ == "__main__":
	obj = GameObject(position=Vector(12.3,-6.555))
	print obj
	objM = ObjectManager()
	objM.add(obj)
	print(objM)
	print objM.objects[0].position.toInt()