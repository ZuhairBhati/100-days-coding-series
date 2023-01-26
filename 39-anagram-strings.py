# Write a Program to check if two strings are Anagram or not

string1 = input('Enter First String: ')
string2 = input('Enter Second String: ')

str1_sorted = sorted(string1)
str2_sorted = sorted(string2)

if str1_sorted == str2_sorted:
    print('Anagram')
else:
    print('Not Anagram')