from tkinter import *
root = Tk()
frame = LabelFrame(root, padx=10, pady=10)

button = Button(frame, text="dont click me")
button.grid(row=0, column=0)
frame.pack(padx= 100, pady=100)

root.mainloop()