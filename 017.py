n = str(input('Insira um nome: '))
print(f'A letra \"A\" aparece {n.lower().count("a")}')
print(f'A primeira vez a letra \"A\" aparece na posição {n.find("a")}')
print(f'A ultima vez a letra \"A\" aparece na posição {n.rfind("a")}')
