maior = 0
menor = 0

for x in range(1,6):
    peso = float(input('Qual é o peso da {}ª pessoa?'.format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print('O maior peso é:{} \nO menor peso é:{}'.format(maior,menor))
