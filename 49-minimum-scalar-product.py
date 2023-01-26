# Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the minimum scalar product (Dot product) of 2 vectors.

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
arr2.sort(reverse=True)

product = 0

for i in range(n):
    product += arr1[i] * arr2[i]

print(product)