n = float(input('Insira a velocidade registrada: '))
if n > 80:
    multa = (n - 80) * 7
    print(f'Você ultrapassou o limite de 80km/h a multa é de R$ {multa:.2f}')
