n = int(input('Insira sua idade: '))
categoria = 'mirim'
if n <= 9:
    categoria = '\033[1;31;40mMirim\033[m'
elif n <= 14:
    categoria = '\033[1;32;40mInfantil\033[m'
elif n <= 19:
    categoria = '\033[1;33;40mJunior\033[m'
elif n <= 20:
    categoria = '\033[1;34;40mSénior\033[m'
else:
    categoria = '\033[1;35;40mMaster\033[m'
print(f'Você esta na categoria {categoria}.')
