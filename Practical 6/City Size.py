# import matplotlib
import matplotlib.pyplot as plt
# create two lists of cities in UK and China
uk_cities = [0.56, 0.62, 0.04, 9.7]
china_cities = [0.58, 8.4, 29.9, 22.2]
uk_cities_names = ['Edinburgh', 'Glasgow', 'Stirling', 'London']
china_cities_names = ['Haining', 'Hangzhou', 'Shanghai', 'Beijing']
# create two dictionaries to link names and numbers
uk = {}
for i in range(len(uk_cities)):
    uk[uk_cities[i]] = uk_cities_names[i]
china = {}
for i in range(len(china_cities)):
    china[china_cities[i]] = china_cities_names[i]
# sort
uk_cities.sort()
china_cities.sort()
# output
print('UK cities:')
for i in range(len(uk_cities)):
    uk_cities_names[i] = uk[uk_cities[i]] # rearrange the city names
    print(uk[uk_cities[i]], ': ', uk_cities[i], sep = '')
print('China cities:')
for i in range(len(china_cities)):
    china_cities_names[i] = china[china_cities[i]] # rearrange the city names
    print(china[china_cities[i]], ': ', china_cities[i], sep = '')
# draw the bar plots of cities in the UK
plt.figure()
plt.bar(uk_cities_names, uk_cities, color = 'pink')
plt.ylabel("Population (millions)") 
plt.title("Populations of cities in the UK in 2024") 
plt.show()
plt.clf()
# draw the bar plots of cities in China
plt.bar(china_cities_names, china_cities, color = 'orange')
plt.ylabel("Population (millions)") 
plt.title("Populations of cities in China in 2024") 
plt.show()
plt.clf()