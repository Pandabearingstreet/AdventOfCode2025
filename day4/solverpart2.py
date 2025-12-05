import numpy as np
import scipy.signal as signal
with open('day4/input.txt') as f:
    data = f.read().split('\n')
# make the data a numpy maxtrix, replacing @ with 1 and . with 0
data = [x.replace('@', '1') for x in data]
data = [x.replace('.', '0') for x in data]
data = [list(x) for x in data]
data = np.array(data, dtype=int)
original_size = np.sum(data)
while True:
    # convolve with a 3x3 uniform kernel
    neighbors = signal.convolve2d(data, np.ones((3,3)), mode= 'same', boundary='fill', fillvalue=0)
    # the relevant condition is where in the data, there is a 1, and in the neighbors there is a 4 or lower
    removable_data = data * (neighbors <= 4)
    if np.sum(removable_data) == 0:
        break
    data = data - removable_data

print(original_size - np.sum(data))
