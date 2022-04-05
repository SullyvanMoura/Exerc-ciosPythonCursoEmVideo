n = int(input('Digite um número inteiro:'))

print('[ 1 ] Pressione para converter para binário\n'
      '[ 2 ] Pressione para converter para octal\n'
      '[ 3 ] Pressione para converter para hexadecial')
x = int(input('Qual opção deseja escolher?'))

if x == 1:
      print('{} convertido para binário é igual {}'.format(n, bin(n)[2:]))

elif x == 2:
      print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))

elif x == 3:
      print('{} convertido para hexadecial é igual a {}'.format(n,hex(n)[2:]))
else:
      print('Comando inválido!')
input('Pressione enter para sair')