# Simple Animation with PyGame, Honesty Johnson, 12/09/21, 8:56AM, v0.3

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.init() 

# Setup the Window 
WINDOWWIDTH = 400 
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variables. 
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4


# Setup color values. 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 