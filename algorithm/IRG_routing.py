from heapq import heappop, heappush
import math
from collections import deque as dq
import numpy as np




class IRG:
    def __init__(self):
        self.pos = {}
        self.adj = {}

    def add_node(self, node, x, y):
        self.pos[node] = (x, y)
        self.adj.setdefault(node, {})

    def add_edge(self, u, v, distance=None):
        
        if distance is None:
            x1, y1 = self.pos[u]
            x2, y2 = self.pos[v]
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.adj[u][v] = distance
        self.adj[v][u] = distance






def main():





if __name__ == "__main__":
    main()


    

    




