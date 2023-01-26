# Write a Program to check if String is a palindrome or not

def strPalindrome(string):
    mid = int(len(string) / 2)

    for i in range(0, mid):
        if string[i] != string[len(string) - i - 1]:
            return False
    
    return True

string = input('Enter a String: ')

if strPalindrome(string):
    print('Palindrome')
else:
    print('Not a Palindrome')