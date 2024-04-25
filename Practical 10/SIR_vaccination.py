# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# set up its dimensions and resolution
plt.figure(figsize =(6 ,4) , dpi=150)
time = range(0,1001) # xlabel
# define a function to try different percentages and plot the number of infected people for each of them.
def herd_immunity(percentage, name):
    # define the basic variables of the model
    N = 10000
    Infected = [1]
    Susceptible = [N - Infected[0]- int(percentage * N)]
    if percentage == 1:
        Infected = [0]
        Susceptible = [0]
    Recovered = [0]
    beta = 0.3
    gamma = 0.05
    # time course
    for i in range(0, 1000):
        # calculate the probability of recovery and infection
        recovery_probability = np.random.choice(range(2), Infected[i], p=[1- gamma, gamma])
        infected_probability = np.random.choice(range(2), Susceptible[i], p=[1- beta * Infected[i] / N, beta * Infected[i] / N])
        # calculate the change in each of the population
        Infected.append(Infected[i] + sum(infected_probability) - sum(recovery_probability))
        Recovered.append(Recovered[i] + sum(recovery_probability))
        Susceptible.append(Susceptible[i] - sum(infected_probability))
    # plot the results
    plt.plot(time, Infected, label = name, color=cm.viridis(percentage))
# repect 11 times to plot all the resilts
for i in range(0, 110, 10):
    herd_immunity(i / 100, str(i) + "%")
# plot the labels, title, and legend
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model with different vaccination rates')
plt.legend()
plt.show()
plt.clf()
