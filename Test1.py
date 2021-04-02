print("Enter Row value:", end=" ")
a = int(input())
print("Enter Column value:", end=" ")
b = int(input())
row = 0
column = 0

while row < a:
    while column < b:
        print("*", end=" ")
        column += 1
    row += 1
    column = 0
    print("")
