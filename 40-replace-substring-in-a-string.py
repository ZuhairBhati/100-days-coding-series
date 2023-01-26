#  Write a Program to Replace substring in a string

# Method 1
string = input('Enter a String: ')
str1 = input('Enter the sub-string to be removed: ')
str2 = input('Enter the new sub-string: ')

output = string.replace(str1, str2)
print('The new string: ',output)

# Method 2 
string = input('Enter a String: ')
str1 = input('Enter the sub-string to be removed: ')
str2 = input('Enter the new sub-string: ')

s = string.split(str1)
new_str = '' 

for i in s:
    if i == '':
        new_str += str2
    else:
        new_str += i

print(new_str)