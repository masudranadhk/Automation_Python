# By assigning only column
print("Enter your value:", end=" ")
a = int(input())
for i in range(a):
    for j in range(i+1):
        print("*", end=" ")
    print()

# # Another way
# # By assigning only column
# print("Enter your value:", end=" ")
# a = int(input())
# b=0
# #print("Row value:", end=" ")
# #b = int(input())
# row = 0
# column = 0
# while row <= a:
#         while column <= b:
#             print("*", end=" ")
#             column += 1
#         row += 1
#         if row > 1:
#             column = 0
#             b += 1
#             print()
