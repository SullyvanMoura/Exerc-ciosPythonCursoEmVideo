soma = 0
maioridadehomem = 0
nomevelho = 0
totalmulher = 0
for x in range(1,5):
    print('{}ª pessoa:'.format(x))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).upper().strip()
    soma += idade
    if x == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and maioridadehomem < idade:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade > 20:
        totalmulher += 1

media = soma/4
print('A média da idade do grupo é igual: {}'.format(media))
print('O nome do homem mais velho({} anos) é: {}'.format(maioridadehomem,nomevelho))
print('O total de mulheres com mais de 20 anos é de: {}'.format(totalmulher))