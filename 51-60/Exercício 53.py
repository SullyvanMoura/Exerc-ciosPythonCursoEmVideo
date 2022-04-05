frase = str(input('Digite uma frase:')).upper().strip()
fra = frase.replace(' ', '')
inverso = ''

for x in range(len(fra) - 1, -1 , -1):
    inverso += fra[x]
if inverso == fra:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')