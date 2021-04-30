from tkinter import *
root = Tk()
root.geometry("400x400")

vertical = Scale(root, from_ = 0, to=200)
vertical.pack()

horizontal = Scale(root, from_ = 0, to = 250, orient=HORIZONTAL)
horizontal.pack()

mainloop()
