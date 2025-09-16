a=int(input())
n=list(map(int,input().split()))
for i in range(len(n)):
    odd=n[i]%2!=0
    if n[i]%2==0:
        print(n[i],end=" ")
    elif(odd<0):
        print()
    