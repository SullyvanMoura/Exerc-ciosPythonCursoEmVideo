a = int(input('Digite um número inteiro:'))
b = int(input('Ditite outro número intreiro:'))
c = int(input('Ditite outro número intreiro:'))
d = int(input('Ditite outro número intreiro:'))

tupla = (a,b,c,d)

print('---'*20)

noves = 0

for x in tupla:
    if x == 9:
        noves += 1

print(f'O número de vezes que o número 9 apareceu foi: {noves}')

if 3 in tupla:
    três = tupla.index(3)
    print(f'A posição do primeiro número 3 é {três + 1}°')
else:
    print('Não possui número 3')

pares = 0

for x in tupla:
    if x % 2 == 0:
        pares += 1

if pares != 0:
    print(f'{pares} Número(s) par(es) apareceu(ram)')
else:
    print('Nenhum número par apareceu')