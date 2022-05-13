jogadores = list()

while True:

    jogador_atual = dict()
    gols_partidas = list()
    jogador_atual['nome'] = str(input('Digite o nome do jogador: '))
    jogador_atual['n_partidas'] = int(input('Digite o numero de partidas do jogador: '))
    jogador_atual['gols'] = gols_partidas

    for i in range(0, jogador_atual['n_partidas']):
        jogador_atual['gols'].append(int(input(f'Quantos gols o jogador fez na partida {i+1}: ')))
    jogador_atual['total de gols'] = sum(jogador_atual['gols'])

    jogadores.append(jogador_atual)

    prox = str(input('Deseja continuar? [S/N] '))
    print('++' * 30)
    if prox in 'nN':
        break

print('cod',end = ' ')

for k in jogador_atual:
    print(f'{str(k):<15}',end='')
print()

print('--'*30)

for i, v in enumerate(jogadores):
    print(f'{i:<4}',end= '')
    for dado in v.values():
        print(f'{str(dado):<15}',end='')
    print()

print('--'*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (-1 para encerrar o programa) '))
    if busca == -1:
        break
    elif busca > len(jogadores):
        print('Número invalido!')
        continue

    atual = jogadores[busca]['gols']
    nome_atual = jogadores[busca]['nome']
    for i,v in enumerate(atual):
        print(f'No jogo {i + 1} o jogador {nome_atual} fez {v} gols')