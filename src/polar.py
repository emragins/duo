import ika
import engine
import math
'''
NOTE: THE CENTER OF THE POLAR COORDINATE IS NOT THE SAME THE CENTER FOR XY-COORDINATES.
	YOU MUST ACCOUNT FOR THIS.

P(r, theta)

x = r*cos(theta)
y = y*sin(theta)

r^2 = x^2 + y^2
tan(theta) = y/x

cos(theta) = x/r
sin(theta) = y/r
'''

def r_from_xy(x, y):
	
	x -= engine.HALF_SCREEN_W
	y -= engine.HALF_SCREEN_H
	sum = x*x + y*y
	if sum == 0:
		sum = 1
	r = math.sqrt(sum)
	r = math.floor(r)
	return r
	
def theta_from_xy(x, y):
	x -= engine.HALF_SCREEN_W
	y -= engine.HALF_SCREEN_H
	if y == 0:
		y = 0.01
	if x == 0:
		theta = 1.5708 
	else:
		div = (float(y)/float(x))
		theta = math.atan(div)
	
	return theta
	
def x_from_polar(r, theta, pos):
	
	x = r*math.cos(theta)
	x = math.floor(x)
	if pos == False:
		x = -x
	x += engine.HALF_SCREEN_W
	x = abs(x)
	return x
	
def y_from_polar(r, theta, pos):
	y = r*math.sin(theta)
	y = math.floor(y)
	if pos == False:
		y = -y
	y += engine.HALF_SCREEN_H
	return y
