"""
What is the sum of the digits of the number 2**1000?

1 - fazer a exponenciação
2 - dividir o numero em caracteres
3 - somar os caracteres
"""
result = 0
value = 2**1000

while value > 0:
    result += value % 10
    value = value // 10

print(result)
