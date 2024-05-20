# Pseudocode:
# Define variables for the average hours spent on various activities by a university student
# Create a dictionary to store the activities and their corresponding hours
# Print the dictionary to display the recorded data
# Import the matplotlib library for plotting graphs
# Prepare data for a pie chart and plot it to visualize the distribution of time spent on activities
# Take user input for a specific activity and print the average hours spent on that activity

# Define variables for the requested activities
Sleeping = 8
Classes = 6
Studying = 3.5
TV = 2
Music = 1
Other = 3.5  # Additional category for hours not included in the table

# Create a dictionary with activities as keys and hours as values
dictionary = {
    'Sleeping': Sleeping,
    'Classes': Classes,
    'Studying': Studying,
    'TV': TV,
    'Music': Music,
    'Other': Other  # New entry 'Other' to account for remaining hours
}

# Print the dictionary to display the recorded data
print("Average Day of a University Student: ")
print(dictionary)

# Import the matplotlib library for plotting graphs
import matplotlib.pyplot as plt

# Prepare data for a pie chart
activity_labels = ['Sleeping', 'Classes', 'Studying', 'TV', 'Music', 'Other']
time = [Sleeping, Classes, Studying, TV, Music, Other]

# Plot a pie chart to visualize the distribution of time spent on activities
plt.figure()
plt.pie(time, labels=activity_labels)
plt.title("Distribution of Time for a University Student's Average Day")
plt.show()

# Close the figure to clear it for any subsequent plots
plt.clf()

# Output the average number of hours spent on one activity taken from the input list
# Prompt the user to input an activity and print the corresponding hours from the dictionary
activity = input("Type in the activity you want to know the average number of hours: ")
print(f"The average number of hours spent on {activity} is: {dictionary[activity]}")
