''' 
movebox.py - moves a rectangle across the screen

'''

#I - import and initialize
import pygame
pygame.init()

#D - Display 

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Move a Box")

#E - Entities (in the game)

background = pygame.Surface(screen.get_size())
background = background.convert()

# Yellow background
background.fill((255,255,0))

# Make a red 25x25 box
box = pygame.Surface((25,25))
box = box.convert()
box.fill((255,0,0))

# set up box co-ordinates
box_x = 0
box_y = 200


#A - action (broken into ALTER steps)

#A - Assign values to key variables
clock = pygame.time.Clock()
keepGoing = True

#L _ Loop (set up the main loop)

while keepGoing:

	# T - timer setup
	clock.tick(30)


	# E - Event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keepGoing = False
	# Modify the box value (to create illusion of motion)

	box_x += 5

	# check boundaries - if you keep incrementing the x-co-ordinate of the 
	# box, it will eventually move off the screen. So we are going to 
	# check the co-ordinates and reset the co-ordinates.

	if box_x > screen.get_width():
		box_x = 0

	# R - Refresh display
	screen.blit(background, (0,0))
	screen.blit(box, (box_x, box_y))
	pygame.display.flip()

