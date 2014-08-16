import ika
import engine
import polar
import line
import collision
from point import Point

class Enemy:

	def __init__(self, x, y, r, max_hp):
		
		self.corner = Point(x,y)
		self.r = r
		
		self.center = self.GetCenter()
		
		
		self.dead = False
		self.hp = max_hp
		self.dmgdealt = 10
		
		self.PLANET_CENTER_X = engine.HALF_SCREEN_W
		self.PLANET_CENTER_Y = engine.HALF_SCREEN_H
		
		self.iter = 0	#for moving enemy in "update"
		
		start = Point(0,0)
		end = Point(0,0)
		self.path = line.Line(start, end)
		self.points = []
		
	def GetCenter(self):
		p = Point(self.corner.x + self.r, self.corner.y + self.r)
		return p 
		
	def Update(self):
		self.center = self.GetCenter()
		if collision.Circle_Circle(self, engine.rungame.entities[2]):
			self.dead = 1
			engine.rungame.entities[2].take_dmg(self.dmgdealt) #planet
		
		
	def Render(self):
		pass
	
	def take_dmg(self, dmg):
		self.hp -= dmg
		if self.hp <= 0:
			self.dead = 1

	def bounce(self, bungee_path):
		
		bungee_points = bungee_path.points_on_line(2)
		
		#get last point of enemy's path
		enemy_final = Point(self.path.end.x, self.path.end.y)
		
		#---find closest point on bungee---
		pos = 0
		#find starting interval on bungee
		num_points = len(bungee_points)
		while ((enemy_final.x < bungee_points[pos].x and enemy_final.y < bungee_points[pos].y) or
			(enemy_final.x > bungee_points[pos].x and enemy_final.y > bungee_points[pos].y)):
			if pos == num_points-1: 
				break
			pos +=1 
			
		#find smallest interval between bungee and enemy path's end--given by 'pos' on bungee
		dist_a = line.dist(enemy_final, Point(bungee_points[pos].x, bungee_points[pos].y))
		while(1):
			if pos == num_points-1: 
				break
			pos += 1
			dist_b = line.dist(enemy_final, bungee_points[pos])
			if (dist_b > dist_a):  #if dist = smallest interval, then stop loop
				break
			else:
				dist_a = dist_b
		
		#find distances from enemy's destination to point on bungee
		#note: sign is irrelevant
		dx = enemy_final.x - bungee_points[pos].x
		dy = enemy_final.y - bungee_points[pos].y
		
		#designate new enemy path's "final point"
		pnx = bungee_points[pos].x - dx
		pny = bungee_points[pos].y - dy
		
		'''NO ERROR CHECKING TO SEE IF IT GOES OFF MAP
		ADD IN HERE WITH PNX, PNY'''
				
		#designate line from current position to new destination
		pn = line.Line(self.corner, Point(pnx, pny)) #enemy's new path
		
		m = pn.slope()
		
		'''
		#figure out what to do with rest of line
		if m > 0:
			pass
		elif m == -11111: #"undefined"
			pass
		elif m < 0:
			pass
		elif m == 0:
			pass
		'''
		
		self.points = pn.points_on_line(1)
		self.iter = 0	#reset iterator for moving enemy
		self.num_points = len(self.points)
		
		
		
		
class en_straight(Enemy):
	
	def __init__(self, x, y):
		
		Enemy.__init__(self, x, y, 16, 1)	#self, xpos, ypos, radius, max_hp
		
		self.dmgdealt = 2
		
		self.speed = 1
		
		
		self.img_en1 = ika.Image("gfx\\en1.png")
		
		start = Point(self.corner.x, self.corner.y)
		end = Point(self.PLANET_CENTER_X, self.PLANET_CENTER_Y)
		self.path = line.Line(start, end)
		
		self.points = self.path.points_on_line(1)
		self.num_points = len(self.points)
		
	def Update(self):
		#update coords
		self.corner = Point(self.points[self.iter].x, self.points[self.iter].y)
		
		self.iter += self.speed
		if self.iter >= self.num_points:
			self.dead = True
			
		Enemy.Update(self)
		
	def Render(self):
		ika.Video.Blit(self.img_en1, self.corner.x, self.corner.y)