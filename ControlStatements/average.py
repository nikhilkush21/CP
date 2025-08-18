# A=int(input("Enter num1: "))
# B=int(input("Enter num2: "))
# C=int(input("Enter num3: "))
# D=int(input("Enter num4: "))
# E=int(input("Enter num5: "))
# avg = (A + B + C + D + E) / 5
# print("The average of A,B,C,D and E is: ", avg)
list=[]
for i in range(1, 6):
   num=int(input("Enter number:"))
   list.append(num)
avg=sum(list)/len(list)
print("The average of the numbers is: ",avg)

