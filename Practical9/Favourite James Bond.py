def Favourite_James_Bond(year):
    year += 18
    RM = "Roger Moore"
    TD = "Timothy Dalton"
    PB = "Pierce Brosnan"
    DC = "Daniel Craig"
    if year >= 1973 and year <= 1986:
        print(RM)
    elif year >= 1987 and year <= 1994:
        print(TD)
    elif year >= 1995 and year <= 2005:
        print(PB)
    elif year >= 2006 and year <= 2021:
        print(DC)
    else:
        print("ERROR")
# Example
year = input("Type in the year you were born. \n")
year = int(year)
Favourite_James_Bond(year)