while True:
    print("Insert a number to see the time table: ", end="")
    n = int(input())
    print("-=" * 25)
    for i in range(1, 11):
        print(f"{n:>2} * {i:>2} = {n*i:>3}")
    print("-=" * 25)
    print('If you want to see other time table isert "S" or "N" to close the program: ', end="")
    op = str(input())
    if op in "Nn":
        break