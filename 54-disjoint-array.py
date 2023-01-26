# Given an integer array of size N. Write Program to find whether Arrays are disjoint or not. 

# Two arrays are said to be disjoint if they have no elements in common.

# Function for checking same elements
def disjointArray(arr1, arr2, n, m):
    for i in range(n):
        for j in range(m):
            if (arr1[i] == arr2[j]):
                return False
    return True

arr1 = []
arr2 = []

n = int(input('Enter size of first array: '))

print('Enter elements of first array: ')
for i in range (n):
    arr1.append(int(input()))

m = int(input('Enter size of second array: '))

print('Enter elements of second array: ')
for i in range (m):
    arr2.append(int(input()))

if (disjointArray(arr1, arr2, n, m)):
    print('Disjoint')
else:
    print('Not Disjoint')