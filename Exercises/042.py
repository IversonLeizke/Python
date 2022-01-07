lista = []
for i in range(0, 5):
    lista.append(input(f'Digite um valor para posição {i}: '))
print(f'Você digitou os valores: {lista}')
print(f'O maior valor que você digitou foi {max(lista)} nas posições: ', end='')
for pos, i in enumerate(lista):
    if i == max(lista):
        print(f'{pos}... ', end='')
print(f'\nO menor valor que você digitou foi {min(lista)} nas posições: ', end='')
for pos, i in enumerate(lista):
    if i == min(lista):
        print(f'{pos}... ', end='')
