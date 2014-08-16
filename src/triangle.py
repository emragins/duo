from point import Point
from line import Line

class Triangle:
	def __init__(point_a = None, point_b = None, point_c = None):
		#--points--
		self.A = point_a
		self.B = point_b
		self.C = point_c
			
		#--lines--
		self.a = Line(self.B, self.C)
		self.b = Line(self.A, self.C)
		self.c = Line(self.A, self.B)
		
		#--lengths--
		self.len_a = len(self.a)
		self.len_b = len(self.b)
		self.len_c = len(self.c)
		
		self.ang_A = 0 ##-------------
	def 