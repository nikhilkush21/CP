n = int(input())
a = list(map(int, input().split()))
passs = 0
fail = 0
for x in a:
   if x >= 35:
       passs += 1
   else:
       fail += 1
print(passs, fail)