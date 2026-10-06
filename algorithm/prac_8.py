import numpy as np

def addEdge(mat, i, j):

    mat[i][j] = 1
    mat[j][i] = 1


def rmEdge(mat, i, j):

    mat[i][j] = 0
    mat[j][i] = 0


def displayMatrix(mat):

    for row in mat:
        print("".join(map(str, row)))



def find_neighbors(graph, node):

    neighbors = []

    for i, value in enumerate(graph[node]):

        if value == 1:

            neighbors.append(i)

    return neighbors

def find_max_neighbors(graph):

    max_node = 0
    max_neighbor = 0

    for node in range(len(graph)):
        neighbors = find_neighbors(graph, node)

        if len(neighbors) > max_neighbor:
            max_neighbor =  len(neighbors)
            max_node = node

    return max_node

def find_degrees(graph):

    degrees = []

    for node in range(len(graph)):

        neighbors = find_neighbors(graph, node)
        degrees.append(len(neighbors))

    return degrees

def is_connected(graph, a, b):
    neighbors = find_neighbors(graph, a)
    return b in neighbors

def can_reach(graph, a, b):
    queue = [a]
    visited = set()

    while queue:
        node = queue.pop(0)

        if node == b:
            return True

        if node in visited:
            continue

        visited.add(node)

        for neighbor in find_neighbors(graph, node):
            if neighbor not in visited:
                queue.append(neighbor)


    return False 

def path(graph, a, b):
    queue = [a]
    visited = set()
    previous = {a: None}

    while queue:
        node = queue.pop(0)

        if node == b:
            break

        visited.add(node)

        for neighbor in find_neighbors(graph, node):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                previous[neighbor] = node


    if b not in previous:
        return []


    path = []
    current = b

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path


if __name__ == "__main__":

    v = 7
    mat = [[0] * v for _ in range(v)]

    addEdge(mat, 2, 1)
    addEdge(mat, 0, 1)
    addEdge(mat, 3, 1)
    addEdge(mat, 4, 1)
    addEdge(mat, 5, 4)
    addEdge(mat, 5, 3)
    addEdge(mat, 0, 2)
    addEdge(mat, 3, 4)
    addEdge(mat, 4, 2)
    addEdge(mat, 5, 2)
    addEdge(mat, 5, 0)
    addEdge(mat, 6, 0)
    addEdge(mat, 6, 1)

    print("Adjacent Matrix: ")
    print(np.array(mat))

    rmEdge(mat, 0, 2)
    rmEdge(mat, 0, 6)
    rmEdge(mat, 4, 1)

    print("Changed Matrix: ")
    print(np.array(mat))

  

    print("Node with most neighbors: ", find_max_neighbors(mat))
    print("Node 0: ", find_neighbors(mat, 0))
    print("Node 1: ", find_neighbors(mat, 1))
    print("Node 2: ", find_neighbors(mat, 2))
    print("Node 3: ", find_neighbors(mat, 3))
    print("Node 4: ", find_neighbors(mat, 4))
    print("Node 5: ", find_neighbors(mat, 5))
    print("Node 6: ", find_neighbors(mat, 6))

    print("Degree: ", find_degrees(mat))

    print("Neighbor: ", is_connected(mat, 6, 1))

    print("can 0 reach 6: ", can_reach(mat, 0, 6))

    print("Path: ", path(mat, 0, 6))
    