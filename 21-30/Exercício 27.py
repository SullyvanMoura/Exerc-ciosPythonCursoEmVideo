nome = input('Digite seu nome completo:').strip()
n = nome.split()

print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[-1]))
input('Aperte enter para sair')
