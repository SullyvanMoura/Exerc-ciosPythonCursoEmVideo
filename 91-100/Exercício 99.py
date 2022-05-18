def maior(* x):
    maior = x[0]
    for v in x:
        if v > maior:
            maior = v
    print(f'Maior valor entre {x} é {maior}')

maior(1,2,3,4)
maior(1,5,9,-5,6)
