# identifica tipos
n = input('Insira um valor: ')
print(f'{n} is {type(n)}.')
if n.isalnum():
    print(f'{n} is alphanumeric')
if n.isalpha():
    print(f'{n} is alpha.')
if n.isnumeric():
    print(f'{n} is numeric.')
if n.isupper():
    print(f'{n} is upper.')