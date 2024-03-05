#set the lenth of holiday and the original culture density
holiday = 0
density = 5
# cell line doubles
while density <= 90/2:
    density *= 2
    holiday += 1
print ("I can stay away from the lab for" , holiday , "days.")
