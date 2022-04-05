tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO','GRATIS')

for palavra in tupla:

    print(f'Na palavra {palavra} temos ',end='')
    for ch in palavra:
        if ch.lower() in 'aeiou':
            print(f'{ch.lower()} ',end='')
    print()