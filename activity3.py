from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Root Window")

label = Label(root, text="This is the ROOT window!")
label.pack()

def open():
    top = Toplevel()
    top.geometry("250x250")
    top.title("Top Window")

    label2 = Label(top, text="This is the TOP window!")
    label2.pack()
    
    top.mainloop()
    

button = Button(root, text="OPEN TOP window", command=open, height=100, width=100)
button.pack()

root.mainloop()