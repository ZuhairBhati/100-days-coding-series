# Kekocity's population consist of N gnomes numbered with unique ids from 1 to N. As they are very joyful gnomes, they usually send jokes to their friends right after they get any (even if they knew it before) via their social network named as Mybeard. Mybeard became popular in the city because of message auto-deletion. It takes exactly one minute to read and resend joke to mates.

# Mayor of Kekocity, Mr. Shaikhinidin, is interested in understanding how the jokes are spread. He gives you database of Mybeard social network, and wants you to answer some queries on it.

# You will be given a list of friends for every gnome and M queries of the following type: Who will receive a message with joke after exactly K minutes, if the creator of joke was gnome with id x?

# Input

# The first line contains a single integer N denoting the number of gnomes.

# The next N lines contain the the matrix g[N][N]. Each of the i-th line, will contain N space separated integers - j-th of those will denote g[i][j]. If gnome j is friend of gnome i, then g[i][j] is 1. Otherwise it will be zero. Plese note that the friendship relationship is not bidirectional, i.e. it might happen that g[i][j] may not be equal to g[j][i]. Also one can be friend of itself also, i.e. g[i][i] may be equal to 1.

# The next line contains a single integer M denoting the number of queries. The next M lines contain two integers k and x described above.

# Output

# For each query, output two lines.

# In the first line, output how many gnomes will know the joke after k minutes.

# In the second line, print these ids (numbering) of these gnomes in increasing order. If no one will know the joke after K minutes, then print -1 in this line.

# Constraints

# 1 ≤ N ≤ 500
# 1 ≤ M ≤ 500
# 0 ≤ k ≤ 109
# 1 ≤ x ≤ N
# 0 ≤ g[i][j] ≤ 1
 

# Sample Input

# 5

# 0 1 0 0 0

# 0 0 1 1 0

# 1 0 0 0 0

# 0 0 0 1 0

# 0 0 0 0 0

# 4

# 3 1

# 10000 1

# 0 5

# 1 5 

# Sample Output

# 2

# 1 4

# 2

# 2 4

# 1

# 5

# 0

# -1

n = int(input().strip())

adj = []
adjlist = []
adjints = []
for row in range(n):
    r = ''.join(input().strip().split(' '))
    adjints.append(int(r, 2))

command = 12
def toBool(x):
    res = bin(x)[2:]
    offset = n - len(res)
    return ('0' * offset) + res

def orit(s):
    global adjints
    cur = 0
    for i, c in enumerate(s):
        if c == '1':
            cur |= adjints[i]
    return cur

nqueries = int(input().strip())
queries = []

for q in range(nqueries):
    atstep, origin = [int(x) for x in input().strip().split(' ')]
    origin -= 1
    queries.append([atstep, origin])
    step = 0
    njokes = 0
    jokers = []
    cur = 1 << (n - origin - 1)
    state = cur
    seen = {}
    seen[state] = 0
    while step < atstep:
        step += 1
        cur = orit(toBool(cur))
        state = cur
        if state in seen: 
            dif = step - seen[state] 
            left = atstep - step
            atstep = (left % dif) + step
        else:
            seen[state] = step
        if not cur: 
            break
    cur = toBool(cur)
    num = len([x for x in cur if x == '1'])
    print(num)
    if num == 0:
        print(-1)
    else:
        ans = [str(x[0] + 1) for x in enumerate(cur) if x[1] == '1'] 
        print(' '.join(ans))
