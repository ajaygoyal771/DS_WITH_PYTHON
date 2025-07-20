# This is Kahn's algorithm

def constructadj(V, edges):
    adj = [[] for _ in range(V)]  # Create a list for each vertex
    for u, v in edges:
        adj[u].append(v)  # Add directed edge from u to v
    return adj

# def isCyclicUtil():



def isCyclic(V, edges):
    adj = constructadj(V, edges)
    visited = [False] * V
    temp = []
    temp.append(0)
    while temp:
        temp1 = temp.pop(0)
        # print(temp1)
        visited[temp1] = True
        for i in adj[temp1]:
            if visited[i] == True:
                return True
            else:
                temp.append(i)
    return False


V = 4  # Number of vertices
# edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
V = 5
edges = [[0,1],[1,2],[2,3],[3,4],[4,1]]

# Output: True, because there is a cycle (0 → 2 → 0)
print(isCyclic(V, edges))