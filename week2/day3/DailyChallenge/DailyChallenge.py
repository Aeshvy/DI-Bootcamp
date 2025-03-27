# Daily challenge : Advanced Algorithm

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

pairs = []

for num in list_of_numbers:
    complement = target_number - num
    if complement in list_of_numbers:
        pairs.append((num, complement))

for pair in pairs:
    print(f'{pair[0]} and {pair[1]} sums to the target number 3728')