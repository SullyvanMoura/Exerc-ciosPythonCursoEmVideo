from random import randint

print('~~'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('~~'*15)

n = 0
escolha = ''
winner = ''
wins = 0

while True:
    pc = randint(1,10)
    n = int(input('Digite um valor:'))
    if n < 0:
        print('Valor inválido!')
        break
    escolha = (input('Par ou ímpar? [P/I]')).upper().strip()[0]
    if (n + pc)%2 == 0:
        winner = 'P'
    else:
        winner = 'I'
    if escolha == winner:
        print(f'Você ganhou! O computador escolheu {pc}.\nVamos continuar!')
        wins += 1
    else:
        print(f'Você perdeu! O computador escolheu {pc}.')
        break
    if escolha not in 'PI':
        print('Escolha inválida!')
        break
print(f'Seu número de vitórias foi igual a {wins}! Obrigado por jogar!')