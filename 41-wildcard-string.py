# Check if two strings match where one string contains wildcard characters

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

def matchString(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 == 0 and len_str2 == 0:
        return True
    if len_str1 > 1 and str1[0] == '*' and len_str2 == 0:
        return False
    if (len_str1 > 1 and str1[0] == '?') or (len_str1 != 0 and len_str2 != 0 and str1[0] == str2[0]):
        return matchString(str1[1:], str2[1:])
    if len_str1 != 0 and str1[0] == '*':
        return matchString(str1[1:], str2) or matchString(str1, str2[1:])
    return False

if matchString(str1, str2):
    print('Yes they match')
else:
    print('No')
    