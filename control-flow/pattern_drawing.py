number = int(input("Enter the size of the pattern: "))
i = number
while (i > 0):
    for j in range(number):
        print('*', end='')
    print()
    i -= 1