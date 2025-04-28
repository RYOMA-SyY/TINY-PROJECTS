import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import webbrowser

leaderboard = {"X": 0, "O": 0}
player_x_name = "Player X"
player_o_name = "Player O"

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def highlight_winner(combo):
    for index in combo:
        buttons[index].config(bg="yellow")

def on_click(button, index):
    global turn, board, buttons
    if board[index] == ' ':
        board[index] = turn
        button.config(text=turn, state=tk.DISABLED, foreground="blue" if turn == 'X' else "red")
        play_sound("move")
        if check_win(board, turn):
            play_sound("win")
            messagebox.showinfo("Game Over", f"Player {turn} wins!")
            update_leaderboard(turn)
            reset_game()
        elif ' ' not in board:
            play_sound("draw")
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            turn = 'O' if turn == 'X' else 'X'
    else:
        messagebox.showwarning("Invalid Move", "This cell is already taken!")

def reset_game():
    global board, buttons, turn
    board = [' '] * 9
    turn = 'X'
    for button in buttons:
        button.config(text=' ', state=tk.NORMAL, foreground="black")

def restart_game():
    reset_game()

def start_game():
    global buttons, board, turn
    turn = 'X'
    board = [' '] * 9

    # Create the game window
    game_window = tk.Toplevel(root)
    game_window.title("Tic-Tac-Toe")
    game_window.geometry("400x400")
    game_window.resizable(False, False)
    game_window.configure(bg="#f0f0f0")

    # Create a grid of buttons
    global buttons
    buttons = []
    frame = ttk.Frame(game_window, padding=10)
    frame.pack(expand=True)
    for i in range(9):
        button = tk.Button(frame, text=' ', font=("Helvetica", 20), width=5, height=2,
                           bg="#ffffff", command=lambda b=i: on_click(buttons[b], b))
        button.grid(row=i // 3, column=i % 3, sticky="nsew", padx=5, pady=5)
        button.bind("<Enter>", on_hover)
        button.bind("<Leave>", on_leave)
        buttons.append(button)

    # Configure grid weights for responsiveness
    for i in range(3):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)

    restart_button = ttk.Button(game_window, text="Restart", command=restart_game)
    restart_button.pack(pady=10)

def show_settings():
    messagebox.showinfo("Settings", "Settings feature coming soon!")

def show_credits():
    messagebox.showinfo("Credits", "Tic-Tac-Toe Game\nDeveloped by: RIYOMA")

def main_menu():
    global root
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("400x400")
    root.resizable(False, False)
    root.configure(bg="#282c34")

    # Title Label
    title_label = tk.Label(root, text="Tic-Tac-Toe", font=("Helvetica", 24, "bold"), bg="#282c34", fg="white")
    title_label.pack(pady=20)

    # Play Button
    play_button = ttk.Button(root, text="Play", style="Menu.TButton", command=start_game)
    play_button.pack(pady=10)

    # Settings Button
    settings_button = ttk.Button(root, text="Settings", style="Menu.TButton", command=show_settings)
    settings_button.pack(pady=10)

    # Credits Button
    credits_button = ttk.Button(root, text="Credits", style="Menu.TButton", command=show_credits)
    credits_button.pack(pady=10)

    # Apply modern styling
    style = ttk.Style()
    style.configure("Menu.TButton", font=("Helvetica", 16), padding=10)
    style.configure("TButton", font=("Helvetica", 20), padding=10)
    style.configure("TFrame", background="#f0f0f0")

    root.mainloop()

def play_sound(event):
    pygame.mixer.init()
    if event == "move":
        pygame.mixer.Sound("move.wav").play()
    elif event == "win":
        pygame.mixer.Sound("win.wav").play()
    elif event == "draw":
        pygame.mixer.Sound("draw.wav").play()

    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)  # Loop indefinitely

def ai_move():
    # Implement AI logic here (e.g., minimax algorithm)
    pass

def apply_theme(theme):
    if theme == "dark":
        root.configure(bg="#282c34")
        style.configure("TButton", background="#444", foreground="white")
    elif theme == "light":
        root.configure(bg="#f0f0f0")
        style.configure("TButton", background="#fff", foreground="black")

def update_leaderboard(winner):
    if winner in leaderboard:
        leaderboard[winner] += 1

def start_timer():
    # Implement a countdown timer
    pass

def on_hover(event):
    event.widget.config(background="#ddd")

def on_leave(event):
    event.widget.config(background="#fff")

def share_result():
    webbrowser.open("https://twitter.com/intent/tweet?text=I%20just%20played%20Tic-Tac-Toe!")

if __name__ == "__main__":
    main_menu()