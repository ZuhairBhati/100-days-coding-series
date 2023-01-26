# Write Program to find longest palindrome in an array

# Function to check if n is palindrom
def isPlaindrome(n):

    divisor = 1

    while (int(n / divisor) >= 10):
        divisor *= 10

    while (n != 0):
        start = int(n / divisor)
        end = n % 10
        
        if (start != end):
            return False

        n = int((n % divisor) / 10)
        divisor = int(divisor / 100)

    return True

# Function to find the largest palindromic element
def largestPalindrome(arr, n):
    result = -1

    for i in range(0, n, 1):
        if (arr[i] > result and isPlaindrome(arr[i])):
            result = arr[i]
    
    return result

# Driver Code
n = int(input('Enter size of array: '))
arr = []

print('Enter elements of array: ')

for i in range (n):
    temp = int(input())
    arr.append(temp)

print(largestPalindrome(arr, n))


