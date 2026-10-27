import tkinter as tk
from tkinter import messagebox
import database
from services import player_services
from services import picks_services

from models.player import Player

def run_contest_UI():

    def submit_picks():
        game1 = game1_pick.get()
        game2 = game2_pick.get()

        pick_record = picks_services.add_picks(name_entry.get(), 1, [game1,game2])

    def process_name():
        name = name_entry.get()
        show_score(name)

    def get_picks(team):
        name = name_entry.get()

    def get_score(name):
        return player_services.get_player_score(name)

    def show_score(name):
        score = get_score(name)

        if score is None:
            score_label.config(text="SCORE: Player not found")
        else:
            score_label.config(text=f"SCORE: {score}")



    # Create the main window
    window = tk.Tk()
    window.title("Family NFL Pick'em")
    window.geometry("500x600")

    game1_pick = tk.StringVar(value="")
    game2_pick = tk.StringVar(value="")

    # Title
    title = tk.Label(
        window,
        text="🏈 FAMILY NFL PICK'EM 🏈",
        font=("Arial", 22, "bold")
    )
    title.pack(pady=20)

    # Player name
    name_label = tk.Label(
        window,
        text="Player Name:",
        font=("Arial", 12)
    )
    name_label.pack()


    name_entry = tk.Entry(
        window,
        font=("Arial", 14),
        width=25
    )
    name_entry.pack(pady=10)

    enter_frame = tk.Frame(window)
    enter_frame.pack()

    grab_data_button = tk.Button(
        enter_frame,
        text="Enter",
        font=("Arial",12),
        width=8,
        command=process_name
        )
    grab_data_button.pack(side="top",padx=10)

    def select_team(selected_team, pick_variable, selected_button, other_button):
        
        pick_variable.set(selected_team)

        selected_button.config(
            bg="green",
            fg="white",
            relief="sunken"
        )

        other_button.config(
            bg="SystemButtonFace",
            fg="black",
            relief="raised"
        )


    # Game 1
    game1_label = tk.Label(
        window,
        text="CHIEFS vs BILLS",
        font=("Arial", 16, "bold")
    )
    game1_label.pack(pady=15)

    game1_frame = tk.Frame(window)
    game1_frame.pack()

    chiefs_button = tk.Button(
        game1_frame,
        text="Chiefs",
        font=("Arial", 12),
        width=12,
        command=lambda: game1_pick.set("KC")
    )
    chiefs_button.pack(side="left", padx=10)

    bills_button = tk.Button(
        game1_frame,
        text="Bills",
        font=("Arial", 12),
        width=12,
        command=lambda: game1_pick.set("BUF")
    )
    bills_button.pack(side="left", padx=10)

    chiefs_button.config(
    command=lambda: select_team("KC",game1_pick,chiefs_button, bills_button)
    )

    bills_button.config(
    command=lambda: select_team("BUF",game1_pick,bills_button, chiefs_button)
    )
   

    # Game 2
    game2_label = tk.Label(
        window,
        text="COWBOYS vs EAGLES",
        font=("Arial", 16, "bold")
    )
    game2_label.pack(pady=15)

    game2_frame = tk.Frame(window)
    game2_frame.pack()

    cowboys_button = tk.Button(
        game2_frame,
        text="Cowboys",
        font=("Arial", 12),
        width=12,
        command=lambda: game2_pick.set("DAL")
    )
    cowboys_button.pack(side="left", padx=10)


    eagles_button = tk.Button(
        game2_frame,
        text="Eagles",
        font=("Arial", 12),
        width=12,
        command=lambda: game2_pick.set("PHI")
    )

    eagles_button.pack(side="left", padx=10)

    # Submit button
    submit_button = tk.Button(
        window,
        text="SUBMIT PICKS",
        font=("Arial", 14, "bold"),
        width=20,
        command=submit_picks
    )
    submit_button.pack(pady=30)

    cowboys_button.config(
    command=lambda: select_team("DAL", game2_pick,cowboys_button, eagles_button)
    )

    eagles_button.config(
    command=lambda: select_team("PHI", game2_pick,eagles_button, cowboys_button)
    )

    # Score
    score_label = tk.Label(
        window,
        text="Score: --",
        font=("Arial", 16, "bold")
    )
    score_label.pack()

    # Start the application
    window.mainloop()


