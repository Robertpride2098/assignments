# basketball 
# Robert pride
# put the robot on the screen

import pygame
# import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False