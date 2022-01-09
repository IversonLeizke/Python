products = []
cheapest = 99999
total = 0
overH = 0
op = "Y"

print("-" * 50)
print("LOJA SUPER BARATÃO".center(50, " "))
print("-" * 50)

while op in "Yy":
    print("Insert the name of the product: ", end="")
    product = str(input())
    print("Insert the value of the product: ", end="")
    price = float(input())
    products.append({"Product":product, "Price": price})
    print("Do you want to add other product? (Y/N)")
    op = str(input())
    if price < cheapest:
        cheapest = price 
    if price > 1000:
        overH += 1
    total += price

print("-" * 15, end="")
print("FIM DO PROGRAMA".center(20, " "), end="")
print("-" * 15)
print(f"The total of the buying is $ {total:.2f}")
print(f"We have {overH:.0f} products over $ 1.000,00.")
print(f"The cheapest product cust $ {cheapest:.2f}.")
