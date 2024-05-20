# Pseudocode:
# Define a function named 'Favourite_James_Bond' that takes one parameter:
# 'year' which is the year in which the person was born.
# The function calculates the favorite James Bond actor based on the year the person turned 18.
# Add 18 to the birth year to find the year when the person was 18.
# Set up variables for each James Bond actor with their respective years.
# Use a series of if-elif-else statements to determine the favorite actor based on the calculated year.
# Print the name of the actor as the output.

def Favourite_James_Bond(year):
    """
    Determine an individual's favorite James Bond actor based on the year they turned 18.
    
    Parameters:
    year (int): The year in which the person was born.
    
    Returns:
    str: The name of the James Bond actor that the individual most likely prefers.
    """
    # Calculate the year when the person turned 18
    year_turned_18 = year + 18
    
    # Define the years each actor played James Bond
    RM_years = (1973, 1986)
    TD_years = (1987, 1994)
    PB_years = (1995, 2005)
    DC_years = (2006, 2021)
    
    # Determine the favorite James Bond actor based on the year the person turned 18
    if RM_years[0] <= year_turned_18 <= RM_years[1]:
        return "Roger Moore"
    elif TD_years[0] <= year_turned_18 <= TD_years[1]:
        return "Timothy Dalton"
    elif PB_years[0] <= year_turned_18 <= PB_years[1]:
        return "Pierce Brosnan"
    elif DC_years[0] <= year_turned_18 <= DC_years[1]:
        return "Daniel Craig"
    else:
        return "ERROR"

# Example usage of the function:
# Prompt the user to input the year they were born
birth_year = int(input("Type in the year you were born. \n"))

# Call the function with the birth year and print the result
favorite_bond_actor = Favourite_James_Bond(birth_year)
print(f"Your favorite James Bond actor is: {favorite_bond_actor}")
