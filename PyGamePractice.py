# PyGame Practice, Honesty Johnson, 11/29/21 8:33am, v0.0

import pygame, sys
from pygame.locals import *

#start Pygame
pygame.init()

# Create game window
windowSurface = pygame.display.set_mode(( 500, 400), 0, 32)
pygame.display.set_caption("Hello World!")

# Set Color Values 
BLACK = (0, 0, 0) 
WHITE = (255, 225, 225) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 