import tkinter as tk

board = [[' ' for x in range(3)] for y in range(3)]
players = ['X', 'O']

def print_board():
    print("---------")
    for row in board:
        print("|", row[0], row[1], row[2], "|")
    print("---------")

def is_winner(player):
    # Check rows
    for row in board:
        if row == [player, player, player]:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_tie():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def update_cell(row, col, player):
    board[row][col] = player
    b = buttons[row][col]
    b.config(text=player, state='disabled')
    check_game_over()

def check_game_over():
    if is_winner(players[0]):
        tk.messagebox.showinfo("Tic Tac Toe", f"{players[0]} wins!")
        window.quit()
    elif is_tie():
        tk.messagebox.showinfo("Tic Tac Toe", "It's a tie.")
        window.quit()

def button_click(row, col):
    update_cell(row, col, players[len([cell for row in board for cell in row if cell != ' ']) % 2])

window = tk.Tk()
buttons = [[tk.Button(master=window, height=3, width=6, font=("Arial", 16), command=lambda r=row, c=col: button_click(r, c)) for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        b = buttons[row][col]
        b.grid(row=row, column=col)

window.mainloop()
