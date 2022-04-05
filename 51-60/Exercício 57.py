sexo = str(input('Informe o seu sexo [M/F]:')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Variável inválida! Tente novamente:')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
if sexo == 'F':
    sexo = 'Feminino'
print('Sexo {} registrado com sucesso!'.format(sexo))