# Author: Navjot Singh
# Created: March 22, 2024
# Modified: March 22, 2024
# Description:
# Attempts to determine and output the difference 
# in their BMI if they lost weight, successively, in increments
# of 5 pounds up to a maximum of 15% of their body weight.

MINIMUM_HEIGHT = 20
MAXIMUM_HEIGHT = 120
MINIMUM_WEIGHT = 10
WEIGHT_LOSS_INCREMENT = 5
WEIGHT_THRESHOLD = 0.85
BMI_CONVERSION = 703

keep_running = True

while keep_running:
    # Accept valid height input
    # Start a while loop while valid_height is False.
    valid_height = False
    while not valid_height:
        # Get the height.
        try:
            height = float(input(f"Please enter your height ({MINIMUM_HEIGHT}-{MAXIMUM_HEIGHT}) in inches: "))
            if MINIMUM_HEIGHT <= height <= MAXIMUM_HEIGHT:
            # If yes, valid_height = True
                valid_height = True
            else:
            # If no, write an invalid input.
                print(f"The height requirement is {MINIMUM_HEIGHT} and {MAXIMUM_HEIGHT} inches.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Accept valid weight input
    # Start a while loop while valid_weight is False.
    valid_weight = False
    while not valid_weight:
        # Get the weight.
        try:
            weight = float(input(f"Put your weight in {MINIMUM_WEIGHT} pounds and above): "))
            if weight >= MINIMUM_WEIGHT:
            # If yes, valid_weight = True
                valid_weight = True
            else:
            # If no, write an invalid input.
                print(f"The weight must be at least {MINIMUM_WEIGHT} pounds.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Processing
# Calculate BMI and display category
    derivative_weight = weight
    while weight >= derivative_weight * WEIGHT_THRESHOLD:
        bmi = (weight / (height ** 2)) * BMI_CONVERSION

        if bmi < 16:
            category = "severely underweight"
        elif 16 <= bmi < 18.5:
            category = "underweight"
        elif 18.5 <= bmi < 25:
            category = "healthy"
        elif 25 <= bmi < 30:
            category = "overweight"
        else:
            category = "obese"

        print(f"\nWeight: {weight} lbs, BMI: {bmi:.1f}, Category: {category}")

        # Decrease weight by WEIGHT_LOSS_INCREMENT
        weight -= WEIGHT_LOSS_INCREMENT

    # Ask for input another numbers.
    valid_input = False
    while not valid_input:
        repeat = input("Would you like to input a different set of numbers? (yes/no): ").lower()
        if repeat == "yes":
            # if yes, ask for another numeric value.
            valid_input = True
        elif repeat == "no":
           # if no, appreciate their work.
            keep_running = False
            print("It is appreciative of you to utilizing the BMI calculator,Farewell.")
            valid_input = True
        else:
            print("Invalid input. Please answer in 'yes' or 'no'.")