cidade = input('Diga o nome de uma cidade que direi se começa com "Santo":')

n = (cidade.upper()).split()

print('Tem Santo? {}'.format('SANTO'in n))
input('Aperte enter para sair')
