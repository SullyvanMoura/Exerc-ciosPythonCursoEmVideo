times = ('São Paulo', 'Internacional','Atlético-MG','Flamengo','Grêmio','Palmeiras','Fluminense','Corinthians','Santos','Ceará SC','Athletico-PR','Atlético-GO','Bragantino','Sport Recife','Vasco da Gama','Fortaleza','Bahia','Goiás','Botafogo','Coritiba')

print('-_-'*20)
print('{:^60}'.format('CAMPEONATO BRASILEIRO DE FUTEBOL'))
print('_-_'*20 + '\n')

print('Os primeiros 20 colocados são:',end='  ')
for time in times:
    print(time,end=' -> ')

print('\n' + '---'*20)

print('Apenas os primeiros 5 colocados são:',end='  ')
for time in times[:5]:
    print(time,end=' -> ')

print('\n' + '---'*20)

print('Os últimos 4 colocados são:',end='  ')
for time in times[(len(times)-4):]:
    print(time,end=' -> ')

print('\n' + '---'*20)

print('A lista dos times em ordem alfabética: ',end='   ')
for time in sorted(times):
    print(time,end=' -> ')

print('\n' + '---'*20)

print('O flamengo está na posição: {}'.format((times.index('Flamengo')) + 1 ))