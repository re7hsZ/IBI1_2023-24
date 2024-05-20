# Pseudocode:
# Import the required library for plotting graphs
# Initialize lists containing the populations of cities in the UK and China
# Create corresponding lists with city names
# Create dictionaries to link city populations with their names for both UK and China
# Sort the population lists in ascending order
# Print the sorted city names and their populations for both UK and China
# Plot bar graphs for the populations of cities in the UK and China
# Clear the figure after each plot to avoid overlap

# Import the matplotlib library for plotting graphs
import matplotlib.pyplot as plt

# Create lists of city populations in the UK and China
uk_cities = [0.56, 0.62, 0.04, 9.7]
china_cities = [0.58, 8.4, 29.9, 22.2]

# Create lists of corresponding city names
uk_cities_names = ['Edinburgh', 'Glasgow', 'Stirling', 'London']
china_cities_names = ['Haining', 'Hangzhou', 'Shanghai', 'Beijing']

# Create dictionaries to link city populations with their names
# Pseudocode: For each city in the list, add an entry to the dictionary with population as key and city name as value
uk = {}
for i in range(len(uk_cities)):
    uk[uk_cities[i]] = uk_cities_names[i]

china = {}
for i in range(len(china_cities)):
    china[china_cities[i]] = china_cities_names[i]

# Sort the city populations in ascending order
# Pseudocode: Use the sort function to order the populations
uk_cities.sort()
china_cities.sort()

# After sorting, rearrange the city names to match the sorted populations
# Pseudocode: Iterate over the sorted populations and update the city names list with corresponding names from the dictionary
uk_cities_names = [uk[city] for city in uk_cities]
china_cities_names = [china[city] for city in china_cities]

# Output the sorted city names and their populations
print('UK cities:')
for city_name in uk_cities_names:
    print(city_name, ': ', uk[city_name])

print('China cities:')
for city_name in china_cities_names:
    print(city_name, ': ', china[city_name])

# Draw the bar plots for the populations of cities in the UK and China
# Pseudocode: Use matplotlib to create bar plots with city names on the x-axis and populations on the y-axis
plt.figure()
plt.bar(uk_cities_names, uk_cities, color='pink')
plt.ylabel("Population (millions)") 
plt.title("Populations of cities in the UK in 2024") 
plt.show()
plt.clf()  # Clear the figure

# Draw the bar plots for the populations of cities in China
plt.bar(china_cities_names, china_cities, color='orange')
plt.ylabel("Population (millions)") 
plt.title("Populations of cities in China in 2024") 
plt.show()
plt.clf()  # Clear the figure
