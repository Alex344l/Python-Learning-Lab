from collections import deque as dq

def add_edge(mat, i, j):

    mat[i][j] = 1
    mat[j][i] = 1

def display_matrix(mat):

    for row in mat:
        print("".join(map(str, row)))


def find_neighbors(graph, node):

    neighbors = []

    for i , value in enumerate(graph[node]):
        if value == 1:

            neighbors.append(i)

    return neighbors


def bfs(graph, a):

    visited = [False] * len(graph)
    result = []

    queue = dq()

    queue.append(a)

    visited[a] = True

    while queue:

        vertex = queue.popleft()

        result.append(vertex)

        for neighbor in find_neighbors(graph, vertex):

            if graph[vertex][neighbor] == 1:

                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    return result



def dfs(graph, a):

    visited = [False] * len(graph)
    result = []

    stack = []

    stack.append(a)

    visited[a] = True

    while stack:

        vertex = stack.pop()

        result.append(vertex)

        for neighbor in find_neighbors(graph, vertex):

            if graph[vertex][neighbor] == 1:

                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    return result


def shortest_path(graph, start, end):

    visited = [False] * len(graph)
    queue = dq()
    queue.append((start, [start]))

    while queue:

        node, path = queue.popleft()

        if node == end:
            return path, len(path) - 1
            
            
        for neighbor in find_neighbors(graph, node):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))


    return "Path not found", -1

def dfs_cycle(graph, node, visited, parent):

    visited[node] = True

    for neighbor in find_neighbors(graph, node):

        if not visited[neighbor]:
            parent[neighbor] = node

            cycle = dfs_cycle(graph, neighbor, visited, parent)

            if cycle:
                return cycle

        elif parent[node] != neighbor:

            cycle = [neighbor]
            current = node

            while current != neighbor:
                cycle.append(current)
                current = parent[current]

          
            cycle.append(neighbor)
    
            cycle.reverse()
            return cycle

    return "No cycle found"






if __name__ == "__main__":

    v = 9
    mat = [[0] * v for _ in range(v)]


    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 3)
    add_edge(mat, 1, 4)
    add_edge(mat, 2, 5)
    add_edge(mat, 2, 6)
    add_edge(mat, 6, 7)
    add_edge(mat, 5, 8)
    add_edge(mat, 8, 7)
    add_edge(mat, 3, 8)


    print("Node 0: ",find_neighbors(mat, 0))
    print("Node 1: ", find_neighbors(mat, 1))
    print("Node 2: ", find_neighbors(mat, 2))
    print("Node 3: ", find_neighbors(mat, 3))
    print("Node 4: ", find_neighbors(mat, 4))
    print("Node 5: ", find_neighbors(mat, 5))
    print("Node 6: ", find_neighbors(mat, 6))
    print("Node 7: ", find_neighbors(mat, 7))
    print("Node 8: ", find_neighbors(mat, 8))

    print("BFS from 0:", bfs(mat, 0))
    print("DFS from 0:", dfs(mat, 0))

    path, length = shortest_path(mat, 0, 8)
    print("Shortest path from 0 to 8:", path)
    print("Length of shortest path:", length, "edges")


    visited = [False] * len(mat)
    parent = [-1] * len(mat)

    cycle = dfs_cycle(mat, 0, visited, parent)
    print("Cycle detected:", cycle)
    



    