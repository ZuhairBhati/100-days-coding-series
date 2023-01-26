#  Write a Program to Count the sum of numbers in a string

string = input('Enter a String: ')

def sum_of_digits(string): 
    sum = 0
    for i in string:
        if i.isdigit():
            sum = sum + int(i)
    return sum

print(sum_of_digits(string))