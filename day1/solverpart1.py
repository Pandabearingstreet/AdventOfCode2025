import numpy as np
with open('day1/input.txt') as f:
    data = f.read().split('\n')

#replace L with - and R with +
data = [x.replace('L', '-') for x in data]
data = [x.replace('R', '+') for x in data]
data = [int(x) for x in data]
data = (50 + np.cumsum(data)) % 100
# the pw is the amount of times we land on the position 0
pw = len(np.where(data == 0)[0])
print(pw)


