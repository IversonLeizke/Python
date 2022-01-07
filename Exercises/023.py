n = int(input('Insira um ano (aaaa): '))
if n % 2000 == 0:
    print(f'{n} é um ano bissexto.')
elif n % 400 == 0:
    print(f'{n} não é um ano bissexto.')
elif n % 4 == 0:
    print(f'{n} é uma ano bissexto.')
else:
    print(f'{n} não é um ano bissexto.')
