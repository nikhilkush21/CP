n=int(input())
passed=0
failed=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]>=35:
        passed+passed+1
        print("Passed")
    else:
        print("Failed")