from datetime import date

print('Confederação Nacional de Natação')

ano = int(input('Qual seu ano de nascimento?'))

idade = date.today().year - ano

if idade <= 0:
    print('Idade inválida!')
elif idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
input('Pressione ENTER para sair')