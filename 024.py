r1 = int(input('Insira o valor para reta 1: '))
r2 = int(input('insira o valor para reta 2: '))
r3 = int(input('Insira o valor para reta 3: '))
maior = r1
if r2 > r1 and r2 > r3:
    maior = r2
elif r3 > r1 and r3 > r2:
    maior = r3
if maior < (r1 + r2 + r3 - maior):
    print(f'\033[1;32;47mÉ possivel formar uma reta com os valores de {r1}, {r2} e {r3}.\033[m')
else:
    print(f'\033[4;30;41mNão é possivel formar uma reta com os valores de {r1}, {r2} e {r3}.\033[m')