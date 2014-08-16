import line
import game

class Bungee:

	def __init__(Line, points, duration):
		self.points = points
		self.dead = False
		self.time = duration
		
	def Update():
		self.time -= 1
		if self.time == 0:
			self.dead = True
	
	def Render():
		pass
		
	