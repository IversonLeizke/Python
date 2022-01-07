from random import  randint


c = 0
n = 'a'
n1 = randint(1, 10)
while n != n1:
    n = int(input('Tente adivinhar o número entre 1 e 10: '))
    c += 1
print(f'Você precisou de {c} tentativas para adivinhar que o número era {n}.')