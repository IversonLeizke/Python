from math import hypot
print('Insira os valores para calcular a hipotenusa: ')
n = float(input('x: '))
n2 = float(input('y: '))
print(f'O resultado é {hypot(n, n2):.2f}')