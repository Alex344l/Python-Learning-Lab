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

    print(bfs(mat, 0))
    print(dfs(mat, 0))

    