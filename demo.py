from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.title("image")

insert = Image.open("download.jpg")
image = ImageTk.PhotoImage(insert)

label = Label(root, image=image, height=250, width=250)
#button = Button(root, image=image, height=100, width=100)
#messagebox.Display(title, message)

#messagebox.askquestion("Suggestion box", "Is this lesson fun?")

root.mainloop()