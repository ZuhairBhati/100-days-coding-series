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

import sys

def check(a, x, k, c):
    if k * x > len(a):
        return False
    if x == 0:
        return True
    v = [[0] * x for i in range(k)]
    for i in range(x):
        v[0][i] = a[i]
    s = x
    for i in range(1, k):
        for j in range(x):
            flag = False
            while s < len(a):
                if a[s] >= c * v[i - 1][j]:
                    v[i][j] = a[s]
                    s += 1
                    flag = True
                    break
                s += 1
            if not flag:
                return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n, k, c = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        min = 0
        max = n // k
        ans = 0
        while min <= max:
            mid = min + (max - min) // 2
            if check(a, mid, k, c):
                ans = mid
                min = mid + 1
            else:
                max = mid - 1
        print(ans)

if __name__ == '__main__':
    main()