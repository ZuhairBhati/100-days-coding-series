#  Write Program to remove duplicate elements in an array

def removeDuplicates(arr, n):

    # Return, if array is empty or contains a single element
    if n == 0 or n == 1:
        return n
    
    temp = list(range(n))
    j = 0

    # Start traversing elements
    for i in range(0, n-1):
        # If current element is not equal to next element then store that current element

        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1
    
    temp[j] = arr[n-1]
    j += 1

    for i in range(0, j):
        arr[i] = temp[i]
    return j    

# Driver code   
n = int(input('Enter size of array: '))
arr = []

print('Enter elements of array: ')

for i in range (n):
    temp = int(input())
    arr.append(temp)

n = removeDuplicates(arr, n)

# Print updated array
for i in range(n):
    print ("%d"%(arr[i]), end = " ")
