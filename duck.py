#Author: Navjot Singh
# Created: February 2, 2024
# Modified: February 2, 2024
# Description:
# Dyck and Reservoir

# Input

# Determine what data is needed, and how to get it

# Have the user input the length and width of the ducks.
length_of_duck = input("Enter the length_of_duck of the duck in centimeters: ")

# Validate the duck length  
try: 
    length_of_duck = float(length_of_duck)
    if length_of_duck> 0:
        is_valid = True
    else:
        is_valid = False
        print(" The length_of_duck must be a positive")
except:
    is_valid = False
    print("The length_of_duck must be numeric")

# Have the user input the width of the ducks.
width_of_duck = input("Enterthe width of the duck in centimeters: ")

# Validate the duck width
try: 
    width_of_duck = float(width_of_duck)
    if width_of_duck> 0:
        is_valid = True
    else:
        is_valid = False
        print(" The width_of_duck must be a positive")
except:
    is_valid = False
    print("The width_of_duck must be numeric")

# Have the user input the length of the reservoir
length_of_reservoir = input("Enter the length of the reservoir in centimeters: ")

# Validate the reservoir length  
try: 
    length_of_reservoir = float(length_of_reservoir)
    if length_of_reservoir > 0:
        is_valid = True
    else:
        is_valid = False
        print(" The length_of_reservoir must be a positive")
except:
    is_valid = False
    print("The length_of_reservoir must be numeric")

# Have the user input the width of the reservoir
width_of_reservoir = input("Enter the width of the reservoir in centimeters: ")

# Validate the reservoir width
try: 
    width_of_reservoir = float(width_of_reservoir)
    if width_of_reservoir> 0:
        is_valid = True
    else:
        is_valid = False
        print(" The width_of_reservoir must be a positive")
except:
    is_valid = False
    print("The width_of_reservoir must be numeric")

if is_valid:
# Process

# Calculating the area of the reservoir and the area of the duck

    area_of_reservoir = length_of_reservoir * width_of_reservoir
    area_of_duck = length_of_duck * width_of_duck 

# Dividing the area of the reservoir by the area of duck
# To find the amount of rubber ducks needed to cover the reservoir completely.

    number_of_ducks_needed = area_of_reservoir / area_of_duck

# Output
# Clearly define the result
# The amount of ducks needed to cover a reservoir completely
    print("\nThe amount of ducks needed to cover a reservoir completely " + str(number_of_ducks_needed))
print("\nPress Enter to end the program.....")
