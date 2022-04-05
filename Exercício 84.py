pessoas = []
dados = []

resp = 'S'
maior = 0
menor = 0

while resp.upper() not in 'N':
    nome = str(input("Digite o nome: "))
    dados.append(nome)
    peso = float(input("Digite o peso: "))
    dados.append(peso)
    if len(pessoas) == 0:
        maior = menor = peso

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

    pessoas.append(dados[:])
    dados.clear()

    resp = str(input("Deseja continuar? [S/N] "))

print(f'{len(pessoas)} pessoas foram cadastradas')
print('As pessoas mais pesadas são: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' - ')
print()
print('As pessoas mais levees são: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' - ')

