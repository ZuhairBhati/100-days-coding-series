# Given an integer array of size N, write a program to reverse the array

n = int(input('Enter size of array: '))
arr = []
print('Enter elements: ')

for i in range(n):
    arr.append(int(input()))

arr = list(reversed(arr))
print(arr)

