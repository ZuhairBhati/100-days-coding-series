# Write a Program to calculate the Frequency of characters in a string

string = input('Enter a String: ')

for char in string:
    frequency = string.count(char)
    print('The frequency of',char,'is',frequency)