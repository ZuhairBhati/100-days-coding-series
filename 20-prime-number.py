#  Write a program to identify if the number is Prime number or not

num = int(input('Enter a Number: '))

for i in range(2, num):
    if num % i == 0:
            print(num,'is not a prime number')
            break
else:
    print(num,'is a prime number')