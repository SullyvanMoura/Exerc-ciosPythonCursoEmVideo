s = 0

for x in range(0,6):

    n = int(input('Digite um número inteiro:'))
    if n % 2 == 0:
        s = s + n
print('A soma apenas dos números pares que você digitou é igual a: {}'.format(s))

