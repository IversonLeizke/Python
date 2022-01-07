n = int(input('Insira um número inteiro para exibir a tabuada: '))
m = 11 if n <= 10 else n + 1
for c in range(0, m):
    print(f'{n:>2} X {c:>2} = {(c*n):>3}')
