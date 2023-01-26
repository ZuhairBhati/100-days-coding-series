# Given an array, rotate the array by one position in clock-wise direction.

def rotateArray(arr, n):

    x = arr[n - 1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x
  
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

rotateArray(arr, n)

print(arr, end=' ')