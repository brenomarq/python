import pandas
import tkinter as tk
from random import randint

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# Functions
def next_card() -> None:
    """It selects a random word from the database to display it to the user."""
    global current_word

    random_index = randint(0, len(words) - 1)
    current_word = words[random_index]

    flashcard.itemconfig(card_image, image=front_flashcard_img)
    flashcard.itemconfig(language_reference, text="French", fill="black")
    flashcard.itemconfig(word_reference, text=current_word["French"], fill="black")

    window.after(3000, flip_card)

def know_word() -> None:
    """Selects a random word from the database and delete that word."""
    words.remove(current_word)
    new_data = pandas.DataFrame(words)
    new_data.to_csv("./data/to_learn.csv", index=False)
    next_card()

def flip_card() -> None:
    """It displays the translation of the current word."""
    flashcard.itemconfig(card_image, image=back_flashcard_img)
    flashcard.itemconfig(language_reference, text="English", fill="white")
    flashcard.itemconfig(word_reference, text=current_word["English"], fill="white")

# Read the data
try:
    data = pandas.read_csv("./data/to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    words = data.to_dict(orient="records")

else:
    words = data.to_dict(orient="records")

# Variables to be accessed by the functions
current_word = {}

# UI
window = tk.Tk()
window.title("My Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_flashcard_img = tk.PhotoImage(file="./images/card_front.png")
back_flashcard_img = tk.PhotoImage(file="./images/card_back.png")
flashcard = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = flashcard.create_image(400, 263, image=front_flashcard_img)
language_reference = flashcard.create_text(400, 150, font=LANGUAGE_FONT)
word_reference = flashcard.create_text(400, 263, font=WORD_FONT)
next_card()
flashcard.grid(row=0, column=0, columnspan=2)

wrong_img = tk.PhotoImage(file="./images/wrong.png")
wrong_btn = tk.Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

right_img = tk.PhotoImage(file="./images/right.png")
right_btn = tk.Button(image=right_img, command=know_word, highlightthickness=0)
right_btn.grid(row=1, column=1)

window.mainloop()
