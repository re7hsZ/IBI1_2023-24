# Set the initial culture density and the length of the holiday
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
