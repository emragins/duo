import ika
import engine

class text:

	blackbg = ika.Image("gfx\\blackbg.png")
	
	def __init__(self, x, y, text):
	
		self.x = x
		self.y = y
		self.fh = engine.font.height
		
		self.alive = True
		
		self.text = text
		
		while self.alive == True:
			self.Update()
			self.Render()
			ika.Input.Update()
			ika.Video.ShowPage()
		
	def Update(self):
		if ika.Input.enter.Pressed():
			self.alive = False
				
	def Render(self):
		ika.Video.Blit(self.blackbg,0,0)
		for a, b in enumerate(self.text):
			engine.font.Print(self.x, self.y + a*self.fh, b)
		