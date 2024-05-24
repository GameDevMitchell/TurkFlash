from tkinter import *
from customtkinter import *

# the background colours
BACKGROUND_COLOR = "#B1DDC6"


# creating the user interface
app = Tk()
app.title("TurkFlash")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# creating the word display canvas
display_canvas = Canvas(
    width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0
)
front = PhotoImage(file="images/card_front.png")
display_canvas.create_image(400, 263, image=front)
display_canvas.create_text(
    400, 150, text="English", fill="black", font=("ariel", 40, "italic")
)
display_canvas.create_text(
    400, 263, text="trouve", fill="black", font=("ariel", 60, "bold")
)
display_canvas.grid(row=1, column=1, columnspan=2)

# the wrong and right button images
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")


# right and wrong buttons
right_button = CTkButton(
    app, image=right_image, fg_color="transparent", text="", hover=False
)
wrong_button = CTkButton(
    app, image=wrong_image, fg_color="transparent", text="", hover=False
)
right_button.grid(row=2, column=2)
wrong_button.grid(row=2, column=1)


app.mainloop()
