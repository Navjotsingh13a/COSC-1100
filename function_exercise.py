# Author: Navjot Singh
# Created: March 15, 2024
# Modified: March 15, 2024
# Description:

def is_list_numeric(list_to_check):
    try:
        for item in list_to_check:
            float(item)  # Try to convert each item to float
    # If ValueError is raised, return False
    except ValueError:
        return False
     # If all items are successfully converted, return True
    return True

def cap_list(list_to_cap, minimum=0, maximum=100):
    capped_list = []
    for item in list_to_cap:
         # If item is less than the minimum, append the minimum value
        if item < minimum:
            capped_list.append(minimum)
       # If item is greater than the maximum, append the maximum value
        elif item > maximum:
              # Otherwise, append the original item
            capped_list.append(maximum)
        else:
            capped_list.append(item)
    return capped_list

def drop_highest_and_lowest(list_to_drop):
    if len(list_to_drop) < 3:
        return []
    else:
        # Remove the minimum and maximum values from the list
        list_to_drop.remove(min(list_to_drop))
        list_to_drop.remove(max(list_to_drop))

        return list_to_drop