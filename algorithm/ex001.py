import math
from heapq import heappush, heappop
from collections import deque as dq
import matplotlib.pyplot as plt

# Define the Cell class
class Cell:
    def __init__(self):
        self.parent_i = 0  # Parent cell's row index
        self.parent_j = 0  # Parent cell's column index
        self.f = float('inf')  # Total cost of the cell (g + h)
        self.g = float('inf')  # Cost from start to this cell
        self.h = 0  # Heuristic cost from this cell to destination


# Define the size of the grid
ROW = 9
COL = 10

# Check if a cell is valid (within the grid)
def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Check if a cell is unblocked
def is_unblocked(grid, row, col):
    return grid[row][col] == 1

# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

def is_diag(dir):
    return dir[0] != 0 and dir[1] != 0

# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

# Trace the path from source to destination
def trace_path(cell_details, dest):
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    return path


# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Checks before searching
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return None

    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return None

    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return [tuple(src)]

    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Start cell
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    open_list = []
    heappush(open_list, (0.0, i, j))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while len(open_list) > 0:
        p = heappop(open_list)
        i = p[1]
        j = p[2]

        # CHANGED: skip old duplicate entries for a cell we already finished
        if closed_list[i][j]:
            continue

        # CHANGED: stop when the destination is POPPED, not when it is first seen
        if is_destination(i, j, dest):
            return trace_path(cell_details, dest)

        closed_list[i][j] = True

        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if not (is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j)
                    and not closed_list[new_i][new_j]):
                continue

            #is_diag = dir[0] != 0 and dir[1] != 0

            # CHANGED: don't cut corners past a wall
            if is_diag(dir) and (grid[i][new_j] == 0 or grid[new_i][j] == 0):
                continue

            # CHANGED: a diagonal step costs sqrt(2), not 1
            step = math.sqrt(2) if is_diag else 1.0
            g_new = cell_details[i][j].g + step
            h_new = calculate_h_value(new_i, new_j, dest)
            f_new = g_new + h_new

            # CHANGED: update only if this is a cheaper way to reach the cell
            if g_new < cell_details[new_i][new_j].g:
                heappush(open_list, (f_new, new_i, new_j))
                cell_details[new_i][new_j].f = f_new
                cell_details[new_i][new_j].g = g_new
                cell_details[new_i][new_j].h = h_new
                cell_details[new_i][new_j].parent_i = i
                cell_details[new_i][new_j].parent_j = j

    print("Failed to find the destination cell")
    return None


#Experimenting with BFS and DFS
#BFS and DFS


def shortest_path(grid, src, dest):

    src, dest = tuple(src), tuple(dest)

    if not is_unblocked(grid, *src) or not is_unblocked(grid, *dest):
        return None

    if not is_valid(*src) or not is_valid(*dest):
        return None
    

    visited = {src}
    queue = dq([(src, [src])])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)] 

    while queue:

        (r, c), path = queue.popleft()

        if (r, c) == dest:
            return path



        for dr, dc in directions:
            nr, nc = r + dr, c + dc


            if not (is_valid(nr, nc) and is_unblocked(grid, nr, nc)) and (nr, nc) not in visited:
                continue

            if dr != 0 and dc != 0 and (grid[r][nc] == 0 or grid[nr][c] == 0):
                continue

            visited.add((nr, nc))
            queue.append(((nr, nc), path + [(nr, nc)]))
                

    return "Path not found"

#Cycle detection using DFS

def has_cycle(grid, src):
    src = tuple(src)

    if not is_unblocked(grid, *src):
        return False

    if not is_valid(*src):
        return False

    visited = set()
    stack = [(src, None)]  # (current cell, parent cell)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)] 

    while stack:
        (r, c), parent = stack.pop()

        if (r, c) in visited:
            continue

        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and is_unblocked(grid, nr, nc):
                if (nr, nc) != parent:  # Avoid going back to the parent
                    if (nr, nc) in visited:
                        return True  # Cycle detected
                    stack.append(((nr, nc), (r, c)))

    return False  # No cycle detected


def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

   

    # Define the source and destination
    src = [0, 8]
    dest = [7, 0]

    # Run the A* search algorithm


    a_star_path_result = a_star_search(grid, src, dest)
    print("Shortest Path using A*:")
    for i in a_star_path_result:
        print("->", i, end=" ")
    print()


    shortest_path_result = shortest_path(grid, src, dest)
    print("Shortest Path using BFS:")
    for i in shortest_path_result:
        print("->", i, end=" ")
    print()

    has_cycle_result = has_cycle(grid, src)
    print("Has a cycle:", has_cycle_result)


    fig, ax = plt.subplots(1, 2, figsize=(10, 5))


    ax[0].set_title('BFS Shortest Path')
    ax[0].plot(src[1], src[0], 'ro')  # Start point
    ax[0].plot(dest[1], dest[0], 'go')  # End point
    ax[0].plot([p[1] for p in shortest_path_result], [p[0] for p in shortest_path_result], 'b-')  # Path
    ax[0].imshow(grid, cmap='gray_r', origin='upper')

    ax[1].set_title('A* Shortest Path')
    ax[1].plot(src[1], src[0], 'ro')  # Start point
    ax[1].plot(dest[1], dest[0], 'go')
    ax[1].plot([p[1] for p in a_star_path_result], [p[0] for p in a_star_path_result], 'b-')  # End point
    ax[1].imshow(grid, cmap='gray_r', origin='upper')
    ax[1].plot( 'b-')  # Path


    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
