from tkinter import *
root = Tk()
def clickme():
    mylabel = Label(root,text="you clicked me. Thank you",bg="blue")
    mylabel.grid()
mybutton = Button(root, text="click me",command=clickme, bg="red")
mybutton.grid()
mybutton.mainloop()