# create a sequence with the first number
sequence=[4]
# recursive
for i in range (0,5):
    sequence.append(2*sequence[i]+3) # add next number with a[n]=2*a[n-1]+3
print(sequence) #print the answer