# Write a Program to Remove vowels from a string

string = input('Enter a String: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
string1 = ''

for char in string:
    if char not in vowels:
        string1 += char

print(string1)