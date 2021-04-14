from tkinter import * 
from PIL import ImageTk,Image
root = Tk()
root.title("image with tkinter")
my_img1 = ImageTk.PhotoImage(Image.open("./images/pikachu.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("./images/bulbasaur.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("./images/charmander.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("./images/squirtle.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4]
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3)

def forward(image_number):
    return

button_back = Button(root,text="<<")
button_exit = Button(root,text="exit program", command=root.quit)
button_forward = Button(root,text=">>")
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()