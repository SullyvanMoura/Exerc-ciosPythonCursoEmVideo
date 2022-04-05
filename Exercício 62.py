primeiro = float(input('Digite o primeiro termo de uma Progressão Aritmética:'))
razao = float(input('Digite a razão dessa Progressão Aritmética:'))
objetivo = primeiro + 10*razao
pa = primeiro
while pa != objetivo:
    print(pa)
    pa = pa + razao

mais = int(input('Deseja mostrar mais termo? Quantos?'))

while mais != 0:
    objetivo = pa + mais*razao
    while pa != objetivo:
        print(pa)
        pa += razao
    objetivo = pa
    mais = int(input('Deseja mostras mais quantos temos?'))