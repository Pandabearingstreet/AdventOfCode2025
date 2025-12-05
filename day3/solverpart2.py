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
    digits = [0] * 12
    idx = -1
    for digit_number in range(0, 11):
        digits[digit_number], idx = earliest_highest(bank[:-(11-digit_number)], idx+1)
    digits[11] = earliest_highest(bank, idx+1)[0]
    bankpower = int(''.join([str(x) for x in digits]))
    bankpowers.append(bankpower)

print(sum(bankpowers))

