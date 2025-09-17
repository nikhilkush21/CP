n=[]
num=int(input())
n.append(num)
highest=0
lowest=0
for i in range(len(n)):
    if n[i]> highest:
        highest=n[i]    
    if n[i]< lowest:
        lowest=n[i]
print("Highest:",highest)
print("Lowest:",lowest)