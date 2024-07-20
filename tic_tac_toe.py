from tkinter import *
from tkinter import messagebox

class PlayerNamesDialog:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Enter Player Names")

        self.player1_name = None
        self.player2_name = None

        label1 = Label(parent, text="Player 1 Name:", font=("Arial", 14), bg="#f0f0f0")
        label1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry1 = Entry(parent, font=("Arial", 14), bg="#f5f5f5", relief="solid", bd=1)
        self.entry1.grid(row=0, column=1, padx=10, pady=5)

        label2 = Label(parent, text="Player 2 Name:", font=("Arial", 14), bg="#f0f0f0")
        label2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry2 = Entry(parent, font=("Arial", 14), bg="#f5f5f5", relief="solid", bd=1)
        self.entry2.grid(row=1, column=1, padx=10, pady=5)

        start_button = Button(parent, text="Start Game", font=("Arial", 14), command=self.start_game, bg="#4caf50", fg="white", relief="raised")
        start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def start_game(self):
        self.player1_name = self.entry1.get()
        self.player2_name = self.entry2.get()
        if not self.player1_name or not self.player2_name:
            messagebox.showerror("Error", "Please enter names for both players.")
        else:
            self.parent.destroy()

class TicTacToe:
    def __init__(self, root, player1_name, player2_name):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.frame = Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=20)

        title_label = Label(self.frame, text="Tic Tac Toe", font=("Arial", 24, "bold"), fg="#4caf50", bg="#f0f0f0")
        title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.player1_name = player1_name
        self.player2_name = player2_name
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.player1_label = Label(self.frame, text=f"{self.player1_name} (X)", font=("Arial", 16), bg="#f0f0f0")
        self.player1_label.grid(row=1, column=0, columnspan=3, padx=10)

        self.player2_label = Label(self.frame, text=f"{self.player2_name} (O)", font=("Arial", 16), bg="#f0f0f0")
        self.player2_label.grid(row=2, column=0, columnspan=3, padx=10)

        self.current_player_label = Label(self.frame, text=f"Current Player: {self.player1_name}", font=("Arial", 14), bg="#f0f0f0")
        self.current_player_label.grid(row=3, column=0, columnspan=3, padx=10)

        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.frame, text=" ", font=("Arial", 24), width=6, height=3,
                                            command=lambda row=i, col=j: self.on_button_click(row, col),
                                            bg="#e0e0e0", fg="#333333", bd=2, relief="raised")
                self.buttons[i][j].grid(row=i+4, column=j, padx=5, pady=5)

        self.update_current_player_label()

        exit_button = Button(self.frame, text="Exit", font=("Arial", 14), command=self.exit_game, bg="#f44336", fg="white", relief="raised")
        exit_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player, state="disabled", bg="#bbdefb")

            if self.check_winner(self.current_player):
                winner_name = self.player1_name if self.current_player == "X" else self.player2_name
                self.highlight_winning_line()
                messagebox.showinfo("Tic Tac Toe", f"{winner_name} wins!")
                self.reset_game()
            elif self.board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_current_player_label()

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def board_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].configure(text=" ", state="normal", bg="#e0e0e0")
        self.current_player = "X"
        self.update_current_player_label()

    def update_current_player_label(self):
        if self.current_player == "X":
            self.current_player_label.config(text=f"Current Player: {self.player1_name}")
            self.player1_label.config(font=("Arial", 16, "bold"), fg="#333333")
            self.player2_label.config(font=("Arial", 16), fg="#9e9e9e")
        else:
            self.current_player_label.config(text=f"Current Player: {self.player2_name}")
            self.player1_label.config(font=("Arial", 16), fg="#9e9e9e")
            self.player2_label.config(font=("Arial", 16, "bold"), fg="#333333")

    def highlight_winning_line(self):
        winning_lines = self.find_winning_lines(self.current_player)
        if winning_lines:
            for line in winning_lines:
                for row, col in line:
                    self.buttons[row][col].configure(bg="#a5d6a7")

    def find_winning_lines(self, player):
        winning_lines = []
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                winning_lines.append([(i, 0), (i, 1), (i, 2)])
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                winning_lines.append([(0, i), (1, i), (2, i)])
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            winning_lines.append([(0, 0), (1, 1), (2, 2)])
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            winning_lines.append([(0, 2), (1, 1), (2, 0)])
        return winning_lines

    def exit_game(self):
        self.root.destroy()
        import Menu_screen

def get_player_names():
    root = Tk()
    root.title("Enter Player Names")
    dialog = PlayerNamesDialog(root)
    root.mainloop()
    return dialog.player1_name, dialog.player2_name

if __name__ == "__main__":
    player1_name, player2_name = get_player_names()
    if player1_name and player2_name:
        root = Tk()
        root.title("Tic Tac Toe")
        root.configure(bg="#f0f0f0")

        game = TicTacToe(root, player1_name, player2_name)

        root.update()
        width = root.winfo_width() + 100
        height = root.winfo_height() + 50
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        root.geometry(f"{width}x{height}+{x}+{y}")

        root.mainloop()
