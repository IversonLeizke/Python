from random import randint


n1 = int(input('Adivinhe o núemro que estou pensando entre 1 e 5: '))
n2 = randint(1, 5)
print('Você acertou!' if n1 == n2 else f'Você errou o número era {n2}!')