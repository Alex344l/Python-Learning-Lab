import numpy as np
import matplotlib.pyplot as plt

INF = float('inf')

def add_edge(graph, u, v, cost):

    graph[u][v] = cost
    graph[v][u] = INF

def display_graph(graph):
    for row in graph:
        print(" ".join(map(str, row)))  

def dijkstra(graph, start, end):

    n = len(graph)
    visited = [False] * n
    distance = [INF] * n
    distance[start] = 0
    previous = [None] * n

    path = []
    current = end
        

    for _ in range(n):
        
        min_distance = INF
        min_index = -1

        for v in range(n):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                min_index = v


        if min_index == -1:
            break

        visited[min_index] = True
        
        if min_index == end:
            break


        for v in range(n):

            if graph[min_index][v] != INF and not visited[v]:

                new_distance = (
                    distance[min_index] + 
                    graph[min_index][v]
                )

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    previous[v] = min_index

           
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distance, path



if __name__ == "__main__":


   
    v = 6
    graph = [[INF] * v for _ in range(v)] 

    add_edge(graph, 0, 1, 2)
    add_edge(graph, 0, 2, 4)
    add_edge(graph, 1, 2, 1)
    add_edge(graph, 1, 3, 4)
    add_edge(graph, 2, 4, 3)
    add_edge(graph, 3, 4, 2)
    add_edge(graph, 4, 5, 5)
    add_edge(graph, 3, 5, 2)
    add_edge(graph, 1, 5, 7)
    add_edge(graph, 0, 5, 10)
    add_edge(graph, 5, 0, 10)

    print("Weighted Graph:")
    print(np.array(graph))

    print("\nShortest distances from node 0 to node 4:")
    distances, path = dijkstra(graph, 0, 4)

    print("Cost:", distances[4])
    print("Path:", " -> ".join(map(str, path)))


