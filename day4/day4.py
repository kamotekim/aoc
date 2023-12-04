
import re
with open("input.txt") as f:
    lines = f.readlines()


# Part 1
res = 0
for row, line in enumerate(lines):
    card, rest = line.split(':')
    winning, others = rest.split('|')
    winning_nums = set(re.findall("\d+", winning))
    other_nums = set(re.findall("\d+", others))
    both = winning_nums.intersection(other_nums)

    res += 2**(len(both) - 1) if len(both) > 1 else 0

print(f"P1: {res}")



# Part 2
dp = [1] * len(lines)
for row, line in reversed(list(enumerate(lines))):
    card, rest = line.split(':')
    winning, others = rest.split('|')
    winning_nums = set(re.findall("\d+", winning))
    other_nums = set(re.findall("\d+", others))
    both = winning_nums.intersection(other_nums)
    
    for i in range(1, len(both) + 1):
        dp[row] += dp[row + i] if row + i < len(lines) else 0

print(f"P2: {sum(dp)}")


        

