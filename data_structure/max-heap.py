

def max_heap(heap, value):

    # Add the new value to the heap
    heap.append(value)

    # Get the index of the last element (the newly added value)
    index = len(heap) - 1

    # Bubble up the new value to maintain the max-heap property
    while index > 0:
        parent_index = (index - 1) // 2
        if heap[parent_index] < heap[index]:
            heap[parent_index], heap[index] = heap[index], heap[parent_index]
            index = parent_index
        else:
            break


if __name__ == "__main__":
    
    heap = []
    values = [5, 3, 8, 1, 2, 7, 9, 4, 6]

    n = len(values)

    for i in range(n):
        max_heap(heap, values[i])
        print(f"Inserted {values[i]} into the max-heap: {heap}")

        for j in range(len(heap)):
            print(heap[j], end=" ")