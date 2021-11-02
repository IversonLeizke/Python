n1 = int(input('Digite um número para calcular seu fatorial: '))
s = 1
for n2 in range(1, n1 +1):
    s *= n2
print(f'O fatorial de {n1} é {s}.')