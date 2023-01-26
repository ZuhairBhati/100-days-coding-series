# Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the sum of maximum scalar product (Dot product) of 2 vectors.

arr1 = []
arr2 = []

n = int(input('Enter size of the arrays: '))

print('Enter elements of first array: ')
for i in range (n):
    arr1.append(int(input()))

# m = int(input('Enter size of second array: '))

print('Enter elements of second array: ')
for i in range (n):
    arr2.append(int(input()))

arr1.sort()
arr2.sort()

product = 0

for i in range(n):
    product += arr1[i] * arr2[i]

print(product)