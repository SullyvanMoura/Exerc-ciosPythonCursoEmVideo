D = int(input('Por quantos dias você alugou o carro?'))
Km = float(input('Quantos KM você percorreu com o carro?'))
V = 60*D + 0.15*Km
print('O valor total a pagar é igual a R${:.2f}!'.format(V))
