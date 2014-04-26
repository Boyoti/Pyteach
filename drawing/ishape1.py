'''
iShape1 - an interactive shape drawing program. Get the shape type from user and the number of shapes and draw them
'''
from tutil import shape

shapesdict ={} # holds some shape information
shapesdict ={'triangle':3, 'rectangle':4, 'square':4, 'pentagon':5, 'hexagon':6}
shapetype = raw_input("Choose a shape name - Triangle, Square, Pentagon, Hexagon :")
shapetype = shapetype.lower()
sides = shapesdict[shapetype] 
shape(50, sides)

