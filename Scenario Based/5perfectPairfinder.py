n=6
l=[1,5,7,-1,5,3]
tar=6
count=0
for i in range(len(l)):
    for j in range (i+1,len(l)):
        if l[i]+l[j]==tar:
            count=count+1
print(count)