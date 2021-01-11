from tkinter import Tk
from random import randint
import pygame

pygame.init()
root = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Sets the application to full screen
screen_size = pygame.display.get_surface() # gets the surface size
pygame.display.set_caption('Bouncing DVD') # sets the caption of the window
image = pygame.image.load('rowlett.png') # loads up the image
CONSTANTS = {'x_move': 3, 
            'y_move': 3, 
            'x': randint(0, screen_size.get_width() - image.get_width()), 
            'y':randint(0, screen_size.get_height() - image.get_height())} # constants

black = (0, 0, 0) # background color to fill in rgb values
timer = pygame.time.Clock() # clock to update the frames


def moving():
    '''
    Moves the image by changing its coordinates at incremental values. When the image hits one of the sides of the screen
    the value becomes negative.
    '''
    global CONSTANTS
    if CONSTANTS['x'] + image.get_width() >=screen_size.get_width() or CONSTANTS['x'] <= 0:
        CONSTANTS['x_move'] = -CONSTANTS['x_move']
    if CONSTANTS['y'] + image.get_height() >= screen_size.get_height() or CONSTANTS['y'] <= 0:
        CONSTANTS['y_move'] = -CONSTANTS['y_move']
    CONSTANTS['x'] += CONSTANTS['x_move']
    CONSTANTS['y'] += CONSTANTS['y_move']
    root.blit(image, (CONSTANTS['x'], CONSTANTS['y']))


while True:
    root.fill(black) 
    moving()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    timer.tick(30)
