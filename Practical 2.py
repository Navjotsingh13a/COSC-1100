# Author: Navjot Singh
# Date: April 12, 2024
# Modified: April 12, 2024
# Function: format_team_name
# Description: Accepts a string "Home" or "Away" (regardless of case) and returns
# the string in proper casing via the String.title() method, along 
# with a notation if they are in the lead. All invalid entries 
# return "Error".
 
VALID_TEAMS = {"home", "away"}
KING_SIGN = " (king sign)"

def format_team_name(team):

    if team.lower() in VALID_TEAMS:
        formatted_team = team.title()
        if formatted_team == "Home":
            formatted_team += KING_SIGN
        return formatted_team
    else:
        return "Error"

print(format_team_name("Home"))   
print(format_team_name("AWAY"))   
print(format_team_name("Invalid"))