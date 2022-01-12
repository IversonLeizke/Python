teams = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense"
)

print("-=" * 30)
print(f'The Brazilian football teams are  {teams}')
print("-=" * 30)
print(f"The first five are {teams[0:5]}")
print("-=" * 30)
print(f"The last four are {teams[-4:]}")
print("-=" * 30)
print(f"The teams ordered are {sorted(teams)}")
print("-=" * 30)
print(f"The Chapecoense is in the position number {teams.index('Chapecoense')}.")