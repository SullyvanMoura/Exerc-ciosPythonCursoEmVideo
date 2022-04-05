dicio = {'nome': input("Qual é o nome do aluno?"), 'media': float(input("Qual é a média do aluno?"))}

if dicio['media'] >= 7.0:
    dicio['situação'] = 'Aprovado'
else:
    dicio['situação'] = 'Reprovado'

for k, v in dicio.items():
    print(f"{k} é igual a {v}")