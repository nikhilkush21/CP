num=int(input("enter"))
for i in range(1, num + 1):
    for j in range(num-i):
        print("_",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()