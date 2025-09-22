l=[2,23,43,20,45]
search=int(input("Enter element to be searched "))
count=0
for i in range(1,len(l)):
    if l[i]==search:
        print("Element found in an array")
        break

