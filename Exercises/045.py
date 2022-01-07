estudante = {}
estudante['nome'] = input('Insira o nome do estudante: ')
estudante['media'] = float(input('Insira a média do estudante: '))
if estudante['media'] >= 7:
    estudante['situação'] = 'Aprovado'
else:
    estudante['situação'] = 'Reprovado'
print(estudante)