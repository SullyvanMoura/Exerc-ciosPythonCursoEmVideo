from datetime import date

ano = int(input('Qual seu ano de nascimento?'))
alist = ano + 18
atual = date.today().year

if atual < alist:
    print('Você ainda não precisa se alistar,pois tem apenas {} anos.\n'
          'Precisará se alistar no ano de {}!'.format(atual - ano,alist))
elif atual == alist:
    print('Você precisa se alistar durante esse ano de {}, pois nele você completa 18 anos de idade!'.format(atual))
else:
    print('Você deve ter se alistado há {} anos, no ano de {}!'.format(abs(atual - alist),alist))
input('Pressione enter para sair')

