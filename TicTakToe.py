import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.iconbitmap("C:\\Users\\админ\\Desktop\\python projects\\Tic Tac Toe game\\icon1.ico")
root.title("Крестики-нолики")

buttons = [] 
current_player = "X"

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            return True
    return False


def on_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        
        if check_winner():
            messagebox.showinfo("Победа!", f"Победил {current_player}!")
        elif all(button["text"] != "" for button in buttons):
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!")
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

def reset_game():
    global current_player
    current_player = "X"
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

for i in range(9):  
    button = tk.Button(
        root, 
        text="",  
        font=("Arial", 30),  
        width=5,  
        height=2,
        command=lambda idx=i: on_click(idx)
    )
    button.grid(row=i//3, column=i%3)  
    buttons.append(button)  

reset_button = tk.Button(root, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we") 

root.mainloop()