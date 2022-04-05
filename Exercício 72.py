numeros = ("Zero", 'Um','Dois','Três','Quatro','Cinco'
           ,'Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Quatorze','Quinze',
           'Dezeseis','Dezesete','Dezoito','Dezenove', "Vinte")

x = int(input("Digite um número entre 0 e 20: "))

while x < 0 or x > 20:
    x = int(input("Tente novamente. Digite um número entre 0 e 20: "))

print(f"Você digitou o número {numeros[x]}")