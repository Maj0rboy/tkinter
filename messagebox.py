from tkinter import *
from tkinter import messagebox
root = Tk()

# askyesno, showinfo, showwarning, showerror, askquestion, askokcancel

def popup():
    response = messagebox.askokcancel("This is my pop up", "Hello world!")
    Label(root, text=response).pack()
button = Button(root, text="popup", command=popup).pack()
root.mainloop()