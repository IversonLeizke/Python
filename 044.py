notas = []
while True:
    notas.append([
        input('Insira o nome do aluno: '),
        [input('Insira a prinmeira nota: '),
        input('Insira a segunda nota: ')]
    ])
    if input('Deseja inserir novo registro [S/N]: ') in 'nN':
        break
print(notas)