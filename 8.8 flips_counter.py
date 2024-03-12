# -*- coding: utf-8 -*-
import random

def flips_per_sequence():
    
    """calculate how many flips are needed for the sequence to contain both heads and tails"""
    
    head_total = 0
    tail_total = 0

    while(head_total == 0 or tail_total == 0):
        integer = random.randint(0, 1)
        if integer == 1:
            head_total = head_total + 1
        else:
            tail_total = tail_total + 1
    return head_total + tail_total


total = 0
for i in range(10_000):
    total = total + flips_per_sequence()

print(f"Average number rolled: {total / 10_000:.2f}")
    