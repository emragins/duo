import engine
import game
import effects
import enemy
import player
import line
import collision
import bungee
from point import Point
def fire():
	
	pl = engine.GetPlayerL()
	pr = engine.GetPlayerR()
	
	mid = engine.TILE_SIZE/2
	full = engine.TILE_SIZE
	dmg = 0
	
	#single laser
	if pl.gun == 1:
		dmg = 1
			
		path = line.Line(pl.center, pr.center)
				
		points = path.points_on_line(5)  #CHANGE IF ENEMIES ARE PASSING THROUGH
	
		engine.rungame.effects.append(effects.SingleLaser(points))
	
		#check for collision
		for enemy in engine.rungame.enemies:
			if collision.Line_Circle(path, enemy):
				enemy.take_dmg(dmg)
						
	#double laser
	elif pl.gun == 2:
		dmg = 1		
		
		if pl.center.x < pr.center.x and pl.center.y < pr.center.y:
			patha = line.Line(pl.bottom, pr.left)
			pathb = line.Line(pl.right, pr.top)
		elif pl.center.x > pr.center.x and pl.center.y < pr.center.y:
			patha = line.Line(pl.bottom, pr.right)
			pathb = line.Line(pl.left, pr.top)
		elif pl.center.x < pr.center.x and pl.center.y > pr.center.y:
			patha = line.Line(pl.top, pr.left)
			pathb = line.Line(pl.right, pr.bottom)
		elif pl.center.x > pr.center.x and pl.center.y > pr.center.y:
			patha = line.Line(pl.top, pr.right)
			pathb = line.Line(pl.left, pr.bottom)
		elif pl.center.x == pr.center.x:
			patha = line.Line(Point(pl.left.x, pl.center.y), Point(pr.left.x, pr.center.y))
			pathb = line.Line(Point(pl.right.x, pl.center.y), Point(pr.right.x, pr.center.y))
		elif pl.center.y == pr.center.y:
			patha = line.Line(Point(pl.center.x, pl.top.y), Point(pr.center.x, pr.top.y))
			pathb = line.Line(Point(pl.center.x, pl.bottom.y), Point(pr.center.x, pr.bottom.y))
		
		
		pointsa = patha.points_on_line(5)  #CHANGE IF ENEMIES ARE PASSING THROUGH
		pointsb = pathb.points_on_line(5)
	
					
		engine.rungame.effects.append(effects.DoubleLaser(pointsa, pointsb))
		
		#points = pointsa + pointsb
	
		#check for collision
		for enemy in engine.rungame.enemies:
			if collision.Line_Circle(patha, enemy):
				enemy.take_dmg(dmg)
			if collision.Line_Circle(pathb, enemy):
				enemy.take_dmg(dmg)
	"""
	#check for collision
	done = False
	for a in points:
		if done:
			break
		#INSERT LATER: if collides with planet, break and damage planet
		for b in engine.rungame.enemies:
			if(collision.Point_Rect(a,b)):
				b.take_dmg(dmg)
				if(engine.rungame.difficulty != 0):
					done = True
					break
	"""
	
	
def firebungee():
	pl = engine.GetPlayerL()
	pr = engine.GetPlayerR()
	
	path = line.Line(pl.center, pr.center)
		
	engine.rungame.effects.append(effects.Bungee(path))
	#detection in effects class for update reasons
	