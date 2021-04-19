from tkinter import *
root = Tk()
r = IntVar()
r.set("2")

toppings = [
    ("Pepperoni", "Pepperoni"),
    ("cheese", "cheese"), 
    ("mushroom", "mushroom"),
    ("onion", "onion")
    
]
pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in toppings:
    Radiobutton(root, text=text, variable= pizza, value= topping, anchor=W).pack()

def clickme(value):
    mylabel = Label(root, text= value)
    mylabel.pack()
    
Radiobutton(root, text="option 1", variable= r, value=1, command=lambda: clickme(r.get())).pack()
Radiobutton(root, text="option 2", variable= r, value=2, command=lambda: clickme(r.get())).pack()
mybutton = Button(root, text="click me", command= lambda: clickme(pizza.get())).pack()

mylabel = Label(root, text= r.get())
mylabel.pack()

root.mainloop()
