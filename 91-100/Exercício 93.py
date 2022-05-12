jogador = {'nome': str(input('Qual o nome do jogador?')),
           'Quantidade de partidas': int(input('Quantas partidas o jogador jogou?'))}
partidas = list()
jogador['gols'] = partidas

total = 0
for p in range(0, jogador['Quantidade de partidas']):
    partidas.append(int(input(f'Quantos gols jogador fez na partida {p+1}?')))

print('++'*30)
print(jogador)
print('++'*30)

jogador['total de Gols'] = sum(partidas)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('++'*30)

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} fez {v} gols')