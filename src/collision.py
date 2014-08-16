import math
import line
import point
def Rect_Rect(box1, box2):
	"Returns a boolean evaluation of whether two boxes collide"
	if (box1.x  + box1.w >= box2.x
		and box1.x <= box2.x + box2.w
		and box1.y + box1.h >= box2.y
		and box1.y <= box2.y + box2.h):
			return True
	return False


def Point_Rect(point, box):
	if(point.x < box.x or point.y < box.y):
		return False
	if(point.x > box.x + box.w or point.y > box.y + box.h):
		return False
	return True
	
	
def Circle_Circle(cir1, cir2):
	rad_total = cir1.r + cir2.r
	dx = (cir1.center.x - cir2.center.x)
	dy = (cir1.center.y - cir2.center.y)
	d = int((dx**2 + dy**2)**0.5)
	if d <= rad_total:
		return 1
	return 0
	
def Line_Circle(line, cir):
	"Returns boolean of whether a line collides with a circle."
	"""
	C: (cir.center.x, cir.center.y)
	make two points: A: (a, cir.center.y) B: (cir.center.x, b).  
		if distance between is less than 2*cir.r, then collides
	
	OR if d(A, C) < cir.r -> collision
	OR if d(B, C) < cir.r -> collision
	"""
	
	if abs(line.end.x - cir.center.x) > abs(line.end.x - line.start.x):
		return 0					
	if abs(line.end.y - cir.center.y) > abs(line.end.y - line.start.y):
		return 0
		
	m = line.slope()
	
	'''print "m = ", m'''
	#make points
	if m == 0:
		a = cir.center.x
	else:
		a = int((cir.center.y - line.start.y)/m + line.start.x )
	if m == -11111:
		b = cir.center.y
	else:
		b = int(m*(cir.center.x - line.start.x) + line.start.y)

	'''
	print "line.start.x =", line.start.x
	print "line.start.y =", line.start.y
	print "line.end.x =", line.end.x
	print "line.end.y =", line.end.y
	print "a (x)= ", a
	print "b (y)= ", b
	'''
	
	if b < line.start.y and b < line.end.y:
		return 0
	if b > line.start.y and b > line.end.y:
		return 0
	if a < line.start.x and a < line.end.x:
		return 0
	if a > line.start.x and a > line.end.x:
		return 0
	'''
	print "cir.center.x= ", cir.center.x
	print "cir.center.y= ", cir.center.y
	'''
	
	dx = abs((a - cir.center.x))
	dy = abs((cir.center.y - b))
	if dx <= cir.r:
		return 1
	if dy <= cir.r:
		return 1
	d = int((dx**2 + dy**2)**0.5)
	if d <= 2*cir.r:
		return 1
	
	return 0
	