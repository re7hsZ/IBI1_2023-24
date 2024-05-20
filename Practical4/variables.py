# Initial time
a = 40  # Initial 5km run time before any training
b = 36  # Time after a month of running training
c = 30  # Time after a second month of combined running and strength training

# Calculate the time improvement
d = a - b  # Time improvement from running training alone
e = b - c  # Time improvement from combined running and strength training

# Output the improvement results
print("Improvement from running only:", d) # d = 4
print("Improvement from running and strength training:", e) # e = 6

# Comment explaining which training regime had a greater effect
if e > d:
    print("# Using a combination of running and strength exercises had a greater improvement on running time.")
elif d == e:
    print('d & e are same, two training has the same influence.')
else:
    print("# Running only had a greater improvement on running time.")
#e is greater
#Using a combination of running and strength exercises had a greater improvement on running time.

# Boolean variables
X = True
Y = False

# Dynamically calculate W based on the values of X and Y
W = X or Y  # In Python, the 'or' operator represents the logical 'either X or Y'
#W = 'True'

#The truth table for W is like this
'''
X	    Y	    W(either X or Y)
True	True	False
True	False	True
False	True	True
False	False	False
'''
