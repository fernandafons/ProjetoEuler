"""
What is the sum of the digits of the number 2**1000?
"""

value = map(int,str(2 ** 1000))
total = 0

for i in value:
    total += i

print(total)