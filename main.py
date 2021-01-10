from tkinter import Tk, Canvas, NW
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.update()
root.title('Bouncing DVD')
root.state('zoomed')
root.geometry('800x600')

width = root.winfo_width()
height = root.winfo_height()

img = ImageTk.PhotoImage(file="windows.webp")

c = Canvas(root, bg='black')
c.pack(fill="both", expand=True)


image = c.create_image(randint(0, 800), randint(0, 600), anchor=NW, image=img)  # Main image

x_move = 3
y_move = 3


def moving():
    '''
    Moves the image by changing its coordinates at incremental values. When the image hits one of the sides of the screen
    the value becomes negative.
    '''
    global x_move, y_move
    c.move(image, x_move, y_move)
    if c.coords(image)[0] + img.width() >= width or c.coords(image)[0] <= 0:
        x_move = -x_move
    if c.coords(image)[1] + img.height() >= height or c.coords(image)[1] <= 0:
        y_move = -y_move
    root.after(8, moving)


moving()

root.mainloop()
