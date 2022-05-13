def contador(inicio, fim, passo):

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')

    if passo == 0:
        passo = 1

    if inicio > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1

    for v in range(inicio,fim, passo):
        print(v,end=' ')
    print('\n'+'-~'*15)


contador(1, 10, 1)
contador(10, 0, 2)

print('Contagem personalizada:\n')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)