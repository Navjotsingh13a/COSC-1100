# Author: Navjot Singh
# Date: April 03, 2024
# Modified: April 03, 2024
# Description:
# This program uses a tkinter UI to help someone determine whether
# they should pass another car.

from tkinter import *
from idlelib.tooltip import Hovertip

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

WINDOW_MIN_WIDTH = 220
WINDOW_MIN_HEIGHT = 220

window = Tk()

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)

window.title("Should I Pass?")


def calculate():
    try:
        SECONDS_PER_HOUR = 3600

        # Get the value from entry_speed_1 and treat it as a number.
        speed_one = float(entry_current_speed.get())

        # Get the value from entry_speed_2 and treat it as a number.
        speed_two = float(entry_desired_speed.get())

        low_speed = min((speed_one, speed_two))
        high_speed = max((speed_one, speed_two))

        speed_difference = high_speed - low_speed
        time_saved_per_km =  1 / (speed_difference / 3600)
        speed_difference_in_seconds = speed_difference / SECONDS_PER_HOUR


        label_output.configure(
         text="Time saved: " + str(round(time_saved_per_km, 2)) + "seconds/km\n" +  
         "Speed difference: "+ str(round(speed_difference_in_seconds, 2)) + "km/s"
        )
        
    # If they don’t both have numbers:
    except:
        # Show an error message in the output labels
        label_output.configure(text="Error: speed entries must be numeric.")

def reset():
    entry_current_speed.delete(0, END)
    entry_desired_speed.delete(0, END)
    label_output.configure(text = "")
    entry_current_speed.focus()

# Row 0 widgets.
label_current_speed = Label(text ="Current speed:")
label_current_speed.grid(row=0, column=0, padx=5, pady=5, sticky=E)
entry_current_speed = Entry()
entry_current_speed.grid(row=0, column=1, padx=5, pady=5, sticky=W)
Hovertip(entry_current_speed, text= "Enter your current speed in km/h.")

# Row 1 widgets
label_desired_speed = Label(text ="Desired speed:")
label_desired_speed.grid(row=1, column=0, padx=5, pady=5, sticky=E)
entry_desired_speed = Entry()
entry_desired_speed.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Hovertip(entry_desired_speed, text= "Enter your desired speed in km/h.")

# Row 2 widgets
label_output = Label(width=25, relief=SUNKEN, height=3, wraplength=180)
label_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
Hovertip(label_output, text="Display the difference in the speed")

# Row 3 widgets
button_calculate = Button(text="Calculate", command= calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
Hovertip(button_calculate, text= "Click to calculate the time difference")

# Row 4 widgets
button_clear = Button(text="Clear", command=reset)
button_clear.grid(row=4, column=0, padx=5, pady=5)
Hovertip(button_clear, text="Click to reset the application")
button_exit =Button(text= "Exit", command=exit)
button_exit.grid(row=4, column=1, padx=5, pady=5)
Hovertip(button_exit, text="Calculate to exit the application")

# Add hotkey support.
window.bind("<Alt-c>", calculate)
window.bind("<Return>", calculate)
window.bind("<Alt-r>", reset)
window.bind("<Alt-x>", exit)

# Set the columns and rows to take up equal proportions of the screen.
window.columnconfigure(0, weight=1)
window.columnconfigure(1,weight=1)
for row in range(5):
    window.rowconfigure(row, weight=1)

window.mainloop()