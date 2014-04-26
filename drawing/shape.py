'''
shape.py - draw a shape given the side and angle
'''
from turtle import *

def shape(length,sides):
	angle = 360/int(sides)
	for i in range(sides):
		forward(length)
		right(angle)


# use shape function to draw different shapes from triangle to an octogon

for i in range(6):
	sides = i+3
	length = 60
	shape(length, sides)
raw_input()
