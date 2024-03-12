# -*- coding: utf-8 -*-
integer = input("Enter a positive integer: ")
if int(integer) <= 0:
    print(f"{integer} is not a positive integer.")
else:
    for i in range(1, int(integer)+1):
        if int(integer) % i == 0: 
            print(f"{i} is a factor of {integer}")
