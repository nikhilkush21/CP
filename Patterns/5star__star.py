num=int(input("enter the number"))
for i in range(1, num + 1):
     print("*", end=" ")
     for j in range(num+1-1):
         print("_", end=" ")
     print("*",end=" ")
     print()
        