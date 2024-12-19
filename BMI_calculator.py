# Author: Navjot Singh
# Created: February 27, 2024
# Modified: February 27, 2024
# Description:
# Attempts to determine and output the difference 
# in their BMI if they lost weight, successively, in increments
# of 5 pounds up to a maximum of 15% of their body weight.

keep_running = True

while keep_running:
    # Accept valid height input
    # Start a while loop while valid_height is False.
    valid_height = False
    while not valid_height:
        # Get the height between 20-120 inches.
        try:
            height = float(input("Please enter your height (20-120) in inches: "))
            if 20 <= height <= 120:
        # If yes, valid_height = True
                valid_height = True
            else:
        # If no, write an invalid input.
                print("The height requirement is 20 to 120 inches.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Accept valid weight input
    # Start a while loop while valid_weight is False.
    valid_weight = False
    while not valid_weight:
        # Get the weight in pounds (10 and up)
        try:
            weight = float(input("Put your weight in pounds (10 and up): "))
            if weight >= 10:
            # If yes, valid_weight = True
                valid_weight = True
            else:
                # If no, write an invalid input.
                print("The weight must be at least ten pounds.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Processing
                      
    derivative_weight = weight

    while weight >= derivative_weight * 0.85:
        bmi = (weight / (height ** 2)) * 703

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

        # loss of weight, successively, in increments of 5 pounds 
        # up to a maximum of 15% of their body weight
        # Decrease weight by 5 pounds
        weight -= 5

# Output
        
    valid_input = False
    while not valid_input:
        # Ask for input another numbers.
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