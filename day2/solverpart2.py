import numpy as np

with open('day2/input.txt') as f:
    data = f.read().split(',')

data = [x.split('-') for x in data]

data = [np.arange(int(x[0]), int(x[1])+1) for x in data]
invalid_data = []
for IDrange in data:
    for ID in IDrange:
        length = len(str(ID))
        divisors_of_length = [x for x in range(2, length+1) if length % x == 0]

        for divisor in divisors_of_length[::-1]:
            #divide the number into as many parts as the divisor says
            parts = [str(ID)[i:i+length//divisor] for i in range(0, length, length//divisor)]
            if all([x == parts[0] for x in parts]):
                invalid_data.append(ID)
                break

print(sum(invalid_data))