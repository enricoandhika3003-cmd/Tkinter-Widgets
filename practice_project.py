from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Rock Paper Scissors: The Game")
window.geometry("250x250")
window.config(bg="lightblue")

title = Label(window, text="Rock Paper Scissors: The Game", bg="lightblue")
title.pack()

score = Label(window, text="<---- Score ----> \nYou: 0 VS Computer: 0", bg="lightblue")
score.pack()

options = ["Rock 🪨", "Paper 📄", "Scissors ✂️"]
player_score = 0
computer_score = 0
winning_score = 5

for choice in options:
    button = Button(window, text=choice, width=15, command=lambda c=choice: rock_paper_scissors(c))
    button.pack()

def rock_paper_scissors(player_choice):
    global player_score, computer_score
    
    computer_choice = random.choice(options)
    results = f"Your choice: {player_choice}\nThe computer chose: {computer_choice}\n"
    
    if player_choice == computer_choice:
        results += "It's a tie!"
    elif (
        (player_choice == "Rock 🪨" and computer_choice == "Scissors ✂️") or
        (player_choice == "Paper 📄" and computer_choice == "Rock 🪨") or
        (player_choice == "Scissors ✂️" and computer_choice == "Paper 📄")):
        results+= f"{player_choice} beats {computer_choice}, \nYou win!"
        player_score += 1
    else:
        results += f"{computer_choice} beats {player_choice}, \nComputer wins!"
        computer_score += 1
    
    score.config(text=f"<---- Score ----> \nYou: {player_score} VS Computer: {computer_score}")
    messagebox.showinfo("Result", results)
    
    if player_score == winning_score:
        messagebox.showinfo("Game Over!", "\nYou won the game, Congratulations! 🎉")
        reset()
    elif computer_score == winning_score:
        messagebox.showinfo("Game Over!", "\nThe computer won the game, 💻 Try again. . .")
        reset()

def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score.config(text="<---- Score ----> \nYou: 0 VS Computer: 0")

reset_button = Button(window, text="Reset Game", bg="red", fg="white", command=reset)
reset_button.pack()

window.mainloop()