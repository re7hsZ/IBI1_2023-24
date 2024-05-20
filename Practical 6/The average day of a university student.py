# create variables of the requested activities
Sleeping = 8
Classes = 6
Studying = 3.5
TV = 2
Music = 1
Other = 3.5
# create a dictionary
dictionary = {'Sleeping':Sleeping, 'Classes':Classes, 'Studying':Studying, 'TV':TV, 'Music':Music, 'Other':Other}
print(dictionary)
# import matplotlib
import matplotlib.pyplot as plt
# two list for activities and their time costs
activity_lables = ['Sleeping', 'Classes', 'Studying', 'TV', 'Music', 'Other']
time = [Sleeping, Classes, Studying, TV, Music, Other]
# draw the pie chart
plt.figure()
plt.pie(time, labels = activity_lables)
plt.show()
# close the figure
plt.clf()
# output the average number of hours spent on one activity taken from the input list
activity = input("Type in the activity you want to know the average number of hours: ")
print(dictionary[activity])
