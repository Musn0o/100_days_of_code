from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn: list[dict] = []

DATA_PATH = "Day_031_Flash_Card_App/data/"
IMG_PATH = "Day_031_Flash_Card_App/images/"
WORDS_FILE = os.path.join(DATA_PATH, "words_to_learn.csv")
FRENCH_FILE = os.path.join(DATA_PATH, "french_words.csv")

# --- Load Data Safely ---
try:
    data = pd.read_csv(WORDS_FILE)
    if data.empty:
        raise ValueError("The learning list is empty.")
    to_learn = data.to_dict(orient="records")
except (FileNotFoundError, ValueError):
    try:
        original_data = pd.read_csv(FRENCH_FILE)
        to_learn = original_data.to_dict(orient="records")
    except FileNotFoundError:
        messagebox.showerror("Error", "Required data file not found.")
        exit()


# --- Functions ---
def next_card():
    global current_card, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    if not to_learn:
        messagebox.showinfo("Congratulations!", "You've learned all the words! 🎉")
        known_button.config(state="disabled")
        unknown_button.config(state="disabled")
        return

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv(WORDS_FILE, index=False)
    next_card()


# --- UI Setup ---
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = None

# --- Canvas ---
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

try:
    card_front_img = PhotoImage(file=os.path.join(IMG_PATH, "card_front.png"))
    card_back_img = PhotoImage(file=os.path.join(IMG_PATH, "card_back.png"))
except Exception as e:
    messagebox.showerror("Image Error", f"Couldn't load images: {e}")
    exit()

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# --- Buttons ---
try:
    cross_image = PhotoImage(file=os.path.join(IMG_PATH, "wrong.png"))
    check_image = PhotoImage(file=os.path.join(IMG_PATH, "right.png"))
except Exception as e:
    messagebox.showerror("Image Error", f"Couldn't load button images: {e}")
    exit()

unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# --- Start ---
next_card()
window.mainloop()
