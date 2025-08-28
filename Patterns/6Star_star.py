n = int(input("Enter number of rows for Question 6: "))
for i in range(n):
    print("*", end="")
    for j in range(n-i-1):
        print(" -", end="")
    print(" *")

print()