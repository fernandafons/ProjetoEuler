lista = [1, 2]
valor = 0
soma = 0

while valor < 4000000:
    valor = lista[-1] + lista[-2]
    if valor < 4000000:
        lista.append(valor)

for i in lista:
    if i % 2 == 0:
        soma += i

print(lista)
print(soma)