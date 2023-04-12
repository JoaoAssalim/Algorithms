B = int(input('End: '))
element = int(input('Number to Search: '))
binarios = list(range(0,B))

right = len(binarios)
left = 0

while True:
    idx = len(binarios) // 2
    middle = (right + left) // 2
    if len(binarios) > 0:
        if element == binarios[idx]:
            print(f'Element found on position {middle}')
            break
        elif element > binarios[idx]:
            binarios = binarios[idx:]
            left = middle
        else:
            binarios = binarios[:idx]
            right = middle
    else:
        print('Element not found!')
        break
