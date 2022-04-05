primeiro = float(input('Digite o primeiro termo de uma Progressão Aritmética:'))
razao = float(input('Digite a razão dessa Progressão Aritmética:'))
decimo = primeiro + 10*razao
pa = primeiro
while pa != decimo:
    print(pa)
    pa = pa + razao