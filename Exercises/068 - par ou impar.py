import random

op = n = n2 = -1
r = 0

print("Vamos jogar par ou impar! 😁")

while n < 0 or n >10:
    print("Digite um número de 0 a 10: ", end="")
    n = int(input())
    if n < 0 or n > 10:
        print("Valor invalido!")

while op < 1 or op >2:
    print('Escolha "1" para par e "2" para impar: ', end="")
    op = int(input())
    if op < 1 or op > 2:
        print("Opção invalida!")

n2 = random.randint(0, 10)

r = (n + n2) % 2

if (r == 0 and op == 1) or (r != 0 and op == 2):
    print(f"Você escolheu {'par' if op == 1 else 'impar'}, jogou {n} e o computador jogou {n2} a soma é {n+n2} que é {'par' if op == 1 else 'impar'}, você ganhou! 🏆")
else:
    print(f"Você escolheu {'par' if op == 1 else 'impar'}, jogou {n} e o computador jogou {n2} a soma é {n+n2} que é {'par' if op != 1 else 'impar'}, você perdeu! 😢")
