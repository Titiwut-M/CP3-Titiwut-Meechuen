numberRow = int(input())
for x in range(numberRow):
    space = ' ' * (numberRow - (x+1))
    arterisk = '*' * ((2*x)+1)
    print(space,arterisk)



