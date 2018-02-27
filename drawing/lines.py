'''
lines.py - draw multiple lines
'''

import turtle as t
from random import *
import sys

count = int(sys.argv[1]) # get the number of lines to draw 

t.clear()
t.tracer(0)
for i in range(count):
	x = random()*100 # find a random coordinates between 1 and 100
	y = random()*100 
	t.goto(x,y)
input()
