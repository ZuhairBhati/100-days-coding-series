# Write Program to find smallest and largest element in an array

n = int(input('Enter size of array: '))
arr = []

print('Enter elements: ')
for i in range (n):
    temp = int(input())
    arr.append(temp)

max = arr[0]
min = arr[0]

for i in range (n):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]

print('Smallest Number:',min)
print('Largest Number:',max)