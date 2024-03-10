# -*- coding: utf-8 -*-
def invest(amount, rate, years):
    num = float(amount)
    for i in range(int(years)):
        num = num * (1 + float(rate)) #count amount of the investment at the end of each year
        print(f"year {i+1}: ${num:,.2f}")
        
amount = input("Please enter your initial deposit: ")
rate = input("Please enter the annual rate of return: ")
years = input("Please enter the number of years to count: ")

invest(amount, rate, years)