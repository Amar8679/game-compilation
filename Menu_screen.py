from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import os

def hangman_clicked(event):
    root.destroy()
    os.system('python hangman.py')

def tic_tac_toe_clicked(event):
    root.destroy()
    os.system('python tic_tac_toe.py')

def snake_clicked(event):
    root.destroy()
    os.system('python snake.py')

def game2048_clicked(event):
    root.destroy()
    os.system('python g_2048.py')

root = Tk()
root.geometry("500x700")
root.configure(background='lightblue4')

title = Label(root, text="GAME ON", font=("Arial", 24, "bold"), fg="white", bg='lightblue4')
title.grid(row=0, column=0, columnspan=2, pady=20)

# Hangman
game1_title = Label(root, text="Hangman", font=("Arial", 18), fg="white", bg='lightblue4', cursor="hand2")
game1_title.grid(row=1, column=0, padx=20, pady=5, sticky='w')
game1_title.bind("<Button-1>", hangman_clicked)

hangman_img = Image.open("hangman.png")
hangman_img = hangman_img.resize((200, 200), Image.ANTIALIAS)
hangman_image = ImageTk.PhotoImage(hangman_img)
hangman_img_label = Label(root, image=hangman_image, cursor="hand2")
hangman_img_label.image = hangman_image
hangman_img_label.grid(row=2, column=0, padx=20, pady=5, sticky='w')
hangman_img_label.bind("<Button-1>", hangman_clicked)

# Tic Tac Toe
game2_title = Label(root, text="Tic Tac Toe", font=("Arial", 18), fg="white", bg='lightblue4', cursor="hand2")
game2_title.grid(row=1, column=1, padx=20, pady=5, sticky='w')
game2_title.bind("<Button-1>", tic_tac_toe_clicked)

tic_tac_toe_img = Image.open("tic_tac_toe.png")
tic_tac_toe_img = tic_tac_toe_img.resize((200, 200), Image.ANTIALIAS)
tic_tac_toe_image = ImageTk.PhotoImage(tic_tac_toe_img)
tic_tac_toe_img_label = Label(root, image=tic_tac_toe_image, cursor="hand2")
tic_tac_toe_img_label.image = tic_tac_toe_image
tic_tac_toe_img_label.grid(row=2, column=1, padx=20, pady=5, sticky='w')
tic_tac_toe_img_label.bind("<Button-1>", tic_tac_toe_clicked)

# Snake Game
game3_title = Label(root, text="Snake Game", font=("Arial", 18), fg="white", bg='lightblue4', cursor="hand2")
game3_title.grid(row=3, column=0, padx=20, pady=5, sticky='w')
game3_title.bind("<Button-1>", snake_clicked)

snake_img = Image.open("snake.png")
snake_img = snake_img.resize((200, 200), Image.ANTIALIAS)
snake_image = ImageTk.PhotoImage(snake_img)
snake_img_label = Label(root, image=snake_image, cursor="hand2")
snake_img_label.image = snake_image
snake_img_label.grid(row=4, column=0, padx=20, pady=5, sticky='w')
snake_img_label.bind("<Button-1>", snake_clicked)

# 2048
game4_title = Label(root, text="2048", font=("Arial", 18), fg="white", bg='lightblue4', cursor="hand2")
game4_title.grid(row=3, column=1, padx=20, pady=5, sticky='w')
game4_title.bind("<Button-1>", game2048_clicked)

game2048_img = Image.open("2048.png")
game2048_img = game2048_img.resize((200, 200), Image.ANTIALIAS)
game2048_image = ImageTk.PhotoImage(game2048_img)
game2048_img_label = Label(root, image=game2048_image, cursor="hand2")
game2048_img_label.image = game2048_img
game2048_img_label.grid(row=4, column=1, padx=20, pady=5, sticky='w')
game2048_img_label.bind("<Button-1>", game2048_clicked)

# Exit
exit_button = Button(root, text="Exit", font=("Comic Sans MS", 12), bg="#283149", fg="white", padx=3, pady=2.5, command=root.destroy)
exit_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
