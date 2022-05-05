from datetime import date

cadastro = {'nome': str(input('Digite seu nome: ')),
            'idade': date.today().year - int(input("Digite o ano de seu nascimento: ")),
            'carteira de trabalho': int(input("Digite sua carteira de trabalho (Caso não tenha, digite 0): "))}

if cadastro['carteira de trabalho'] != 0:
    cadastro['ano de contratacao'] = int(input("Digite o ano de sua contradação: "))
    cadastro['salario'] = float(input("Digite seu salário: "))
    cadastro['idade de aposentar'] = cadastro['ano de contratacao'] + 35 - date.today().year

for k, v in cadastro.items():
    print(f"{k} é {v}")

