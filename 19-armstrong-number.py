#  Write a program to identify if the number is Armstrong number or not

number = int(input('Enter a Number: '))
num = number
digit = 0
sum = 0
length = len(str(num))

for i in range(length):
    digit = int(num % 10)
    num = num // 10
    sum += pow(digit, length)

if sum == number:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')