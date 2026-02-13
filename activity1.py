from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("500x500")
window.title("image")

upload = Image.open("download.jpg")
image = ImageTk.PhotoImage(upload)

label = Label(window, image=image, height=250, width=250)
label.image = image
label.pack()

text = Label(window, text="This is the original Windows© background!")
text.pack()

window.mainloop()