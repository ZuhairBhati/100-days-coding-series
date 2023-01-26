# Palindromic substrings

# Anoop likes strings a lot but he likes palindromic strings more. Today, Anoop has two strings A and B, each consisting of lower case alphabets.
# Anoop is eager to know whether it is possible to choose some non empty strings s1 and s2 where s1 is a substring of A, s2 is a substring of B such that s1 + s2 is a palindromic string.
# Here '+' denotes the concatenation between the strings.

# Input
# First line of input contains a single integer T denoting the number of test cases.
# For each test case:
# First line contains the string A
# Second line contains the string B.

# Output
# For each test case, Print "Yes" (without quotes) if it possible to choose such strings s1 & s2. Print "No" (without quotes) otherwise.

# Input
# 3
# abc
# abc
# a
# b
# abba
# baab

# Output
# Yes
# No
# Yes

test = int(input())

for x in range (test):
    A = input()
    B = input()
    flag = 0
    for i in range(len(A)):
        if A[i] in B:
            flag = 1
            break
    if flag == 1:
        print('Yes')
    else:
        print('No')