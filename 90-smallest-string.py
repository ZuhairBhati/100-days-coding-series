# Gru has a string S of length N, consisting of only characters a and b for banana and P points to spend.

# Now Gru wants to replace and/or re-arrange characters of this given string to get the lexicographically smallest string possible. For this, he can perform the following two operations any number of times.

# Swap any two characters in the string. This operation costs 11point. (any two, need not be adjacent)
# Replace a character in the string with any other lower case english letter. This operation costs 2 points.
# Help Gru in obtaining the lexicographically smallest string possible, by using at most P points.

# Input:

# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains two lines of input, first-line containing two integers N , P.
# The second line contains a string S consisting of N characters.
# Output: For each testcase, output in a single containing the lexicographically smallest string obtained.

# Sample Input

# 1

# 3 3

# bba

# Sample Output

# aab
 
t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    s = list(input())
    a = s.count('a')
    b = s.count('b')
    swap = 0
    arr = [i for i in s]
    for i in range(a):
        if s[i] == 'b':
            swap += 1
    if p <= swap:
        i = 0
        temp = p
        while p > 0 and i < n:
            if arr[i] == 'b':
                arr[i] = 'a'
                p -= 1
            i += 1
        p = temp
        i = n - 1
        while p > 0 and i > 0:
            if arr[i] == 'a':
                arr[i] = 'b'
                p -= 1
            i -= 1
        print(''.join(arr))
    else:
        for j in range(n):
            if j < a:
                arr[j] = 'a'
            else:
                arr[j] = 'b'
        p -= swap
        for k in range(n):
            if arr[k] == 'b':
                if s[k] == 'b' and p >= 2:
                    p -= 2
                    arr[k] = 'a'
                if s[k] == 'a' and p >= 1:
                    p -= 1
                    arr[k] = 'a'
        print(''.join(arr))
