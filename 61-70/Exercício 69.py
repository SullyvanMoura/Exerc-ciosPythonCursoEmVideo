print('~~'*10)
print('CADASTRO DE PESSOAS!')
print('~~'*10)

homens = 0
F20 = 0
menos18 = 0

while True:
    print('-'*20)
    idade = int(input('Qual é a idade da pessoas?'))
    if idade < 0:
        print('Idade inválida!')
        break
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o sexo da pessoas? [M/F]')).upper().strip()[0]
    print('-'*20)
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        F20 += 1
    if idade < 18:
        menos18 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Analisando os dados:\n{menos18} pessoas tem menos de 18 anos.\n{homens} homens foram cadastrados.\n{F20} mulheres com menos de 20 anos foram cadastradas.')