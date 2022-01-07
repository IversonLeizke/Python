lista = []
n = 0
while True:
    n = int(input('Insira um valor para adicionar: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado...')
    else:
        print('Valor já na lista, não sera adicionado.')
    if input('Você deseja inserir um novo valor [S/N]: ') in "nN":
        break
print('=-'*10+'=')
print(f'Você digitou os valores: {sorted(lista)}')
