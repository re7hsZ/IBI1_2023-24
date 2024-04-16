# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define the basic variables of the model
N = 10000
Infected = [1]
Susceptible = [N - Infected[0]]
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
plt.figure(figsize =(6 ,4) , dpi=150)
time = range(0,1001)
plt.plot(time, Susceptible, label='Susceptible')
plt.plot(time, Infected, label='Infected')
plt.plot(time, Recovered, label='Recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model')
plt.legend()
plt.show()
plt.clf()