size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for i in range(size):
        print("*", end="")
    print()  # moving to the next line after each row is printed
    row += 1
