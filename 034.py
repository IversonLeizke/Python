n = int(input('Insira um valor: '))
primo = True
for c in range(2, n):
    if n % c == 0:
        primo = False
print(f'{n} é um numero primo.' if primo else f'{n} não é um número primo.')
