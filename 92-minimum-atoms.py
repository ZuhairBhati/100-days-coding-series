# Let X be the set of all integers between 0 and n-1. Suppose we have a collection S1, S2, ..., Sm of subsets of X. Say an atom A is a subset of X such that for each Si we have either A is a subset of Si or A and Si do not have any common elements.

# Your task is to find a collection A1, ..., Ak of atoms such that every item in X is in some Ai and no two Ai, Aj with i ≠ j share a common item. Surely such a collection exists as we could create a single set {x} for each x in X. A more interesting question is to minimize k, the number of atoms.

# Input

# The first line contains a single positive integer t ≤ 30 indicating the number of test cases. Each test case begins with two integers n,m where n is the size of X and m is the number of sets Si. Then m lines follow where the i'th such line begins with an integer vi between 1 and n (inclusive) indicating the size of Si. Following this are vi distinct integers between 0 and n-1 that describe the contents of Si.

# You are guaranteed that 1 ≤ n ≤ 100 and 1 ≤ m ≤ 30. Furthermore, each number between 0 and n-1 will appear in at least one set Si.

# Output

# For each test case you are to output a single integer indicating the minimum number of atoms that X can be partitioned into to satisfy the constraints.

# Sample Input

# 2

# 5 2

# 3 0 1 2

# 3 2 3 4

# 4 3

# 2 0 1

# 2 1 2

# 2 2 3

# Sample Output

# 3

# 4

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    atomlist = ['']*n
    for k in range(m):
        s = []
        s.extend(input().split()[1:])
        for w in range(n):
            if str(w) in s:
                atomlist[w] += '1'
            else:
                atomlist[w] += '0'
print(len(set(atomlist)))
