# Write Program to find the array type (even, odd, mixed)

n = int(input('Enter size of array: '))
arr = []

print('Enter elements: ')
for i in range (n):
    temp = int(input())
    arr.append(temp)

odd = 0
even = 0

for i in range(n):
    if (arr[i] % 2 == 1):
        odd += 1
    else:
        even += 1

if odd == n:
    print('Odd')
elif even == n:
    print('Even')
else:
    print('Mixed')