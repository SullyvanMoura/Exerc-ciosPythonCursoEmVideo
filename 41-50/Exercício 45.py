from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)

print('{:-^40}'.format('Vamos jogar Jokenpô!'))
print('[ 0 ] Pedra\n'
     '[ 1 ] Papel\n'
    '[ 2 ] Tesoura')
x = int(input('Qual opção deseja escolher?'))
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOOOU-')
sleep(0.5)
print('-RA')

print('-_'*14)

print('O computador escolheu {}!'.format(itens[pc]))
print('Você escolheu {}!'.format(itens[x]))

print('-_'*14)

if pc == 0:
    if x == 0:
        print('Empate!')
    elif x == 1:
        print('Você ganhou!!!')
    elif x == 2:
        print('Você perdeu!!!')

elif pc == 1:
    if x == 0:
        print('Você perdeu!!!')
    elif x == 1:
        print('Empate!')
    elif x == 2:
        print('Você ganhou!!!')

elif pc == 2:
    if x == 0:
        print('Você ganhou!!!')
    elif x == 1:
        print('Você perdeu!!!')
    elif x == 2:
        print('Empate!')

input('Pressione ENTER para sair')