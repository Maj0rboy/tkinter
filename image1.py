from tkinter import * 
from PIL import ImageTk,Image
root = Tk()
root.title("image with tkinter")
my_img = ImageTk.PhotoImage(Image.open("./images/pikachu.jpg"))
my_label = Label(image=my_img)
my_label.pack()

my_button = Button(root,text="quit", command=root.quit)
my_button.pack()

root.mainloop()