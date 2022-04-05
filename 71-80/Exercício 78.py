lista = list()

y = int(input('Digite um valor: '))
lista.append(y)

maior = y
menor = y

for i in range(1,5):
    x = int(input('Digite um valor: '))
    lista.append(x)
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print(f'O maior valor é {maior} e está nas posições ',end='')
for i in range(0,5):
    if lista[i] == maior:
        print(i, end=' ')

print()

print(f'O menor valor é {menor} e está nas posições ',end='')
for i in range(0,5):
    if lista[i] == menor:
        print(i, end=' ')
print()
print(lista)