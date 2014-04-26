'''
tutbg3.py - A tutorial on how to create a simple background using an existing image

Some cool pics are available. 
http://commons.wikimedia.org/wiki/File:Duna_dorada_en_Argelia_-_Guadalupe_Cervilla.jpg

'''



#I - import and initialize

import pygame as pg
import sys

pg.init()

#D - Display 

screen = pg.display.set_mode((640,480))
pg.display.set_caption("Surface as Background")

#E - Entities (in the game)

# Got the picture from wikimedia commons - picture of the day - http://commons.wikimedia.org/wiki/Main_Page
background = pg.image.load("guadalupe.jpg")
background = background.convert()


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

