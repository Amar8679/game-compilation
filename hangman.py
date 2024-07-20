import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root, words_file):
        self.root = root
        self.load_words(words_file)
        self.init_ui()

    def load_words(self, filename):
        with open(filename, 'r') as file:
            self.text1 = file.read().splitlines()

    def new_game(self):
        self.secret_word = random.choice(self.text1)
        self.guessed_letters = []
        self.attempts_left = 6
        self.init_drawing_canvas()
        self.update_display()

    def update_display(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 30, text=f"Attempts Left: {self.attempts_left}", font=('Comic Sans MS', 14), anchor='center', fill='white')
        word_display = ''
        for char in self.secret_word:
            if char in self.guessed_letters:
                word_display += char + ' '
            else:
                word_display += '_ '
        self.canvas.create_text(200, 100, text=word_display, font=('Comic Sans MS', 24), anchor='center', fill='white')
        self.drawing_canvas.delete("all")
        self.draw_hangman()

    def draw_hangman(self):
        draw_functions = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm, self.draw_left_leg, self.draw_right_leg]
        for i in range(6 - self.attempts_left):
            draw_functions[i]()
        if self.attempts_left == 0:
            self.draw_gallows()
            self.draw_rope()

    def draw_head(self):
        self.drawing_canvas.create_oval(90, 70, 170, 150, outline='white', fill='white', width=2)

    def draw_body(self):
        self.drawing_canvas.create_line(130, 150, 130, 270, fill='white', width=4)

    def draw_left_arm(self):
        self.drawing_canvas.create_line(130, 170, 80, 220, fill='white', width=4)

    def draw_right_arm(self):
        self.drawing_canvas.create_line(130, 170, 180, 220, fill='white', width=4)

    def draw_left_leg(self):
        self.drawing_canvas.create_line(130, 270, 80, 320, fill='white', width=4)

    def draw_right_leg(self):
        self.drawing_canvas.create_line(130, 270, 180, 320, fill='white', width=4)

    def draw_rope(self):
        self.drawing_canvas.create_line(130, 0, 130, 60, fill='saddle brown', width=4)
        self.drawing_canvas.create_line(130, 60, 130, 70, fill='saddle brown', width=4)
        self.drawing_canvas.create_oval(80, 60, 180, 160, outline='saddle brown', width=4)

    def draw_gallows(self):
        self.drawing_canvas.create_line(55, 50, 55, 350, fill='tomato3', width=4)
        self.drawing_canvas.create_line(55, 50, 200, 50, fill='tomato3', width=4)
        self.drawing_canvas.create_line(200, 50, 200, 150, fill='tomato3', width=4)

    def guess_letter(self, event=None):
        letter = self.letter_entry.get().lower().strip()
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single alphabetic character.")
        elif letter in self.guessed_letters:
            messagebox.showinfo("Duplicate Guess", f"You already guessed '{letter}'. Try another letter.")
        else:
            self.guessed_letters.append(letter)
            if letter not in self.secret_word:
                self.attempts_left -= 1
            self.update_display()
            if all(char in self.guessed_letters for char in self.secret_word):
                messagebox.showinfo("Congratulations!", "You guessed the word! You win!")
                self.new_game()
            elif self.attempts_left == 0:
                messagebox.showinfo("Game Over", f"Out of attempts! The word was '{self.secret_word}'. Try again.")
                self.new_game()

        self.letter_entry.delete(0, tk.END)

    def init_ui(self):
        self.root.title("Hangman Game")
        self.root.geometry("800x400")
        self.root.configure(background='#6E7B91')
        content_frame = tk.Frame(self.root, bg='#6E7B91')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas = tk.Canvas(content_frame, width=400, height=200, bg="#99AAB5", highlightthickness=0)
        self.canvas.pack(pady=20)
        self.letter_entry = tk.Entry(content_frame, font=('Comic Sans MS', 14))
        self.letter_entry.pack(pady=10)
        self.letter_entry.bind("<Return>", self.guess_letter)
        guess_button = tk.Button(content_frame, text="Guess", font=("Comic Sans MS", 14), bg="#283149", fg="white", padx=20, pady=10, command=self.guess_letter)
        guess_button.pack(pady=10)
        exit_button = tk.Button(self.root, text="Exit", font=("Comic Sans MS", 12), bg="#283149", fg="white", padx=3, pady=2.5, command=self.exit_game)
        exit_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)
        content_frame.place(relx=0.67, rely=0.5, anchor='center')
        drawing_frame = tk.Frame(self.root, bg="#6E7B91")
        drawing_frame.place(relx=0, rely=0, relwidth=0.33, relheight=1)
        self.drawing_canvas = tk.Canvas(drawing_frame, bg="#6E7B91", width=260, height=400)
        self.drawing_canvas.pack()
        self.drawing_canvas.place(relx=0.5, rely=0.5, anchor='center')
        self.new_game()

    def init_drawing_canvas(self):
        self.drawing_canvas.delete("all")

    def exit_game(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root, 'text1.txt')
    root.mainloop()
