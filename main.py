import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
choice = {}
words_and_translations = {}
count = 0
# read the turkish words in the csv file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Turkish_words - Sheet1.csv")
    words_and_translations = original_data.to_dict(orient="records")
else:
    words_and_translations = data.to_dict(orient="records")


# to generate a random turkish word:
def turkish():
    """Generates a random turkish word"""
    global count
    global choice, switch_timer
    if count < 21:
        app.after_cancel(switch_timer)
        choice = random.choice(words_and_translations)
        word = choice["Turkish"]
        display_canvas.itemconfig(word_text, text=word, fill="black")
        display_canvas.itemconfig(language_text, text="Turkish", fill="black")
        display_canvas.itemconfig(background, image=front)
        switch_timer = app.after(4000, english)
        count += 1
    else:
        app.quit()


# to get the translation of the turkish word
def english():
    """Gets the english translation of the word"""

    translation = choice["English"]
    display_canvas.itemconfig(background, image=back)
    display_canvas.itemconfig(
        word_text, text=translation, fill="white", font=("ariel", 50, "bold")
    )
    display_canvas.itemconfig(
        language_text, text="English", fill="white", font=("ariel", 30, "italic")
    )


def known():
    """removes what the user knows from the list of words"""
    if count < 21:
        words_and_translations.remove(choice)
        info = pandas.DataFrame(words_and_translations)
        info.to_csv("data/words_to_learn")
        turkish()
    else:
        app.quit()


# creating the user interface
app = Tk()
app.title("Flashy")
# app.geometry("900x800")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
switch_timer = app.after(4000, english)

# creating the word display canvas
display_canvas = Canvas(
    width=650, height=427, bg=BACKGROUND_COLOR, highlightthickness=0
)
front = PhotoImage(file="images/card_front_resized.png")
back = PhotoImage(file="images/card_back_resized.png")
# s = front.subsample(2, 1)
background = display_canvas.create_image(325, 213, image=front)
language_text = display_canvas.create_text(
    325, 120, text="English", fill="black", font=("ariel", 30, "italic")
)
word_text = display_canvas.create_text(
    325, 235, text="trouve", fill="black", font=("ariel", 50, "bold")
)
display_canvas.grid(row=1, column=1, columnspan=2)

# the wrong and right button images
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

# right and wrong buttons
right_button = Button(image=right_image, highlightthickness=0, command=known)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=turkish)
right_button.grid(row=2, column=2)
wrong_button.grid(row=2, column=1)

turkish()

app.mainloop()
