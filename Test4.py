# print("Enter Row value:", end=" ")
for row in range(4):
    for column in range(8):
        if (column==0 or column==7) or (column==1 and row!=3) or (column==2 and row<2) or (column==6 and row<3) or (column==5 and row<2) or ((column==3 or column==4) and row==0):
          print ("*", end="")
        else:
            print("",end=" ")
    print()