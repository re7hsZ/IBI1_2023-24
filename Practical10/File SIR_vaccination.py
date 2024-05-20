# Import the necessary libraries for numerical operations, plotting, and color mapping.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Set up the plot dimensions and resolution.
plt.figure(figsize=(6, 4), dpi=150)
time = range(0, 1001)  # Time points for the x-axis.

# Define a function to simulate the SIR model with different vaccination percentages and plot the number of infected people.
def herd_immunity(percentage, name):
    """
    Simulate the SIR model with a given vaccination percentage and plot the infected population over time.
    
    Parameters:
    percentage (float): The percentage of the population vaccinated.
    name (str): The label for the specific vaccination percentage line on the plot.
    """
    # Define the basic variables of the model.
    N = 10000  # Total population size.
    Infected = [1]  # Initially, one person is infected.
    Susceptible = [N - Infected[0] - int(percentage * N)]  # Calculate the initial number of susceptible individuals.
    Recovered = [0]  # Initially, no one has recovered.
    beta = 0.3  # Infection rate.
    gamma = 0.05  # Recovery rate.
    
    # If the percentage is 100, all are vaccinated, and the infection cannot start.
    if percentage == 1:
        Infected = [0]
        Susceptible = [0]
    
    # Time course of the model.
    for i in range(1000):  # Loop over 1000 time points.
        # Calculate the number of recoveries at this time step.
        recovery_probability = np.random.choice([0, 1], size=Infected[i], p=[1 - gamma, gamma])
        recoveries = sum(recovery_probability)
        
        # Calculate the number of new infections at this time step.
        infected_probability = np.random.choice([0, 1], size=Susceptible[i], p=[1 - beta * Infected[i] / N, beta * Infected[i] / N])
        new_infections = sum(infected_probability)
        
        # Update the counts for each group.
        Infected.append(Infected[i] + new_infections - recoveries)
        Recovered.append(Recovered[i] + recoveries)
        Susceptible.append(Susceptible[i] - new_infections)
    
    # Plot the results for the given vaccination percentage.
    # Use a color gradient based on the percentage for visual distinction.
    plt.plot(time, Infected, label=name, color=cm.viridis(percentage))

# Call the herd_immunity function for different vaccination percentages to plot the results.
for i in range(0, 110, 10):
    herd_immunity(i / 100, str(i) + "%")

# Add plot labels, title, and legend.
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()

# Display the plot.
plt.show()
plt.clf()  # Clear the current figure to prepare for any subsequent plots.
