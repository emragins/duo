import ika
import engine
import point

class Planet:

	def __init__(self, hp, radius):
	
		self.center = point.Point(engine.HALF_SCREEN_W, engine.HALF_SCREEN_H)
		self.r = radius
		
		self.corner = point.Point(self.center.x - self.r, self.center.y - self.r)
		self.img = ika.Image("gfx\\planet.png")
		
		
		self.hp = hp
		
		#imagine square inside a circle oriented parallel to screen.  
		#it cuts edge of circle into 4 sections, below
		self.len = int(self.r/(2**(1/2))) #distance from center to square
		self.sq_top = self.center.y - self.len
		self.sq_right = self.center.x + self.len/2
		self.sq_bottom = self.center.y + self.len/2
		self.sq_left = self.center.x - self.len
		
	def Update(self):
		pass
	
	def Render(self):
		ika.Video.Blit(self.img, self.corner.x, self.corner.y)
		
	def take_dmg(self, dmg):
		self.hp -= dmg