d = int(input('Qual é a distância da viagem em km:'))

if d <= 200:
    print('O valor da viagem dá R${}'.format(d*0.5))
else:
    print('O valor da viagem dá R${}'.format(d*0.45))