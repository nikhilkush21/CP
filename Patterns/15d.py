num=int(input("enter: "))
for i in range(1, num ):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(num, 0, -1):       
    for j in range(i):           
        print("*", end=" ")
    print()
