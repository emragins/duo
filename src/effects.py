import ika
import engine
#import game
import line
import collision
from point import Point

class Effect:

	def __init__(self, points):
		
		self.pos = 0
		self.dead = 0
		
		self.points = points
		self.num_points = len(points)
		
		self.points = []
	
	def Render(self):
		for point in self.points:
			ika.Video.DrawPixel(point.x, point.y, self.color)
		
	def Update(self):
		pass

		
class Bungee(Effect):

	def __init__(self, path):
		
		pl = engine.GetPlayerL()
		
		self.dead = 0
		self.color = engine.YELLOW
		self.duration = pl.bungee_time
		
		self.path = path
		self.start = path.start
		self.end = path.end
			
	
	def Render(self):
		##make color deteriorate as duration runs out
		ika.Video.DrawLine(self.start.x, self.start.y, self.end.x, self.end.y, self.color)
	
	def Update(self):
		self.duration -= 1
		if self.duration == 0:
			self.dead = 1
	
		for enemy in engine.rungame.enemies:
			if collision.Line_Circle(self.path, enemy):
				enemy.bounce(self.path)
				break
	
	
#laser = particle beam
class SingleLaser(Effect):
	
	#path = set of points tested for collision in form [point, point, etc.]
	def __init__(self, points):
		
		Effect.__init__(self, points)
		self.color = engine.RED
		
		self.laser_points = points
		
	def Render(self):
		Effect.Render(self)
		
	def Update(self):
		num = self.num_points/2
		num += 1
				
		for iter in range(5):
			if self.pos < num:
				self.points.append(self.laser_points[self.pos])
				self.points.append(self.laser_points[-self.pos])
		
			self.pos += 1
			if self.pos > self.num_points:
				self.dead = 1
		
		
#laser = particle beam			
class DoubleLaser(Effect):
		
	def __init__(self, pointsa, pointsb):
		
		self.dead = 0
		self.pos = 0
		self.points = []
		
		self.color = engine.RED
				
		self.pointsa = pointsa
		self.pointsb = pointsb
		self.num_pointsa = len(pointsa)
		self.num_pointsb = len(pointsb)
				
	def Render(self):
		Effect.Render(self)
		
	def Update(self):
		numa = self.num_pointsa/2
		numb = self.num_pointsb/2
		numa += 1
		numb +=1
		
		for x in range(2):
			if self.pos < numa:
				self.points.append(self.pointsa[self.pos])
				self.points.append(self.pointsa[-self.pos])
			
			if self.pos < numb:
				self.points.append(self.pointsb[self.pos])
				self.points.append(self.pointsb[-self.pos])
			
			self.pos += 1
		
		if self.pos > numa+numb:
			self.dead = 1	
			
class Explosion:

	def __init__(self, x, y, max_r):
	
		self.x = x
		self.y = y
		self.max_r = max_r
		self.r = 0
		self.dead = 0
		
	def Update(self):
		self.r += 1
		if self.r == self.max_r:
			self.dead = 1
			
	def Render(self):
		ika.Video.DrawEllipse(self.x, self.y, self.r, self.r, engine.YELLOW, 1)
