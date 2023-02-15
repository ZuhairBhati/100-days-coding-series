# There are N stones in a pond, each having a value Ai? written on it. A frog is at stone 1 and wants to reach stone N. The frog can jump from a stone i to any stone j(j>i). Let d be the length of subarray (i.e. j−i+1), then the energy required for the jump is (d⋅Ai?)−Aj?. Find the minimum non-negative amount of energy required by the frog to reach the N-th stone.

# Note: It is possible that the total amount of energy required is negative, in that case, you should print the minimum non-negative value (i.e. 0).

# Input Format

# The first line contains an integer T - the number of test cases. Then the test cases follow.
# The first line of each test case contains an integer N - the number of stones.
# The second line contains N integers denoting the numbers written on the stones.
# Output Format

# For each test case output a single integer - the minimum non-negative energy required by the frog.

# Sample Input

# 4

# 3

# 6 1 3

# 4

# 3 1 10 4

# 3

# 7 9 1

# 2

# 1 5

# Sample Output

# 10

# 4

# 20

# 0

t = int(input())
for u in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    x, y = 0, 0
    s = 0
    while (y < n):
        if (l[y] >= l[x]):
            y += 1
        else:
            s += (y-x+1) * l[x]-l[y]
            x = y
    s += (n - x) * l[x]-l[n-1]
    if (s <= 0):
        print(0)
    else:
        print(s)