# -*- coding: utf-8 -*-
# round i: only stops at every ith cat and change their states 
def action_round(i):
    for j in range(1, 101):
        if j%i == 0:
            if cat_dict[j]:
                cat_dict[j] = False
            else:
                cat_dict[j] = True
# set every cat's number to False initially                
cat_dict = {}
for j in range(1, 101):
    cat_dict[j] = False

#repeat action for 100 rounds    
for i in range(1, 101):
    action_round(i)

# output which cats have hats at the end
for i in range(1, 101):
    if cat_dict[i]:
        print(f"Cat {i} has a hat")
       
        
        
        
        

