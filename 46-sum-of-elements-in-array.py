# Write Program to find sum of elements in an array

n = int(input('Enter size of array: '))
arr = []
sum = 0

print('Enter elements: ')
for i in range (n):
    temp = int(input())
    arr.append(temp)

for i in range (n):
    sum += arr[i]

print(sum)
