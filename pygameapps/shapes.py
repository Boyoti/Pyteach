import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DS = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption("Drawing")

# set up the colors
BLACK =(0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DS.fill(WHITE)


pygame.draw.polygon(DS, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.circle(DS, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DS, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DS, RED, (200, 150, 100, 50))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
