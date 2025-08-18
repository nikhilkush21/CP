A=int(input("Enter num1: "))
B=int(input("Enter num2: "))
C=int(input("Enter num3: "))
if A<B and A<C:
    print("A is mimimum among A,B,C")
elif(B<A and B<C):
    print("B is minimum among A,B,C")
elif(C<A and C<B):
    print("C is the minimum among A,B,C")
