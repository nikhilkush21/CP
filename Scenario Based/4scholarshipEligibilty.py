count=0
n=int(input())
for i in range(n):
    marks , att= map(int,input().split())
   
    if marks>=75 and att>=80:
        count=count+1
print(count)
        