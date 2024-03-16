# -*- coding: utf-8 -*-
import random

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
 }


state, capital = random.choice(list(capitals.items()))

# Game loops until guest enter correct answer
# Or enter "exit" to quit
while True:
    print(f"What's the capital of {state}?")
    reply = (input("Enter your answer or type 'exit' to quit: ")).lower()
    if reply == "exit":
        print(f"The answer is {capital}, goodbye!")
        break
    elif reply == capital.lower():
        print("Corrct! Well done!")
        break
       
        
        
        
        

