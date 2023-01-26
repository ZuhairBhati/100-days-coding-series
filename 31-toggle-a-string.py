# Write a Program to Toggle each character in a string

string = input('Enter a String: ')
string1 = ''

for i in string:
    if i.isupper():
        i = i.lower()
        string1 += i
    else:
        i = i.upper()
        string1 += i
        
print(string1)        