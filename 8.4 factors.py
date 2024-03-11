# -*- coding: utf-8 -*-
integer = input("Enter a positive integer: ")
if int(integer) <= 0:
    print(f"{integer} is not a positive integer.")
else:
    for i in range(int(integer)):
        if int(integer) % (i + 1) == 0: #(i+1) range from 1 to 12
            print(f"{i+1} is a factor of {integer}")