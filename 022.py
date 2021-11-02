n = float(input('Insira a distancia da viagem em km: '))
print(f'O preço para viajar {n:.2f} é de R$ {((n*0.50) if n <= 200 else (n*0.45)):.2f}.')
