# -*- coding: utf-8 -*-
def convert_cel_to_far(deg_Celcius):
    deg_Fahrenheit = deg_Celcius * 9/5 + 32
    return deg_Fahrenheit

def convert_far_to_cel(deg_Fahrenheit):
    deg_Celcius = (deg_Fahrenheit - 32) * 5/9
    return deg_Celcius

deg_Fahrenheit = input("Enter a temperature in degrees F: ")
print(f"{deg_Fahrenheit} degrees F = {convert_far_to_cel(float(deg_Fahrenheit)):.2f} degrees C")

deg_Celcius = input("Enter a temperature in degrees C: ")
print(f"{deg_Celcius} degrees C = {convert_cel_to_far(float(deg_Celcius)):.2f} degrees F")