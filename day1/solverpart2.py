import numpy as np
with open('day1/input.txt') as f:
    data = f.read().split('\n')

#replace L with - and R with +
data = [x.replace('L', '-') for x in data]
data = [x.replace('R', '+') for x in data]
data = [int(x) for x in data]

positions = [49, 50]
# go through each rotation one step at a time
for x in data:
    positions+=list(np.linspace(positions[-1], positions[-1] + x, abs(x)+1, dtype=int)[1:])

# the pw is the amount of times we land on the position 0
positions = np.array(positions)
print(positions[:100])
pw = len(np.where(positions%100 == 0)[0])
print(pw)


