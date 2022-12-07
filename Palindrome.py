num = 101
num2 = num
rev = 0
while num > 0:
    result=num%10
    rev=rev*10+result
    num=num//10
if num2 == rev:
    print("YES,",num2,"is a palindrome.")
else:
    print("NO,",num2,"It isn't a palindrome.")