'''
tutbg1.py - A tutorial on how to create a simple background
'''



#I - import and initialize

import pygame as pg
import sys

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
	# R - Refresh display
	screen.blit(background, (0,0))
	pg.display.flip()

