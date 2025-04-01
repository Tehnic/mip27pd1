import tkinter as tk
from tkinter import Entry, Label
import logging
import global_variables
import main


def show_game_screen():
    algorithm_choice_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)


def show_mistake_game_screen():
    game_frame.pack_forget()
    mistake_game_frame.pack(fill="both", expand=True)


def show_multiplier_screen():
    game_frame.pack_forget()
    multiplier_frame.pack(fill="both", expand=True)
    print("Current number is: ", global_variables.current_number)


def show_from_mistake_to_multiplier_screen():
    mistake_game_frame.pack_forget()
    multiplier_frame.pack(fill="both", expand=True)
    print("Current number is: ", global_variables.current_number)


def start_game():
    logging.basicConfig(filename="game.log", level=logging.INFO, datefmt="%H:%M:%S.%f")
    user_input = entry.get()
    if user_input.isdigit() and 20 <= int(user_input) <= 30:
        global_variables.current_number = int(user_input)
        main.generate_tree(int(user_input))
        logging.info(f"Sakuma skaitlis: {user_input}")
        if main.global_variables.chosen_player == 1:
            new_number = main.computer_logic(global_variables.chosen_algorithm, main.Tree(number=global_variables.current_number, player=1, children=[]))
            global_variables.current_number = new_number
        current_number_label.config(text=str(global_variables.current_number))
        show_multiplier_screen()
    else:
        print("Please enter a valid number between 20 and 30")
        show_mistake_game_screen()


def mistake_start_game():
    mistake_user_input = mistake_entry.get()
    if mistake_user_input.isdigit() and 20 <= int(mistake_user_input) <= 30:
        main.generate_tree(int(mistake_user_input))
        global_variables.current_number = int(mistake_user_input)
        if main.global_variables.chosen_player == 1:
            new_number = main.computer_logic(global_variables.chosen_algorithm, main.Tree(number=global_variables.current_number, player=1, children=[]))
            global_variables.current_number = new_number
        current_number_label.config(text=str(global_variables.current_number))
        show_from_mistake_to_multiplier_screen()
    else:
        print("Please enter a valid number between 20 and 30")


def update_number(multiplier):
    global_variables.current_number *= multiplier
    print("Player just did the move, current number", global_variables.current_number)
    if global_variables.current_number % 2 == 0:
        global_variables.total_points += 1
    else:
        global_variables.total_points -= 1
    if global_variables.current_number % 10 == 0 or global_variables.current_number % 10 == 5:
        global_variables.bank_points += 1
    current_number_label.config(text=str(global_variables.current_number))
    bank_label.config(text=f"BANK: {global_variables.bank_points}")
    points_label.config(text=f"POINTS: {global_variables.total_points}")

    if global_variables.current_number >= global_variables.limit:
        final_score = global_variables.total_points + global_variables.bank_points
        winner = "first" if final_score % 2 == 0 else "second"
        show_result_screen(winner, final_score % 2 == 0)

    if global_variables.current_number < global_variables.limit:
        print("Before AI move  total_points=", global_variables.total_points,
              " bank_points=", global_variables.bank_points,
              " final_score=", (global_variables.total_points + global_variables.bank_points))
        
        new_number = main.computer_logic(global_variables.chosen_algorithm, main.Tree(number=global_variables.current_number, player=1, children=[]))
        print("AI did move, number is ", new_number)
        global_variables.current_number = new_number
        print("Now current number ", global_variables.current_number)

        if global_variables.current_number % 2 == 0:
            global_variables.total_points += 1
        else:
            global_variables.total_points -= 1
        if global_variables.current_number % 10 == 0 or global_variables.current_number % 10 == 5:
            global_variables.bank_points += 1
        current_number_label.config(text=str(global_variables.current_number))
        bank_label.config(text=f"BANK: {global_variables.bank_points}")
        points_label.config(text=f"POINTS: {global_variables.total_points}")

        if global_variables.current_number >= global_variables.limit:
            final_score = global_variables.total_points + global_variables.bank_points
            winner = "first" if final_score % 2 == 0 else "second"
            show_result_screen(winner, final_score % 2 == 0)
        
        print("AFTER AI  total_points=", global_variables.total_points,
              " bank_points=", global_variables.bank_points,
              " final_score=", (global_variables.total_points+global_variables.bank_points))


def show_start_choice_screen():
    rules_frame.pack_forget()
    start_choice_frame.pack(fill="both", expand=True)


def start_as_user():
    global_variables.chosen_player = -1
    main.choose_player(-1)
    start_choice_frame.pack_forget()
    algorithm_choice_frame.pack(fill="both", expand=True)


def start_as_computer():
    global_variables.chosen_player = 1
    main.choose_player(1)
    start_choice_frame.pack_forget()
    algorithm_choice_frame.pack(fill="both", expand=True)


def choose_algorithm(algo):
    logging.basicConfig(filename="game.log", level=logging.INFO, datefmt="%H:%M:%S.%f")
    if algo == "min-max":
        choose_algorithm(int(0))
        global_variables.chosen_algorithm = 0
        logging.info(f"Algoritms: Minimaksa")
    elif algo == "alpha-beta":
        choose_algorithm(int(1))
        global_variables.chosen_algorithm = 1
        logging.info(f"Algoritms: Alfa-Beta")
    print(f"Chosen algorithm: {algo}")
    algorithm_choice_frame.pack_forget()
    show_game_screen()


def show_result_screen(winner, total_even):
    logging.basicConfig(filename="game.log", level=logging.INFO, datefmt="%H:%M:%S.%f") 
    multiplier_frame.pack_forget()
    result_frame.pack(fill="both", expand=True)

    if winner == "first":
        winner_label.config(text="FIRST PLAYER WON!")
        if global_variables.chosen_player == 1:
            logging.info(f"Uzvareja dators")
        else:
            logging.info("Uzvareja speletajs")
    else:
        winner_label.config(text="SECOND PLAYER WON!")
        if global_variables.chosen_player == -1:
            logging.info(f"Uzvareja dators")
        else:
            logging.info("Uzvareja speletajs")

    logging.info(f"Spele beidzas")

    if total_even:
        reason_label.config(text="THE TOTAL IS AN EVEN NUMBER!")
    else:
        reason_label.config(text="THE TOTAL IS AN ODD NUMBER!")


def restart_game():
    result_frame.pack_forget()
    rules_frame.pack(fill="both", expand=True)

    global_variables.chosen_player = 0
    global_variables.current_number = 0
    global_variables.bank_points = 0
    global_variables.total_points = 0
    global_variables.visitedNodes = 0
    entry.delete(0, "end")
    current_number_label.config(text=str(global_variables.current_number))
    bank_label.config(text=f"BANK: {global_variables.bank_points}")
    points_label.config(text=f"POINTS: {global_variables.total_points}")


first_move_done = False
global_variables.chosen_algorithm = 0
global_variables.current_number = 0
global_variables.bank_points = 0
global_variables.total_points = 0

root = tk.Tk()
root.title("Game UI")
root.geometry("800x460")
root.configure(bg="#6A0DAD")

# --- RULES FRAME ---
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

next_shapes = [
    rules_frame.create_oval(330, 360, 370, 400, fill="yellow", outline=""),
    rules_frame.create_oval(440, 360, 480, 400, fill="yellow", outline=""),
    rules_frame.create_oval(330, 400, 370, 440, fill="yellow", outline=""),
    rules_frame.create_oval(440, 400, 480, 440, fill="yellow", outline=""),
    rules_frame.create_rectangle(350, 360, 460, 440, fill="yellow", outline=""),
    rules_frame.create_rectangle(330, 380, 480, 420, fill="yellow", outline=""),
    rules_frame.create_text(407, 398, text="NEXT", font=("Comic Sans MS", 14, "bold"), fill="black")
]
for shape in next_shapes:
    rules_frame.addtag_withtag("next_button", shape)
rules_frame.tag_bind("next_button", "<Button-1>", lambda event: show_start_choice_screen())

# --- START CHOICE FRAME ---
start_choice_frame = tk.Canvas(root, bg="#6A0DAD")

choice_label = Label(start_choice_frame, text="WHO'S GONNA START FIRST?", font=("Comic Sans MS", 18, "bold"), fg="white", bg="#6A0DAD")
choice_label.pack(pady=30)

# Button "me"
me_oval1 = start_choice_frame.create_oval(120, 180, 180, 300, fill="#DAF043", outline="")
me_oval2 = start_choice_frame.create_oval(320, 180, 380, 300, fill="#DAF043", outline="")
me_rect = start_choice_frame.create_rectangle(150, 180, 350, 300, fill="#DAF043", outline="")
me_text = start_choice_frame.create_text(250, 240, text="me", font=("Comic Sans MS", 18, "bold"), fill="black")

start_choice_frame.addtag_withtag("me_choice", me_oval1)
start_choice_frame.addtag_withtag("me_choice", me_oval2)
start_choice_frame.addtag_withtag("me_choice", me_rect)
start_choice_frame.addtag_withtag("me_choice", me_text)
start_choice_frame.tag_bind("me_choice", "<Button-1>", lambda e: start_as_user())

# Button "computer"
comp_oval1 = start_choice_frame.create_oval(420, 180, 480, 300, fill="#71EFFF", outline="")
comp_oval2 = start_choice_frame.create_oval(620, 180, 680, 300, fill="#71EFFF", outline="")
comp_rect = start_choice_frame.create_rectangle(450, 180, 650, 300, fill="#71EFFF", outline="")
comp_text = start_choice_frame.create_text(550, 240, text="computer", font=("Comic Sans MS", 18, "bold"), fill="black")

start_choice_frame.addtag_withtag("comp_choice", comp_oval1)
start_choice_frame.addtag_withtag("comp_choice", comp_oval2)
start_choice_frame.addtag_withtag("comp_choice", comp_rect)
start_choice_frame.addtag_withtag("comp_choice", comp_text)
start_choice_frame.tag_bind("comp_choice", "<Button-1>", lambda e: start_as_computer())


# --- ALGORITHM CHOICE FRAME ---
algorithm_choice_frame = tk.Canvas(root, bg="#6A0DAD")

algo_label = Label(algorithm_choice_frame, text="CHOOSE ALGORITHM", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#6A0DAD")
algo_label.pack(pady=30)

minmax_oval1 = algorithm_choice_frame.create_oval(120, 180, 180, 300, fill="#F080F0", outline="")
minmax_oval2 = algorithm_choice_frame.create_oval(320, 180, 380, 300, fill="#F080F0", outline="")
minmax_rect = algorithm_choice_frame.create_rectangle(150, 180, 350, 300, fill="#F080F0", outline="")
minmax_text = algorithm_choice_frame.create_text(250, 240, text="MIN-MAX", font=("Comic Sans MS", 18, "bold"), fill="black")

algorithm_choice_frame.addtag_withtag("minmax", minmax_oval1)
algorithm_choice_frame.addtag_withtag("minmax", minmax_oval2)
algorithm_choice_frame.addtag_withtag("minmax", minmax_rect)
algorithm_choice_frame.addtag_withtag("minmax", minmax_text)
algorithm_choice_frame.tag_bind("minmax", "<Button-1>", lambda e: choose_algorithm("min-max"))


ab_oval1 = algorithm_choice_frame.create_oval(420, 180, 480, 300, fill="#7CF58B", outline="")
ab_oval2 = algorithm_choice_frame.create_oval(620, 180, 680, 300, fill="#7CF58B", outline="")
ab_rect = algorithm_choice_frame.create_rectangle(450, 180, 650, 300, fill="#7CF58B", outline="")
ab_text = algorithm_choice_frame.create_text(550, 240, text="ALPHA-BETA", font=("Comic Sans MS", 18, "bold"), fill="black")

algorithm_choice_frame.addtag_withtag("alphabeta", ab_oval1)
algorithm_choice_frame.addtag_withtag("alphabeta", ab_oval2)
algorithm_choice_frame.addtag_withtag("alphabeta", ab_rect)
algorithm_choice_frame.addtag_withtag("alphabeta", ab_text)
algorithm_choice_frame.tag_bind("alphabeta", "<Button-1>", lambda e: choose_algorithm("alpha-beta"))

# --- GAME FRAME ---
game_frame = tk.Canvas(root, bg="#6A0DAD")
title_label = Label(game_frame, text="WELCOME TO THE GAME", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#6A0DAD")
title_label.pack(pady=30)
instruction_label = Label(game_frame, text="INPUT A NUMBER FROM 20 TO 30", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD")
instruction_label.pack(pady=10)
entry = Entry(game_frame, font=("Arial", 14), width=10, justify="center", bg="lightgray")
entry.pack(pady=10)

start_shapes = [
    game_frame.create_oval(330, 210, 370, 250, fill="yellow", outline=""),
    game_frame.create_oval(440, 210, 480, 250, fill="yellow", outline=""),
    game_frame.create_oval(330, 250, 370, 290, fill="yellow", outline=""),
    game_frame.create_oval(440, 250, 480, 290, fill="yellow", outline=""),
    game_frame.create_rectangle(350, 210, 460, 290, fill="yellow", outline=""),
    game_frame.create_rectangle(330, 230, 480, 270, fill="yellow", outline=""),
    game_frame.create_text(407, 248, text="START", font=("Comic Sans MS", 14, "bold"), fill="black")
]
for shape in start_shapes:
    game_frame.addtag_withtag("start_button", shape)
game_frame.tag_bind("start_button", "<Button-1>", lambda event: start_game())

# --- MISTAKE FRAME ---
mistake_game_frame = tk.Canvas(root, bg="#6A0DAD")
mistake_title_label = Label(mistake_game_frame, text="WELCOME TO THE GAME", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#6A0DAD")
mistake_title_label.pack(pady=30)
mistake_instruction_label = Label(mistake_game_frame, text="INPUT A NUMBER FROM 20 TO 30", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD")
mistake_instruction_label.pack(pady=10)
mistake_entry = Entry(mistake_game_frame, font=("Arial", 14), width=10, justify="center", bg="lightgray")
mistake_entry.pack(pady=10)
mistake_input_mistake_label = Label(mistake_game_frame, text="THE ENTERED NUMBER IS OUTSIDE OF THE SPECIFIED NUMBER RANGE", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#6A0DAD")
mistake_input_mistake_label.pack(pady=10)

mistake_shapes = [
    mistake_game_frame.create_oval(330, 250, 370, 290, fill="yellow", outline=""),
    mistake_game_frame.create_oval(440, 250, 480, 290, fill="yellow", outline=""),
    mistake_game_frame.create_oval(330, 290, 370, 330, fill="yellow", outline=""),
    mistake_game_frame.create_oval(440, 300, 480, 330, fill="yellow", outline=""),
    mistake_game_frame.create_rectangle(350, 250, 460, 330, fill="yellow", outline=""),
    mistake_game_frame.create_rectangle(330, 270, 480, 310, fill="yellow", outline=""),
    mistake_game_frame.create_text(407, 288, text="START", font=("Comic Sans MS", 14, "bold"), fill="black")
]
for shape in mistake_shapes:
    mistake_game_frame.addtag_withtag("mistake_start_button", shape)
mistake_game_frame.tag_bind("mistake_start_button", "<Button-1>", lambda event: mistake_start_game())

# --- MULTIPLIER FRAME ---
multiplier_frame = tk.Canvas(root, bg="#6A0DAD")
bank_label = Label(multiplier_frame, text=f"BANK: {global_variables.bank_points}", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#6A0DAD")
bank_label.place(x=650, y=50)
points_label = Label(multiplier_frame, text=f"POINTS: {global_variables.total_points}", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#6A0DAD")
points_label.place(x=650, y=80)
current_label = Label(multiplier_frame, text="CURRENT NUMBER", font=("Comic Sans MS", 16, "bold"), fg="white", bg="#6A0DAD")
current_label.pack(pady=20)
current_number_label = Label(multiplier_frame, text=str(global_variables.current_number), font=("Arial", 18), width=10, justify="center", bg="lightgray")
current_number_label.pack(pady=10)
multiplier_label = Label(multiplier_frame, text="CHOOSE THE MULTIPLIER:", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#6A0DAD")
multiplier_label.pack(pady=20)

button3 = multiplier_frame.create_oval(200, 220, 300, 320, fill="yellow", outline="")
text3 = multiplier_frame.create_text(250, 270, text="3", font=("Comic Sans MS", 14, "bold"), fill="black")
multiplier_frame.addtag_withtag("btn3", button3)
multiplier_frame.addtag_withtag("btn3", text3)
multiplier_frame.tag_bind("btn3", "<Button-1>", lambda e: update_number(3))

button4 = multiplier_frame.create_oval(350, 220, 450, 320, fill="cyan", outline="")
text4 = multiplier_frame.create_text(400, 270, text="4", font=("Comic Sans MS", 14, "bold"), fill="black")
multiplier_frame.addtag_withtag("btn4", button4)
multiplier_frame.addtag_withtag("btn4", text4)
multiplier_frame.tag_bind("btn4", "<Button-1>", lambda e: update_number(4))

button5 = multiplier_frame.create_oval(500, 220, 600, 320, fill="pink", outline="")
text5 = multiplier_frame.create_text(550, 270, text="5", font=("Comic Sans MS", 14, "bold"), fill="black")
multiplier_frame.addtag_withtag("btn5", button5)
multiplier_frame.addtag_withtag("btn5", text5)
multiplier_frame.tag_bind("btn5", "<Button-1>", lambda e: update_number(5))

# --- RESULT FRAME ---
result_frame = tk.Canvas(root, bg="#6A0DAD")

winner_label = Label(result_frame, text="", font=("Comic Sans MS", 24, "bold"), fg="white", bg="#6A0DAD")
winner_label.pack(pady=30)

reason_label = Label(result_frame, text="", font=("Comic Sans MS", 16, "bold"), fg="yellow", bg="#6A0DAD")
reason_label.pack(pady=10)

play_rect = result_frame.create_rectangle(300, 250, 500, 310, fill="yellow", outline="")
play_oval1 = result_frame.create_oval(280, 250, 320, 310, fill="yellow", outline="")
play_oval2 = result_frame.create_oval(480, 250, 520, 310, fill="yellow", outline="")
play_text = result_frame.create_text(400, 280, text="PLAY AGAIN", font=("Comic Sans MS", 14, "bold"), fill="black")

result_frame.addtag_withtag("play_again", play_rect)
result_frame.addtag_withtag("play_again", play_oval1)
result_frame.addtag_withtag("play_again", play_oval2)
result_frame.addtag_withtag("play_again", play_text)
result_frame.tag_bind("play_again", "<Button-1>", lambda e: restart_game())


root.mainloop()
