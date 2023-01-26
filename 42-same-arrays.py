#  Write Program to check if two arrays are the same or not

n = int(input('Enter size of first array: '))
m = int(input('Enter size of second array: '))

arr1 = []
arr2 = []

print('Enter elements of first array: ')
for i in range (n):
    arr1.append(int(input()))

print('Enter elements of second array: ')
for i in range (m):
    arr2.append(int(input()))

arr1.sort()
arr2.sort()

if arr1 == arr2:
    print('Same')
else:
    print('Not Same')