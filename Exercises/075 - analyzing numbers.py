numbers = (
    int(input('Type the first number: ')),
    int(input("Type another number: ")),
    int(input('Type one more number: ')),
    int(input('Type the last number: ')),
)
print(f'The number 9 shows {numbers.count(9)} times in the array')
if 3 in numbers:
    print(f'The number 3 is in position {numbers.index(3) + 1}')
print('The even numbers are ', end='')
for i in numbers:
    if i % 2 == 0:
        print(i, end="")
