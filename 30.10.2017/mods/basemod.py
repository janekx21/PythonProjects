draw = player.draw
def draw2(self,app):
	pygame.draw.circle(app.draw,(255,255,0),(self.x+14,self.y+12),8)
	draw(self,app)

player.draw = draw2
import math
draw3 = enemy.draw
def draw4(self,app):
	draw3(self,app)
	self.y += math.sin(app.time/21)
enemy.draw = draw4
