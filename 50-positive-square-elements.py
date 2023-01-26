# Given an integer array of size N. Write Program to find sum of positive square elements in the array.

n = int(input('Enter size of array: '))
arr = []
print('Enter elements: ')

for i in range(n):
    arr.append(int(input()))

sum = 0
for i in arr:
    sum += i * i

print(sum)