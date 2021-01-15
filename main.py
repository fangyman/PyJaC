from tkinter import filedialog, Tk
from random import randint
import pygame
from pygame_widgets import Slider, Button, TextBox
import easygui

global image
pygame.init()
# Sets the application to full screen
root = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_size = pygame.display.get_surface()  # gets the surface size
pygame.display.set_caption('Bouncing Windows')  # sets the caption of the window
image = pygame.image.load('dvd.jpg')  # loads up the image

CONSTANTS = {'x_move': 3,
             'y_move': 3,
             'x': randint(0, screen_size.get_width() - image.get_width() - 100),
             'y': randint(0, screen_size.get_height() - image.get_height())}  # constants

black = (0, 0, 0)  # background color to fill in rgb values
timer = pygame.time.Clock()  # clock to update the frames
xslider = Slider(root, screen_size.get_width() - 80, 100, 60, 40, min=0,
                 max=50, step=1, colour=(220,174,150), handleColour=(255, 255, 255), handleRadius=15, curved=True)
xtextbox = TextBox(root, screen_size.get_width() - 100, 150, 100, 40, fontSize=15, borderColour=(91,100,103))
yslider = Slider(root, screen_size.get_width() - 80, 0, 60, 40, min=0,
                 max=50, step=1, colour=(220,174,150), handleColour=(255, 255, 255), handleRadius=15, curved=True)
ytextbox = TextBox(root, screen_size.get_width() - 100, 50, 100, 40, fontSize=15,  borderColour=(91,100,103))
quitButton = Button(root, screen_size.get_width() - 100, screen_size.get_height() - 80, 100, 50, text='Quit',
                    fontSize=20, margin=20, inactiveColour=(220,174,150), radius=20, onClick=lambda: pygame.quit())
fileButton = Button(root, screen_size.get_width() - 100, screen_size.get_height() - 150, 100, 60, text='File Select',
                    fontSize=20, margin=10, inactiveColour=(220,174,150), radius=20)
FB = pygame.Rect(screen_size.get_width() - 100, screen_size.get_height() - 150, 100, 60)


def moving():
    '''
    Moves the image by changing its coordinates at incremental values. When the image hits one of the sides of the screen
    the value becomes negative.
    '''
    global CONSTANTS
    if CONSTANTS['x'] + image.get_width() + 100 >= screen_size.get_width() or CONSTANTS['x'] <= 0:
        CONSTANTS['x_move'] = -CONSTANTS['x_move']
    if CONSTANTS['y'] + image.get_height() >= screen_size.get_height() or CONSTANTS['y'] <= 0:
        CONSTANTS['y_move'] = -CONSTANTS['y_move']
    CONSTANTS['x'] += CONSTANTS['x_move']
    CONSTANTS['y'] += CONSTANTS['y_move']
    root.blit(image, (CONSTANTS['x'], CONSTANTS['y']))


while True:
    root.fill(black)
    pygame.draw.rect(root, (91,100,103),
                     pygame.Rect(screen_size.get_width() - 100, 0, 100, screen_size.get_height()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if FB.collidepoint(event.pos):
                    file = easygui.fileopenbox()
                    if file is not None:
                        checkfile = file.split(".")
                        if checkfile[len(checkfile)-1] != "py" and checkfile[len(checkfile)-1] != "md":
                            image = pygame.image.load(file)
                            CONSTANTS['x'] = randint(0, screen_size.get_width() - image.get_width() - 100)
                            CONSTANTS['y'] = randint(0, screen_size.get_height() - image.get_height())
                            pygame.display.update()

    events = pygame.event.get()
    xslider.listen(events)
    xslider.draw()
    xtextbox.setText(f"x-speed: {xslider.getValue()}")
    xtextbox.draw()
    if CONSTANTS['x_move'] > 0:
        CONSTANTS['x_move'] = xslider.getValue()
        if xslider.getValue() != 0:
            last_x = CONSTANTS['x_move']
    elif CONSTANTS['x_move'] == 0 and xslider.getValue() > 0:
        if last_x > 0:
            CONSTANTS['x_move'] = xslider.getValue()
        else:
            CONSTANTS['x_move'] = -xslider.getValue()
    else:
        CONSTANTS['x_move'] = -xslider.getValue()
        if xslider.getValue() != 0:
            last_x = CONSTANTS['x_move']

    yslider.listen(events)
    yslider.draw()
    ytextbox.setText(f"y-speed: {yslider.getValue()}")
    ytextbox.draw()
    if CONSTANTS['y_move'] > 0:
        CONSTANTS['y_move'] = yslider.getValue()
        if yslider.getValue() != 0:
            last_y = CONSTANTS['y_move']
    elif CONSTANTS['y_move'] == 0 and yslider.getValue() > 0:
        if last_y > 0:
            CONSTANTS['y_move'] = yslider.getValue()
        else:
            CONSTANTS['y_move'] = -yslider.getValue()
    else:
        CONSTANTS['y_move'] = -yslider.getValue()
        if yslider.getValue() != 0:
            last_y = CONSTANTS['y_move']
    quitButton.listen(events)
    quitButton.draw()
    fileButton.listen(events)
    fileButton.draw()
    moving()

    pygame.display.update()
    timer.tick(30)
