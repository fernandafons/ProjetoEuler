numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    x = 0
    while x <= 10:
        mult = i * x
        print(i, "x", x, "=", mult)
        x += 1