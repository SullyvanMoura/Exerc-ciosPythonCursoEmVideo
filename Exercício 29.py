v = int(input('Qual a velocidade que o carro passou em km/h?'))

if v <= 80:
    print('Sua velocidade estava ok')
else:
    print('Sua multa vai custar R${}!'.format((v - 80)*7))