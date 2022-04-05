p = float(input('Peso em Kg: '))
a = float(input('Altura em metros: '))
imc = (p)/(a ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}, você está \033[33mABAIXO\033[m do peso!'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.1f}, você está no peso \033[32mIDEAL\033[m!'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.1f}, você está com \033[33mSOBREPESO\033[m!'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f}, você está com \033[31mOBESIDADE\033[m!'.format(imc))
else:
    print('Seu IMC é {:.1f}, você está com \033[1;31mOBESIDADE MÓRBIDA\033[m!'.format(imc))
input('Pressione ENTER para sair')