import ika
import attack
import planet
import player
import effects
import enemy
import engine
import manager
import text
import line
import collision



class Game:
	effects = []
	enemies = []	#enemies
	entities = []	#everything else
	bungees = []
	
	def __init__(self):
		manager.render.append(self.Render)
		manager.update.append(self.Update)
		
		self.difficulty = 0
		self.level = 0
		self.max_level = 1
		self.blackbg = ika.Image("gfx\\blackbg.png")
		
		self.killcount = 0
		
		
	def Update(self):
		for x in self.entities:
			x.Update()
		
		pos = 0
		for en in self.enemies:
			en.Update()
			if(en.dead == True):
				self.enemydead(en)
				del self.enemies[pos]
				self.killcount += 1
				
				if self.enemies == []:
					if self.level < self.max_level:
						self.dolevel()
						self.level += 1
					else:
						self.endgame()
			pos += 1
				
		if ika.Input.keyboard['SPACE'].Pressed():
			attack.fire()
		
		if ika.Input.keyboard['LCTRL'].Pressed():
			switchweapon()
		
		if ika.Input.keyboard['LSHIFT'].Pressed():
			attack.firebungee()
		
		#in-game reset 
		if ika.Input.keyboard['F5'].Pressed():
			engine.startgame()
		
		pos = 0
		for x in self.effects:
			x.Update()
			if(x.dead == True):
				del self.effects[pos]
			pos += 1
		
		
		
	def Render(self):
		ika.Video.Blit(self.blackbg,0,0)
		for x in self.entities:
			x.Render()
		for x in self.enemies:
			x.Render()
		for x in self.effects:
			x.Render()
		
		engine.font.Print(engine.SCREEN_WIDTH - 200, engine.SCREEN_HEIGHT - 20, "Enemies killed = %s" % (self.killcount,))
		engine.font.Print(5, engine.SCREEN_HEIGHT - 60, "Green Shield = %s" % (self.entities[0].shieldhp,))
		engine.font.Print(5, engine.SCREEN_HEIGHT - 40, "Pink Shield = %s" % (self.entities[1].shieldhp,))
		engine.font.Print(5, engine.SCREEN_HEIGHT - 20, "Planet Health = %s" % (self.entities[2].hp,))
	
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		
	def dolevel(self):
		if self.level == 0:
			en1 = enemy.en_straight(0,0)
			en2 = enemy.en_straight(engine.SCREEN_WIDTH-32,0)
			en3 = enemy.en_straight(0, engine.SCREEN_HEIGHT-32)
			en4 = enemy.en_straight(engine.SCREEN_WIDTH-32, engine.SCREEN_HEIGHT-32)
			self.enemies.append(en1)
			self.enemies.append(en2)
			self.enemies.append(en3)
			self.enemies.append(en4)
		elif self.level == 1:
			en1 = enemy.en_straight(0,0)
			en2 = enemy.en_straight(engine.SCREEN_WIDTH-32,0)
			en3 = enemy.en_straight(0, engine.SCREEN_HEIGHT-32)
			en4 = enemy.en_straight(engine.SCREEN_WIDTH-32, engine.SCREEN_HEIGHT-32)
			self.enemies.append(en1)
			self.enemies.append(en2)
			self.enemies.append(en3)
			self.enemies.append(en4)
			
	def endgame(self):
		pass

	def reset(self):
		#clear entities list
		length = len(self.entities)
		for x in self.entities:
			self.entities.pop(length-1)
			length -= 1
		
		#clear enemies list
		length = len(self.enemies)
		for x in self.enemies:
			self.enemies.pop(length-1)
			length -= 1
	
		
		
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	
	def enemydead(self, enemy):
		self.effects.append(effects.Explosion(enemy.center.x, enemy.center.y, enemy.r/2))
		#10% chance
		num = ika.Random(0,10)
		if num == 1:
			pass	
			'''turn into giving power-up'''
	
	
	
def switchweapon():
	pl = engine.GetPlayerL()
	pl.gun += 1
	if pl.gun > pl.num_guns:
		pl.gun = 1

