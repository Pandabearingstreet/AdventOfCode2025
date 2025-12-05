import numpy as np


with open('day5/input.txt') as f:
    data = f.read().split('\n')

# split at the item in the list containing ''
fresh_item_ranges = data[:data.index('')]

# split the ranges into start and end
for i in range(len(fresh_item_ranges)):
    fresh_item_ranges[i] = fresh_item_ranges[i].split('-')

# combine ranges with overlap into a single range
fresh_item_ranges = np.array(fresh_item_ranges, dtype=int)


for i, range in enumerate(fresh_item_ranges):
    for j, range2 in enumerate(fresh_item_ranges):
        # if range j is [0, -1], skip
        if range2[0] == 0 and range2[1] == -1:
            continue
        if i == j:
            continue
        # case 1, start of range i is in range j
        if range[0] <= range2[1] and range[0] >= range2[0]:
            
            # 1.1 end of range i is in range j, set range i to [0,-1]
            if range[1] <= range2[1]:

                fresh_item_ranges[i] = [0, -1]
            # 1.2 end of range i is not in range j, set range j to end of range i
            else:

                fresh_item_ranges[j][1] = range[1]
                fresh_item_ranges[i] = [0, -1]
            break
        # case 2 end of range i is in range j  
        elif range[1] <= range2[1] and range[1] >= range2[0]: 
             # since start of range i is not in range j, set range j to start of range i
             fresh_item_ranges[j][0] = range[0]
             fresh_item_ranges[i] = [0, -1]
             break
             

amount_of_fresh_ingredients = 0
for i in fresh_item_ranges:
       amount_of_fresh_ingredients += int(i[1])-int(i[0]) +1

print(amount_of_fresh_ingredients)