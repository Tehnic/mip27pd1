import tkinter as tk
from tkinter import Entry, Label, Button

def show_game_screen():
    rules_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

def show_multiplier_screen():
    game_frame.pack_forget()
    multiplier_frame.pack(fill="both", expand=True)

def start_game():
    global current_number
    user_input = entry.get()
    if user_input.isdigit() and 20 <= int(user_input) <= 30:
        current_number = int(user_input)
        show_multiplier_screen()
    else:
        print("Please enter a valid number between 20 and 30")

def update_number(multiplier):
    global current_number, bank_points, total_points
    current_number *= multiplier
    
    if current_number % 2 == 0:
        total_points += 1
    else:
        total_points -= 1
    
    if current_number % 10 == 0 or current_number % 10 == 5:
        bank_points += 1
    
    current_number_label.config(text=str(current_number))
    bank_label.config(text=f"BANK: {bank_points}")
    points_label.config(text=f"POINTS: {total_points}")

# Initialize values
current_number = 20  # Example starting number
bank_points = 0
total_points = 0

# Create the main window
root = tk.Tk()
root.title("Game UI")
root.geometry("600x400")
root.configure(bg="#6A0DAD")

# Rules Screen
rules_frame = tk.Frame(root, bg="#6A0DAD")
rules_frame.pack(fill="both", expand=True)

rules_label = Label(rules_frame, text="GAME RULES!", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#6A0DAD")
rules_label.pack(pady=20)

rules_text = """
THE FIRST PLAYER CHOOSES A STARTING NUMBER BETWEEN 20 AND 30
 THEN PLAYERS TAKE TURNS MULTIPLYING IT BY 3, 4, OR 5;
IF THE RESULT IS EVEN, 1 POINT IS ADDED TO THE TOTAL SCORE
IF ODD, 1 POINT IS SUBTRACTED, AND IF IT ENDS IN 0 OR 5
1 POINT IS ADDED TO THE BANK; 

THE GAME ENDS WHEN THE NUMBER REACHES 3000 OR MORE
THE FINAL SCORE IS ADJUSTED BY THE BANK POINTS
IF THE FINAL SCORE IS EVEN, THE FIRST PLAYER WINS
OTHERWISE, THE SECOND PLAYER WINS."""


rules_description = Label(rules_frame, text=rules_text, font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD", justify="center")
rules_description.pack(pady=10)

next_button = Button(rules_frame, text="NEXT", font=("Comic Sans MS", 14, "bold"), fg="black", bg="#FF69B4", width=10, command=show_game_screen)
next_button.pack(pady=20)

# Game Screen
game_frame = tk.Frame(root, bg="#6A0DAD")

title_label = Label(game_frame, text="WELCOME TO THE GAME", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#6A0DAD")
title_label.pack(pady=30)

instruction_label = Label(game_frame, text="INPUT A NUMBER FROM 20 TO 30", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD")
instruction_label.pack(pady=10)

entry = Entry(game_frame, font=("Arial", 14), width=10, justify="center", bg="lightgray")
entry.pack(pady=10)

start_button = Button(game_frame, text="START", font=("Comic Sans MS", 14, "bold"), fg="black", bg="#FF69B4", width=10, command=start_game)
start_button.pack(pady=20)

# Multiplier Screen
multiplier_frame = tk.Frame(root, bg="#6A0DAD")

bank_label = Label(multiplier_frame, text=f"BANK: {bank_points}", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#6A0DAD")
bank_label.place(x=650, y=50)

points_label = Label(multiplier_frame, text=f"POINTS: {total_points}", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#6A0DAD")
points_label.place(x=650, y=80)

current_label = Label(multiplier_frame, text="CURRENT NUMBER", font=("Comic Sans MS", 16, "bold"), fg="white", bg="#6A0DAD")
current_label.pack(pady=20)

current_number_label = Label(multiplier_frame, text=str(current_number), font=("Arial", 18), width=10, justify="center", bg="lightgray")
current_number_label.pack(pady=10)

multiplier_label = Label(multiplier_frame, text="CHOOSE THE MULTIPLIER:", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#6A0DAD")
multiplier_label.pack(pady=20)

button_frame = tk.Frame(multiplier_frame, bg="#6A0DAD")
button_frame.pack()

button_3 = Button(button_frame, text="3", font=("Comic Sans MS", 14, "bold"), fg="black", bg="yellow", width=4, height=2, command=lambda: update_number(3))
button_3.grid(row=0, column=0, padx=20, pady=10)

button_4 = Button(button_frame, text="4", font=("Comic Sans MS", 14, "bold"), fg="black", bg="cyan", width=4, height=2, command=lambda: update_number(4))
button_4.grid(row=0, column=1, padx=20, pady=10)

button_5 = Button(button_frame, text="5", font=("Comic Sans MS", 14, "bold"), fg="black", bg="pink", width=4, height=2, command=lambda: update_number(5))
button_5.grid(row=0, column=2, padx=20, pady=10)

root.mainloop()
