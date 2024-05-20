# Import the necessary libraries for numerical operations and plotting.
import numpy as np
import matplotlib.pyplot as plt

# Define the basic variables of the SIR model.
# Set the total population size, N.
# Initially, set the number of infected individuals to 1.
# Calculate the initial number of susceptible individuals by subtracting the initial infected from N.
# Set the number of recovered individuals to 0.
# Define the infection rate, beta, and the recovery rate, gamma.
N = 10000
Infected = [1]
Susceptible = [N - Infected[0]]
Recovered = [0]
beta = 0.3
gamma = 0.05

# Create arrays to track the evolution of each population group over time.
# We will loop over a set number of time points.
for i in range(1000):
    # Pseudocode for the time loop:
    # At each time point, perform the following steps:
    # 1. Calculate the number of recoveries this time point.
    # 2. Calculate the number of new infections this time point.
    # 3. Update the total counts for each group based on recoveries and new infections.
    # 4. Record the state of each group at this time point for later plotting.

    # Calculate the number of individuals recovering this time step.
    recoveries = np.random.choice([0, 1], size=Infected[i], p=[1 - gamma, gamma])
    
    # Calculate the number of new infections this time step.
    # The probability of a susceptible individual becoming infected is beta times the proportion of infected individuals.
    infections = np.random.choice([0, 1], size=Susceptible[i], p=[1 - beta * Infected[i] / N, beta * Infected[i] / N])
    
    # Update the counts for each group.
    new_infected = Infected[i] + sum(infections) - sum(recoveries)
    new_recovered = Recovered[i] + sum(recoveries)
    new_susceptible = Susceptible[i] - sum(infections)
    
    # Record the state of each group at this time point.
    Infected.append(new_infected)
    Recovered.append(new_recovered)
    Susceptible.append(new_susceptible)

# Plot the results of the simulation.
plt.figure(figsize=(6, 4), dpi=150)
time = range(0, 1001)

# Plot the number of susceptible individuals over time.
plt.plot(time, Susceptible, label='Susceptible')

# Plot the number of infected individuals over time.
plt.plot(time, Infected, label='Infected')

# Plot the number of recovered individuals over time.
plt.plot(time, Recovered, label='Recovered')

# Label the axes and provide a title and legend for the plot.
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()

# Display the plot.
plt.show()
plt.clf()  # Clear the current figure to free memory and reset the plot for the next use.
