

#GRAPH THEORY
import numpy as np
import math


def add_edge(mat, i, j, o, w):

    INF = math.inf


    mat[i][j][o] = INF
    mat[j][i][o] = w
    mat[o][i][j] = w
    mat[o][j][i] = INF
    mat[j][o][i] = w
    mat[i][o][j] = INF
    


def display_matrix(mat):

    for row in mat:
        print("".join(map(str, row)))

if __name__ == "__main__":
    v = 5
    mat = [[[0] * v for _ in range(v)] for _ in range(v)]

    add_edge(mat, 0, 3, 4, 10)
    add_edge(mat, 0, 2, 1, 20)
    add_edge(mat, 0, 3, 4, 10)
    add_edge(mat, 0, 2, 1, 20)
    add_edge(mat, 2, 3, 0, 5)
    add_edge(mat, 3, 1, 4, 2)
    add_edge(mat, 4, 2, 0, 5)
    add_edge(mat, 1, 4, 2, 13)
    add_edge(mat, 4, 0, 2, 15)
    add_edge(mat, 1, 2, 3, 3)
    add_edge(mat, 3, 0, 4, 6)



    print("Adjacent Matrix")
    print(mat)
    print(np.array(mat))
    