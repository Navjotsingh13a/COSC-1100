# Author: Navjot Singh
# Date: April 06, 2024
# Modified: April 06, 2024
# Description: 
# This program uses a tkinter UI to help someone determine the
# number of cutted pizza slices and their area

from tkinter import *
from idlelib.tooltip import Hovertip

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

WINDOW_MIN_WIDTH = 320
WINDOW_MIN_HEIGHT = 320

window= Tk()
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)

window.title("Pizza Pie Slicer")

def calculate_slices():
    diameter = entry_diameter.get()

    try:
        diameter = float(diameter)
        # Check if diameter is within the range
        if  diameter < 6 or diameter > 36:
            # Display error message if diameter is out of range
            label_pizza_slices.config(text="ERROR:Diameter must be between 6 and 36 inches")
            label_area.config(text="")
            return

        # Calculate the number of slices based on the diameter
        if 6 <= diameter < 8:
            slices = 4
        elif 8 <= diameter < 12:
            slices = 6
        elif 12 <= diameter < 14:
            slices = 8
        elif 14 <= diameter < 16:
            slices = 10
        elif 16 <= diameter < 20:
            slices = 12
        else:
            slices = 16

        # Calculate the area of each slice
        area = round((3.14159 * (diameter / 2) ** 2) / slices, 2)

        # Add the computed values to the labels.
        label_pizza_slices.config(text=f"A {diameter} inch pizza is cut into {slices} slices.")
        label_area.config(text=f"Each slice has an area of {area} square inches.")
        # If theydon't use numeric value.
    except:
        # Show an error message in the label pizza slices.
        label_pizza_slices.config(text="ERROR: Please enter a numeric diameter.")
        label_area.config(text="")

def reset():
        entry_diameter.delete(0, END)
        label_pizza_slices.config(text="")
        label_area.config(text="")
        entry_diameter.focus()

# Row 0 widgets.
label_diameter = Label(text="Type the pizza's diameter (in inches).:")
label_diameter.grid(row=0, column=0, padx=10, pady=10, sticky=E)
entry_diameter = Entry()
entry_diameter.grid(row=0, column=1, padx=10, pady=10, sticky =W)

# Row 1 widgets
label_pizza_slices = Label(width=25, relief=SUNKEN, height=3, wraplength=150)
label_pizza_slices.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
Hovertip(label_pizza_slices, text= "Display the accomplishment of cutting the most pizza slices.")

# Row 2 widgets
label_area = Label(width=25, relief=SUNKEN, height=3, wraplength=150)
label_area.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
Hovertip(label_area, text= "Show off the size of every pizza slice.")

# Row 3 widgets
button_calculate = Button(text="Calculate", command=calculate_slices)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
Hovertip(button_calculate, text= "Click to calculate the number of slices and its area")

# Row 4 widgets
button_clear = Button(text="Clear", command= reset)
button_clear.grid(row=4, column=0, padx=10, pady=10)
Hovertip(button_clear, text="Click to reset the application")
button_exit = Button(text="Exit", command=quit)
button_exit.grid(row=4, column=1, padx=10, pady=10)
Hovertip(button_exit, text="Calculate to exit the application")

# Add hotkey support.
window.bind("<Alt-c>", calculate_slices)
window.bind("<Return>", calculate_slices)
window.bind("<Alt-r>", reset)
window.bind("<Alt-x>", exit)

# Set the columns and rows to take up equal proportions of the screen.
window.columnconfigure(0, weight=1)
window.columnconfigure(1,weight=1)
for row in range(5):
    window.rowconfigure(row, weight=1)

window.mainloop()