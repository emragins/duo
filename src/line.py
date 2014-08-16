import ika
import math
import point

class Line:
	
	def __init__(self, start, end):
		self.start = start
		self.end = end
		
	def Update():
		pass
	
	def Render():
		pass
		
	def slope(self):
		dx = self.end.x - self.start.x
		dy = self.end.y - self.start.y
		if dx != 0:
			m = float(dy)/float(dx)
		else: 
			m = -11111
		return m
	
	#returns list; list = [ point, point, ..., point ]	
	def points_on_line(self, inc):
		#Uses Bresenham's line function
	
		list = []
		
		tx1 = self.start.x
		ty1 = self.start.y
		tx2 = self.end.x
		ty2 = self.end.y

		
		steep = abs(self.end.y - self.start.y) > abs(self.end.x - self.start.x)
		if steep:
			self.start.x, self.start.y = self.start.y, self.start.x
			self.end.x, self.end.y = self.end.y, self.end.x
		if self.start.x > self.end.x:
			self.start.x, self.end.x = self.end.x, self.start.x
			self.start.y, self.end.y = self.end.y, self.start.y
		delta_x = self.end.x - self.start.x
		delta_y = abs(self.end.y - self.start.y)
		error = -(delta_x + 1) / 2
		
		y = self.start.y
		if self.start.y < self.end.y:
			ystep = 1 
		else:
			ystep = -1
	
		for x in range(self.start.x,self.end.x):
			if x%inc == 0:
				if steep:
					list.append(point.Point(y,x)) 
				else:
					list.append(point.Point(x,y)) 
			error += delta_y
			if error >= 0:
				y += ystep
				error -= delta_x
		
		if tx1 != list[0].x or ty1 != list[0].y:
			list.reverse()
		
		#restore original line
		self.start.x = tx1
		self.start.y = ty1
		self.end.x = tx2
		self.end.y = ty2
		
		return list
		
	def __len__(self):
		l = dist(self.start, self.end)
		return l 
		
def dist(start, end):
	dx = end.x - start.x
	dy = end.y - start.y
	c = (dx**2 + dy**2)**0.5
	return c