# There is a hallway of length N−1 and you have M workers to clean the floor. Each worker is responsible for segment [Li?,Ri?], i.e., the segment starting at Li? and ending at Ri?. The segments might overlap.

# Every unit of length of the floor should be cleaned by at least one worker. A worker can clean 1 unit of length of the floor in 1 unit of time and can start from any position within their segment. A worker can also choose to move in any direction. However, the flow of each worker should be continuous, i.e, they can’t skip any portion and jump to the next one, though they can change their direction. What’s the minimum amount of time required to clean the floor, if the workers work simultaneously?

# Input:

# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains of M+1 lines of input.
# First line contains 22 space separated integers N, M, length of the hallway and number of workers.
# Each of the next M lines contain 2 space separated integers Li?, Ri?, endpoints of the segment under ith worker.
# Output: For each testcase, output in a single line minimum time required to clean the hallway or −1 if it's not possible to clean the entire floor.

# Sample Input

# 3

# 10 3

# 1 10

# 1 5

# 6 10

# 10 1

# 2 10

# 10 2

# 5 10

# 1 5

# Sample Output

# 3

# -1

# 5

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    v = []
    for j in range(m):
        x,y = map(int, input().split())
        v.append([y,x])
    v.sort()
    l = 0
    r = n - 1
    count = -1
    while(l <= r):
        mid = (l + r) // 2
        seg = 1
        for i in range(m):
            if (seg >= v[i][0] or v[i][1] > seg):
                continue
            else:
                seg = min(seg + mid, v[i][0])
        if (seg == n):
            count = mid
            r = mid - 1
        else:
            l = mid + 1
    print(count)