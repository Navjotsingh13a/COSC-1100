# Author: Navjot Singh
# Created: March 03, 2024
# Modified: March 03, 2024
# Description:
# Allow the user tom enter all of their grades so far
# through a semester to determine their overall 
# midterm grade as well as their grade in different
# categories

# Declarations.
MINIMUM_GRADE = 0
MAXIMUM_GRADE = 100

NUMBER_OF_PCAS = 4
NUMBER_OF_CES = 4
NUMBER_OF_TEST = 2
NUMBER_OF_BAS = 2
PCA_TOTAL_WEIGHT = 12
CE_TOTAL_WEIGHT = 12
TEST_TOTAL_WEIGHT = 12
BA_TOTAL_WEIGHT = 2
OVERALL_WEIGHT = PCA_TOTAL_WEIGHT + CE_TOTAL_WEIGHT + TEST_TOTAL_WEIGHT + BA_TOTAL_WEIGHT 

pca_list = []
ce_list = []
test_list = []
Bonus_list = []

# Input.

for pca_grade in range(NUMBER_OF_PCAS):
    is_valid = False

    while not is_valid:
        user_value = input("Enter your grade on Pre-Class Activity " + str(pca_grade + 1) + ": ")

        try:
            user_value = float(user_value)

            if MINIMUM_GRADE <= user_value <= MAXIMUM_GRADE:
                is_valid = True
                pca_list.append(user_value)
            else:
                print(f"The grade must be between {MINIMUM_GRADE} and {MAXIMUM_GRADE}.")
        except ValueError:
            print("You must enter the grade as a number.")
print(pca_list)

for ce_grade in range(NUMBER_OF_CES):
    is_valid = False

    while not is_valid:
        user_value = input("Enter your grade on Class Exercise " + str(ce_grade + 1) + ": ")

        try:
            user_value = float(user_value)

            if MINIMUM_GRADE <= user_value <= MAXIMUM_GRADE:
                is_valid = True
                ce_list.append(user_value)
            else:
                print(f"The grade must be between {MINIMUM_GRADE} and {MAXIMUM_GRADE}.")
        except ValueError:
            print("You must enter the grade as a number.")
print(ce_list)

for test_grade in range(NUMBER_OF_TEST):
    is_valid = False

    while not is_valid:
        user_value = input("Enter your grade on Test Activity " + str(test_grade + 1) + ": ")

        try:
            user_value = float(user_value)

            if MINIMUM_GRADE <= user_value <= MAXIMUM_GRADE:
                is_valid = True
                test_list.append(user_value)
            else:
                print(f"The grade must be between {MINIMUM_GRADE} and {MAXIMUM_GRADE}.")
        except ValueError:
            print("You must enter the grade as a number.")
print(test_list)

for ba_grade in range(NUMBER_OF_BAS):
    is_valid = False

    while not is_valid:
        user_value = input("Enter your grade on Bonus Assignment " + str(ba_grade + 1) + ": ")

        try:
            user_value = float(user_value)

            if MINIMUM_GRADE <= user_value <= MAXIMUM_GRADE:
                is_valid = True
                Bonus_list.append(user_value)
            else:
                print(f"The grade must be between {MINIMUM_GRADE} and {MAXIMUM_GRADE}.")
        except ValueError:
            print("You must enter the grade as a number.")
print(Bonus_list)


# Processing.

# Get the average of the PCAs.
pca_average_grade = sum(pca_list) / len(pca_list)
# Calculate the total weight of PCAs by multiplying the average by the weight.
pca_weight_earned = pca_average_grade / 100 * PCA_TOTAL_WEIGHT

# Add up all of the CEs in the list.
ce_average_grade = sum(ce_list) / len(ce_list)
# Divide the CE grade by the number of CEs and multiply by its weight.
ce_weight_earned = ce_average_grade / 100 * CE_TOTAL_WEIGHT

# Get the average of the Tests.
test_average_grade =  sum(test_list) / len(test_list)
# Calculate the total weight of Tests by multiplying the average by the weight.
test_weight_earned = test_average_grade / 100 * TEST_TOTAL_WEIGHT

# Get the average of the Bas.
ba_average_grade = sum(Bonus_list) / len(Bonus_list)
# Calculate the total weight of Bas by multiplying the average by the weight.
ba_weight_earned = ba_average_grade / 100 * BA_TOTAL_WEIGHT

# Get the Overall weight
overall_weight = pca_weight_earned + ce_weight_earned + test_weight_earned  + ba_weight_earned
# Get the overall grade
overall_grade = pca_weight_earned/ PCA_TOTAL_WEIGHT + ce_weight_earned/ CE_TOTAL_WEIGHT + ba_weight_earned/ BA_TOTAL_WEIGHT * 100

# Output.
print(pca_average_grade)
print(ce_average_grade)
print(test_average_grade)
print(ba_average_grade)
print(overall_grade)

input("\nPress Enter to exit the program...")