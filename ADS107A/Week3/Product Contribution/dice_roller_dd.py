# Original: Python Dice Rolling Game using Tkinter
#                                 - Rishaw Kumar
# Dice Roller
# New functionality added by Michael Connell 

from tkinter import *
import random

App = Tk()
App.title("Dice Roller")

# Text label for dice type display
dice_type_display = Label(App, text="Dice Type: d6", font=('Times', 14))
dice_type_display.grid(row=0, column=0)

# First dice character to show when the app starts
lbl = Label(App, text='🎲', font=('Times', 100))
lbl.grid(row=1, column=0, padx=40)

def roll_dice(dice_type):
    return random.randint(1, dice_type)

def roll():
    dice_type = int(dice_type_var.get())
    roll_result = roll_dice(dice_type)
    lbl.configure(text=str(roll_result))
    result_label.configure(text=f"Result: {roll_result} on a d{dice_type}")
    dice_type_display.configure(text=f"Dice Type: d{dice_type}")

# Dropdown menu for selecting dice type
dice_type_var = StringVar(App)
dice_type_var.set("6")  # default value
dice_type_menu = OptionMenu(App, dice_type_var, "4", "6", "8", "10", "12", "20")
dice_type_menu.grid(row=2, column=0)

# Roll button
roll_button = Button(App, text='Roll', command=roll)
roll_button.grid(row=3, column=0)

# Label for displaying the result
result_label = Label(App, text="", font=('Times', 14))
result_label.grid(row=4, column=0)

App.mainloop()

