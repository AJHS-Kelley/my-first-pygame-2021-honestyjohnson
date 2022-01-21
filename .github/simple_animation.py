# Simple Animation with PyGame, Honesty Johnson, 1/21/21, 8:35AM, v0.7

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
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Check to see if the player has stopped moving.
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False 
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False 
            if event.key == K_UP or event.key == K_w:
                moveUp = False 
            if event.key == K_DOWN or event.key == K_s: 
                moveDown = False 
            if event.key == K_x: # Use x to teleport the player. 
               player.top = random.randint(0, WINDOWHEIGHT - player.height)
               player.left = random.randint(0, WINDOWWIDTH - player.width) 



