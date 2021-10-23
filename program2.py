"""
A simple program that asks for how many apples and oranges you want to buy.
After that, it shows the total amount that you have to pay.
"""

#This variable contains the input statements
#then followed by integer function that converts 
#the entered value into an integer number.
apple = int(input('Enter the desired number of apples (20 pesos per apple): '))
orange = int(input('Enter the desired number of oranges (25 pesos per orange): '))

#The fixed price for an apple and orange.
priceApple = 20
priceOrange = 25

#This statement contains the expression
#to get the total amount to be paid.
totalAmount = (priceApple*apple + priceOrange*orange)

#This statement displays the total amount to be paid.
print(f'The total amount is {totalAmount} pesos.')