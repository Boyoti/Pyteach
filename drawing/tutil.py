# a few high level functions of turtle

import turtle as t

def move(x,y):
	t.up() # pen up
	t.goto(x,y) # x and y are co-ordinates
	t.down() # restore pen 

def shape(length,sides):
	if sides < 3:
		sides =3
	angle = 360/sides
	for i in range(sides):
		t.forward(length)
		t.right(angle)


