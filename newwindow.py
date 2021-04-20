from tkinter import *
root = Tk()

def open():
    # global my_label
    top = Toplevel()
    my_label = Label(top, text="stunna dboyyyyyyyyyy!!!!!")
    my_label.pack()
    btn2 = Button(top, text="close second window", command=top.destroy).pack()

btn = Button(root, text="open second window", command=open).pack()

mainloop()