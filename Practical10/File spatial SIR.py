# Import the necessary libraries for numerical operations and plotting.
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array representing the population, with all individuals susceptible (0).
population = np.zeros((100, 100))

# Randomly select a point in the array to be the initial outbreak location.
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # Set the selected point as infected (1).

# Define the infection and recovery rates.
beta = 0.3
gamma = 0.05

# Plot the initial state of the population using a heat map.
plt.figure(figsize=(6, 4), dpi=150)
plt.subplot(2, 2, 1)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Initial Outbreak")

# Time course of the model, iterating through 100 time points.
for i in range(1, 101):
    # Find the coordinates of infected points in the population.
    infected_points = np.where(population == 1)
    
    # For each infected point, find and infect the neighbors.
    for x, y in zip(infected_points[0], infected_points[1]):
        # Define the neighboring positions (8 neighbors in a 2D grid).
        neighbors = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                     (x - 1, y), (x + 1, y), (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        
        # Infect each neighbor if it's within bounds and currently susceptible.
        for nx, ny in neighbors:
            if 0 <= nx < 100 and 0 <= ny < 100 and population[nx, ny] == 0:
                population[nx, ny] = 1 if np.random.rand() < beta else 0
                
    # Allow infected individuals to recover.
    for x, y in zip(infected_points[0], infected_points[1]):
        if np.random.rand() < gamma:
            population[x, y] = 2  # Recovered state (2).
    
    # Plot the state of the population at specific time points.
    if i == 10:
        plt.subplot(2, 2, 2)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title("Time point 10")
    elif i == 50:
        plt.subplot(2, 2, 3)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title("Time point 50")
    elif i == 100:
        plt.subplot(2, 2, 4)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title("Time point 100")

# Display the final plot with all subplots.
plt.tight_layout()
plt.show()
plt.clf()  # Clear the current figure to prepare for any subsequent plots.
