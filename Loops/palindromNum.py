num=int(input("Enter the number: "))
palindrom= 0
temp = num      
while num > 0:
    digit = num % 10
    palindrom = palindrom * 10 + digit
    num //= 10  
if temp == palindrom:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")