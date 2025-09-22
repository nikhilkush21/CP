l=[10,23,31,48,51]
min=0
max=0
for i in range(1,len(l)):
    if l[i]<l[min]:
        min=i
    if l[i]>l[max]:
        max=i
print("minimum number: ",l[min])
print("maximum number: ",l[max])    

