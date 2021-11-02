r1 = int(input('Insira o valor para reta 1: '))
r2 = int(input('Insira o valor para reta 2: '))
r3 = int(input('Insira o valor para reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('É possivel formar um triangulo do tipo Equilátero.')
    elif r1 != r2 != r3:
        print('É possivel formar um triangulo do tipo Escaleno.')
    else:
        print('É possivel formar um triangulo do tipo Isóceles.')
else:
    print('Não é possivel formar um triangulo.')
