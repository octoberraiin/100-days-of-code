from tkinter import *
import pandas
import random


# ------------------------- CONSTANTS ------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


# ------------------- CREATING NEW FLASH CARDS ------- --------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(ms=3000, func=flip_card)


# ------------------------- FLIP CARDS ------------------------ #


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])
    canvas.itemconfig(card_title, text="English", fill="white")

# ----------------- KNOWN / NOT KNOWN PROGRAMS ---------------- #


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


    next_card()

# ----------------------------- UI ---------------------------- #

# Window

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(ms=3000, func=flip_card)

# Canvas (Flashcards, Text)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, command=next_card, highlightbackground=BACKGROUND_COLOR)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, command=is_known, highlightbackground=BACKGROUND_COLOR)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()