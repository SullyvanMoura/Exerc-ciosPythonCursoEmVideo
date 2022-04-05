expressao = str(input("Digite uma expressão: "))

pilha = []

for ch in expressao:
    if ch is '(':
        pilha.append(ch)
    elif ch is ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("A expressão está certa")
else:
    print("A expressão está errada")