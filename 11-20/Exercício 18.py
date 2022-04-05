from math import sin,cos,tan,radians
n = float(input('Digite o valor de um ângulo em graus:'))
sen = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))
print('O seno do seu ângulo é igual a {:.2f}\nO coseno igual a {:.2f}\nA tangente igual a {:.2f}!'.format(sen, cos, tan))
input('Pressione ENTER para sair')
