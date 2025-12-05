import numpy as np

with open('day2/input.txt') as f:
    data = f.read().split(',')

data = [x.split('-') for x in data]

data = [np.arange(int(x[0]), int(x[1])+1) for x in data]
# flatten the data
data = np.concatenate(data)

#data is invalid, if the first half and the second part of the number are the same
invalid_data = np.array([x for x in data if str(x)[:len(str(x))//2] == str(x)[len(str(x))//2:]])

print(sum(invalid_data))