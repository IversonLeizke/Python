nome = str(input('Insira seu nome completo: '))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
firstName = nome[0:nome.find(' ')]
print(nome.find(' '))
print(firstName)