# Pseudocode:
# Initialize variables for the holiday length and the starting culture density
# Set the holiday length to 0
# Set the initial culture density to 5%

# Start a loop that will continue as long as the culture density is less than or equal to 90%
# Inside the loop:
    # Double the culture density for each day
    # Increment the holiday counter by 1 day
    # After doubling the density, check if it exceeds 90%
    # If it does, break out of the loop as the cells will die

# Print the maximum number of days that can be taken as a holiday before the culture density goes over 90%

# Actual Code:
holiday = 0  # Initialize the number of days the holiday can last
density = 5  # Initial culture density percentage

# Start a loop to simulate the cell line doubling every day
while density <= 90:
    density *= 2  # Double the culture density each day
    holiday += 1  # Increment the holiday counter by one day

    # Check if the culture density has exceeded 90%
    if density > 90:
        # If the density is over 90%, the cells will die, so break the loop
        break

# Print out the result
print("I can stay away from the lab for", holiday, "days.")
