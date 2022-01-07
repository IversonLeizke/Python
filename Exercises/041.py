preços = ('Lapís', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25,
          'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
          'Caneta', 2.20, 'Livro', 34.9)
print('-'*50)
print(f'{"Listagem de Preços":^50}')
print('-'*50)
for pos, i in enumerate(preços):
    if pos % 2 == 0:
        print(f'{i:.<40}R$', end='')
    else:
        print(f'{i:>8.2f}')
print('-'*50)
