'''
tutbg2.py - Create a simple background and change it whenever user presses a key
'''



#I - import and initialize

import pygame as pg
import sys
from random import *

pg.init()

#D - Display 

screen = pg.display.set_mode((640,480))
pg.display.set_caption("Surface as Background")

#E - Entities (in the game)

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,255))

#A - action (broken into ALTER steps)

#A - Assign values to key variables

keepGoing = True

#L _ Loop (set up the main loop)

while keepGoing:

	

	# E - Event handling
	for event in pg.event.get():
		if event.type == pg.QUIT:
			keepGoing = False
		if event.type == pg.KEYDOWN:
			red = int(random()*255)
			green = int(random()*255)
			blue = int(random()*255)
			background.fill((red,green,blue))

	# R - Refresh display
	screen.blit(background, (0,0))
	pg.display.flip()

