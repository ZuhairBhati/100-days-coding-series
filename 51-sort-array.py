# Given an integer array of size N, write a program to sort the array

n = int(input('Enter size of array: '))
arr = []
print('Enter elements: ')

for i in range(n):
    arr.append(int(input()))

arr.sort()
print(arr)