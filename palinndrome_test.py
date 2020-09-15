
num = int(input("enter a number : "))
#121

temp = num
rev= 0
while temp>0:
    digit = temp % 10   #1
    rev = rev*10 + digit #1 #12 #121
    temp = temp//10 #12
        


if(rev == num):
    print(num," is palindrome")

else:
    print(num,"is not palindrome")
