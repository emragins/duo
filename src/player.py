import ika
import engine
import collision
import point


class Player:

	def __init__(self, x, y):
	
		self.corner = point.Point(x,y)
		self.r = 16
		self.center = self.GetCenter()
		
		
		
		self.mid = engine.TILE_SIZE/2
		self.full = engine.TILE_SIZE
		
		self.top = point.Point(self.corner.x + self.mid, self.corner.y)
		self.right = point.Point(self.corner.x + self.full, self.corner.y + self.mid)
		self.left = point.Point(self.corner.x, self.corner.y + self.mid)
		self.bottom = point.Point(self.corner.x + self.mid, self.corner.y + self.full)
	
		#weaponry controlled through PlayerLeft
		#energy controlled through PlayerLeft
		#powers controlled through PlayerLeft
		
		self.shieldhp = 50
		self.dead = 0
		self.movespeed = 5
		
		
		self.img1 = ika.Image("gfx\\p1.png")
		self.img2 = ika.Image("gfx\\p2.png")
	
	def GetCenter(self):
		p = point.Point(self.corner.x + self.r, self.corner.y + self.r)
		return p 
		
	def Update(self):
		#collision with planet
		if collision.Circle_Circle(self, engine.rungame.entities[2]):
			if self.corner.y < engine.rungame.entities[2].sq_top:
				while collision.Circle_Circle(self, engine.rungame.entities[2]):
					self.corner.y -= 1
					self.center.y = self.corner.y + self.r
			elif self.corner.x < engine.rungame.entities[2].sq_left:
				while collision.Circle_Circle(self, engine.rungame.entities[2]):
					self.corner.x -= 1
					self.center.x = self.corner.x + self.r
			elif self.center.y >= engine.rungame.entities[2].sq_bottom:
				while collision.Circle_Circle(self, engine.rungame.entities[2]):
					self.corner.y += 1
					self.center.y = self.corner.y + self.r
			elif self.center.x >= engine.rungame.entities[2].sq_right:
				while collision.Circle_Circle(self, engine.rungame.entities[2]):
					self.corner.x += 1
					self.center.x = self.corner.x + self.r
					
			
		self.center = self.GetCenter()
		self.top = point.Point(self.center.x, self.corner.y)
		self.right = point.Point(self.corner.x + self.full, self.center.y)
		self.left = point.Point(self.corner.x, self.center.y)
		self.bottom = point.Point(self.center.x, self.corner.y + self.full)
		
		for en in engine.rungame.enemies:
			if collision.Circle_Circle(self, en):
				self.take_dmg(en.dmgdealt)
				en.dead = 1
				'''add animation (little explosion)???? sound?????'''
		
		
		
	def Render(self):
		pass
	
		
	def	moveleft(self):
		self.corner.x -= self.movespeed
		if self.corner.x < 0:
			self.corner.x = 0
	def moveup(self):
		self.corner.y -= self.movespeed
		if self.corner.y < 0:
			self.corner.y = 0
	def moveright(self):
		self.corner.x += self.movespeed
		if self.corner.x > engine.SCREEN_WIDTH - self.full:
			self.corner.x = engine.SCREEN_WIDTH - self.full
	def movedown(self):
		self.corner.y += self.movespeed
		if self.corner.y > engine.SCREEN_HEIGHT - self.full:
			self.corner.y = engine.SCREEN_HEIGHT - self.full
			
	def take_dmg(self, dmg):
		self.shieldhp -= dmg
		if self.shieldhp <= 0:
			self.dead = 1
	
class PlayerLeft(Player):
		
	def __init__(self, x, y):
		Player.__init__(self, x, y)
		
		self.gun = 1		
		'''CHANGE THIS BACK TO 1 SO THAT WEAPON UPGRADES ARE NECESSARY.  IT IS '2' FOR TESTING'''
		self.num_guns = 2	#bounce and single laser for defaults
		
		self.energy_level = 0
		self.energy_level_inc = 5
		self.bungee_time = 200
		
		
	def Update(self):
		Player.Update(self)
		
		self.energy_level += self.energy_level_inc
		
		if ika.Input.keyboard['A'].Position():
			self.moveleft()
		if ika.Input.keyboard['W'].Position():
			self.moveup()
		if ika.Input.keyboard['D'].Position():
			self.moveright()
		if ika.Input.keyboard['S'].Position():
			self.movedown()
	
	def Render(self):
		#ika.Video.DrawRect(self.corner.x, self.corner.y, self.corner.x+self.w, self.corner.y+self.h, engine.RED)
		ika.Video.Blit(self.img2, self.corner.x, self.corner.y)
	
	
	def increase_bungee_time(amt):
		self.bungee_time += amt
	
		
class PlayerRight(Player):
	
	def Update(self):
		Player.Update(self)
		
		if ika.Input.keyboard['LEFT'].Position():
			self.moveleft()
		if ika.Input.keyboard['UP'].Position():
			self.moveup()
		if ika.Input.keyboard['RIGHT'].Position():
			self.moveright()
		if ika.Input.keyboard['DOWN'].Position():
			self.movedown()
	
	def Render(self):
		#ika.Video.DrawRect(self.corner.x, self.corner.y, self.corner.x+self.w, self.corner.y+self.h, engine.PURPLE)
		ika.Video.Blit(self.img1, self.corner.x, self.corner.y)
		

					