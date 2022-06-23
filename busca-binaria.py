A = int(input('Inicio da lista: '))
B = int(input('Fim da lista: '))
element = int(input('Numero que deseja: '))
binarios = list(range(A,B))

right = len(binarios)
left = 0

while True:
    idx = len(binarios) // 2
    middle = (right + left) // 2
    if len(binarios) > 0:
        if element == binarios[idx]:
            print(f'Elemento Encontrado na posição {middle}')
            break
        elif element >= binarios[idx]:
            binarios = binarios[idx:]
            left = middle
        else:
            binarios = binarios[:idx]
            right = middle
    else:
        print('Elemento não encontrado')
        break