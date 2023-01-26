# Write a Program to Capitalize the first and last letter of each word of a string

string = input('Enter a String: ')

def capitalize(string):
    string, result = string.title(), ''
    for word in string.split():
        result += word[:-1] + word[-1].upper() + ' '
    return result[:-1]

print(capitalize(string))