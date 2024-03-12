# -*- coding: utf-8 -*-
def enrollment_stats(list):
    enrollment_values = [element[1] for element in list]
    tuition_fees = [element[2] for element in list]
    return (enrollment_values, tuition_fees)

def mean(list):
    return sum(list)/len(list)

def median(list):
    list.sort()
    if len(list) % 2 == 0:
        median_num = (list[len(list)//2] + list[len(list)//2-1])/2
        # If even values contained in list
        # median is usually defined to be the arithmetic mean of the two middle values
    else:
        median_num = list[len(list)//2]
        # If odd values contained in list
        # median is the middle value
    return median_num 

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollment_values, tuition_fees = enrollment_stats(universities)

print("*****" * 6)
print(f"Total students:   {sum(enrollment_values):,}")
print(f"Total tuition:  $ {sum(tuition_fees):,}\n\n")
print(f"Student mean:     {mean(enrollment_values):,.2f}")
print(f"Student median:   {median(enrollment_values):,}\n\n")
print(f"Tuition mean:   $ {mean(tuition_fees):,.2f}")
print(f"Tuition median: $ {median(tuition_fees):,}")
print("*****" * 6)

        
        
        
        
        
        
        
        

