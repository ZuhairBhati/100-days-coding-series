# Write Program to find whether the numbers of an array be made equal

# Function to check whether an array is equal or not
def equalArray(arr, n):
    for i in range(n):

        # Divide the element by 2
        while arr[i] % 2 == 0:
            arr[i] //= 2

        # Divide the element by 3
        while arr[i] % 3 == 0:
            arr[i] //= 3

    if arr[i] != arr[0]:
        return False
    
    return True

# Driver Code
n = int(input('Enter size of array: '))
arr = []
print('Enter elements: ')

for i in range(n):
    arr.append(int(input()))

# Calling the function   
if equalArray(arr, n):
    print('Yes')
else:
    print('No')