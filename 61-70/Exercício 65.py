n = int(input('Digite um número inteiro:'))

continuar = 'S'
soma = n
maior = n
menor = n

while continuar in 'Ss':
    print('A soma dos valores digitados é {} e o maior valor digitado é {} e o menor é {}!'.format(soma,maior,menor))
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar in 'Ss':
        n = int(input('Digite um novo valor inteiro:'))
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('Falou!')