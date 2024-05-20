# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change the current working directory to where the dataset is stored
os.chdir("C:\Users\lenovo\Desktop\IBI\IBI1_2023-24\IBI1_2023-24\Practical7")

# Import the dataset into a pandas dataframe
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Pseudocode:
# Show the fourth column (DALYs) from every 10th row, starting from the first row, up to the first 100 rows (inclusive)
# Use iloc to access specific rows and columns by their index numbers
print(dalys_data.iloc[0:100:10, 3])  # 3 is the index for the fourth column

# Pseudocode:
# Create a Boolean list to filter rows corresponding to Afghanistan
# Use this list with loc to display only the DALYs for Afghanistan
Afghanistan = (dalys_data.iloc[:, 0] == 'Afghanistan')  # Compare the first column with 'Afghanistan'
print(dalys_data.loc[Afghanistan, "DALYs"])  # Use loc to filter rows and select the "DALYs" column

# Pseudocode:
# Create a Boolean list to filter rows corresponding to China
# Use this list to create a new dataframe 'china_data' with only China's data
China = (dalys_data.iloc[:, 0] == 'China')  # Compare the first column with 'China'
china_data = dalys_data.loc[China, :]  # Create a new dataframe with China's data

# Pseudocode:
# Compute the mean DALYs in China using numpy's mean function
# Print the result and compare it with the DALYs in 2019
mean_china_DALYs = np.mean(china_data['DALYs'])  # Calculate the mean of the "DALYs" column for China
print('The mean DALYs in China:' , mean_china_DALYs)  # Add a comment about the 2019 DALYs compared to the mean

# Pseudocode:
# Create a plot showing the DALYs over time in China
# Customize the plot with appropriate title and rotated x-axis labels
plt.figure()
plt.plot(china_data['Year'], china_data['DALYs'], 'b+')  # Plot the "Year" vs "DALYs" for China
plt.xticks(china_data['Year'], rotation=-90)  # Rotate the x-axis labels for better readability
plt.title('DALYs over time in China')  # Add a title to the plot
plt.show()
plt.clf()  # Clear the plot

# Pseudocode:
# Create a Boolean list to filter rows with data from the year 2019
# Use this list to create a new dataframe 'data_2019' with only the 2019 data
DALYs_2019 = (dalys_data.iloc[:, 2] == 2019)  # Compare the third column (Year) with 2019
data_2019 = dalys_data.loc[DALYs_2019, :]  # Create a new dataframe with data from 2019

# Pseudocode:
# Plot a boxplot of DALYs across countries in 2019
# Label the plot appropriately
plt.boxplot(data_2019['DALYs'], labels=['DALYs across countries in 2019'])  # Create a boxplot for the "DALYs" column
plt.show()
plt.clf()  # Clear the plot
