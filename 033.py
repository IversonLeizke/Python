n = int(input('Insira o primeiro número de uma PA: '))
n1 = int(input('Insira a razão da PA: '))
print(f'( {n}', end='')
for c in range(n + n1, (n + n1 * 10), n1):
    if c < (n + n1 * 9):
        print(f', {c}', end='')
    else:
        print(f', {c})')
