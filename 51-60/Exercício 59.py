x = float(input('Digite o primeiro valor:'))
y = float(input('Digite o segundo valor:'))
print('[1] SOMAR\n[2]MULTIPLICAR\n[3]MOSTAR O MAIOR\n[4]DIGITAR NOVOS NÚMEROS\n[5]SAIOR DO PROGRAMA')
act = 0
while act != 5:
    act = int(input('O que deseja fazer?'))
    while act < 1 or act > 5:
        act = int(input('Dados inválidos! Selecione uma opção válida:'))
    if act == 1:
        print('O resultado operação é {}!'.format(x + y))
    if act == 2:
        print('O resultado da operação é {}!'.format(x*y))
    if act == 3:
        if x > y:
            print('O maior valor é {}'.format(x))
        if y > x:
            print('O maior valor é {}'.format(y))
    if act == 4:
        x = float(input('Digite um novo primeiro valor:'))
        y = float(input('Digite um novo segundo valor:'))
    if act == 5:
        input('Tudo certo! Até mais!')