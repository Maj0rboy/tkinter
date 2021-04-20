from tkinter import *
from tkinter import filedialog
root = Tk()

root.filename = filedialog.askopenfilename(initialdir="/users/stunna/document/kinter/images/", title= "my dialogbox", filetype=(("jpeg files", "*.jpeg"),("all files", "*.*")))
mainloop()