frase = input('Digite uma frase qualquer:').lower().strip()

print("A quantidades de A's da frase é igual a: {}".format(frase.count('a')))
print('A primeita vez que a letra A aparece é na posição {}'.format(frase.find('a')+1))
print('A última vez que a letra A aparece é na posição {}'.format(frase.rfind('a')+1))
input('Aperte enter para sair')
