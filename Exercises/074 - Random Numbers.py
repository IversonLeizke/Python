from random import randint

numbers = []

for i  in range(0, 5):
    number = randint(0, 9)
    numbers.append(number)
    if i == 0:
        maxN = minN = number
    else:
        if number > maxN: maxN = number
        if number < minN: minN = number

print(f'The randons numbers gerated are: {numbers}.')
print(f"The higher number is {maxN}.")
print(f'The lowest number is {minN}.')

print()
print('=' * 50)
print('Guanabara solution')
print

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end="")
for i in numeros:
    print(f'{i} ', end="")
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')
