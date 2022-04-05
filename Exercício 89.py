def media(x,y):
    return (x+y)/2

alunos = []
temp = []

while True:
    nome = str(input("Digite o nome do aluno: "))
    temp.append(nome)
    nota1 = float(input("Digite a primeira nota do aluno: "))
    temp.append(nota1)
    nota2 = float(input("Digite a segunda nota do aluno:  "))
    temp.append(nota2)

    alunos.append(temp[:])
    temp.clear()

    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "Nn":
        break

print(alunos)

print("Lista de notas:")
sp = ' '
print(f'N°  NOME{sp*16}Média')

for i,aluno in enumerate(alunos):
    print(i,end='   ')
    print(aluno[0], end='')
    print(sp*(20 - len(aluno[0])),end='')
    print(media(aluno[1],aluno[2]))

while True:
    x = int(input("Deseja ver as notas de qual dos alunos? [999 interrompe o programa] "))
    print(f"Nota 1: {alunos[x][1]}\nNota 2:{alunos[x][2]}")
    if x == 999:
        break

