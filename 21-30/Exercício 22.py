nome = input('Qual é seu nome completo?')

print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))

print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))

print('A quantidade de letras do seu nome todo é: {}'.format(len(nome.replace(' ', ''))))

sep = nome.split()

print('A quantidade de letras do seu primeiro nome é: {}'.format(len(sep[0])))
input('Aperte enter para sair')
