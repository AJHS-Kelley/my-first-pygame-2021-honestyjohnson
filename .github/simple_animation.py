# Simple Animation with PyGame, Honesty Johnson, 1/19/21, 9:22AM, v0.6

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.init() 
mainClock = pygame.time.Clock() 

# Setup the Pygame Window 
WINDOWWIDTH = 400 
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
pygame.display.set_caption('Animation Example!')

# Setup colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255) 

# Setup the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player= pygame.Rect( 300, 100, 50, 50)
foods = []

for i in range (20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

#Movement Variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False 

MOVESPEED = 6

# Run the game loop.
while True:
    # Check for events. 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False 
                moveLeft = True 
            if event.key == K_Right or event.key == K_d: 
                moveLeft = False
                moveRight = True 
            if event.key == K_UP or event.key == K_w:
                movedown = False 
                moveUp = True 
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False 
                moveDown = True 


MOVESPEED = 4


# Setup color values. 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 

# Setup the box data. 
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop. 
while True:
    # Check for QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)

    for b in boxes:
        # Change the keyboard variable 
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
            if b['dir'] == DONRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top += MOVESPEED
            if b['dir'] == UPLEFT:
                b['rect'].left -= MOVESPEED
                b['rect'].top -= MOVESPEED
            if b['dir'] == UPRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top -= MOVESPEED

