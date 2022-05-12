pessoas = list()
while True:
    atual = dict()
    atual['nome'] = str(input('Nome da pessoa: '))
    atual['sexo'] = str(input('Sexo da pessoa[M/F]: '))
    atual['idade'] = int(input('Idade da pessoa: '))

    pessoas.append(atual)
    prox = str(input('Deseja continuar? [S/N] '))
    if prox in 'nN':
        break

print(f'{len(pessoas)} pessoas foram cadastradas')

# Calcula média de idades

total = 0
for p in pessoas:
    total += p['idade']

media = total/len(pessoas)

print(f'Média das idades {media}')

print('As mulheres cadastradas foram: ',end='')
for p in pessoas:
    if p['sexo'] in 'fF':
        print(p['nome'],end=' ')

print('\nPessoas com idade acima da média:',end=' ')

for p in pessoas:
    if p['idade'] > media:
        print(p['nome'],end=' ')