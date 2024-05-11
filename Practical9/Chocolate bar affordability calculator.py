def Chocolate_bar_affordability_calculator(total_money, price):
    """
    Determine how many chocolate bars the user is able to afford at the supermarket.
    Return the number of bars that can be bought and the change that will be left over.
    """
    bars = total_money // price
    change = total_money % price
    return bars, change 
# Example
print(Chocolate_bar_affordability_calculator(100, 7))