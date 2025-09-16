# l=[5,2,9]

# l.append(100)
# print (l)

# l=[1,2,3,4,5,6]
# print(l[1])

# l=[21,3445,[2,4,5,3],12]
# print(l[2][3])

# l=[1,2,3,4]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

# l=[1,2,3,4]
# n=len(l)
# sum=0
# for i in range(n):
#     sum=sum+l[i]
# print(sum)


# l=[1,2,3,4]
# l.extend([100,200])
# print(l)
# l.remove(2)
# print(l)

# l.pop()
# print(l) 

# l=[1,2,3,4]

# l.reverse()
# print(l)

# rev_l=reversed(l)
# print(rev_l)    
# rev_l=list(rev_l)
# print(rev_l)

# n=len(l)
# for i in range(n//2):
#     l[i],l[n-i-1]=l[n-i-1],l[i] 
# print(l)


# str1="hello this is split funtion"
# l=str1.split()
# print(l)

# str2="1234"
# l2=str2.split()
# print(l2)


# a=list(map(int,input().split()))
# print(a)


############QUESTIONS########################
 
# Given an array compute the sum of all elements

## method 1 
# arr= list(map(int, input().split()))
# l.append(arr)
# sum=0
# for i in arr:
#     sum=sum+i   
# print(sum)

## method 2
# arr= list(map(int, input().split()))
# sum=0
# for i in range(len(arr));
#     sum=sum+arr[i]
# print(sum)


#given an array find the maximum value in it.

## method 1 
# arr= list(map(int, input().split()))
# max=0
# for i in arr:
#     if i>max:
#         max=i
# print(max)

## method 2
# arr= list(map(int, input().split()))
# ans=0
# ans == -float("inf")
# for i in arr:
#     if(ans<i):
#         ans=i
# print(ans)  


## given an array and a target a number find number of occurance of target in the given array.
# arr= list(map(int, input().split()))
# target=int(input())
# count=0
# for i in arr:
#     if i==target:
#         count=count+1
# print(count)

# given an array and n increment number generate a
# number that contain all value of original  array incresed by increment value

# arr= list(map(int, input().split()))  
# n=int(input())
# for i in range(len(arr)):
#     arr[i]=arr[i]+n 
# print(arr)


# given an array filter out odd number from it.
# arr= list(map(int, input().split()))
# even_arr=[]
# for i in arr:   
#     if i%2!=0:
#         even_arr.append(i)
# print(even_arr)

#given a list of integer and a target number find an print the index of a target of  number 

l=[12,3,3,32,1,87,88]
target=int(input())
for i in range(0,len(l)):
    if l[i] ==target:
        print(i)
       









