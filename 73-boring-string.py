# A string is called boring if all the characters of the string are same.

# You are given a string S of length N, consisting of lowercase english alphabets. Find the length of the longest boring substring of S which occurs more than once.

# Note that if there is no boring substring which occurs more than once in S, the answer will be 00.

# A substring is obtained by deleting some (possibly zero) elements from the beginning of the string and some (possibly zero) elements from the end of the string.

# Input Format

# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two lines of input.
# The first line of each test case contains an integer N, denoting the length of string S.
# The next contains string S.
# Output Format

# For each test case, output on a new line, the length of the longest boring substring of S which occurs more than once.

# Sample Input

# 4

# 3

# aaa

# 3

# abc

# 5

# bcaca

# 6

# caabaa

# Sample Output

# 2

# 0

# 1

# 2

test = int(input())

for j in range(test):
    n = int(input())
    s = input()
    Max = 0
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = [1,1]
            k = 1
        else:
            if prev == s[i]:
                k += 1
                if k > d[prev][0]:
                    d[prev][0] = k
                    d[prev][1] = 1
                elif k == d[prev][0]:
                    d[prev][1] += 1
            else:
                if d[s[i]][0] == 1:
                    d[s[i]][1] += 1
                k = 1
        prev = s[i]
    Max = []
    for i in d:
        if d[i] > Max:
            Max = d[i]
    if Max[1] == 1:
        print(Max[0] - 1)
    else:
        print(Max[0])