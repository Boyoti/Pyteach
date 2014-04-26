import pygame, sys, random
from pygame.locals import *

pygame.init()
width = 500
height = 400

count = int(sys.argv[1])

# set up the window
DS = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Drawing")

# set up the colors
BLACK =(0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DS.fill(WHITE)

for n in range(count):
	x1 = width*random.random()
	y1 = height* random.random()
	x2 = width*random.random()
	y2 = height* random.random()
	pygame.draw.line(DS, BLUE, (x1,y1), (x2,y2), 4)


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
