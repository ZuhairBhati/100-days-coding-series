# Write Program to find number of even and odd elements in an array

n = int(input('Enter size of array: '))
arr = []

print('Enter elements: ')
for i in range (n):
    temp = int(input())
    arr.append(temp)

even = 0
odd = 0

for i in range (n):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print('Number of even elements:',even)
print('Number of odd elements:',odd)