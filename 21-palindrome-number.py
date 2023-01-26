# Write a program to identify if the number is Palindrome or not

num = int(input('Enter a Number: ')) 
temp = num 
reverse = 0

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
    print('Palindrome')
else:
    print('Not a Palindrome')