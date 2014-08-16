render = []
update = []

def globalrender():
	for x in render:
		x()

def globalupdate():
	for x in update:
		x()