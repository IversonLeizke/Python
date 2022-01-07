s = str(input('Insira uma frase para verificar se é um palindromo: '))
s1 = s.replace(' ','').lower()
t = int(len(s1) / 2 if len(s1) % 2 == 0 else (len(s1) + 1) / 2)
palindromo = True
for c in range(0, t):
    if s1[c] != s1[-c-1]:
        palindromo = False
print(f'\"{s}\" é um palindromo.' if palindromo else f'\"{s}\" não é um palindromo.')
