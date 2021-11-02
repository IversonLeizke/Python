n = str(input('Insira seu nome: '))
print(f'Seu primeiro nome é {n[:n.find(" ")]}.')
print(f'Seu ultimo nome é {n[n.rfind(" "):]}.')
