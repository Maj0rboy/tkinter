from tkinter import *
root = Tk()
e=Entry(root)
e.grid(row=0,column=0, columnspan=4)
e.insert(0,"enter your name")
def clickme():
    hello = "Hello " + e.get()
    mylabel = Label(root,text=hello,bg="blue")
    mylabel.grid()
mybutton = Button(root,text="click me",fg="black",command=clickme, padx=50)
mybutton.grid()
mybutton.mainloop()
e.mainloop()