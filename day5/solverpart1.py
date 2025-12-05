import numpy as np


with open('day5/testinput.txt') as f:
    data = f.read().split('\n')

# split at the item in the list containing ''
fresh_item_ranges = data[:data.index('')]
available_items = data[data.index('')+1:]

for i in range(len(fresh_item_ranges)):
    fresh_item_ranges[i] = fresh_item_ranges[i].split('-')
        
fresh_available_items = []
for i in available_items:
    for j in fresh_item_ranges:
        if int(i) >= int(j[0]) and int(i) <= int(j[1]):
            fresh_available_items.append(i)
            break

print(len(fresh_available_items))

### Unfeeasble solution, _ArrayMemoryError: Unable to allocate 16.3 TiB for an array with shape (2237023032841,) and data type int64
# # expand the ranges
# for i in range(len(fresh_item_ranges)):
#     fresh_item_ranges[i] = fresh_item_ranges[i].split('-')
#     fresh_item_ranges[i] = np.arange(int(fresh_item_ranges[i][0]), int(fresh_item_ranges[i][1])+1)

# # collapse the ranges
# fresh_items = np.concatenate(fresh_item_ranges)

# # check if the available items are fresh
# fresh_available_items = []
# for item in available_items:
#     if int(item) in fresh_items:
#         fresh_available_items.append(item)
# print(len(fresh_available_items))
