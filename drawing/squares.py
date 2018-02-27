'''
squares.py - draw multiple squares
'''
import turtle as t
from random import *
from tutil import *

count  = 10
t.tracer(5)
move(-100,-100)

for i in range(count):
	side = int(random()*200)
	x = y = int(random()*100)
	move(x,y)
	length = int(random()*100)
	shape(length,4)
	

input()



