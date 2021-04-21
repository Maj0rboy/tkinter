from tkinter import *
root = Tk()
root.geometry("400x400")

# var = IntVar()

var = StringVar()

check = Checkbutton(root, text="check me!!", variable= var, onvalue="on", offvalue="off")
check.deselect()
check.pack()

def show():
    mylabel = Label(root, text=var.get()).pack()
    
    
btn = Button(root, text="show selection", command=show).pack()
mainloop()
