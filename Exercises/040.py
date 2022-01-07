times = ('Atlético-MG', 'Flamengo', 'São Paulo', 'Internacional', 'Fluminense',
         'Palmeiras', 'Santos', 'Grêmio', 'Athletico-PR', 'Bahia', 'Fortaleza',
         'Atlético-GO', 'Bragantino', 'Corinthians', 'Sport', 'Ceará', 'Vasco',
         'Coritiba', 'Botafogo', 'Goiás')
print('Os primeiros cinco colocados são: ')
for pos, t in enumerate(times):
    print(f'{pos + 1}º - {t}')
    if pos == 4:
        break
print('=-='*10)
print(f'Os ultimos quatro colocados são: ', end='')
for i in range(4, 0, -1):
    print(f'{times[(i*-1)]}, ', end='')
print('\n'+'=-='*10)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=-='*10)
print(f'O Bragantino esta na {times.index("Bragantino")}º.')
