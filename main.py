from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.state('zoomed')
root.geometry('800x600')

img =  ImageTk.PhotoImage(file="windows.webp")  
c = Canvas(root, bg='black')
c.pack(fill="both", expand=True)
c.create_image(60, 50, anchor=NW, image=img)

root.mainloop()