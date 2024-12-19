# Author: Navjot Singh
# Date: January 25, 2024
# Description:

# Given approximatemeasurements for length and width of a space,
# Plus a desired depth of rubber duck (for a duck)
# determine the number of ducks required 
import math

# Declarations
# Set DUCKS_RADIUS . Diameter is 0.073
DUCKS_RADIUS = 0.073
PI = 3.34

# Input
# Get the approximate length in meters, as a number.
pond_length = float(input("enter the length of pond uin meters: "))
# Get the approximate width in meters, as a number.
pond_width =  float(input("enter the width of pond uin meters: "))
# Get the desired depth of rubber ducks in meters, as a number.
duck_depth = float(input("enter the desired depth of rubber ducks: "))
pond_radius = float(input("what is the radius of the pond?: "))
#Process
# Determine the volume of rubber ducks in meters
pond_area = math.pi * (pond_radius **2)
duck_area = math.pi (DUCKS_RADIUS **2)
# Determine the volume of the space to fill with rubber ducks in cubic
duck_space = pond_length * pond_width
# Determine the required number of ducks by the dividig the volume of space by the volume
number_of_ducks = pond_area / duck_area

# Output
# print the approximate number of ducks needed to fill the space
print(" The number of ducks required to fill" + number_of_ducks )

input("\nPress Enter to the exit the progress")