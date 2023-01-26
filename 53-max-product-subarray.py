#  Given an integer array of size N. Write Program to find maximum product subarray in a given array.

def maxSubarray(arr, n):

    # Initialize result
    result = arr[0]
    for i in range(n):
        m = arr[i]

        # Traversing in current subarray
        for j in range(i + 1, n):
            result = max(result, m)
            m *= arr[j]

        # updating the result for the (n -1)th index
        result = max(result, m)
    return result

n = int(input('Enter size of array: '))
arr = []
print('Enter elements: ')

for i in range(n):
    arr.append(int(input()))

print(maxSubarray(arr, n))