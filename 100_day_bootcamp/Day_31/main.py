from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

word_choice = {}

try:
    csv = pandas.read_csv(open("Day_31/data/words_to_learn.csv"))
except FileNotFoundError:
    csv = pandas.read_csv(open("Day_31/data/spanish_words.csv"))
finally:
    spanish_words = csv.to_dict("records")

def flip_card():
    global word_choice
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="English", fill='#FFF')
    canvas.itemconfig(word, text=word_choice["English"], fill='#FFF')

def next_card():
    global word_choice, flip_timer
    window.after_cancel(flip_timer)

    canvas.itemconfig(card, image=card_front)
    word_choice = random.choice(spanish_words)
    canvas.itemconfig(language, text="Spanish", fill='#000')
    canvas.itemconfig(word, text=word_choice["Spanish"], fill='#000')
    flip_timer = window.after(3000, flip_card)

def know_word():
    if word_choice:
        spanish_words.remove(word_choice)
        data = pandas.DataFrame(spanish_words)
        data.to_csv("Day_31/data/words_to_learn.csv", index=False)
            
    next_card()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, width=1000, height=1000, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)
window.after_cancel(flip_timer)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="Day_31/images/card_front.png")
card_back = PhotoImage(file="Day_31/images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="Day_31/images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)
right_image = PhotoImage(file="Day_31/images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=know_word)
button_right.grid(row=1, column=1)

window.mainloop()