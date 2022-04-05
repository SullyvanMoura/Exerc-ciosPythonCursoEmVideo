from random import randint
from time import sleep
tentativas = 0
n = randint(1,10)
print('O computador gerou um número aleatóriamente')
sleep(0.6)
print('.')
sleep(0.6)
print('.')
sleep(0.6)
print('.')
resp = int(input('Adivinhe o número:'))
while resp != n:
    resp = int(input('Errado! Mais uma chance:'))
    tentativas += 1
print('Acertou em {} tentativa(s)!'.format(tentativas))