n = int(input('Quantos números da sequencia de fibonacci: '))
cont = 0
n1 = 0
n2 = 1
n3 = 0
while cont < n:
    if cont == 0:
        print(f'( {n1}', end='')
    elif cont == n - 1:
        print(f', {n1})', end='')
    else:
        print(f', {n1}', end='')
    cont += 1
    n3 = n2
    n2 = n3 + n1
    n1 = n3