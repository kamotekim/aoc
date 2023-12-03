from collections import defaultdict
import re
with open("input.txt") as f:
    lines = f.readlines()

# Map positions to the indices of numbers
pos_to_ind = defaultdict(lambda: -1)

# Build an array of numbers
numbers = []

# Parse the numbers
for row, line in enumerate(lines):
    line = line.strip()
    for index, num in map(lambda m: (m.start(0), m.group(0)), re.finditer("\d+", line)):
        numbers.append(int(num))
        # Each position the number occupies is added
        for col, _ in enumerate(num):
            pos_to_ind[(row, index + col)] = len(numbers) - 1

# Offsets to use at each symbol
offsets = [(i,j) for i in range(-1,2) for j in range(-1,2)]

# Get the sum of adjacent numbers
result = 0
for row, line in enumerate(lines):
    line = line.strip()
    for col, character in enumerate(line):
        if character in "0123456789.": continue
        adjacent = []
        for offset_r, offset_c in offsets:
            new_row = offset_r + row
            new_col = offset_c + col
            if new_row < 0 or 0 >= len(lines): continue
            if new_col < 0 or 0 >= len(line): continue
            
            num_index = pos_to_ind[(new_row, new_col)]

            if num_index < 0: continue
            if num_index in adjacent: continue
            adjacent.append(num_index)
        result += sum((numbers[index] for index in adjacent))

print(f"P1: {result}")


        
result = 0
for row, line in enumerate(lines):
    line = line.strip()
    for col, character in enumerate(line):
        if character != '*': continue
        adjacent = []
        for offset_r, offset_c in offsets:
            new_row = offset_r + row
            new_col = offset_c + col
            if new_row < 0 or 0 >= len(lines): continue
            if new_col < 0 or 0 >= len(line): continue
            
            num_index = pos_to_ind[(new_row, new_col)]

            if num_index < 0: continue
            if num_index in adjacent: continue
            adjacent.append(num_index)
        
        if len(adjacent) != 2: continue
        result += numbers[adjacent[0]] * numbers[adjacent[1]]

print(f"P2: {result}")


        

