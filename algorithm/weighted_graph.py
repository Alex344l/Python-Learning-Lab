import numpy as np
import matplotlib.pyplot as plt
from heapq import heappop, heappush

INF = float('inf')

def add_edge(graph, u, v, cost):

    graph[u][v] = cost
    graph[v][u] = INF

def display_graph(graph):
    for row in graph:
        print(" ".join(map(str, row)))  



def dijkstra(graph, start, end):

    n = len(graph)

    distance = [INF] * n

    distance[start] = 0
    previous = [None] * n


    heap = [(0, start)]  # (distance, vertex)


    while heap:

        current_distance, current_vertex = heappop(heap)

        if current_distance > distance[current_vertex]:
            continue

        if current_vertex == end:
            break

        for neighbor in range(n):

            if graph[current_vertex][neighbor] == INF:
                continue

            new_distance = (
                current_distance + 
                graph[current_vertex][neighbor]
            )

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heappush(heap, (new_distance, neighbor))

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return distance, path

   

if __name__ == "__main__":


   
    v = 10
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
    add_edge(graph, 5, 6, 1)
    add_edge(graph, 6, 7, 2)
    add_edge(graph, 7, 8, 3)
    add_edge(graph, 8, 9, 4)        
    add_edge(graph, 9, 0, 5)  # Adding a cycle for testing
    add_edge(graph, 6, 8, 1) 

    print("Weighted Graph:")
    print(np.array(graph))

    print("\nShortest distances from node 0 to node 4:")
    distances, path = dijkstra(graph, 0, 8)

    print("Cost:", distances[8])
    print("Path:", " -> ".join(map(str, path)))

    plt.plot(path, marker='o')
    plt.xlabel('Nodes in Path')
    plt.ylabel('Shortest Distance')
    plt.title('Dijkstra\'s Algorithm')

    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color="#36a4ee")


    plt.show()      


