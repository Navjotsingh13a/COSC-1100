# Author : Navjot
# Date : January 19, 2024
# Description:
# App tp calculate the amount of ice cream sold in a week 
# in mL .

# Declarations.
KIDDIE_CONE_ML = 60
SMALL_CONE_ML = 120
MEDIUM_CONE_ML =240
LARGE_CONE_ML=360

# Input.
# How many kiddle cones were sold in a week ?
kiddie_cones_sold= int(input("How many kiddie cones were sold this week?: "))
# How many small cones were sold in a week?
small_cones_sold = int(input("How many small cones were sold this week? "))
# How many medium cones were sold in a week? 
medium_cones_sold = int(input("How many medium cones were sold this week? "))
# How many large cones were sold in a week?
large_cones_sold = int(input("How many large cones were sold this week? "))
# We're expecting a positive whole number.

# Process.
# Set the total ice cream equal to kiddie cones * 60.
total_ice_cream = kiddie_cones_sold * KIDDIE_CONE_ML
# Add to the total ice cream small cones * 120
total_ice_cream = total_ice_cream + (small_cones_sold * SMALL_CONE_ML)
# Add to the total ice cream medium cones * 240.
# Add to the total ice cream large cones * 360.

# Output.
# The amount of ice cream sold in 1 week.
# output it in text:"The total amount of ice cream sold this week"
print("\nThe amount of ice cream sold this week was:"+ str(total_ice_cream)+ "medium_cone_sold")
      
    # Confirm close.
input("\nPress Enter to end the program...")
