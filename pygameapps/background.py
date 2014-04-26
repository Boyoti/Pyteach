''' idea.py
Simplest possible program display demonstrates IDEA/ ALTER model
Andy Harris 5/06
'''

#I - import and initialize
import pygame
pygame.init()

#D - Display 

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Hello Class!")

#E - Entities (in the game)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,255))

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
	# R - Refresh display
	screen.blit(background, (0,0))
	pygame.display.flip()

