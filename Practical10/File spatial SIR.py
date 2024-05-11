# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# make array of all susceptible population
population = np.zeros((100, 100))
# chooseonerandom point in the 100 × 100 array for where the outbreak happens
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
# plot a heat map
plt.figure(figsize = (6, 4), dpi = 150)
plt.subplot(2, 2, 1)
plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
# define the basic variables of the model
beta = 0.3
gamma = 0.05
# time course
for i in range(1, 101):
    # find the infected points
    infected_points = np.where(population == 1)
    # find the neighbours
    for x, y in zip(infected_points[0], infected_points[1]):
        neighbours = [(x - 1, y - 1), (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y), (x + 1, y + 1), (x -+1, y - 1), (x - 1, y + 1)]
        # infect the neighbours
        for nx, ny in neighbours:
            if 0 <= nx < 100 and 0 <= ny < 100:
                if population[nx, ny] == 0:
                    population[nx, ny] = sum(np.random.choice(range(2), 1, p = [1 - beta, beta]))
        # recover
        population[x, y] = sum(np.random.choice([1, 2], 1, p = [1 - gamma, gamma]))
    # plot subplots   
    if i == 10:
        plt.subplot(2, 2, 2)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    if i == 50:
        plt.subplot(2, 2, 3)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    if i == 100:
        plt.subplot(2, 2, 4)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
plt.show()
plt.clf()