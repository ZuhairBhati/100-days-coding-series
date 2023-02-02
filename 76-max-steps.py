# You are given N integers. In each step you can choose some K of the remaining numbers and delete them, if the following condition holds: Let the K numbers you've chosen be a1, a2, a3, ..., aK in sorted order. Then, for each i ≤ K - 1, ai+1 must be greater than or equal to ai * C.

# You are asked to calculate the maximum number of steps you can possibly make.

# Input

# The first line of the input contains an integer T, denoting the number of test cases. The description of each testcase follows.
# The first line of each testcase contains three integers: N, K, and C
# The second line of each testcase contains the N initial numbers
# Output

# For each test case output the answer in a new line.

# Sample Input

# 2

# 6 3 2

# 4 1 2 2 3 1

# 6 3 2

# 1 2 2 1 4 4

# Sample Output

# 1

# 2

from sys import stdin

def check(x):
    ls = [[] for _ in range(x)]
    clND = 0
    for i in range(n):
        if len(ls[clND]) == k:
            return True
        if len(ls[clND]) == 0 or ls[clND][-1] * c <= a[i]:
            ls[clND].append(a[i])
            clND = (clND + 1) % x
    if len(ls[clND]) == k:
        return True
    return False

for _ in range(int(input())):
    n,k,c = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    a.sort()
    l = 0
    r = n + 1

    while r - 1 > l:
        mid = (l + r) // 2
        if check(mid):
            l = mid
        else:
            r = mid
    print(l)