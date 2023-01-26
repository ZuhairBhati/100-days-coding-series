num = int(input('Enter a Number: '))
sum = 0
if num <= 0:
    print('Invalid Number')
else:
    for i in range(num+1):
        sum += i
print(sum)