n1 = float(input('Insira a nota do 1º semestre: '))
n2 = float(input('Insira a nota do 2º semestre: '))
media = (n1 + n2) / 2
if media >= 7:
    print('\033[1;30;42mParabens você foi aprovado!\033[m')
elif media >= 5:
    print('\033[1;31;40mVocê ficou em recuperação, estude mais!\033[m')
else :
    print('\033[4;30;41mVocê reprovou!\033[m')
