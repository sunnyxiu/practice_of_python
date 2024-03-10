# -*- coding: utf-8 -*-
"""
Perform calculations on user input
for example:
Enter a base: 1.2
Enter an exponent: 3
1.2 to the power of 3 = 1.7279999999999998
"""
base = input('Enter a base: ')
exponent = input('Enter an exponent: ')
result = float(base) ** float(exponent)
print(f"{base} to the power of {exponent} =  {result}")

