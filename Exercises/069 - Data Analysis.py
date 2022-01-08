people = []
op = "s"
age = -1
gender = "a"
wOver20 = mReg = over18 = 0

while op not in "Nn":
    print("-" * 30)
    print("CADASTRE UMA PESSOA".center(30," "))
    print("-" * 30)
    while (age not in range(0, 120)):
        print("Person's age: ", end="")
        age = int(input())
        if age not in range(0, 120):
            print("The value is invalid, please insert a value between 1 and 120.")
    while gender not in "FfMm":
        print('Wich is the person gender "F"" for feminine or "M" for masculine: ', end="")
        gender = str(input())
        if gender not in "FfMm":
            print("Please inser a valid gender!")
    people.append({'age': age, "gender": gender})
    if age > 18: 
        over18 += 1
    if age > 20 and gender in "Ff": 
        wOver20 += 1
    if gender in "Mm": 
        mReg += 1
    print("Do you want to add a new person? (Y/N): ", end="")
    op = str(input())
    if op not in "Nn":
        age = -1
        gender = "a"

print(people)
print(f"Total of people over eigtheen is {over18:.0f}.")
print(f"Total of men regitered is {mReg:.0f}.")
print(f"Total of women over twenty is {wOver20:.0f}.")