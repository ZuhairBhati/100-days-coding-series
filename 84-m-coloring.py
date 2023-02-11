# Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

# Example 1:

# Input:
# N = 4
# M = 3
# E = 5
# Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}

# Output: 1
# Explanation: It is possible to colour the given graph using 3 colours.

# Example 2:

# Input:
# N = 3
# M = 2
# E = 3
# Edges[] = {(0,1),(1,2),(0,2)}
# Output: 0


def isSafe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] and c == color[i]:
            return False
    return True

def graphColor(graph, m, color, v):
    if v == len(graph):
        return True
    
    for c in range(1, m+1):
        if isSafe(graph, color, v, c):
            color[v] = c
            if graphColor(graph, m, color, v+1):
                return True
            color[v] = 0
    return False

n = int(input())
m = int(input())
e = int(input())
graph = [[0 for x in range(n)] for y in range(n)]

for i in range(e):
    a = int(input())
    b = int(input())
    graph[a][b] = 1
    graph[b][a] = 1

color = [0 for i in range(n)]

if graphColor(graph, m, color, 0):
    print('1')
else:
    print('0')
