import ika
import manager
import game
import text
import player
import enemy
import planet



rungame = game.Game()

last_fps = 0
font = ika.Font("font.fnt")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HALF_SCREEN_W = 400
HALF_SCREEN_H = 300
TILE_SIZE = 32

GREEN = ika.RGB(0,255,0)
RED = ika.RGB(255,0,0)
PURPLE = ika.RGB(255,0,255)
YELLOW = ika.RGB(255,255,0)

def mainloop():
	last_update = 0
	last_update2 = 0
	while 1:
		
		if ika.GetTime() > last_update:
			global last_fps
			
			last_update = ika.GetTime()+1
			
			
			# from hawk's code
			if last_fps != ika.GetFrameRate():
				ika.SetCaption( "'Duo' (FPS: "+str(ika.GetFrameRate())+")" )
				last_fps = ika.GetFrameRate()
			
			ika.Input.Update()
			manager.globalupdate()
			ika.ProcessEntities()
			
		#note: get rid of last_update2 and functionality for better performace (combine with last_update1 or drop if FPS low)
		if ika.GetTime() >= last_update2:
			ika.Render()
			manager.globalrender()

			ika.Video.ShowPage()
		
			last_update2 = ika.GetTime()+1
		
def intro():
	text.text(10,10, ["(Press 'Enter' to proceed)"])
	
	startgame(0)  #number for possible future additions of difficulty level	
	
def startgame(difficulty = 0):
	'''
	difficuly factors: 
		-size of planet to defend: larger planet = harder since less time to kill enemies
		-number enemies (duh)
		-capability of beam to fire through multiple enemies or just 1
	'''
	global rungame
	rungame.difficulty = difficulty
	
	#make players
	players_exist = False
	for x in rungame.entities:
		if isinstance(x, player.PlayerLeft):
			players_exist = True
			break
	if players_exist == False:
		p1 = player.PlayerLeft(50,50)
		p2 = player.PlayerRight(200,50)
		rungame.entities.append(p1)
		rungame.entities.append(p2)
	
	
	if difficulty == 0:		#current all-encompasing difficulty
		p = planet.Planet(500, 75)	#hp, radius
		rungame.entities.append(p)
		
		rungame.dolevel()

def GetPlayerL():
	for x in rungame.entities:
		if isinstance(x, player.PlayerLeft):
			return x
		
def GetPlayerR():
	for x in rungame.entities:
		if isinstance(x, player.PlayerRight):
			return x		