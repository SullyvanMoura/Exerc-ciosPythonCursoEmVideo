x = int(input('Digite seu salário:'))

if x <= 1250:
    print('Novo salário: {}'.format(x*1.15))
else:
    print('Novo salário: {}'.format(x*1.1))