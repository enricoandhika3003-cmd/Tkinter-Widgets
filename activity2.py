from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("virus scanner")

def alert():
    messagebox.showwarning("Virus Scanner 3000", "Stop! Virus Found.")
    
button = Button(window, text="Scanning for Virus. . .", command=alert, height=100, width=100)
button.pack()

window.mainloop()