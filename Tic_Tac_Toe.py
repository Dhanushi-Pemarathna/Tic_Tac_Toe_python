import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.config(bg="#f0f0f0")

current_player = "X"
buttons = []

# Style settings
style = {
    "X": {"fg": "white", "bg": "#007acc"},  # Blue
    "O": {"fg": "white", "bg": "#d43f3a"},  # Red
    "font": ("Helvetica", 32, "bold"),
    "default_bg": "#f9f9f9",
    "hover": "#dddddd"
}

# Check winner
def check_winner():
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for a, b, c in wins:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            messagebox.showinfo("Game Over", f"Player {buttons[a]['text']} wins!")
            reset_board()
            return
    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()

# On button click
def on_click(i):
    global current_player
    if buttons[i]["text"] == "":
        buttons[i]["text"] = current_player
        buttons[i]["fg"] = style[current_player]["fg"]
        buttons[i]["bg"] = style[current_player]["bg"]
        check_winner()
        current_player = "O" if current_player == "X" else "X"

# Reset board
def reset_board():
    global current_player
    for btn in buttons:
        btn["text"] = ""
        btn["bg"] = style["default_bg"]
    current_player = "X"

# Hover (optional visual)
def on_enter(btn):
    if btn["text"] == "":
        btn["bg"] = style["hover"]

def on_leave(btn):
    if btn["text"] == "":
        btn["bg"] = style["default_bg"]

# Create 3x3 buttons
for i in range(9):
    btn = tk.Button(root, text="", font=style["font"],
                    width=5, height=2, bg=style["default_bg"], relief="raised",
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    btn.bind("<Enter>", lambda e, b=btn: on_enter(b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(b))
    buttons.append(btn)

root.mainloop()
