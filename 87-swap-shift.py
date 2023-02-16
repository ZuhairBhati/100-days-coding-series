# Blobo2 is in his practical exam. The teacher gave him a permutation A of N integers.

# The teacher has allowed Blobo2 to make a certain type of operation on the permutation. In one operation, he can:

# Apply left shift on the permutation. In other words, he can take the first element of the permutation and move it to the back of the permutation.
# The teacher has asked Blobo2 to find the lexicographically smallest permutation possible after applying any (possibly zero) number of given operations.

# Since Blobo2 wants to impress his teacher, he decided to perform at most two swaps in addition to the allowed operation.

# Find the lexicographically smallest possible permutation Blobo2 can generate after applying at most two swaps and any number of given operations.

# Note:

# A permutation of size N consists of all integers from 1 to N exactly once.
# During a swap, Blobo2 can choose any two indices i and j (1≤i,j≤N) and swap Ai? with Aj?.
# A permutation X is said to be lexicographically smaller than a permutation Y if Xi?<Yi?, where i is the first index where both the permutations differ.
# Input Format

# The first line of input will contain a single integer T, denoting the number of test cases.
# The second line will contain the integer N, denoting the size of the permutation.
# The third line contains N distinct integers, the elements of the permutation A.
# Output Format

# Output the lexicographically smallest possible permutation Blobo2 can generate after applying at most two swaps and any number of given operations.

# Sample Input

# 2

# 5

# 5 2 1 4 3

# 5

# 3 5 2 1 4

# Sample Output

# 1 2 3 4 5

# 1 2 3 4 5


def rotate(p):
    i = p.index(0)
    return p[i : ] + p[: i]

def swap(p, i1, i2):
    i1 %= len(p)
    i2 %= len(p)
    rv = p.copy()
    rv[i1], rv[i2] = rv[i2], rv[i1]
    return rv

def swaps(p):
    j = 1
    while j != len(p) and p[j] == j:
        j += 1
    if j == len(p):
        return [p]
    i1 = p.index(1)
    tries = [(j, p.index(j)), (0, i1 - 1), (0, i1), (0, -1), (0, -2), (i1, i1 - 1)]
    if len(p) > 2:
        tries.append((i1, p.index(2) - 1))
    return [rotate(swap(p, j, k)) for j, k in tries]

for _ in range(int(input())):
    input()
    v = [int(x) - 1 for x in input().split()]
    for x in min(r for q in swaps(rotate(v)) for r in swaps(q)):
        print(x + 1, end = ' ')
    print()