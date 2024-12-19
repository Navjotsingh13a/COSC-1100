# Author: Navjot Singh
# Created: February 9, 2024
# Modified: February 9, 2024
# Description:
# Application to do something t-shirt sales

user_selection = ""
small_shirt_total = 0
medium_shirt_total = 0
large_shirt_total = 0
extra_large_shirt_total = 0

while user_selection != "5":
    print(" please make a selection:")
    print ("1) small t-shirt")
    print ("2) medium t-shirt")
    print ("3) large t-shirt")
    print ("4) X-large t-shirt")
    print ("5) tally and exit")
    user_selection = input("Enter your choice  (1-5): ")

    # Get the user input for their selection an
    if  user_selection == "1" or \
         user_selection == "2" or \
          user_selection == "3" or \
           user_selection == "4":

        is_valid = False

        # Start a while loop while is_valid is False.
        while is_valid == False:
        # Get the number of hirts of whatever size.
            shirt_quantity = input("How many shirts were sold?: ")
          # Is shirt quantity a whole number ?
            if shirt_quantity.isnumeric():
             # If yes, is_valid = True
                is_valid = True
            else:
             # If no, write an error message.
             print("please enter a valid number of shirts.")
        
 # Based on the selection, update the appropriate 
        if user_selection == "1":
            small_shirt_total += int(shirt_quantity)
        elif user_selection == "2":
            medium_shirt_total += int(shirt_quantity)
        elif user_selection == "3":
            large_shirt_total += int(shirt_quantity)
        elif user_selection == "4":
            extra_large_shirt_total += int(shirt_quantity)
        # if the user didn't enter 1,2,3,4,5..... eror message.
        elif user_selection != "5":
            print("Pease enter a selection between 1 and 5.")


# Processing
# Get the total number of t-shirt by adding them all.
total_shirt_sold = small_shirt_total + medium_shirt_total + \
                   large_shirt_total + extra_large_shirt_total
if total_shirt_sold != 0:
  # Get the percentage of small t-shirt with division.
   small_shirt_percentage = round(100 * small_shirt_total/total_shirt_sold,2)
  # Get the percentage of medium t-shirt with division.
   medium_shirt_percentage = round(100 * medium_shirt_total/total_shirt_sold,2)
  # Get the percentage of large t-shirt with division.
   large_shirt_percentage = round(100 * large_shirt_total/total_shirt_sold,2)
  # Get the percentage  of extra large t-shirt with division.
   extra_large_shirt_percentage =(100 * extra_large_shirt_total/total_shirt_sold,2)

# Output 
# Output the percentage and quantity of small shirts.
   print("percentage of small shirt sold is:", small_shirt_percentage)
# Output the percentage and quantity of medium shirts.
   print("percentage of medium shirt sold is:", medium_shirt_percentage)
# Output the percentage and quantity of large shirts.
   print("percentage of large shirt sold is:", large_shirt_percentage)
# Output the percentage and quantity of extra large shirts.
   print("percentage of extra large shirt sold is:", extra_large_shirt_percentage)
else:
    print("zero shirt were sold please do some more marketing")
# Confirm close
input("\nPress Enter to end the program....")