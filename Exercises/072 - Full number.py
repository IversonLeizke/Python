numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', \
'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

number = -1

while number not in range(1, 20):
    print("Choose a unmber between 1 and 20 to write it in the consol: ", end="")
    number = int(input())
    if number not in range(1, 20):
        print('You insert a wrong option!')

print(f'You choose number {numbers[number - 1]}.')
