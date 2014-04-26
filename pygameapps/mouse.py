import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SC = (800,600)
screen = pygame.display.set_mode(SC, 0, 32)

font = pygame.font.SysFont("arial", 16)

font_height = font.get_linesize()
event_text = []

while True:
	event = pygame.event.wait()
#	print event
	event_text.append(str(event))
#	print event_text
	event_text = event_text[-SC[1]/font_height:]
	print event_text

	if event.type == QUIT:
		exit()
	screen.fill((255, 255, 255))
	y = SC[1]-font_height
	for text in reversed(event_text):
		screen.blit(font.render(text, True, (0,0,0)),(0,y))
		y -= font_height
	pygame.display.update()

