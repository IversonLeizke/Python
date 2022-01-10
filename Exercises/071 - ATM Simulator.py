money = {"$ 100": 0, "$ 50": 0, "$ 10": 0, "$ 5": 0,"$ 1": 0}

print(f"=" * 60)
print("BANK OF BRAZIL".center(60, " "))
print("=" * 60)
print("Please insert the amount you wnat to withdraw: ", end="")
amount = int(input())
money["$ 100"] = amount // 100
amount -= money["$ 100"] * 100
money["$ 50"] = amount // 50
amount -= money["$ 50"] * 50
money["$ 10"] = amount // 10
amount -= money["$ 10"] * 10
money["$ 5"] = amount // 5
amount -= money["$ 5"] * 5
money["$ 1"] = amount // 1

print(f"Total of {money['$ 100']} 100 bills")
print(f"Total of {money['$ 50']} 50 bills")
print(f"Total of {money['$ 10']} 10 bills")
print(f"Total of {money['$ 5']} 5 bills")
print(f"Total of {money['$ 1']} 1 bills")

print("=" * 60)