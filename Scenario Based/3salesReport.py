n=int(input())
a=list(map(int,input().split()))
highest=a[0]
lowest=a[0]
for i in a :
    if i> highest:
        highest=i    
    if i < lowest:
        lowest=i
print("Highest:",highest)
print("Lowest:",lowest)