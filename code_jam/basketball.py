# basketball 
# Robert pride
# put the robot on the screen

import pygame
# import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
 
running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,255,0))
    # screen.blit(my_image, image_rect)
    pygame.display.flip()