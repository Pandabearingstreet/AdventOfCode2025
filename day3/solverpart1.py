import numpy as np

with open('day3/input.txt') as f:
    data = f.read().split('\n')

# separate digits
data = [list(x) for x in data]

data = np.array(data, dtype=int)

def earliest_highest(x: np.ndarray, starting_index: int = 0):
    # returns the highest digit in the array, and its index
    return np.max(x[starting_index:]), np.argmax(x[starting_index:]) + starting_index
bankpowers = []

for bank in data:
    power_digit1, idx = earliest_highest(bank[:-1]) # we ignore the last digit, because we need two digits in total
    power_digit2, idx = earliest_highest(bank, idx+1)
    bankpower = int(str(power_digit1) + str(power_digit2))
    bankpowers.append(bankpower)
print(sum(bankpowers))

