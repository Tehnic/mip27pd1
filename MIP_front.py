import tkinter as tk
from tkinter import Entry, Label, Button

def show_game_screen():
    rules_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)


def show_mistake_game_screen():
    game_frame.pack_forget()
    mistake_game_frame.pack(fill="both", expand=True)


def show_multiplier_screen():
    game_frame.pack_forget()
    multiplier_frame.pack(fill="both", expand=True)
    print("Current number is: ", current_number)
 
   
def show_from_mistake_to_multiplier_screen():
    mistake_game_frame.pack_forget()
    multiplier_frame.pack(fill="both", expand=True)
    print("Current number is: ", current_number)



#def other_start_game():
#    global current_number
#    user_input = entry.get()
#    if user_input.isdigit() and 20 <= int(user_input) <= 30:
#        current_number = int(user_input)
#        show_multiplier_screen()
#    else:
#        print("Please enter a valid number between 20 and 30")



def start_game():
    global current_number
    user_input = entry.get()
    if user_input.isdigit() and 20 <= int(user_input) <= 30:
        #print("input mistake is ",input_mistake)
        current_number = int(user_input)
        current_number_label.config(text=str(current_number))
        show_multiplier_screen()
    else:
       print("Please enter a valid number between 20 and 30")
       show_mistake_game_screen()
        
        
def mistake_start_game():
    global current_number
    mistake_user_input = mistake_entry.get()
    if mistake_user_input.isdigit() and 20 <= int(mistake_user_input) <= 30:
        current_number = int(mistake_user_input)
        current_number_label.config(text=str(current_number))
        show_from_mistake_to_multiplier_screen()
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
#current_number = 20  # Example starting number
current_number=0
bank_points = 0
total_points = 0

# Create the main window
root = tk.Tk()
root.title("Game UI")
#root.geometry("650x460")
root.geometry("800x460")
root.configure(bg="#6A0DAD")

# Rules Screen
#rules_frame = tk.Frame(root, bg="#6A0DAD")
rules_frame = tk.Canvas(root, bg="#6A0DAD")
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

#next_button = Button(rules_frame, text="NEXT", font=("Comic Sans MS", 14, "bold"), fg="black", bg="#FF69B4", width=10, command=show_game_screen)
#next_button.pack(pady=20)

next_button_circle_1 = rules_frame.create_oval(330, 360, 370, 400, fill="yellow", outline="black")
next_button_circle_2 = rules_frame.create_oval(440, 360, 480, 400, fill="yellow", outline="black")
next_button_circle_3 = rules_frame.create_oval(330, 400, 370, 440, fill="yellow", outline="black")
next_button_circle_4 = rules_frame.create_oval(440, 400, 480, 440, fill="yellow", outline="black")
next_button_rectangle_1 = rules_frame.create_rectangle(350, 360, 460, 440, fill="yellow", outline="black")
next_button_rectangle_2 = rules_frame.create_rectangle(330, 380, 480, 420, fill="yellow", outline="black")
next_button = rules_frame.create_text(407, 398, text="NEXT", font=("Comic Sans MS", 14, "bold"), fill="black")

rules_frame.addtag_withtag("next_button", next_button_circle_1)
rules_frame.addtag_withtag("next_button", next_button_circle_2)
rules_frame.addtag_withtag("next_button", next_button_circle_3)
rules_frame.addtag_withtag("next_button", next_button_circle_4)
rules_frame.addtag_withtag("next_button", next_button_rectangle_1)
rules_frame.addtag_withtag("next_button", next_button_rectangle_2)

rules_frame.tag_bind("next_button", "<Button-1>", lambda event: show_game_screen())


# Game Screen
#game_frame = tk.Frame(root, bg="#6A0DAD")
game_frame = tk.Canvas(root, bg="#6A0DAD")

title_label = Label(game_frame, text="WELCOME TO THE GAME", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#6A0DAD")
title_label.pack(pady=30)

instruction_label = Label(game_frame, text="INPUT A NUMBER FROM 20 TO 30", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD")
instruction_label.pack(pady=10)

entry = Entry(game_frame, font=("Arial", 14), width=10, justify="center", bg="lightgray")
entry.pack(pady=10)

#start_button = Button(game_frame, text="START", font=("Comic Sans MS", 14, "bold"), fg="black", bg="#FF69B4", width=10, command=start_game)
#start_button.pack(pady=20)

start_button_circle_1 = game_frame.create_oval(330, 210, 370, 250, fill="yellow", outline="black")
start_button_circle_2 = game_frame.create_oval(440, 210, 480, 250, fill="yellow", outline="black")
start_button_circle_3 = game_frame.create_oval(330, 250, 370, 290, fill="yellow", outline="black")
start_button_circle_4 = game_frame.create_oval(440, 250, 480, 290, fill="yellow", outline="black")
start_button_rectangle_1 = game_frame.create_rectangle(350, 210, 460, 290, fill="yellow", outline="black")
start_button_rectangle_2 = game_frame.create_rectangle(330, 230, 480, 270, fill="yellow", outline="black")
start_button = game_frame.create_text(407, 248, text="START", font=("Comic Sans MS", 14, "bold"), fill="black")

game_frame.addtag_withtag("start_button", start_button_circle_1)
game_frame.addtag_withtag("start_button", start_button_circle_2)
game_frame.addtag_withtag("start_button", start_button_circle_3)
game_frame.addtag_withtag("start_button", start_button_circle_4)
game_frame.addtag_withtag("start_button", start_button_rectangle_1)
game_frame.addtag_withtag("start_button", start_button_rectangle_2)

game_frame.tag_bind("start_button", "<Button-1>", lambda event: start_game())




# Mistake Game Screen
#mistake_game_frame = tk.Frame(root, bg="#6A0DAD")
mistake_game_frame = tk.Canvas(root, bg="#6A0DAD")

mistake_title_label = Label(mistake_game_frame, text="WELCOME TO THE GAME", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#6A0DAD")
mistake_title_label.pack(pady=30)

mistake_instruction_label = Label(mistake_game_frame, text="INPUT A NUMBER FROM 20 TO 30", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD")
mistake_instruction_label.pack(pady=10)

mistake_entry = Entry(mistake_game_frame, font=("Arial", 14), width=10, justify="center", bg="lightgray")
mistake_entry.pack(pady=10)

mistake_input_mistake_label = Label(mistake_game_frame, text="Ievadītais skaitlis nav norādītajā diapazonā", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD")
mistake_input_mistake_label.pack(pady=10)

#mistake_start_button = Button(mistake_game_frame, text="START", font=("Comic Sans MS", 14, "bold"), fg="black", bg="#FF69B4", width=10, command=mistake_start_game)
#mistake_start_button.pack(pady=20)

mistake_start_button_circle_1 = mistake_game_frame.create_oval(330, 250, 370, 290, fill="yellow", outline="black")
mistake_start_button_circle_2 = mistake_game_frame.create_oval(440, 250, 480, 290, fill="yellow", outline="black")
mistake_start_button_circle_3 = mistake_game_frame.create_oval(330, 290, 370, 330, fill="yellow", outline="black")
mistake_start_button_circle_4 = mistake_game_frame.create_oval(440, 300, 480, 330, fill="yellow", outline="black")
mistake_start_button_rectangle_1 = mistake_game_frame.create_rectangle(350, 250, 460, 330, fill="yellow", outline="black")
mistake_start_button_rectangle_2 = mistake_game_frame.create_rectangle(330, 270, 480, 310, fill="yellow", outline="black")
mistake_mistake_start_button = mistake_game_frame.create_text(407, 288, text="START", font=("Comic Sans MS", 14, "bold"), fill="black")

mistake_game_frame.addtag_withtag("mistake_start_button", mistake_start_button_circle_1)
mistake_game_frame.addtag_withtag("mistake_start_button", mistake_start_button_circle_2)
mistake_game_frame.addtag_withtag("mistake_start_button", mistake_start_button_circle_3)
mistake_game_frame.addtag_withtag("mistake_start_button", mistake_start_button_circle_4)
mistake_game_frame.addtag_withtag("mistake_start_button", mistake_start_button_rectangle_1)
mistake_game_frame.addtag_withtag("mistake_start_button", mistake_start_button_rectangle_2)

mistake_game_frame.tag_bind("mistake_start_button", "<Button-1>", lambda event: mistake_start_game())



# Multiplier Screen
#multiplier_frame = tk.Frame(root, bg="#6A0DAD")
multiplier_frame = tk.Canvas(root, bg="#6A0DAD")

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

#button_frame = tk.Frame(multiplier_frame, bg="#6A0DAD")
#button_frame.pack()

#button_3 = Button(button_frame, text="3", font=("Comic Sans MS", 14, "bold"), fg="black", bg="yellow", width=4, height=2, command=lambda: update_number(3))
#button_3.grid(row=0, column=0, padx=20, pady=10)

#button_4 = Button(button_frame, text="4", font=("Comic Sans MS", 14, "bold"), fg="black", bg="cyan", width=4, height=2, command=lambda: update_number(4))
#button_4.grid(row=0, column=1, padx=20, pady=10)

#button_5 = Button(button_frame, text="5", font=("Comic Sans MS", 14, "bold"), fg="black", bg="pink", width=4, height=2, command=lambda: update_number(5))
#button_5.grid(row=0, column=2, padx=20, pady=10)

button_3 = multiplier_frame.create_oval(200, 220, 300, 320, fill="yellow", outline="black")
button_3_number= multiplier_frame.create_text(250, 270, text="3", font=("Comic Sans MS", 14, "bold"), fill="black")
multiplier_frame.tag_bind(button_3, "<Button-1>", lambda event: update_number(3))

button_4 = multiplier_frame.create_oval(350, 220, 450, 320, fill="cyan", outline="black")
button_4_number= multiplier_frame.create_text(400, 270, text="4", font=("Comic Sans MS", 14, "bold"), fill="black")
multiplier_frame.tag_bind(button_4, "<Button-1>", lambda event: update_number(4))

button_5 = multiplier_frame.create_oval(500, 220, 600, 320, fill="pink", outline="black")
button_5_number= multiplier_frame.create_text(550, 270, text="5", font=("Comic Sans MS", 14, "bold"), fill="black")
multiplier_frame.tag_bind(button_5, "<Button-1>", lambda event: update_number(5))

root.mainloop()
