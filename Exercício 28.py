import random

x = random.randint(0,5)

n = int(input('Adivinhe qual número de 0 a 5 o computador pensou:'))

if n == x :
    print('Acertou!')
else:
    print('ERROU!')
