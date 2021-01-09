from tkinter import *

root = Tk()
root.state('zoomed')
root.geometry('800x600')

c = Canvas(root, bg='black')
c.pack(fill="both", expand=True)

root.mainloop()