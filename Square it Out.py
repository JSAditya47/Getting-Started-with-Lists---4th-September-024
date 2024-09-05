user_range = int(input("Enter the Range: "))
square = []

for i in range(0, user_range + 1):
    x = i ** 2
    square.append(x)
    
print(square)

for i in square:
    if i % 2 == 0:
        print(f"\n{i} is an Even Number!")
    else:
        print(f"\n{i} is an Odd Number!")
