from random import randint

n = int(input("Quantos palpites deseja gerar? "))

lista = []
dados = []

for j in range(0,n):
    for i in range (0,6):
        dados.append(randint(0,60))

    lista.append(dados[:])
    dados.clear()

for i in range(0,n):
    print(f'Jogo {i+1}: {lista[i]}')