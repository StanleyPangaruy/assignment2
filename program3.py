"""
This program shows how much apple you can get for your money
and tells your change if you do have any.
"""

#These variables gather numerical inputs for money and price.
money = int(input('Enter the amount of money you have: '))
price = int(input('Enter the price of the apple: '))

#These variables contains the expression to get
#the maximum apple you can afford as well as your change.
maxApple = int((money/price))
change = int((money - maxApple*price))

#This statement displays the maximum 
#apples you have and your change.
print(f'You can buy {maxApple} apples and your change is {change} pesos.')